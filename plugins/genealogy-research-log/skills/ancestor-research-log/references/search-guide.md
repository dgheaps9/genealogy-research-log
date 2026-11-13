# Search guide

## FamilySearch

Profile: `https://www.familysearch.org/tree/person/details/<PID>`
Attached sources: `https://www.familysearch.org/tree/person/sources/<PID>`
Record (persona) link used in citations: `https://www.familysearch.org/ark:/61903/1:1:<ID>`
Other-user tree (Pedigree Resource File) link: `https://www.familysearch.org/ark:/61903/2:2:<ID>` — cite as Possible, unsourced.

Historical records search (read results with get_page_text):

`https://www.familysearch.org/search/record/results?q.givenName=<given>&q.surname=<surname>&q.birthLikeDate.from=<yyyy>&q.birthLikeDate.to=<yyyy>&q.birthLikePlace=<place>&count=50`

Useful extra parameters: `q.spouseGivenName`, `q.spouseSurname`, `q.fatherGivenName`, `q.fatherSurname`, `q.motherGivenName`, `q.marriageLikeDate.from` / `.to`, `q.marriageLikePlace`, `q.deathLikeDate.from` / `.to`, `q.deathLikePlace`, `q.anyPlace`.

Tree search for possible duplicates: same parameters at `https://www.familysearch.org/search/tree/results?...`

Collect record links from a results page with find/read_page; open each likely match and read its details.

## Other sites

Use each site's normal search form in the user's signed-in Chrome, one person at a time. Record the collection, search terms and result for every search. Keep the record page URL for the Sources table.

- **Find a Grave**: `https://www.findagrave.com/memorial/search?firstname=<given>&lastname=<surname>&birthyear=<yyyy>&deathyear=<yyyy>` — memorial URL is `https://www.findagrave.com/memorial/<no.>`.
- **GRO (England & Wales)**: index search needs the user signed in at `https://www.gro.gov.uk/gro/content/certificates/`.
- **FreeBMD** (free, England & Wales index): `https://www.freebmd.org.uk/cgi/search.pl`

If a page will not load after one retry, note it under "Still to search" and in "Searches performed" as not searched.

## Browser tips

- Read pages with get_page_text; if only the page shell loads, wait a few seconds and read again.
- Work in new tabs and close them at the end.
- If a site asks the user to sign in or prove they are human, stop and ask the user to do it, then continue.
- If a page loads but can't be read (get_page_text or read_page times out, or says it is blocked by site permissions), the site is probably not yet approved in Claude in Chrome. Ask the user to approve it ("Always allow actions on this site" in the extension's prompt, or check Claude icon → ⋮ → Extension settings → Permissions), then read it again. If they don't approve it, record the site as "not searched – site not approved in Claude in Chrome".
