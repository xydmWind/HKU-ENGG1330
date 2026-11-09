# Museum Escape

## Basic Information

**Group Number:** 1E-08

**Tutorial Subclass:** 1E

**Members' Name:** Zhang Chenrui, Jiang Yiran, Liu Henghui, Leung Chiu Ming

**Container Version:** `engg1330-project:2026-v03`

**Environment:** Python and Rich library in the course container. Use a terminal of at least 80 columns by 24 rows. The interface and story are in English.

**Exact Run Command:**

In this Code folder, open the course-container terminal, then run:

```shell
python main.py
```

All nine companion modules must remain beside `main.py`.  Save files are created only when the player saves in the root folder.

**Starting and Exiting:** Press Enter at the title screen. Use `next` and `prev` to read the introduction and instructions, then enter `back` to begin. Enter a displayed option number and press Enter to act. During play, use `setting` → `quit` → `1` to exit, or `setting` → `restart` → `1` to start again. After an ending, enter `back` to leave the result pages, then choose `1` to restart or `2` to quit.

---

## Game Purpose and Rules

**Game Purpose:**

Museum Escape is a single-player, turn-based console puzzle adventure game. The goal is to escape **with the painting** before steps or time run out.

**Connected Puzzles:**

The clues and scene descriptions you obtain will help you solve puzzles. The player must combine multiple clues to solve the final puzzle, including the sequence and the digit value of a four-character code.

The key collected during the process can help players skip one puzzle. If the player finds two tools related to a lowering line during the process, and combines them with other clues, the player will be able to escape through the window instead of solving the four-character code lock.

There are 17 discoverable clues, labeled `C01`–`C17`. Clues are recorded automatically when their scenes are reached. Tools require explicit pickup actions. Optional clues are not all required for every route.

**Steps, Time, and Endings:**

- A new run begins with **24 steps** and **10 minutes** on the countdown. Ordinary actions normally cost 1 step; each option displays its cost. Some submenus and planning choices are free.
- An incorrect physical action usually costs 1 step and enters danger. Choose `1` to spend another 2 steps returning to the checkpoint, or `2` to surrender. Recovery does not refund steps or erase the recorded close call.
- At the staff exit, submit exactly four digits (`0`–`9`). Each correctly formatted submission costs 1 step; an incorrect code also adds one error. The fifth incorrect code ends the run. A format error costs no steps and does not count as a wrong code.
- The code is randomly generated when a new run starts. Its four tag values are distinct single digits; the clue numbers and correct code remain unchanged during that run and are preserved in a save. A new run can coincidentally generate the same code.
- Reading, viewing information, turning pages, writing notes, opening menus, and changing window-plan choices cost no steps. During active play, however, **waiting for input still consumes time**, including thinking, reading a displayed page, and using menus. Invalid and empty input also consume this waiting time.
- The timer starts in the first gameplay scene. Title/introductory screens, automatic text output, terminal-resize pauses, and ending screens are excluded. Time is updated when Enter is pressed. If time has expired, that input triggers a loss before the command, save, code, or escape action is executed.
- Win by opening the staff exit with the correct code or completing the window escape with both tools and a correct plan. There must still be at least 1 step left after the final action. An action that reduces steps to zero ends in failure even if its answer is correct.
- Other losses are surrender, five incorrect codes, time expiry, and escaping through the window without the painting. 

**Alternative Routes:**

- The service-key branch costs 1 step to enter the supply alcove and 1 step to take the key and return. The key enables a service-stair option after the crate puzzle, bypassing one action at the lobby. Collecting it therefore adds a net cost of 1 step compared with the direct fire-stair route. 
- For the window route, actively collect the lowering line beside the statue and the padded lifting sling at the cart. The line must be collected before leaving the statue floor. Entering the window inspection submenu is free; preparing the descent costs 1 step. With both tools, choose the backpack's passage orientation, the equipment for the painting and player, and the descent order. Choices can be revised without spending steps. Executing the complete plan costs 1 step. A wrong plan causes danger and preserves tools and choices for another attempt. Without both tools, the offered descent leaves the painting behind and ends in a loss.

**Commands:**

Commands are entered one line at a time. Menu names are case-insensitive, and surrounding command whitespace is ignored. Submenus accept their displayed number or name.

