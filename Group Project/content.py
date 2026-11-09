# Scene, clue, map, and feedback content built from game progress.
import rich

from game_data import SceneInfo, WindowPlanScenes
from game_logic import AvailableActions, CanLowerPainting
from game_text import Text, Locations, SceneText, Choices, Clues
from puzzles import LockValues


# Use the same availability check for display and execution.
def SceneChoices(Game):
    Available = AvailableActions(Game)
    Options = [Choice for Choice in Choices[Game["Scene"]]
               if Choice.split(".", 1)[0] in Available or Choice.startswith("back.")]
    if Game["Scene"] == "P2.DESCENT" and not CanLowerPainting(Game):
        Options[0] = Text["P2.DESCEND_ALONE"]
    return Options


# Repeat the selected option text without its menu number or planning cost.
def WindowPlanSummary(Game):
    Selected = [Choices[Scene][Choice - 1].split(". ", 1)[1].removesuffix(" (Free)")
                for Scene, Choice in zip(WindowPlanScenes, Game["WindowPlan"])]
    return Text["P2.PLAN_SUMMARY"].format(passage=Selected[0], equipment=Selected[1], order=Selected[2])


# Fill templates with steps, errors, tries left, clue count, location, and checkpoint name.
def MessageText(Game, Key):
    CheckpointName = ""
    if Game["Checkpoint"]:
        CheckpointName = Text["TITLE." + Game["Checkpoint"]]
    ToolNames = [Text["TOOL." + Tool.upper()].capitalize() for Tool in sorted(Game["Tools"])]
    return Text[Key].format(
        steps=Game["Steps"], errors=Game["Errors"],
        tries_left=5 - Game["Errors"], clue_count=len(Game["Clues"]),
        location=Locations[Game["Location"]], checkpoint_name=CheckpointName,
        close_calls=Game["CloseCalls"],
        tools=", ".join(ToolNames) if ToolNames else Text["TOOL.NONE"])


# Fill and style clue templates for both scenes and the notebook.
# New=True also adds new-clue notifications.
def ClueParagraphs(Game, ClueIds, New=False):
    Paragraphs = []
    Puzzle = Game["LockPuzzle"]
    Values = LockValues(Puzzle)
    ObsoleteOperator = "-" if Values["Bucket"] < Values["Claw"] else "+"
    for ClueId in ClueIds:
        Title, Source, Original = Clues[ClueId]
        Original = Original.format(**Puzzle, obsolete_operator=ObsoleteOperator)
        if New:
            Paragraphs.append(Text["UI.CLUE_ADDED"].format(clue_id=ClueId, source=Source))
        Paragraphs.append(rich.text.Text.assemble(
            (ClueId, "clue.id"), " - ", (Title, "clue.title"),
            "\n" + Text["UI.SOURCE"].format(source=Source) + "\n",
            rich.text.Text.from_markup(Original, emoji=False),
        ))
    return Paragraphs


# Build map information from the current location, visited locations, and progress, hiding unopened names.
def MapParagraphs(Game):
    Scene = Game["Scene"]
    if Scene == "DANGER":
        Scene = Game["Checkpoint"]
    # In danger, use checkpoint progress; this table identifies the extra next location visible in each scene.
    Visible = {"P1.OPEN": ["S02"], "P1.NEXT": ["S03"], "P2.AFTER": ["S04", "S09"],
               "P2.WINDOW": ["S10"], "P2.DESCENT": ["S10"],
               "P2.PASS": ["S10"], "P2.GEAR": ["S10"], "P2.ORDER": ["S10"], "P2.REVIEW": ["S10"],
               "P2.SUPPLY": ["S03"], "P4.ROUTE": ["S05"], "P4.LOBBY": ["S06"],
               "P5.EXIT": ["S07"], "P5.SERVICE": ["S07"], "P5.NEXT": ["S08"]}
    if "service_key" in Game["Tools"] and Scene == "P4.ROUTE":
        Visible[Scene].append("S06")
    MapLines = []
    # Mark the current [>], visited [v], visible [o], and unopened [?] locations separately.
    for LocationId in Locations:
        if LocationId == Game["Location"]:
            MapLines.append("[>] " + Locations[LocationId])
        elif LocationId in Game["Visited"]:
            MapLines.append("[v] " + Locations[LocationId])
        elif LocationId in Visible.get(Scene, []):
            MapLines.append("[o] " + Locations[LocationId])
        else:
            MapLines.append("[?] " + Text["MAP.UNOPENED"].format(scene_id=LocationId))
    Paragraphs = [MessageText(Game, "UI.MAP_TITLE"), Text["UI.MAP_LEGEND"], "\n".join(MapLines), Text["MAP.START"]]
    # Reveal route descriptions only after their clues are acquired, then append the locked-route notice.
    if "C01" in Game["Clues"]:
        Paragraphs.append(Text["MAP.DESCENT"])
    if "C06" in Game["Clues"]:
        Paragraphs.append(Text["MAP.1F"])
    if "C08" in Game["Clues"]:
        Paragraphs.append(Text["MAP.WINDOW"])
        Paragraphs.append(Text["MAP.WINDOW_READY"] if CanLowerPainting(Game) else Text["MAP.WINDOW_MISSING"])
    if "C12" in Game["Clues"]:
        Paragraphs.append(Text["MAP.GF"])
    if "C09" in Game["Clues"]:
        Paragraphs.append(Text["MAP.SERVICE"])
        Paragraphs.append(Text["MAP.KEY_READY"] if "service_key" in Game["Tools"] else Text["MAP.KEY_MISSING"])
    Paragraphs.append(Text["UI.LOCKED_ROUTE"])
    return Paragraphs


