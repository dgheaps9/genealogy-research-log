# Genealogy Research Log

A free Claude plugin for family historians. Give Claude an ancestor's name and FamilySearch ID; it searches FamilySearch and the genealogy sites you subscribe to, then delivers a finished **Ancestor Research Log** (.docx, .pdf and .md) with:

- vital events, spouses and children, each with a confidence level (Proven / Probable / Possible)
- a Sources table with full citations, a clickable link for every source, and whether it is already attached in FamilySearch
- research notes, including every search performed (even those that found nothing)
- **Tree Actions Suggested** — step-by-step fixes for problems in your FamilySearch tree, with a citation and link at each step

After each log, Claude offers an optional **Ancestor Story** — a warm, footnoted life story ("The Life of Mary Example, 1874–1940") written from the same research, with your FamilySearch relationship and what each occupation involved in its time and place. When you have fixed your tree, say **"fixed, run again"** and Claude re-checks FamilySearch and updates the log and story.

Claude never edits FamilySearch. It suggests the fixes; you make them.

## What's included

| Skill | What it does |
|---|---|
| **genealogy-setup** | Walks you through a paid Claude plan, the Claude desktop app, Claude in Chrome, signing in to your genealogy sites, connecting your Genealogy folder, installing the toolkit, and creating a Claude Project with ready-made instructions |
| **ancestor-research-log** | Researches one person and builds the log; also updates existing logs and keeps a Research Tracker spreadsheet |
| **ancestor-story** | Writes the optional Ancestor Story from a finished log (.docx, .pdf, .md) |
| **rerun-ancestor-log** | After you fix your tree, re-checks FamilySearch and updates the log, story and tracker |

The toolkit (installed into `Genealogy/_tools` by the setup skill): a blank Research Log template and small scripts that fill it, make the PDF and Markdown copies, keep older versions, build the Ancestor Story, and rebuild `Research_Tracker.xlsx`.

## What you need

- A paid Claude plan (Pro or Max) and the Claude desktop app
- Google Chrome with the Claude in Chrome extension
- A free FamilySearch account; any other genealogy subscriptions you already have
- Optional: LibreOffice (free) for making PDFs on your own computer

## Installing

From GitHub:

- **Claude app:** add the plugin marketplace `dgheaps9/genealogy-research-log`, then install **genealogy-research-log** from it.
- **Claude Code:**

      /plugin install genealogy-research-log --marketplace dgheaps9/genealogy-research-log

Or install the `.plugin` file directly if someone sends it to you.

## Getting started

After installing, say: **"Set up genealogy research."**
After setup: **"Research Mary Example, FamilySearch ID ABCD-123, born 1874 in Tuscarawas County, Ohio."** Add "with story" or "no story" to skip the story question.

### Keeping usage down

- One ancestor per chat; start a new chat for each person or rerun.
- Claude searches only the sites that cover the countries the ancestor lived in, so a UK-only ancestor isn't searched on US-only or French sites.
- After fixing your tree, say "fixed" (or "fixed actions 1 and 3"). A rerun re-checks FamilySearch only; say "rerun with full search" if you want the sites searched again.
- Say "with story" or "no story" up front.
- A lighter model (e.g. Sonnet) is usually enough for reruns and straightforward ancestors.

## Updating

Update the plugin in Claude, then say **"Update my genealogy toolkit."** Claude copies the new and changed scripts into `Genealogy/_tools` (your logs, data and tracker entries are kept). If you pasted Project instructions from an earlier version, ask Claude for the new sections to add (0.4.0: site selection by place lived, KEEPING USAGE DOWN, and the rerun lines under SKILLS; 0.3.0: ANCESTOR STORY and SKILLS).

## Your responsibilities

- You sign in to each site yourself. The plugin never asks for or stores passwords.
- You are responsible for following each site's terms of use. Claude reads pages at your direction, one person at a time, as you would.
- Check Claude's findings before changing your tree. Confidence levels and conflicting evidence are shown so you can judge.
- Logs for living people are marked "LIVING – do not upload to Memories."

This plugin is not affiliated with or endorsed by FamilySearch, Ancestry, Findmypast, MyHeritage or any other site it mentions.

## License and version

Free to use, share and change under the MIT License (see LICENSE).

0.4.0 — lower usage: sites chosen by the countries the ancestor lived in; reruns re-check FamilySearch only ("rerun with full search" to search again); fewer page reads; story context lookups capped; usage tips in setup and README.
0.3.1 — skill description fix for claude.ai.
0.3.0 — Ancestor Story (new ancestor-story skill and `story.py`; Story (Y/N) column in the tracker); new rerun-ancestor-log skill; tracker shows "abt" birth years correctly.
0.2.0 — setup lists up to 20 sites and checks each is signed in and approved in Claude in Chrome; log dates use your own time zone (`_tools/timezone.txt`) instead of UTC.
0.1.0 — first draft, by David Heaps.
