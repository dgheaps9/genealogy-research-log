---
name: ancestor-research-log
description: Researches one ancestor (name and FamilySearch PID, plus birth year and place when known) across FamilySearch and the user's genealogy sites, and produces an Ancestor Research Log as .docx, .pdf and .md with full citations and step-by-step FamilySearch tree fixes. Use when the user says "research my ancestor", "make a research log for", "research log for [name] [PID]", gives an ancestor's name with a FamilySearch ID, approves a log for a spouse or child, or asks to update an existing research log.
---

# Ancestor Research Log

Research one person and deliver a 7-section Ancestor Research Log. Act as a top genealogy research assistant: thorough, evidence-based, and honest about uncertainty.

Read `references/research-standards.md` before researching and `references/log-format.md` before building the log. If the user's Claude Project has its own instructions, those take priority over this skill where they differ.

## Ground rules

- Never edit FamilySearch or any other site. Only suggest changes; the user makes them.
- Research the target person only. Offer separate logs for spouses or children found along the way.
- Use the user's name spellings and IDs. If the user corrects a name, use the corrected spelling everywhere (file name, document, Project copy).
- The user signs in to their own sites. Never ask for, type, or store passwords. If a site shows a sign-in page, ask the user to sign in, then continue.
- If a site's page loads but can't be read (timeouts, "blocked by your site permissions"), Claude in Chrome is probably waiting for the user to approve the site. Stop and ask them to choose "Always allow actions on this site", then continue. If they don't approve it, list the site in "Searches performed" as "not searched – site not approved in Claude in Chrome".
- Respect each site's terms: read pages as the user would, one person at a time. Do not bulk-download or scrape.
- If the person may be living (born within about 110 years with no death record), treat the log as private and add "LIVING – do not upload to Memories" in Identification.

## 0. Start

1. Say in one line who is being researched. Make a short task list: FamilySearch profile, record search, other sites, build log, save, tracker, check.
2. Work out the file name: `Ancestor_Research_Log_<Full Name> <birth year>`.
   - Women: maiden name with married name in parentheses, e.g. `Annie Beale (Street) 1874`.
   - Unknown or estimated year: `abt 1874`.
3. Find the user's Genealogy folder: the connected folder that contains `_tools/make_log.sh`. If no folder has it, run the **genealogy-setup** skill first (or ask the user which folder to use and install the toolkit as that skill describes). If `_tools/timezone.txt` is missing, create it with the user's time zone (one IANA name, e.g. `America/Denver`, from the session) so log dates match their local date.
4. Check the Genealogy folder and its `Not in my line` subfolder for an existing log with that name. If updating an existing log, start from `_data/data_<name>.json`; if that is missing, make it with `python3 _tools/extract.py "<log.docx>" "_data/data_<name>.json"`.
5. If the user says the person is not their ancestor, the log goes in `Not in my line/`.

## 1. Read the FamilySearch profile (Claude in Chrome)

- Load the Chrome tools in one ToolSearch call (tabs_context_mcp, navigate, computer, get_page_text, find, read_page, browser_batch, tabs_close_mcp). Open new tabs; close them at the end.
- Open `https://www.familysearch.org/tree/person/details/<PID>` and read it with get_page_text (wait a few seconds; re-read if only the page shell loaded). Note vitals, living/deceased, spouses, children, parents and every sibling. Watch for duplicate siblings with the same name and year — often duplicates of the target.
- Open the Sources tab (`https://www.familysearch.org/tree/person/sources/<PID>`) and list every attached source with its record link. Open each record page and note names, dates, places, relationships and the collection title (used in citations).

## 2. Search for new records

Follow `references/research-standards.md` for coverage and `references/search-guide.md` for search URLs. In short:

- FamilySearch historical records first, then the user's other sites (Ancestry, Findmypast, MyHeritage, Find a Grave, American Ancestors, Geneanet, Filae, Storied, Newspaper Archive, the GRO and any others the user has).
- Try spelling variants; for women, search the maiden name with the father's name and birthplace.
- Keep a running list of EVERY search — site, collection, search terms, result — including searches that found nothing and sites that could not be searched (with the reason). This becomes the "Searches performed" block.
- Give every fact a confidence level (Proven / Probable / Possible) and record conflicting evidence.

## 3. Build the log

Use the toolkit in the Genealogy folder's `_tools` (run it with the shell on the user's computer when available; otherwise stage the files into the workspace, run there, and copy results back). Do not rewrite the scripts. If a script needs a fix, edit it in `_tools` and tell the user.

1. Write `_data/data_<Full Name> <year>.json` in the format in `references/log-format.md` (start from `_tools/data_SKELETON.json`). Use `_tools/helpers.py` (`cite()`, `search()`, `L()`, `prof()`, `T()`, `B()`) for citations, search rows and Tree Actions.
2. Run `bash "<Genealogy>/_tools/make_log.sh" "<Full Name> <year>"` (add `"Not in my line"` as a second argument for non-ancestors). It backs up any existing log to `Superseded/` with today's date, builds the .docx from `Research_Log_Template.docx`, converts to PDF with LibreOffice when installed, and writes the .md to `_claude_staging/`.
   - If it reports an existing Superseded copy with today's date, ask the user before overwriting.
   - If no PDF was made (LibreOffice missing), stage the .docx into the workspace, convert it there, and copy the PDF back next to the .docx.
3. Run `python3 "<Genealogy>/_tools/tracker.py"` to refresh `Research_Tracker.xlsx`.

## 4. Check and deliver

- Check the PDF: page count; look at page 1, a Sources page and the Tree Actions page. Confirm portrait layout, all 7 sections in order, a full clickable URL for every source, and in every Tree Action a short citation before each URL.
- If this conversation belongs to a Claude Project, save the .md to the Project (path `claude/<file name>.md`), replacing any earlier copy, so the Project keeps one copy per person.
- Close the Chrome tabs you opened.
- Reply briefly: key findings with confidence, conflicts, what is still to search (and sites that would not load), and offer logs for spouses or children found.