| Input | Function |
| --- | --- |
| Displayed number | Perform the current scene's action or select a menu item. |
| Four digits at the staff exit | Submit a code attempt. |
| `map` | Show the current, visited, visible, and unopened locations. |
| `notebook` | Choose `1` / `clue` to reread discovered evidence, or `2` / `board` to write notes. |
| `board` | Open the editable notes board directly. |
| `bag` | Show the painting and collected tools. |
| `status` | Show steps, code errors, close calls, clue count, location, and tools. |
| `help` | Choose `1` / `hint` for two levels of help with the current puzzle, or `2` / `help` for the instructions. |
| `setting` | Choose `save`, `load`, `restart`, `quit`, or `speed` (numbered `1`–`5`). |
| `next` / `prev` | Move between pages. |
| `back` | Return from a reading page or submenu, or cancel a note edit. Some route submenus also display a free `back` option. |

`board` and `setting` can also be opened from normal input prompts on reading pages, other menus, the title screen, and ending screens. Ordinary returns restore the calling screen and page. Successful loading, confirmed restarting, and confirmed quitting close the previous menus. 

**Notes, Saves, and Settings:**

- In `board`, type a line and press Enter to append it. Use `edit N` to replace line N; an empty replacement deletes that line, and `back` cancels the edit. Each note is limited to 60 characters and 60 display columns. Ordinary command input is limited to 20 characters and 20 display columns.
- The board stores the player's own reasoning. `setting` remains available while writing or editing; the word `board` itself is treated as note text inside the board.
- Use `setting` → `save` → a digit from `0` to `9`, and `setting` → `load` → the same digit to restore progress. The slot list shows `Saved` or `Empty`; `back` cancels slot selection. Saving to an occupied slot will overwrite it.
- Saves are plain-text files named `save0.txt` to `save9.txt` in the root folder. They preserve the scene, steps, remaining seconds, clues, visited locations, tools, random puzzle parameters, window-plan choices, notes, error counters, and danger checkpoint. Loading resumes at the saved scene's first page.
- Restarting resets progress, notes, tools, counters, window choices, steps, and time, and generates a new lock puzzle. Restart and quit require confirmation; `2` / `cancel` / `back` cancels. Neither action automatically saves or deletes existing save files.
- `setting` → `speed` offers Normal, Fast, and Instant narrative display. Fast halves the Normal pauses. This preference survives restarts and loads within the running program, but is not stored in save files; launching the program again restores Normal. Previously read narrative and information/menu text display immediately.

**Escape Ratings:**

| Rating | Conditions |
| --- | --- |
| Clean getaway | At least 10 steps remain; no close calls and no wrong codes. |
| Kept ahead | The first row does not apply; at least 6 steps remain, with at most 1 close call and at most 2 wrong codes. |
| Narrow escape | Any other successful escape with the painting. |

---

## Program Structure

| File in `Code` | Responsibility |
| --- | --- |
| `main.py` | Entry point, introduction, main gameplay loop, and restart/load/exit flow. |
| `game_data.py` | Scene locations, clue awards, action costs, destinations, and window-plan stages. |
| `game_state.py` | New-game state, scene entry, step deductions, and session preferences. |
| `game_logic.py` | Action availability, tool requirements, route progression, danger recovery, win/loss decisions, and ratings. |
| `puzzles.py` | Random lock generation, arithmetic/branch evaluation, code ordering, and four-digit validation. |
| `game_text.py` | English narrative, choices, clues, hints, location names, messages, and text-art banners. |
| `content.py` | Assemble scene text, currently available options, clue pages, maps, and window-plan summaries from state. |
| `display.py` | Rich styles, character widths, 78-column wrapping, narrative speed, terminal-size checks, and frame drawing. |
| `interaction.py` | Line input, elapsed input-wait timing, pagination, global shortcuts, notes, settings, hints, and ending menus. |
| `storage.py` | Ten-slot plain-text saving/loading and support for the preceding save format. |

---

## Tests

**Verification Record:**

The latest checks passed in course container at 2026-11-4 16:34.  

Checks covered three complete routes, invalid actions, danger and step boundaries, code validation, 20 generated lock puzzles, all 27 window plans, all four combinations of the two required tools, save/load behavior, notes and settings, timer behavior, restart/rating rules, and rendered content.

