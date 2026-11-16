# Ancestor Story format

## File name and title

- File: `Ancestor_Story_<Full Name> <birth year>` (.docx, .pdf, .md), using the log's naming rules: women by maiden name with married name in parentheses (`Annie Beale (Street) 1874`); unknown or estimated year `abt 1874`.
- Title: `The Life of <Full Name>, <birth year>–<death year>`, e.g. "The Life of Louisa Butcher (Sims), 1882–1940". Never use "Ancestor Story" as a heading.
- No death year: `<birth year>–present` (living), `<birth year>–?` (unknown), `<birth year>–abt <year>` (estimated).

## Top of the story, in this order

1. `LIVING – do not upload to Memories` — living people only (`"living": true`).
2. Title.
3. Bold line: name · dates · PID — story.py adds " · Written <today>".
4. Relationship line, exactly as FamilySearch "View My Relationship" shows it, with the user's name in place of "you/your", e.g. "George Example is Mary Smith's father (FamilySearch, View My Relationship, accessed 13 Nov 2026)." Or "Relationship to <user's name> not confirmed in FamilySearch" plus the reason.

## Sections (headings are up to you; keep this order)

Origins and parents · Birth and childhood · Marriage(s) · Children · Work and homes (occupations and residences) · Migrations · Military service · Later life · Death and burial · Open questions (story.py adds this heading from `open_questions`) · Notes (story.py builds this from `footnotes`).

Skip a section the sources say nothing about rather than padding it.

## The `story` section of data.json

```json
"story": {
 "living": false,
 "title": "The Life of Louisa Butcher (Sims), 1882–1940",
 "byline": "Louisa Butcher (Sims) · 12 Mar 1882 – 4 Jun 1940 · PID ABCD-123",
 "relationship": "Louisa Butcher is Mary Smith's 1st cousin 2x removed (FamilySearch, View My Relationship, accessed 16 Nov 2026).",
 "sections": [
  {"heading": "Origins and Parents", "paragraphs": ["Louisa was born on 12 March 1882 in Bradford, Yorkshire.[^1] ..."]},
  {"heading": "Work and Homes", "paragraphs": [[["In 1901 ", false], ["Louisa", true], [" was a worsted spinner.[^2]", false]]]}
 ],
 "open_questions": "Her christening has not been found.",
 "footnotes": [
  ["England and Wales Birth Registration Index, 1837-2008", "https://www.familysearch.org/ark:/61903/1:1:XXXX-XXX"],
  ["England and Wales Census, 1901", "https://www.familysearch.org/ark:/61903/1:1:YYYY-YYY"],
  ["Find a Grave, memorial 12345, Louisa Butcher"]
 ]
}
```

- Footnote markers `[^1]`, `[^2]` … match the order of `footnotes`. story.py stops if a marker has no note and warns about notes never cited.
- A footnote is `[short citation, url]` or `[short citation]` when there is no link. Use the collection title as the short citation; for a historical-context lookup use the page or publisher title and its URL.
- A paragraph is a string, or a segment list like the log (`[text, bold]` and `{"link": url}`).
- `open_questions` is a string, or a list of strings for several paragraphs.

## Status without a story

`story_status` (set by `story.py --status`) records `"N"` (declined) or `"N – awaiting answer"`. tracker.py shows Y whenever a `story` section exists, otherwise `story_status`.
