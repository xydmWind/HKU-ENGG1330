# AI Use

Generative AI used: Yes

## Entry

- **Member and date:** Zhang Chenrui, 2026-10-28

- **Tool and model/version, where available:** Codex (GPT 6 Astra)

- **Purpose:** Integrate the Rich library to replace the manual line-wrapping function and implement important text highlighting for the display.

- **Relevant prompts and outputs used, or retained transcript location:** 

  > Prompts: Can you help me use Rich to highlight important content (such as key information within clues) by changing its color and replace the current `WrapText` with Rich’s text-wrapping function?
  >
  > Outputs: Completed.
  > - Clue numbers have been changed to orange; key content is now in bold yellow; stamps are displayed in blue/red.
  > - `Rich` has replaced `WrapText`; the layout maintains a 78-column width and 17 lines per page.

- **Files/materials affected:** `game_text.py`, `display.py`, `content.py`

- **What we kept, changed or rejected:** Keep the highlight and replace the old `WrapText` function with Rich's text-wrapping function.

- **How we checked it; tests and corrections:** Check whether the highlighting contents are displayed properly for the whole gameplay.

## Entry

- **Member and date:** Zhang Chenrui, 2026-10-29

- **Tool and model/version, where available:** Codex (GPT 6 Astra)

- **Purpose:** Add clear inline comments to the code so teammates can easily understand the implementation logic and module functions.

- **Relevant prompts and outputs used, or retained transcript location:** 

  > Prompts: Can you add inline comments to my Python code files to explain what each function and key logic block does, so that my teammates can easily understand how my part works?
  >
  > Outputs: Completed.
  >
  > - Added module overviews and inline comments explaining text formatting, display layout parameters, and clue/content handling.
  > - Kept all executable code logic unchanged.

- **Files/materials affected:** All Python code files

- **What we kept, changed or rejected:** Kept the inline explanations for core functions and non-trivial logic; removed redundant line-by-line comments on self-explanatory assignments to keep the files clean and readable.

- **How we checked it; tests and corrections:** Reviewed every added comment against the actual code execution flow, ran the game to confirm no syntax errors or unintended behavioral changes were introduced, and verified readability with teammates.

## Entry

- **Member and date:** Liu Henghui, 2026-10-29 to 2026-11-04.

- **Tool and model/version, where available:** Codex (GPT 6.1 Sol, GPT 6 Astra), ElevenLabs (text-to-speech Eleven v4 (free trial))

- **Purpose:** Develop, edit and verify the *Museum Escape* trailer, ending in v11r17 (version 11, round 17), with the password puzzle as the main gameplay example.

- **Relevant prompts and outputs used**: 

  > I asked Codex to review the game and course brief, draft the narration, and build a trailer from actual terminal gameplay. For v11r17, I directed it to use the selected v6 visual style, macOS-style terminal windows and the November 1 voice-over I generated in ElevenLabs. 
  >
  > Codex wrote the Remotion scene code, produced motion graphics and captions, edited the gameplay excerpts, placed the narration and music on the timeline, and rendered the MP4. I reviewed the preview, requested frame-specific changes and chose the final cut.

- **Files/materials affected**: `MuseumEscape-v6-style-r17-2026-11-04.mp4`, including the English narration, captions, gameplay presentation, explanatory graphics, transitions and closing title.

- **What we kept, changed or rejected**: Earlier work included source and gameplay review, a HyperFrames prototype, Remotion drafts, storyboard refinements and trial renders. v11r17 uses the password-focused script and ElevenLabs voice-over, selected v6 artwork and motion techniques, and excerpts from actual gameplay. I rejected the v8, v9 and v10 visual treatments and directed a simpler edit. In v11r17 the narration was split into 12 segments at its original speed, and the end card was revised to a one-sentence game summary.

- **How we checked it, including tests and corrections**: Codex traced the gameplay excerpts to the original terminal recordings and checked the ten-minute, 24-step premise against the game source. The production checks verified that the original narration samples were retained, checked layout geometry across all 1,755 frames and confirmed that the exported video and audio decoded successfully. Preview review caught a brief overlap between the notes and password slots. Codex adjusted their paths and checked the transition again. The v11r17 MP4 is 58.517 seconds long.

## Entry

- **Member and date:** Zhang Chenrui, 2026-11-04
- **Tool and model/version, where available:** Codex (GPT 6 Astra)
- **Purpose:** Help me to write the README.md.
- **Relevant prompts and outputs used, or retained transcript location:** 

  > Prompts: Based on the existing brief outline, expand the points into complete sentences to finish this README.md.
  >
  > Outputs: Completed with the original format; the document notes existing limitations and items yet to be addressed.
- **Files/materials affected:** `README.md`
- **What we kept, changed or rejected:** Keep the necessary sentences and removed superfluous descriptions.
- **How we checked it; tests and corrections:** Check every sentences with the code and gameplay.

## Entry

- **Member and date:** Zhang Chenrui, 2026-11-10

- **Tool and model/version, where available:** Codex (GPT 6 Astra)

- **Purpose:** Generate an interactive HTML to visually present the overall code structure, module dependencies, and core functional workflows of the project.

- **Relevant prompts and outputs used, or retained transcript location:** 

  > Prompts: Based on our project source files, create a standalone HTML visualization page that clearly illustrates the codebase architecture, module relationships, and core gameplay functions for presentation and team reference.
  >
  > Outputs: Completed.
  >
  > - Built a self-contained HTML page featuring an interactive module architecture diagram, function-level breakdowns, and a step-by-step execution flow of the game loop.

- **Files/materials affected:** `game-code-guide.html`

- **What we kept, changed or rejected:** Kept the high-level architecture diagram, module dependency mapping, and interactive function descriptions.

- **How we checked it; tests and corrections:** Opened the HTML file in a browser to verify layout rendering and interactive components.
