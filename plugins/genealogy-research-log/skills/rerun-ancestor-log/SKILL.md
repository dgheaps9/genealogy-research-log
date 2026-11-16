---
name: rerun-ancestor-log
description: Re-checks one ancestor's FamilySearch record after the user has corrected the tree, then updates their existing Ancestor Research Log, Ancestor Story (if any), Research Tracker and Project copies. Use when the user says "fixed", "fixed, run again", "run again", "rerun", "re-run" or "check and update" for a person who already has a research log.
---

# Rerun an Ancestor Research Log

The user has made some of the log's suggested Tree Actions (or other fixes) in FamilySearch and wants the log brought up to date. This is a re-check, not a fresh research run. If the user's Claude Project has its own instructions, those take priority.

## 0. Start

1. Identify the person (name, or name and PID). Find the Genealogy folder (connected folder with `_tools/make_log.sh`) and the existing log in it or in `Not in my line/`.
2. Load `_data/data_<Full Name> <year>.json`. If it is missing, make it with `python3 _tools/extract.py "<log.docx>" "_data/data_<Full Name> <year>.json"`.
3. If no log exists, say so and offer a full research run (ancestor-research-log skill) instead.
4. Make a short task list: re-read FamilySearch, compare, update data, rebuild log, story, tracker, Project copies.

## 1. Re-read FamilySearch (Claude in Chrome)

- Open `https://www.familysearch.org/tree/person/details/<PID>` and the Sources tab `https://www.familysearch.org/tree/person/sources/<PID>`. Read with get_page_text (re-read if only the page shell loaded).
- If the PID now redirects (a merge), note the surviving PID and use it.
- List what changed since the log was made: vitals, names, spouses, children, parents, and newly attached or detached sources.

## 2. Compare with the log

For each Tree Action in the data file, decide: **Done** (the tree now matches), **Partly done** (say what is left), or **Not done**. Also note anything new that is now inconsistent (e.g. a merge brought in a conflicting date).

Do not repeat the full record search. Only follow up a newly attached source or a new conflict. If something needs real new research, list it in "Still to search" and offer a full research run.

## 3. Update the data file

- `sources`: set "Attached in FS?" to Y for sources now attached; add newly attached sources with full citation (helpers.py `cite()`) and URL.
- `ident`, `vitals`, `spouses`, `children`: update to match the corrected tree, keeping confidence levels and conflict notes accurate.
- `actions`: remove actions that are done, rewrite partly done ones to cover only what is left, add new ones for new issues. Renumber.
- `notes`: add one row, e.g. `RERUN <d Mon yyyy>: ` (bold) + which Tree Actions were confirmed done, what changed in the tree and what is left. Update "Still to search".

## 4. Rebuild and update

1. `bash "<Genealogy>/_tools/make_log.sh" "<Full Name> <year>"` (add `"Not in my line"` for non-ancestors). The old log goes to `Superseded/` with today's date; if a copy with that name already exists, ask before overwriting.
2. If the data file has a `story` section: update any story facts the corrections changed (keep the rest as written; footnote numbers must still match) and run `python3 "<Genealogy>/_tools/story.py" "<Full Name> <year>"`. If it has none, don't ask about a story unless the user does.
3. `python3 "<Genealogy>/_tools/tracker.py"`. Removed Tree Actions lower the "Tree Actions in log" count, so tell the user to reset their "Tree Actions done" entry for this person (usually to 0).
4. If this conversation belongs to a Claude Project, save the updated log .md (and story .md, if rebuilt) to `claude/`, replacing the earlier copies.

## 5. Check and reply

- Check the new PDF's Tree Actions page and Sources table.
- Reply briefly: which actions are confirmed done, what is still open, anything new found, and whether the story was updated.
