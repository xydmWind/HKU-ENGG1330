# Input, shortcuts, information pages, and nested menus.
import os
import subprocess
import time
import rich

from content import ClueParagraphs, MapParagraphs, MessageText
from display import DisplayWidth, DrawFrame, GameConsole, ParagraphLines, StoryLines, TimeText
from game_data import SceneInfo
from game_logic import EscapeRating
from game_state import Settings
from game_text import Text, Hints, Commands
from storage import SaveGame, LoadGame


# Show the title in a fixed 80-column, 24-row layout and wait for Enter.
def ShowStartScreen(Game):
    while ScreenActive(Game):
        subprocess.run(["clear"])
        GameConsole.print("\n" * 5, end="")
        for Line in Text["UI.START_ART"]:
            GameConsole.print(" " * 20 + Line)
        GameConsole.print()
        GameConsole.print(Text["UI.START_PROMPT"].center(80))
        Answer = input().strip().lower()
        if Answer == "":
            return
        if Answer in ("board", "setting"):
            OpenShortcut(Game, Answer)


# Leave suspended screens when a shortcut requests a different menu or game.
def ScreenActive(Game):
    return not Game["MenuRequest"] and (not Game["TimerRunning"] or not Game["Ending"])


# Switch to an existing utility menu, or open one above the current screen.
def OpenShortcut(Game, Command):
    if Command in Game["OpenMenus"]:
        Game["MenuRequest"] = Command
        return
    Game["OpenMenus"].append(Command)
    if Command == "board":
        ShowBoard(Game)
    else:
        ShowSettings(Game)
    Game["OpenMenus"].pop()


# Each wait is timed once; shortcuts return here without submitting a scene action.
# Board treats its own name as note text while keeping setting available.
def ReadInput(Game, Title, Lines, Footer, Prompt, Limit=20, Story=(), BoardShortcut=True):
    while ScreenActive(Game):
        DrawFrame(Game, Title, Lines, Footer, Prompt, Story)
        Started = time.monotonic()
        Answer = input("> ")
        if Game["TimerRunning"]:
            Game["TimeLeft"] = max(0.0, Game["TimeLeft"] - (time.monotonic() - Started))
            if Game["TimeLeft"] == 0:
                Game["Ending"] = "TIME"
                return None
        if len(Answer) > Limit or DisplayWidth(Answer) > Limit:
            return None
        Command = Answer.strip().lower()
        if Command == "setting" or (BoardShortcut and Command == "board"):
            OpenShortcut(Game, Command)
            continue
        return Answer
    return None


# Choose one save number; back cancels without changing the current progress.
def ShowSaveMenu(Game, Command):
    Mode = Command.upper()
    Notice = ""
    while ScreenActive(Game):
        Lines = ParagraphLines([Text[Mode + ".SLOTS"]]) + [""]
        for Number in range(10):
            Status = Text["SAVE.EXISTS"] if os.path.exists(f"save{Number}.txt") else Text["SAVE.EMPTY"]
            Lines.append(f"{Number}. {Status}")
        Answer = ReadInput(Game, Text[Mode + ".TITLE"], Lines, Notice, Text["SAVE.INPUT"])
        if Answer is not None:
            Number = Answer.strip().lower()
            if Number == "back":
                return ""
            if len(Number) == 1 and Number in "0123456789":
                return SaveGame(Game, Number) if Command == "save" else LoadGame(Game, Number)
        Notice = Text["SAVE.INVALID"]


