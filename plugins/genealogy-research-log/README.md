# Genealogy Research Log

A free Claude plugin for family historians. Give Claude an ancestor's name and FamilySearch ID; it searches FamilySearch and the genealogy sites you subscribe to, then delivers a finished **Ancestor Research Log** (.docx, .pdf and .md) with:

- vital events, spouses and children, each with a confidence level (Proven / Probable / Possible)
- a Sources table with full citations, a clickable link for every source, and whether it is already attached in FamilySearch
- research notes, including every search performed (even those that found nothing)
- **Tree Actions Suggested** — step-by-step fixes for problems in your FamilySearch tree, with a citation and link at each step

Claude never edits FamilySearch. It suggests the fixes; you make them.

## What's included

| Skill | What it does |
|---|---|
| **genealogy-setup** | Walks you through a paid Claude plan, the Claude desktop app, Claude in Chrome, signing in to your genealogy sites, connecting your Genealogy folder, installing the toolkit, and creating a Claude Project with ready-made instructions |
| **ancestor-research-log** | Researches one person and builds the log; also updates existing logs and keeps a Research Tracker spreadsheet |

The toolkit (installed into `Genealogy/_tools` by the setup skill): a blank Research Log template and small scripts that fill it, make the PDF and Markdown copies, keep older versions, and rebuild `Research_Tracker.xlsx`.

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
After setup: **"Research Mary Example, FamilySearch ID ABCD-123, born 1874 in Tuscarawas County, Ohio."**

## Your responsibilities

- You sign in to each site yourself. The plugin never asks for or stores passwords.
- You are responsible for following each site's terms of use. Claude reads pages at your direction, one person at a time, as you would.
- Check Claude's findings before changing your tree. Confidence levels and conflicting evidence are shown so you can judge.
- Logs for living people are marked "LIVING – do not upload to Memories."

This plugin is not affiliated with or endorsed by FamilySearch, Ancestry, Findmypast, MyHeritage or any other site it mentions.

## License and version

Free to use, share and change under the MIT License (see LICENSE).

0.2.0 — setup lists up to 20 sites and checks each is signed in and approved in Claude in Chrome; log dates use your own time zone (`_tools/timezone.txt`) instead of UTC.
0.1.0 — first draft, by David Heaps.
