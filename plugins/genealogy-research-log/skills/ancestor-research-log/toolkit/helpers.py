# helpers.py - shortcuts for writing the Tree Actions in data.json (citation, then URL).
FS='https://www.familysearch.org/ark:/61903/1:1:'; P='https://www.familysearch.org/tree/person/details/'
def T(s): return [s,False]
def B(s): return [s,True]
def L(cit,url,after=' '): return [T(cit+', '),{'link':url},T(after)]   # citation, then URL
def prof(name,pid,after=' '): return L('FamilySearch Family Tree, '+name+' ('+pid+')',P+pid,after)
# e.g. [B('1. Attach the census. '),T('Open ')]+prof('John Example (1850–1910)','ABCD-123','. ')+[T('Attach ')]+L('United States, Census, 1880',FS+'XXXX-XXX','. ')

# Full FamilySearch-style source citation with access date (use for the Sources table "Source Citation" column).
# e.g. cite('Ohio, County Births, 1841-2003','FamilySearch','Mary Example','1874; birth, Jefferson Township, Tuscarawas, Ohio')
#  -> '"Ohio, County Births, 1841-2003," database, FamilySearch: accessed 1 Nov 2026, Mary Example, 1874; birth, Jefferson Township, Tuscarawas, Ohio.'
import datetime as _dt
import os as _os
from zoneinfo import ZoneInfo as _ZI
def _tz():  # your time zone from _tools/timezone.txt; UTC if missing
    f=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'timezone.txt')
    try: return _ZI(open(f).read().strip() or 'UTC')
    except Exception: return _ZI('UTC')
def today():  # local date on this computer, e.g. '5 Nov 2026'
    d = _dt.datetime.now(_tz()); return f"{d.day} {d:%b %Y}"
def cite(coll, site, name, detail='', accessed=None, kind='database'):
    s = f'"{coll}," {kind}, {site}: accessed {accessed or today()}, {name}'
    return s + (f', {detail}' if detail else '') + '.'
# Research Notes "Searches performed" row: search(site, collection, terms, result)
def search(site, coll, terms, result): return [B('Search: '), T(f'{site} – {coll} – {terms} – Result: {result}')]