**Reproducible Gameplay Checks:**

| Test | Procedure | Expected result |
| --- | --- | --- |
| Normal play and win | Finish all the routes with no mistakes. | All win with the painting and receive Clean getaway when no errors or close calls occur. |
| Invalid action | Submit an empty line and an unknown command. | Show feedback; scene and steps remain unchanged. |
| Danger and recovery | At the first scene, enter `1`, then `1`. | Danger costs 1 step; recovery costs 2 more. Return to the first scene. |
| Surrender | At the first scene, enter `1`, then `2`. | A surrender loss is shown, followed by restart/quit options. |
| Invalid Code-format | At the staff lock, enter `123`, `12345`, `12a4`, and `1 2 3 4`. | Reject all four without spending steps or adding code errors. |
| Wrong-code limit | Reach the lock and enter `9999` five times. This repeated-digit value cannot equal a generated code with four distinct digits. | Lose on the fifth wrong code. |
| Final-step | Submit the correct final answer with enough time and 1 or 2 remaining steps. | With 1 step, lose when the cost reduces it to zero. With 2 steps, win with 1 remaining. |
| Window plan and recovery | Collect both tools, deliberately select a wrong plan, execute it, and recover with `1`. Revise the choices and try again. | The wrong execution causes danger; recovery returns to preparation. Tools and choices remain. |
| Window without tools | Reach window preparation without both tools and choose the offered solo descent. | The player leaves the painting behind; result is a loss. |
| Board and Setting | Enter `board`, write a line, use `edit 1`, open `setting`, change speed, return with `back`, and submit replacement text. Then test an empty replacement. | Editing resumes on the same line after settings; the replacement is kept, and an empty replacement deletes it. |
| Save/load and slots | Save a run with notes and collected tools to slots `0`–`9`. Change progress, load a slot, then overwrite one slot and inspect the others. Also try an empty slot. | Saved state, puzzle, notes, plan choices, and time return. Only the chosen slot is overwritten. An empty slot produces a feedback message. |
| Timeout | In an active scene or menu, wait until the saved input-wait allowance is exhausted, then press Enter. | A time-expiry loss takes priority over that input. |
| Restart and quit | Try `setting` → `restart` → `cancel` → `back`, then confirm a restart. Test the end-menu restart and confirmed quit as well. | Cancel preserves progress. Restart restores 24 steps and 10 minutes, clears run data, and preserves speed and saved files. Quit closes the program. |
| Display and resizing | In the course-container terminal, inspect pages at 80×24, then reduce the window during play and restore it. | Game should pause for resizing. |

---

## Known Limitations

- **Terminal size check:** The program checks length only after Enter. The program cannot monitor the terminal size real time or force a pause when the terminal becomes too small.
- **Terminal portability:** The implementation calls the Unix `clear` command. Therefore the program can only run in Mac or Linux(course container).
- **Save-Load robustness:** Malformed/truncated files are not caught. There is also no second confirmation when overwriting a occupied slot .
- **Timer and input timing:** The countdown is updated after Enter, rather than every second on screen. 

---

## Contribution Record

| Contribution | Related files or evidence | Member(s) |
| --- | --- | --- |
| Complete the story content and the design of the puzzles. | `game_data.py`, `game_text.py`, `puzzles.py` | Jiang Yiran |
| Build and test the game loop, gameplay and puzzle logic | `main.py`, `game_data.py`, `game_logic.py`, `interaction.py` | Zhang Chenrui, Liu Henghui |
| Build the content display, text printing and timer | `main.py`, `content.py`, `display.py`, `interaction.py` | Zhang Chenrui, Jiang Yiran |
| Build save/load and improve menu logic | `storage.py`, `interaction.py` | Zhang Chenrui |
| Game testing and improvement | `main.py`, `display.py`, `game_text.py` | Zhang Chenrui, Jiang Yiran, Liu Henghui, Leung Chiu Ming |
| Make the trailer video | `Trailer.mp4` | Liu Henghui |
| Make the demo video | `Demo.mp4` | Leung Chiu Ming |

---

## Sources and Acknowledgements

| Source | Use in this project |
| --- | --- |
| Rich | Third-party terminal styling and text wrapping. It is supplied by the course container environment. MIT license. |