# Build the current scene's styled paragraphs and narrative from the existing game state.
def SceneParagraphs(Game):
    Scene = Game["Scene"]
    # Show choices or code instructions directly below the scene; danger shows recovery/surrender choices.
    if Scene == "DANGER":
        Narration = [Text[Game["Danger"]]]
        Paragraphs = Narration + [Text["DANGER.PROMPT"]]
    else:
        Paragraphs = list(SceneText[Scene])
        if Scene == "P1.NEXT" and "lowering_line" in Game["Tools"]:
            Paragraphs[1] = Text["P1.LINE_HELD"]
        if Scene == "P2.AFTER" and "lifting_sling" in Game["Tools"]:
            Paragraphs[2] = Text["P2.SLING_HELD"]
        if Scene == "P2.AFTER" and "service_key" in Game["Tools"]:
            Paragraphs[-1] = Text["P2.KEY_HELD"]
        if Scene == "P2.DESCENT":
            if CanLowerPainting(Game):
                Paragraphs.append(Text["P2.WINDOW_READY"])
            else:
                Missing = [Text["TOOL." + Tool.upper()] for Tool in ("lowering_line", "lifting_sling")
                           if Tool not in Game["Tools"]]
                Paragraphs.append(Text["P2.WINDOW_INCOMPLETE"].format(tools=", ".join(Missing)))
        Narration = list(Paragraphs)
        if Scene in WindowPlanScenes:
            Choice = Game["WindowPlan"][WindowPlanScenes.index(Scene)]
            if Choice:
                Paragraphs.append(Text["P2.PLAN_SELECTED"].format(choice=Choice))
        if Scene == "P2.REVIEW":
            Paragraphs.append(WindowPlanSummary(Game))
        if Scene == "P6.LOCK":
            Paragraphs.append(MessageText(Game, "P6.PROMPT"))
        else:
            Paragraphs.append("\n".join(SceneChoices(Game)))
            if Scene == "P4.ROUTE" and "service_key" not in Game["Tools"]:
                Paragraphs.append(Text["P4.SERVICE_LOCKED"])
    if Game["Notice"]:
        # Put feedback first so long scenes do not push input errors or recovery results to later pages.
        Feedback = MessageText(Game, Game["Notice"])
        Paragraphs.insert(0, Feedback)
        if Game["Notice"] in ("P1.LINE_TAKEN", "P2.SLING_TAKEN", "P2.KEY_TAKEN",
                              "P2.WAIT", "P5.WAIT", "DANGER.RECOVER"):
            Narration.append(Feedback)
    # Parse story markup before adding the already-styled clue paragraphs.
    Paragraphs = [rich.text.Text.from_markup(Paragraph, emoji=False) for Paragraph in Paragraphs]
    # Place scene clues after choices and feedback, keeping the notebook notice for new clues.
    if Scene != "DANGER":
        for ClueId in SceneInfo[Scene][2]:
            Paragraphs.extend(ClueParagraphs(Game, [ClueId], ClueId in Game["Unread"]))
    return Paragraphs, Narration
