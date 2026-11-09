# Read and write numbered game saves in the existing text format.
import os

from puzzles import LockPuzzleKeys


# Version 2 adds the three window choices before the player's note lines.
def SaveGame(Game, Number):
    with open(f"save{Number}.txt", "w") as File:
        File.write("MuseumEscape 2\n")
        for Key in ("Steps", "Errors", "CloseCalls"):
            File.write(str(Game[Key]) + "\n")
        File.write(str(Game["TimeLeft"]) + "\n")
        for Key in ("Scene", "Location", "Checkpoint", "WindowCaller", "Danger", "Ending", "Notice"):
            File.write(Game[Key] + "\n")
        for Key in ("Clues", "Visited", "Unread"):
            File.write(" ".join(Game[Key]) + "\n")
        File.write(" ".join(sorted(Game["Tools"])) + "\n")
        File.write(" ".join(str(Game["LockPuzzle"][Key]) for Key in LockPuzzleKeys) + "\n")
        File.write(" ".join(str(Choice) for Choice in Game["WindowPlan"]) + "\n")
        for Line in Game["Board"]:
            File.write(Line + "\n")
    return "SAVE.OK"


# Read into a separate dictionary, then replace the current state after reading finishes.
def LoadGame(Game, Number):
    if not os.path.exists(f"save{Number}.txt"):
        return "SAVE.MISSING"
    Saved = {}
    with open(f"save{Number}.txt", "r") as File:
        # The previous format starts directly with the remaining step count.
        Version = File.readline().rstrip("\n")
        Saved["Steps"] = int(File.readline()) if Version == "MuseumEscape 2" else int(Version)
        for Key in ("Errors", "CloseCalls"):
            Saved[Key] = int(File.readline())
        Saved["TimeLeft"] = float(File.readline())
        for Key in ("Scene", "Location", "Checkpoint", "WindowCaller", "Danger", "Ending", "Notice"):
            Saved[Key] = File.readline().rstrip("\n")
        for Key in ("Clues", "Visited", "Unread"):
            Saved[Key] = File.readline().split()
        Saved["Tools"] = set(File.readline().split())
        Numbers = [int(Value) for Value in File.readline().split()]
        Saved["LockPuzzle"] = dict(zip(LockPuzzleKeys, Numbers))
        if Version == "MuseumEscape 2":
            Saved["WindowPlan"] = [int(Choice) for Choice in File.readline().split()]
        else:
            Saved["WindowPlan"] = [0, 0, 0]
        Saved["Board"] = [Line.rstrip("\n") for Line in File]
    Game.update(Saved)
    return "SAVE.LOADED"
