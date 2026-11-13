---
name: genealogy-setup
description: Walks a new user through setting up Claude for genealogy research — a paid Claude plan, the Claude desktop app, Claude in Chrome, signing in to FamilySearch and other genealogy sites, connecting a Genealogy folder, installing the research-log toolkit, and creating a Claude Project with ready-made instructions. Use when the user says "set up genealogy research", "get started with the research log plugin", "set up my Genealogy folder", "how do I connect Ancestry", "create my genealogy project", or when the ancestor-research-log skill finds no toolkit.
---

# Genealogy research setup

Guide the user one step at a time in plain language. Many users are not technical: give one step, wait for them to confirm, check it worked where you can, then move on. Skip steps the user has already done. Never ask for or handle passwords — the user signs in to every site themselves.

Detailed wording for each step is in `references/setup-guide.md`. The Project instructions to paste are in `references/project-instructions.md`.

## Steps

1. **Claude plan.** Ask whether they have a paid Claude plan (Pro or Max). Plugins and Claude in Chrome need a paid plan. If not, explain the choice in a sentence or two and point them to https://claude.ai to subscribe. For current plan prices and features, search https://support.claude.com rather than quoting from memory.
2. **Claude desktop app.** Confirm they use the Claude desktop app on the computer where their genealogy files live (download from https://claude.ai/download). The desktop app is what lets Claude reach a folder on their computer.
3. **Claude in Chrome.** Have them install the Claude in Chrome extension in Google Chrome and sign in to it with the same Claude account. Then test it: load the Chrome tools and call tabs_context_mcp. If it fails, walk through the troubleshooting in the setup guide.
4. **Genealogy sites.** Show the full site list from the setup guide as a numbered list in the chat (do not use a multiple-choice prompt — it holds only 4 options). Ask them to reply with the numbers or names of every site they use, plus any sites not on the list. Accept up to 20 sites. Then work through the chosen sites in batches of 3–4:
   - Open each site's home page in a new Chrome tab and ask them to sign in there.
   - Ask them to approve each site in Claude in Chrome: when the extension asks, choose **"Always allow actions on this site"**.
   - Check each site with get_page_text (look for their name or an account menu rather than a "Sign in" button). If reading the page times out or is refused, the approval is probably still pending: have them look at the Claude side panel, or Claude icon → ⋮ → Extension settings → Permissions, then check again.
   - Record a site as ready only when it is both signed in and approved. Close the tabs before the next batch. Remind them to stay signed in before each research session.
5. **Genealogy folder.** Ask where they keep (or want to keep) their genealogy files, e.g. a folder named `Genealogy` in Documents. Have them connect that folder to this Claude task (in the desktop app, add the folder), or request access to it. Then create these subfolders if missing: `_tools`, `_data`, `Superseded`, `Not in my line`, `_claude_staging`.
6. **Install the toolkit.** Copy every file from the plugin's toolkit folder (`../ancestor-research-log/toolkit/`, relative to this skill's folder; `${CLAUDE_PLUGIN_ROOT}/skills/ancestor-research-log/toolkit/`) into the user's `Genealogy/_tools/`. If the folder is reached through a bridge to the user's computer, put the copies in the outputs area and commit them to the folder. Do not overwrite an existing `_tools` file without asking. Then write `_tools/timezone.txt` containing the user's time zone as one IANA name (e.g. `America/Denver`); take it from the session and confirm it with the user. The scripts use it for dates, because the shell on the user's computer may run in UTC.
7. **Check the tools run.** In the shell that can see the folder, run `python3 -c "import docx, openpyxl; print('ok')"` and `command -v soffice || ls /Applications/LibreOffice.app`. If python-docx or openpyxl is missing, try installing them (`pip install python-docx openpyxl`); if that is not possible, tell the user the logs will be built in Claude's workspace instead and copied back. If LibreOffice is missing, PDFs are made in the workspace instead; offer the free download from https://www.libreoffice.org if they want PDFs made locally.
8. **Claude Project.** Have them create a Claude Project (for example "Family Search"). Fill in `references/project-instructions.md` with their folder location and every site they chose (however many), show them the text, and have them paste it into the Project's instructions. Optionally have them add `Research_Log_Template.docx` to the Project's files.
9. **First test.** Suggest a first run on a deceased ancestor they know well: "Research <Name>, FamilySearch ID <PID>, born <year> in <place>." Start it with the ancestor-research-log skill if they want to go now.

Finish with a short summary of what is ready, what is not (e.g. a site that would not sign in), and the one-line way to start research.
