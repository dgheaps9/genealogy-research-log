# Setup guide — wording and troubleshooting

Use plain language. One step at a time. Product screens change; if a button is not where described, ask the user what they see and search https://support.claude.com for the current steps.

## 1. Claude plan

- Claude has a free plan and paid plans. This plugin needs a paid plan (Pro or Max) because plugins and Claude in Chrome are paid features.
- Pro suits occasional research sessions. Max gives much more usage, which helps with long research sessions on many ancestors.
- Sign up or upgrade at https://claude.ai. Look up current prices on the Claude website rather than quoting them.

## 2. Claude desktop app

- Download from https://claude.ai/download (Mac or Windows) and sign in with the same account.
- The desktop app lets Claude read and save files in a folder on the computer.

## 3. Claude in Chrome

- Install the Claude extension for Google Chrome (find it from the Claude website or the Chrome Web Store; make sure the publisher is Anthropic).
- Pin it to the toolbar and sign in with the same Claude account.
- When Claude first opens a site, Chrome may ask the user to allow Claude on that site. They should allow it for their genealogy sites.
- Troubleshooting: Chrome must be open; the extension must be signed in; restarting Chrome fixes most connection problems.

## 4. Genealogy sites

Offer this list and ask which they use:

| Site | Home page | Free or paid |
|---|---|---|
| FamilySearch | https://www.familysearch.org | Free account |
| Ancestry | https://www.ancestry.com | Paid (some free indexes) |
| Findmypast | https://www.findmypast.com | Paid |
| MyHeritage | https://www.myheritage.com | Paid |
| Find a Grave | https://www.findagrave.com | Free |
| American Ancestors | https://www.americanancestors.org | Paid membership |
| Geneanet | https://www.geneanet.org | Free / Premium |
| Filae | https://www.filae.com | Paid |
| Storied | https://www.storied.com | Paid |
| Newspaper Archive | https://newspaperarchive.com | Paid |
| GRO (England & Wales) | https://www.gro.gov.uk | Free account |
| FreeBMD | https://www.freebmd.org.uk | Free, no sign-in |

The user signs in themselves in Chrome. Claude never sees or types passwords. Sites remember the sign-in for a while; before a research session, the user checks they are still signed in.

Remind the user: they are responsible for following each site's terms of use. Claude reads pages the way they would, one person at a time, at their direction.

## 5. Genealogy folder

- Suggest a folder named `Genealogy` in Documents if they do not have one.
- In the Claude desktop app, they add the folder to the task (the add-folder or folder-access option). Claude can also ask for access.
- Subfolders Claude creates: `_tools` (the toolkit), `_data` (one data file per log), `Superseded` (older versions), `Not in my line` (people who are not ancestors), `_claude_staging` (working copies for the Project).

## 6–7. Toolkit

Files: `refill.py`, `makemd.py`, `extract.py`, `helpers.py`, `tracker.py`, `make_log.sh`, `Research_Log_Template.docx`, `data_SKELETON.json`.

They need Python 3 with python-docx and openpyxl. LibreOffice (free) makes the PDFs; without it, Claude makes the PDF in its own workspace.

## 8. Claude Project

- In Claude, create a Project (e.g. "Family Search").
- Paste the filled-in instructions into the Project's instructions.
- Each research log's .md copy is saved into the Project, so later chats in the Project can find earlier findings.

## 9. First research session

Example request: "Research Mary Example, FamilySearch ID ABCD-123, born 1874 in Tuscarawas County, Ohio."
Pick a deceased ancestor the user knows well so they can judge the results.
