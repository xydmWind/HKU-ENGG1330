# Game progress and session preferences.
from game_data import SceneInfo
from puzzles import NewLockPuzzle


# Text speed belongs to the session, so restarting or loading does not change it.
Settings = {"TextSpeed": "normal"}


# Create a game with 24 initial steps and a ten-minute countdown.
def NewGame():
    # Steps/Errors track remaining steps and wrong codes; Clues/Visited store clues and visited locations.
    # Checkpoint is the danger recovery scene, WindowCaller is the pre-window scene, and Ending stores the result.
    # Unread stores newly acquired clue IDs; Notice holds feedback for the next turn.
    # ReadStory tracks displayed narrative lines for this run only; it is not saved.
    # TimeLeft stores seconds; TimerRunning excludes the opening and ending pages.
    # MenuRequest and OpenMenus route shortcuts and are not part of a saved game.
    # WindowPlan records passage, equipment, and order choices; zero means not chosen.
    Game = {"Steps": 24, "Errors": 0, "Clues": [], "Visited": [],
            "Scene": "", "Location": "S01", "Checkpoint": "",
            "WindowCaller": "", "Danger": "", "Ending": "",
            "Unread": [], "Notice": "", "CloseCalls": 0, "Tools": set(),
            "TimeLeft": 600.0, "TimerRunning": False,
            "Board": [], "LockPuzzle": NewLockPuzzle(), "ReadStory": set(),
            "MenuRequest": "", "OpenMenus": [], "WindowPlan": [0, 0, 0]}
    EnterScene(Game, "P1.OPEN")
    return Game


# Change the scene and location, and record newly acquired clues.
def EnterScene(Game, Scene):
    Game["Scene"] = Scene
    Game["Location"] = SceneInfo[Scene][0]
    Game["Unread"] = []
    # Record each visited location and acquired clue once; also queue new clues for display.
    if Game["Location"] not in Game["Visited"]:
        Game["Visited"].append(Game["Location"])
    for ClueId in SceneInfo[Scene][2]:
        if ClueId not in Game["Clues"]:
            Game["Clues"].append(ClueId)
            Game["Unread"].append(ClueId)


# Deduct the action cost, set a loss at zero or fewer steps, and report whether the action can continue.
def SpendSteps(Game, Cost):
    Game["Steps"] -= Cost
    if Game["Steps"] <= 0:
        Game["Ending"] = "STEPS"
        return False
    return True
