# Terminal layout, styled output, and narrative pacing.
import math
import os
import re
import subprocess
import time
import unicodedata
import rich

from game_state import Settings
from game_text import Text, Locations, Clues


rich.reconfigure(markup=False, highlight=False, emoji=False)
GameConsole = rich.get_console()
GameConsole.push_theme(rich.theme.Theme({
    "clue.id": "bold #ff8c00",
    "clue.title": "bold #ff8c00",
    "clue.key": "bold yellow",
    "clue.blue": "bold blue",
    "clue.red": "bold red",
    "result.win": "bold blue",
    "result.loss": "bold red",
}))


# Keep input-width checks and let Rich wrap styled output.
def CharacterWidth(Character):
    # The English version treats combining characters as zero columns and wide/fullwidth characters as two.
    if unicodedata.combining(Character):
        return 0
    if unicodedata.east_asian_width(Character) in ("W", "F"):
        return 2
    return 1


# Sum character widths to calculate the display columns occupied by a string.
def DisplayWidth(Content):
    Width = 0
    for Character in Content:
        Width += CharacterWidth(Character)
    return Width


# Wrap paragraphs to 78 columns, retaining styles and a blank line between paragraphs.
def ParagraphLines(Paragraphs):
    Lines = []
    for Paragraph in Paragraphs:
        if Lines:
            Lines.append(rich.text.Text(""))
        Styled = rich.text.Text.assemble(Paragraph)
        Styled.highlight_words(Clues, "clue.id")
        Lines.extend(Styled.wrap(GameConsole, 78, overflow="fold"))
    return Lines


# Identify narrative lines using the same markup and wrapping as the page.
def StoryLines(Paragraphs):
    Styled = [rich.text.Text.from_markup(Paragraph, emoji=False) for Paragraph in Paragraphs]
    return {Line.plain for Line in ParagraphLines(Styled) if Line.plain}


# Print styled words at the selected speed, or print the whole line immediately.
def PrintStoryLine(Line):
    if Settings["TextSpeed"] == "instant":
        GameConsole.print(Line)
        return
    Factor = 0.5 if Settings["TextSpeed"] == "fast" else 1
    for Word in re.finditer(r"\S+\s*|\s+", Line.plain):
        GameConsole.print(Line[Word.start():Word.end()], end="")
        Content = Word.group().strip().rstrip("\"'\u2019\u201d)]")
        if Content:
            Delay = 0.06
            if Content.endswith((".", "!", "?")):
                Delay += 0.25
            elif Content.endswith((",", ";", ":")):
                Delay += 0.10
            time.sleep(Delay * Factor)
    GameConsole.print()


# Pause while an attached console is below 80 columns or 24 rows.
def WaitForTerminal():
    while True:
        Width, Height = os.get_terminal_size()
        if Width >= 80 and Height >= 24:
            return
        subprocess.run(["clear"])
        GameConsole.print(Text["UI.RESIZE"])
        input(Text["UI.RESIZE_PROMPT"] + " ")


# Use the same minute-and-second display in the header and ending summary.
def TimeText(Game):
    Minutes, Seconds = divmod(math.ceil(Game["TimeLeft"]), 60)
    return f"{Minutes:02d}:{Seconds:02d}"


# Print the current game view in normal top-to-bottom console order.
def DrawFrame(Game, Title, Lines, Footer, Prompt, Story=()):
    WaitForTerminal()
    subprocess.run(["clear"])
    Header = Text["UI.HEADER"].format(
        location=Locations[Game["Location"]], steps=Game["Steps"],
        time_left=TimeText(Game))
    GameConsole.print(Header)
    GameConsole.print(Title)
    GameConsole.print()
    for Line in Lines:
        Content = str(Line)
        if Content in Story and Content not in Game["ReadStory"]:
            PrintStoryLine(Line)
            Game["ReadStory"].add(Content)
        else:
            GameConsole.print(Line)
    if Footer:
        GameConsole.print()
        GameConsole.print(Footer)
    if Prompt:
        GameConsole.print(Prompt)
