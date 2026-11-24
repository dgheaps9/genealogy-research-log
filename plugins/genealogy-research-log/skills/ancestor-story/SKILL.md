---
name: ancestor-story
description: Writes the Ancestor Story — a warm, footnoted narrative biography ("The Life of [Full Name], [birth year]–[death year]") of one person who already has an Ancestor Research Log — and builds it as .docx, .pdf and .md with story.py. Use when the user says "write the story for [name]", "with story", "make an ancestor story", answers Yes to "Write the Ancestor Story for [name] now?", or asks to update an existing story.
---

# Ancestor Story

Turn one person's finished research log into a readable life story for relatives. The story is built only from that person's `_data/data_<Full Name> <year>.json` — the same data as the log. If the user's Claude Project has its own instructions, those take priority over this skill where they differ.

Read `references/story-format.md` before writing.

## 0. Start

1. Find the Genealogy folder (the connected folder containing `_tools/story.py`). If `story.py` is missing, the toolkit is out of date: copy it from this plugin's `../ancestor-research-log/toolkit/` (`${CLAUDE_PLUGIN_ROOT}/skills/ancestor-research-log/toolkit/`) into `_tools`, together with the updated `tracker.py`, and tell the user.
2. Find `_data/data_<Full Name> <year>.json`. If there is no research log yet, say so and offer to make the log first (ancestor-research-log skill); the story needs it.
3. Find the user's name for the relationship line: the name set in the Project instructions (e.g. "with <name> in place of you/your"). If none is set, ask once: "What is your name as it appears in FamilySearch?"

## 1. Gather

- Use only facts already in the data file (ident, vitals, spouses, children, sources, notes). Do **no new genealogical research**.
- Brief web lookups for general historical context are allowed (what an occupation involved in that place and period, local industry, living conditions, a war or migration). Cite each one in a footnote with its own link. Keep these to the key occupations and places, usually no more than 5 lookups.
- Relationship: open `https://www.familysearch.org/tree/person/details/<PID>` in Claude in Chrome and use "View My Relationship". Copy the relationship exactly as shown, with the user's name in place of "you/your", and add "(FamilySearch, View My Relationship, accessed <d Mon yyyy>)". If it can't be opened or shows no relationship, write "Relationship to <user's name> not confirmed in FamilySearch" and the reason. Never describe the family path ("daughter of… niece of…").

## 2. Write

Follow `references/story-format.md`. In short:

- Warm and conversational, like a family historian talking to relatives — not a report. Stay accurate: never invent dialogue, feelings or motives. Say "probably" or "the records suggest" where the log's confidence is Probable or Possible.
- Chronological: origins and parents, birth and childhood, marriage(s), children, occupations and residences, migrations, military service, later life, death and burial. Add short, sourced historical context where it helps.
- Occupations: for the person and each spouse, every recorded occupation with year and place, how the work changed, what it involved day to day then and there, and the employer when a source names one. If a wife has no recorded occupation, mention any hints (pre-marriage work, "assisting" in a census); otherwise say plainly none is recorded.
- Numbered footnotes using the short citation (the collection title) and the record link; full citations stay in the log.
- End with "Open questions": what is still unknown.

## 3. Build

1. Add the `story` section to the data file (format in `references/story-format.md`).
2. Run `python3 "<Genealogy>/_tools/story.py" "<Full Name> <year>"`. It copies any older story to `Superseded/` with today's date (if a copy with that name already exists it says so — ask the user before overwriting), builds `Ancestor_Story_<Full Name> <year>.docx` and `.pdf` next to the log (including `Not in my line/`), writes the `.md` to `_claude_staging/`, and refreshes `Research_Tracker.xlsx` (Story (Y/N) = Y).
3. If no PDF was made (LibreOffice missing), convert the .docx in the workspace and copy the PDF back next to it.

## 4. Check and deliver

- Look at page 1 of the PDF: title, bold name/dates/PID/date-written line, relationship line, in that order ("LIVING – do not upload to Memories" first for a living person). Check every footnote number has a note.
- If this conversation belongs to a Claude Project, save the .md to the Project at `claude/Ancestor_Story_<Full Name> <year>.md`, replacing any earlier copy. The .md goes only to the Project, not the user's folder (story.py's `_claude_staging` copy is a working copy).
- Reply briefly with what the story covers and its open questions.

## Declined or unanswered

- User says No: run `python3 "<Genealogy>/_tools/story.py" "<Full Name> <year>" --status N`. It records N in the tracker, adds "Story declined <date>" to the log's Research Notes and rebuilds the log (older copy to Superseded). Save the updated log .md to the Project. They can ask later with "write the story for <Full Name>".
- No answer (scheduled or unattended run): don't write the story; run `--status awaiting` (tracker shows "N – awaiting answer", log unchanged) and tell the user the story is waiting for their answer.
