# Program entry point and the game loop.
import rich

from content import SceneParagraphs
from display import GameConsole, ParagraphLines, StoryLines
from game_logic import TakeAction
from game_state import NewGame, Settings
from game_text import Text
from interaction import EndingMenu, HandleView, ReadInput, ShowPages, ShowStartScreen


# Display scenes, read commands, and execute actions until an ending is set.
def PlayGame(Game):
    Game["TimerRunning"] = True
    Page = 0
    while not Game["Ending"] and not Game["MenuRequest"]:
        Scene = Game["Scene"]
        Paragraphs, Narration = SceneParagraphs(Game)
        Lines = ParagraphLines(Paragraphs)
        Story = StoryLines(Narration)
        # Resume a loaded scene immediately; reading history is not part of the save file.
        if Game["Notice"] == "SAVE.LOADED":
            Game["ReadStory"].update(Story)
        PageCount = max(1, (len(Lines) + 16) // 17)
        Footer = Text["UI.COMMANDS"] + f" | {Page + 1}/{PageCount}"
        Answer = ReadInput(Game, Text["TITLE." + Scene], Lines[Page * 17:(Page + 1) * 17],
                           Footer, Text["UI.INPUT"], Story=Story)
        if Game["Ending"] or Game["MenuRequest"]:
            break
        # Scene paging is also free; stop at page boundaries without executing numbered actions.
        if Answer is not None:
            Command = Answer.strip().lower()
            if Command == "next":
                Page = min(Page + 1, PageCount - 1)
                continue
            if Command == "prev":
                Page = max(Page - 1, 0)
                continue
        # Process view commands first; send other input to TakeAction and save its feedback for the next turn.
        Result = HandleView(Game, Answer)
        if Result:
            continue
        Game["Unread"] = []
        Game["Notice"] = TakeAction(Game, Answer)
        Page = 0
    Game["TimerRunning"] = False
    return Game["MenuRequest"] or "ENDED"


# Run each game using Rich console output and ordinary line input.
def Main():
    Settings["TextSpeed"] = "normal"
    Game = NewGame()
    ShowStartScreen(Game)
    Result = Game["MenuRequest"]
    # Requests unwind every open screen before restarting, loading, or leaving.
    while Result != "QUIT":
        if Result == "RESTART":
            Game = NewGame()
            Result = ""
        if Result != "SAVE.LOADED":
            Opening = [rich.text.Text.from_markup(Paragraph, emoji=False) for Paragraph in Text["OPEN"]]
            ShowPages(Game, Opening + Text["HELP"], Text["UI.TITLE"],
                      Opening=True, Story=StoryLines(Text["OPEN"]))
            Result = Game["MenuRequest"]
            if Result in ("RESTART", "QUIT"):
                continue
        Game["MenuRequest"] = ""
        Result = PlayGame(Game)
        if Result == "ENDED":
            Restart = EndingMenu(Game)
            Result = Game["MenuRequest"] or ("RESTART" if Restart else "QUIT")
    GameConsole.print(Text["END.QUIT"])


# Start the game only when this file is run directly, not when it is imported as a module.
if __name__ == "__main__":
    Main()
