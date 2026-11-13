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
- Claude in Chrome must be approved on each site before Claude can read it. When Claude first acts on a site, the extension asks; the user chooses **"Always allow actions on this site"** for each genealogy site.
- Signs that approval is still pending: the page loads but Claude cannot read it (timeouts, or "blocked by your site permissions"). The user checks the Claude side panel for the prompt, or opens Claude icon → ⋮ → Extension settings → Permissions to see which sites are allowed. There is no "add site" button there; a site appears after the user approves it in the prompt.
- Even on approved sites, Claude still asks before purchases, downloads, deleting data, creating accounts or entering sensitive information.
- Troubleshooting: Chrome must be open; the extension must be signed in; restarting Chrome fixes most connection problems.

## 4. Genealogy sites

Show this whole list as a numbered list in the chat (not a multiple-choice prompt, which shows only 4 options). The user replies with numbers or names and adds any sites that are not listed. Up to 20 sites is fine.

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
| FreeCEN | https://www.freecen.org.uk | Free, no sign-in |
| FreeREG | https://www.freereg.org.uk | Free, no sign-in |
| ScotlandsPeople | https://www.scotlandspeople.gov.uk | Pay per view (free search) |
| Newspapers.com | https://www.newspapers.com | Paid |
| GenealogyBank | https://www.genealogybank.com | Paid |
| Chronicling America (Library of Congress) | https://www.loc.gov/collections/chronicling-america/ | Free, no sign-in |
| Fold3 | https://www.fold3.com | Paid (some free) |
| BillionGraves | https://billiongraves.com | Free / Plus |
| WikiTree | https://www.wikitree.com | Free |
| Geni | https://www.geni.com | Free / Pro |

Open and check the chosen sites in batches of 3–4, not all at once. For each site: the user signs in, approves it in Claude in Chrome ("Always allow actions on this site"), and Claude reads the page to confirm. A site is ready only when it is both signed in and approved.

The user signs in themselves in Chrome. Claude never sees or types passwords. Sites remember the sign-in for a while; before a research session, the user checks they are still signed in.

Remind the user: they are responsible for following each site's terms of use. Claude reads pages the way they would, one person at a time, at their direction.

## 5. Genealogy folder

- Suggest a folder named `Genealogy` in Documents if they do not have one.
- In the Claude desktop app, they add the folder to the task (the add-folder or folder-access option). Claude can also ask for access.
- Subfolders Claude creates: `_tools` (the toolkit), `_data` (one data file per log), `Superseded` (older versions), `Not in my line` (people who are not ancestors), `_claude_staging` (working copies for the Project).

## 6–7. Toolkit

Files: `refill.py`, `makemd.py`, `extract.py`, `helpers.py`, `tracker.py`, `make_log.sh`, `Research_Log_Template.docx`, `data_SKELETON.json`.

Claude also writes `timezone.txt` with the user's time zone (one IANA name, e.g. `America/Denver`). The scripts use it for the dates in Superseded file names, citation "accessed" dates and the tracker. Without it they use UTC, which can put dates a day off. If the user moves, they change that one line.

They need Python 3 with python-docx and openpyxl. LibreOffice (free) makes the PDFs; without it, Claude makes the PDF in its own workspace.

## 8. Claude Project

- In Claude, create a Project (e.g. "Family Search").
- Paste the filled-in instructions into the Project's instructions.
- Each research log's .md copy is saved into the Project, so later chats in the Project can find earlier findings.

## 9. First research session

Example request: "Research Mary Example, FamilySearch ID ABCD-123, born 1874 in Tuscarawas County, Ohio."
Pick a deceased ancestor the user knows well so they can judge the results.
