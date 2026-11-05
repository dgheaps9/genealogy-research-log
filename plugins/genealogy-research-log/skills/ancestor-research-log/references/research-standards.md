# Research standards

## What to look for

For the target person, look for every available source on: name (given, middle, surname and variants), sex, birth, christening/baptism, death, obituary, burial, cremation, residences, alternative names, affiliations, bar/bat mitzvah, immigration and emigration, naturalization, military service, occupation, religious affiliation, title of nobility, spouses and marriages, children, parents and siblings.

## Where to look

Search every relevant site the user has access to. Typical list:

| Site | Notes |
|---|---|
| FamilySearch | Attached sources, historical records, tree search for duplicates |
| Ancestry | Indexes and images; many US, UK and Scandinavian collections |
| Findmypast | Strong for England, Wales, Scotland, Ireland; parish records, 1921 census, 1939 Register |
| MyHeritage | International collections, newspapers, other users' trees (treat trees as Possible) |
| Find a Grave | Memorials, photos, family links (contributor links can be wrong) |
| American Ancestors | New England and early American records |
| Geneanet / Filae | France and Europe |
| Storied | Newspapers, yearbooks, US records |
| Newspaper Archive | Obituaries, marriages, local news |
| GRO (England & Wales) | Birth and death index with mother's maiden name |

Report every relevant record found, including those behind paywalls. If a site cannot be searched (not signed in, page will not load after one retry, no subscription), list it in "Searches performed" as "not searched" with the reason, and move on.

Coverage checklist (adapt to the country and era): birth/baptism; every census in the person's lifetime; civil birth, marriage and death indexes; parish marriages and burials; probate and wills; military; immigration, emigration and naturalization; newspapers and obituaries; cemetery records.

## Confidence levels

- **Proven** — consistent primary or near-primary evidence, no unresolved conflict.
- **Probable** — good evidence with one gap or minor conflict.
- **Possible** — suggested by indirect, single-source or unsourced evidence (including other users' trees).

Always note conflicting evidence and say which record you trust more and why.

## Watch for

- Records of a different person wrongly attached (dates decades off, wrong parents or place).
- Mis-indexed names and places.
- Duplicate profiles in the tree (same name, similar dates, same parents).
- Children born before a marriage date, or gaps of more than 3 years between children (possible missing children).
- Find a Grave family links added by contributors without evidence.

## Citations (Sources table)

Full FamilySearch style with the access date:

`"<Collection title>," database, <Site>: accessed <d Mon yyyy>, <Name>, <year>; <event>, <place>.`

Example: `"Ohio, County Births, 1841-2003," database, FamilySearch: accessed 1 Nov 2026, Mary Example, 1874; birth, Jefferson Township, Tuscarawas, Ohio.`

Use the same form for Ancestry, Findmypast, MyHeritage and others, putting that site's name in place of FamilySearch. `helpers.cite()` builds this with today's date.

## Tree Actions (step-by-step fixes)

- One numbered action per tree consistency issue, written as steps the user follows in FamilySearch.
- Clean wrong relationships and wrongly attached sources before suggesting merges; name the surviving PID; give a suggested reason statement.
- Inside each action, give the full clickable URL of every source or profile the fix uses, at the step where it is needed, in the order the steps use them. A fix may use sources from any site.
- Put a short citation (the collection title) before every URL, followed by a comma, e.g. `Utah, U.S., Select Marriage Records, 1860-1944, http://www.ancestry.com/search/collections/1971/records/150041777`. Every URL gets its own citation, even when several are listed together.
  - Tree profiles: `FamilySearch Family Tree, <Name> (<PID>), <URL>`
  - Find a Grave: `Find a Grave, memorial <no.>, <Name>, <URL>`
  - Search links: `FamilySearch Historical Records search, <what was searched>, <URL>`
