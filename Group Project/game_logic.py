# Action availability, state transitions, and escape ratings.
from game_data import Actions, WindowPlanScenes
from game_state import EnterScene, SpendSteps
from puzzles import LockCode, ValidCode


# Both collected tools are needed to lower the painting separately from the player.
def CanLowerPainting(Game):
    return "lowering_line" in Game["Tools"] and "lifting_sling" in Game["Tools"]


# Collected tools disappear from their pickup menus; the key opens the service stair.
def AvailableActions(Game):
    Available = dict(Actions[Game["Scene"]])
    HasKey = "service_key" in Game["Tools"]
    if Game["Scene"] == "P4.ROUTE" and not HasKey:
        del Available["4"]
    if HasKey and Game["Scene"] == "P2.AFTER":
        del Available["4"]
    if "lowering_line" in Game["Tools"] and Game["Scene"] == "P1.NEXT":
        del Available["2"]
    if "lifting_sling" in Game["Tools"] and Game["Scene"] == "P2.AFTER":
        del Available["5"]
    if Game["Scene"] == "P2.DESCENT":
        if not CanLowerPainting(Game):
            Available["1"] = [1, "WINDOW_ESCAPE", ""]
            del Available["2"]
        elif 0 in Game["WindowPlan"]:
            del Available["2"]
    return Available


# Process an action, update game state, and return a feedback text key (empty means no feedback).
def TakeAction(Game, Answer):
    # Reject actions after an ending, overlong input, and empty input before changing game state.
    if Game["Ending"]:
        return "UI.INVALID"
    if Answer is None:
        return "UI.TOO_LONG"
    Answer = Answer.strip()
    if Answer == "":
        return "UI.EMPTY"
    Scene = Game["Scene"]
    # In danger, surrender or spend two steps to recover to the checkpoint.
    if Scene == "DANGER":
        if Answer == "2":
            Game["Ending"] = "SURRENDER"
            return ""
        if Answer != "1":
            return "UI.INVALID"
        if not SpendSteps(Game, 2):
            return ""
        Game["Scene"] = Game["Checkpoint"]
        Game["Danger"] = ""
        return "DANGER.RECOVER"
    # Enter back in the window submenu to return to its caller without spending steps.
    if Scene == "P2.WINDOW" and Answer.lower() == "back":
        Game["Scene"] = Game["WindowCaller"]
        return ""
    # Planning pages return one level and retain every recorded choice.
    WindowBack = {"P2.DESCENT": "P2.WINDOW", "P2.PASS": "P2.DESCENT",
                  "P2.GEAR": "P2.PASS", "P2.ORDER": "P2.GEAR", "P2.REVIEW": "P2.ORDER"}
    if Scene in WindowBack and Answer.lower() == "back":
        EnterScene(Game, WindowBack[Scene])
        return ""
    # Leaving the supply alcove is free; taking its key is a separate, paid choice.
    if Scene == "P2.SUPPLY" and Answer.lower() == "back":
        EnterScene(Game, "P2.AFTER")
        return ""
    # Final lock: a valid-format attempt costs one step; five wrong codes trigger lockout.
    if Scene == "P6.LOCK":
        if not ValidCode(Answer):
            return "P6.FORMAT"
        if not SpendSteps(Game, 1):
            return ""
        if Answer == LockCode(Game):
            Game["Ending"] = "WIN"
            return ""
        Game["Errors"] += 1
        if Game["Errors"] == 5:
            Game["Ending"] = "LOCK"
        return "P6.WRONG"
    # Look up ordinary scene actions in the option table; only valid options spend their listed cost.
    Available = AvailableActions(Game)
    if Answer not in Available:
        return "UI.INVALID"
    Cost, Destination, Message = Available[Answer]
    if Cost > 0 and not SpendSteps(Game, Cost):
        return ""
    if Scene in WindowPlanScenes:
        Game["WindowPlan"][WindowPlanScenes.index(Scene)] = int(Answer)
    # Execute the whole plan once; both tools and all three choices are needed for a win.
    if Destination == "WINDOW_ESCAPE":
        if CanLowerPainting(Game) and Game["WindowPlan"] != [3, 1, 2]:
            Destination, Message = "DANGER", "P2.PLAN_WRONG"
        else:
            Game["Ending"] = "WINDOW_WIN" if CanLowerPainting(Game) else "WINDOW_EMPTY"
            Game["Location"] = "S10"
            Game["Visited"].append("S10")
            return ""
    # Save the recovery scene and danger description; danger at the window returns to its calling scene.
    if Destination == "DANGER":
        Game["Checkpoint"] = Scene
        if Scene == "P2.WINDOW":
            Game["Checkpoint"] = Game["WindowCaller"]
        elif Scene == "P2.REVIEW":
            Game["Checkpoint"] = "P2.DESCENT"
        Game["Danger"] = Message
        Game["Scene"] = "DANGER"
        Game["CloseCalls"] += 1
        return ""
    if Scene == "P2.SUPPLY" and Answer == "1":
        Game["Tools"].add("service_key")
    if Scene == "P1.NEXT" and Answer == "2":
        Game["Tools"].add("lowering_line")
    if Scene == "P2.AFTER" and Answer == "5":
        Game["Tools"].add("lifting_sling")
    # Remember the return scene before entering the window; EnterScene updates other locations and clues.
    if Destination == "P2.WINDOW":
        Game["WindowCaller"] = Scene
    if Destination != Scene:
        EnterScene(Game, Destination)
    return Message


# Ratings describe escapes with the painting. Reading clues, notes, or hints does not affect the rating.
def EscapeRating(Game):
    if Game["Ending"] not in ("WIN", "WINDOW_WIN"):
        return ""
    if Game["CloseCalls"] == 0 and Game["Errors"] == 0 and Game["Steps"] >= 10:
        return "CLEAN"
    if Game["CloseCalls"] <= 1 and Game["Errors"] <= 2 and Game["Steps"] >= 6:
        return "STEADY"
    return "NARROW"