# Display information in pages of 17 lines; next/prev turn pages and back returns to the caller.
def ShowPages(Game, Paragraphs, Title, Opening=False, Story=()):
    Lines = ParagraphLines(Paragraphs)
    PageCount = max(1, (len(Lines) + 16) // 17)
    Page = 0
    Notice = ""
    # Ending pages stay readable after the game timer has stopped.
    while ScreenActive(Game):
        Footer = Text["UI.PAGE"].format(page=Page + 1, pages=PageCount)
        if Page == PageCount - 1:
            Footer = Text["UI.LAST_PAGE"].format(page=Page + 1, pages=PageCount)
        # Normally show the page number; temporarily replace the footer with any input-error notice.
        if Notice:
            Footer = Notice
        Prompt = Text["UI.START_INPUT"] if Opening else Text["UI.PAGE_INPUT"]
        Answer = ReadInput(Game, Title, Lines[Page * 17:(Page + 1) * 17], Footer, Prompt, Story=Story)
        # Keep paging between the first and last pages; invalid input only updates the notice.
        if Answer is None:
            Notice = Text["UI.TOO_LONG"]
            continue
        Answer = Answer.strip().lower()
        if Answer == "back":
            return
        if Answer == "next":
            Page = min(Page + 1, PageCount - 1)
            Notice = ""
        elif Answer == "prev":
            Page = max(Page - 1, 0)
            Notice = ""
        elif Answer == "":
            Notice = Text["UI.EMPTY"]
        else:
            Notice = Text["UI.INVALID"]


# A plain list of text lines: type to append, or edit a numbered line in place.
def ShowBoard(Game):
    Page = 0
    Editing = None
    Notice = ""
    while ScreenActive(Game) or Game["MenuRequest"] == "board":
        if Game["MenuRequest"] == "board":
            Game["MenuRequest"] = ""
            Notice = ""
        Lines = [f"{Index}. {Content}" for Index, Content in enumerate(Game["Board"], 1)]
        if not Lines:
            Lines = [Text["BOARD.EMPTY"]]
        PageCount = max(1, (len(Lines) + 16) // 17)
        Page = min(Page, PageCount - 1)
        Footer = Notice or Text["BOARD.PAGE"].format(page=Page + 1, pages=PageCount)
        Prompt = Text["BOARD.INPUT"] if Editing is None else Text["BOARD.EDIT_INPUT"].format(line=Editing + 1)
        Answer = ReadInput(Game, Text["BOARD.TITLE"], Lines[Page * 17:(Page + 1) * 17],
                           Footer, Prompt, Limit=60, BoardShortcut=False)
        if Game["MenuRequest"]:
            continue
        if Answer is None:
            Notice = Text["UI.TOO_LONG"]
            continue
        Command = Answer.strip().lower()
        Notice = ""
        if Editing is not None:
            if Command != "back":
                if Answer.strip():
                    Game["Board"][Editing] = Answer
                else:
                    del Game["Board"][Editing]
            Editing = None
            continue
        if Command == "back":
            return
        if Command in ("next", "prev"):
            Page = min(Page + 1, PageCount - 1) if Command == "next" else max(Page - 1, 0)
        elif Command:
            Parts = Command.split()
            if Parts[0] == "edit":
                if len(Parts) == 2 and Parts[1].isdecimal():
                    Index = int(Parts[1]) - 1
                    if 0 <= Index < len(Game["Board"]):
                        Editing = Index
                        Page = Index // 17
                        continue
                Notice = Text["BOARD.INVALID_LINE"]
            else:
                Game["Board"].append(Answer)
                Page = (len(Game["Board"]) - 1) // 17


# Offer two hint levels for the current puzzle, using the checkpoint puzzle in danger; back returns.
def ShowHints(Game):
    Scene = Game["Scene"]
    if Scene == "DANGER":
        Scene = Game["Checkpoint"]
    Puzzle = SceneInfo[Scene][1]
    Notice = ""
    while ScreenActive(Game):
        Answer = ReadInput(Game, Text["UI.HINT_TITLE"], ParagraphLines([Text["UI.HINT_MENU"]]), Notice, Text["UI.HINT_INPUT"])
        if Answer is None:
            Notice = Text["UI.TOO_LONG"]
            continue
        Answer = Answer.strip().lower()
        if Answer == "back":
            return
        # Hint choices 1/2 select list indices 0/1; return to the hint menu after displaying a hint.
        if Answer in ("1", "2"):
            ShowPages(Game, [Hints[Puzzle][int(Answer) - 1]], Text["UI.HINT_TITLE"])
            Notice = ""
        else:
            Notice = Text["UI.EMPTY"] if Answer == "" else Text["UI.INVALID"]


# Menus accept their displayed number or name and return to their parent with back.
def MenuChoice(Game, Title, Menu, Options, Notice=""):
    while ScreenActive(Game):
        Answer = ReadInput(Game, Title, ParagraphLines([Menu]), Notice, Text["UI.MENU_INPUT"])
        if Answer is None:
            Notice = Text["UI.TOO_LONG"]
            continue
        Answer = Answer.strip().lower()
        if Answer == "back":
            return ""
        for Number, Option in enumerate(Options, 1):
            if Answer in (str(Number), Option):
                return Option
        Notice = Text["UI.EMPTY"] if Answer == "" else Text["UI.INVALID"]
    return ""


# Keep discovered evidence and the player's notes under the same notebook menu.
def ShowNotebook(Game):
    while ScreenActive(Game):
        Choice = MenuChoice(Game, Text["NOTEBOOK.TITLE"], Text["NOTEBOOK.MENU"], ("clue", "board"))
        if Choice == "clue":
            Paragraphs = [Text["UI.NOTEBOOK_TITLE"]]
            if Game["Clues"]:
                Paragraphs.extend(ClueParagraphs(Game, Game["Clues"]))
            else:
                Paragraphs.append(Text["UI.NOTEBOOK_EMPTY"])
            ShowPages(Game, Paragraphs, Text["UI.NOTEBOOK_HEADING"])
        elif Choice == "board":
            OpenShortcut(Game, "board")
        else:
            return


# Puzzle hints and the full instructions return to this help menu after reading.
def ShowHelpMenu(Game):
    while ScreenActive(Game):
        Choice = MenuChoice(Game, Text["HELP.TITLE"], Text["HELP.MENU"], ("hint", "help"))
        if Choice == "hint":
            ShowHints(Game)
        elif Choice == "help":
            ShowPages(Game, Text["HELP"], Text["UI.HELP_TITLE"])
        else:
            return


# Apply a session preference; the existing save format contains only game progress.
def ShowSpeedMenu(Game):
    Menu = Text["SPEED.MENU"].format(speed=Text["SPEED." + Settings["TextSpeed"].upper()])
    Choice = MenuChoice(Game, Text["SPEED.TITLE"], Menu, ("normal", "fast", "instant"))
    if Choice:
        Settings["TextSpeed"] = Choice
        return Text["SPEED.CHANGED"].format(speed=Text["SPEED." + Choice.upper()])
    return ""


# Settings return session actions or a loaded-game result to the calling screen.
def ShowSettings(Game):
    Notice = ""
    while ScreenActive(Game) or Game["MenuRequest"] == "setting":
        if Game["MenuRequest"] == "setting":
            Game["MenuRequest"] = ""
            Notice = ""
        Choice = MenuChoice(Game, Text["SETTING.TITLE"], Text["SETTING.MENU"],
                            ("save", "load", "restart", "quit", "speed"), Notice)
        Notice = ""
        if Game["MenuRequest"]:
            continue
        if Choice in ("save", "load"):
            Result = ShowSaveMenu(Game, Choice)
            if Result == "SAVE.LOADED":
                Game["Notice"] = Result
                Game["MenuRequest"] = Result
                return Result
            Notice = Text[Result] if Result else ""
        elif Choice in ("restart", "quit"):
            Mode = Choice.upper()
            Confirm = MenuChoice(Game, Text[Mode + ".TITLE"], Text[Mode + ".MENU"], (Choice, "cancel"))
            if Confirm == Choice:
                Game["MenuRequest"] = Mode
                return Mode
        elif Choice == "speed":
            Notice = ShowSpeedMenu(Game)
        else:
            return ""
    return ""


# Handle the six free commands and return a viewing or session result to the game loop.
def HandleView(Game, Answer):
    if Answer is None:
        return ""
    # Trim surrounding whitespace and normalize case, then map this language's aliases to internal commands.
    Command = Commands.get(Answer.strip().lower(), "")
    if Command == "map":
        # The map displays known locations and unlocked route information.
        ShowPages(Game, MapParagraphs(Game), Text["UI.MAP_HEADING"])
    elif Command == "notebook":
        ShowNotebook(Game)
    elif Command == "bag":
        Paragraphs = [Text["BAG.PAINTING"]]
        for Tool in sorted(Game["Tools"]):
            Paragraphs.append(Text["TOOL." + Tool.upper()].capitalize() + "\n" + Text["BAG." + Tool.upper()])
        ShowPages(Game, Paragraphs, Text["BAG.TITLE"])
    elif Command == "status":
        # The status page uses MessageText to display current game values.
        ShowPages(Game, [MessageText(Game, "UI.STATUS")], Text["UI.STATUS_TITLE"])
    elif Command == "help":
        ShowHelpMenu(Game)
    elif Command == "setting":
        OpenShortcut(Game, "setting")
    else:
        return ""
    return "VIEWED"


# Show the ending reason and game statistics, then ask to restart or quit; True means restart.
def EndingMenu(Game):
    Narration = [Text["END." + Game["Ending"]]]
    Paragraphs = [rich.text.Text.from_markup(Narration[0], emoji=False)]
    Result = "WIN" if Game["Ending"] in ("WIN", "WINDOW_WIN") else "LOSS"
    ResultStyle = "result." + Result.lower()
    Summary = rich.text.Text(Text["END.SUMMARY"].format(
        result=Text["RESULT." + Result],
        reason=Text["REASON." + Game["Ending"]], steps=Game["Steps"], errors=Game["Errors"],
        clue_count=len(Game["Clues"]), close_calls=Game["CloseCalls"], time_left=TimeText(Game)))
    Summary.highlight_words([Text["RESULT." + Result]], ResultStyle)
    Art = rich.text.Text("\n".join(Text["END.ART." + Result]), style=ResultStyle)
    Paragraphs.extend([Art, Summary])
    Rating = EscapeRating(Game)
    if Rating:
        RatingPrefix = "RATING.WINDOW." if Game["Ending"] == "WINDOW_WIN" else "RATING."
        Paragraphs.append(Text[RatingPrefix + Rating])
        Narration.append(Text[RatingPrefix + Rating])
    ShowPages(Game, Paragraphs, Text["UI.END_TITLE"], Story=StoryLines(Narration))
    Notice = ""
    # Accept only 1 (restart) or 2 (quit); other input keeps the menu open with the appropriate notice.
    while ScreenActive(Game):
        Answer = ReadInput(Game, Text["UI.END_TITLE"], ParagraphLines([Text["END.RESTART"]]), Notice, Text["UI.END_INPUT"])
        if Answer is None:
            Notice = Text["UI.TOO_LONG"]
        elif Answer.strip() in ("1", "2"):
            return Answer.strip() == "1"
        else:
            Notice = Text["UI.EMPTY"] if Answer.strip() == "" else Text["UI.INVALID"]
