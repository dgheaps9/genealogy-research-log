#!/bin/bash
# make_log.sh "<Full Name> <year>" [subfolder]
# Builds the .docx, .pdf and .md research log from _data/data_<Full Name> <year>.json.
# Any existing log of the same name is first copied to Superseded with today's date.
# The .md copy (for the Claude Project) is also placed in _claude_staging.
# Run from anywhere; the Genealogy folder is the folder that contains this _tools folder.
set -e
TZF="$(dirname "$0")/timezone.txt"; export TZ="$( [ -s "$TZF" ] && head -1 "$TZF" | tr -d "[:space:]" || echo UTC)"   # your time zone from _tools/timezone.txt (the shell may run in UTC)
T="$(cd "$(dirname "$0")" && pwd)"; G="$(dirname "$T")"
B="$1"; SUB="${2:-.}"; N="Ancestor_Research_Log_$B"; D=$(date +%F)
[ -z "$B" ] && { echo 'usage: make_log.sh "<Full Name> <year>" [subfolder]'; exit 1; }
[ -f "$G/_data/data_$B.json" ] || { echo "missing $G/_data/data_$B.json"; exit 1; }
cd "$G"; mkdir -p Superseded _data _claude_staging "$SUB"
for e in docx pdf; do
  if [ -f "$SUB/$N.$e" ]; then
    if [ -f "Superseded/$N ($D).$e" ]; then echo "NOTE: Superseded/$N ($D).$e already exists - not overwritten"; else cp "$SUB/$N.$e" "Superseded/$N ($D).$e"; fi
  fi
done
W="$(mktemp -d)"; cd "$W"
python3 "$T/refill.py" "$T/Research_Log_Template.docx" "$N.docx" "$G/_data/data_$B.json"
SO="$(command -v soffice || command -v libreoffice || true)"
[ -z "$SO" ] && [ -x /Applications/LibreOffice.app/Contents/MacOS/soffice ] && SO=/Applications/LibreOffice.app/Contents/MacOS/soffice
if [ -n "$SO" ]; then "$SO" --headless --convert-to pdf "$N.docx" >/dev/null 2>&1 || true; fi
python3 "$T/makemd.py" "$G/_data/data_$B.json" "$N.md"
cp "$N.docx" "$G/$SUB/"; cp "$N.md" "$G/_claude_staging/"
if [ -f "$N.pdf" ]; then cp "$N.pdf" "$G/$SUB/"; echo "pages: $(pdfinfo "$N.pdf" 2>/dev/null | awk '/Pages/{print $2}')"; else echo "NOTE: no PDF made (LibreOffice not found) - Claude will make the PDF another way"; fi
echo "done: $G/$SUB/$N.docx"
