# Research Log format

## Layout

Portrait. Seven sections in this order, each a table in `Research_Log_Template.docx`:

1. Identification
2. Vital Events
3. Spouse(s)
4. Child(ren)
5. Sources — one 6-column table: #, Source Citation, Repository / URL, Attached in FS? (Y/N), Date Accessed, Findings / Notes
6. Research Notes — key findings, a "Searches performed" block, the confidence key, and "Still to search"
7. Tree Actions Suggested

Never change the template's formatting; `refill.py` copies its styles row by row.

## Files and folders (inside the user's Genealogy folder)

| Item | Where |
|---|---|
| `Ancestor_Research_Log_<name>.docx` and `.pdf` | Genealogy folder (or `Not in my line/` for non-ancestors) |
| `data_<name>.json` | `_data/` — the source of truth; edit it and re-run make_log.sh to update a log |
| `.md` copy | `_claude_staging/`, then saved to the Claude Project at `claude/<file name>.md` |
| Older versions | `Superseded/<file name> (yyyy-mm-dd).docx` / `.pdf` |
| Tracker | `Research_Tracker.xlsx`, rebuilt by `tracker.py` (keeps the user's yellow-column entries) |
| Toolkit | `_tools/` (with `timezone.txt`: the user's time zone, used for all dates) |

## data.json

Start from `_tools/data_SKELETON.json`. Keys:

- `title`: `"Research Log – <Full Name> <year>"`
- `layout`: `"current"`
- `ident`: rows of `[label, value]` — Document Name, Ancestor Name, Sex, FamilySearch ID, Parents (per tree). Add `["Privacy", "LIVING – do not upload to Memories"]` for a living person.
- `vitals`: rows of `[event, date + confidence, location]` — Birth, Christening, Residence, Military Service, Death, Burial, Probate, etc.
- `spouses`: rows of `[name (PID), "Married <date> / <place> / <PID>. <notes>"]`
- `children`: rows of `[name, birth date and place, PID, notes]`
- `sources`: rows of `[#, full citation, {"link": url}, "Y" / "N", date accessed, findings]`. Every source gets its full URL, attached or not.
- `notes`: list of cells. Start each with a bold label, e.g. `KEY FINDING – BIRTH (PROVEN): `. Add one `search()` row per search performed (including nothing-found and not-searched), a `CONFIDENCE KEY` row and a `STILL TO SEARCH` row (tracker.py copies this into the tracker).
- `actions`: list of cells, each a numbered Tree Action.

### Cell values

A cell is one of:

- a plain string;
- `{"link": "<url>"}` — a cell holding only a clickable URL;
- a list of segments, where each segment is `[text, bold]` (bold is `true`, `false` or `null`) or `{"link": "<url>"}`.

### helpers.py

```python
import sys; sys.path.insert(0, '<Genealogy>/_tools'); from helpers import *
cite('Ohio, County Births, 1841-2003', 'FamilySearch', 'Mary Example', '1874; birth, Jefferson Township, Tuscarawas, Ohio')
search('FamilySearch', 'England and Wales Census, 1881', 'John Example b. 1850 Wiltshire', 'no match')
[B('1. Attach the census. '), T('Open ')] + prof('John Example (1850–1910)', 'ABCD-123', '. ') + [T('Attach ')] + L('United States, Census, 1880', FS + 'XXXX-XXX', '. ')
```

`FS` is the FamilySearch record link prefix and `P` the tree profile prefix. `L(citation, url, after)` writes "citation, URL" so every URL is preceded by its citation. Never put two URLs side by side with only ", " between them.
