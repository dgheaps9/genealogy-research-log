# refill.py - fills the Research Log template with one ancestor's data (data.json) to make a new log.
# Usage: python3 refill.py "<template.docx>" "<output.docx>" "<data.json>"
import copy, sys, json, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
def first_rpr(tc):
    r = tc.find('.//'+qn('w:r')); rp = r.find(qn('w:rPr')) if r is not None else None
    return copy.deepcopy(rp) if rp is not None else OxmlElement('w:rPr')
def set_bold(rpr, bold):
    b = rpr.find(qn('w:b'))
    if b is None:
        b = OxmlElement('w:b'); rpr.insert(1 if rpr.find(qn('w:rFonts')) is not None else 0, b)
    if bold:
        if b.get(qn('w:val')) is not None: del b.attrib[qn('w:val')]
    else: b.set(qn('w:val'), '0')
    return rpr
def mkrun(text, rpr):
    r = OxmlElement('w:r'); r.append(copy.deepcopy(rpr))
    t = OxmlElement('w:t'); t.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); t.text = text
    r.append(t); return r
LINK_RPR = None
def fill_cell(tc, val, part):
    ps = tc.findall(qn('w:p')); base = first_rpr(tc)
    for p in ps[1:]: tc.remove(p)
    p = ps[0]
    for ch in list(p):
        if ch.tag != qn('w:pPr'): p.remove(ch)
    if isinstance(val, dict) and 'link' in val:
        rid = part.relate_to(val['link'], RT.HYPERLINK, is_external=True)
        h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
        h.append(mkrun(val['link'], LINK_RPR)); p.append(h); return
    segs = val if isinstance(val, list) else [[val, None]]
    for seg in segs:
        if isinstance(seg, dict):
            rid = part.relate_to(seg['link'], RT.HYPERLINK, is_external=True)
            h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
            h.append(mkrun(seg['link'], LINK_RPR)); p.append(h); continue
        text, bold = seg
        rp = copy.deepcopy(base)
        if bold is not None: set_bold(rp, bold)
        p.append(mkrun(text, rp))
def refill(table, rows, part, header=1):
    trs = table._tbl.findall(qn('w:tr')); tmpl = trs[header]
    for tr in trs[header:]: table._tbl.remove(tr)
    for row in rows:
        tr = copy.deepcopy(tmpl)
        for tc, v in zip(tr.findall(qn('w:tc')), row): fill_cell(tc, v, part)
        table._tbl.append(tr)
src, out, data = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
d = docx.Document(src)
LINK_RPR = copy.deepcopy(d.tables[4].rows[1].cells[2]._tc.find('.//'+qn('w:hyperlink')).find('.//'+qn('w:rPr')))
part = d.part
refill(d.tables[0], data['ident'], part, header=0)
refill(d.tables[1], data['vitals'], part)
refill(d.tables[2], data['spouses'], part)
refill(d.tables[3], data['children'], part)
refill(d.tables[4], data['sources'], part)
refill(d.tables[5], [[r] for r in data['notes']], part, header=0)
refill(d.tables[6], [[r] for r in data['actions']], part, header=0)
d.core_properties.title = data['title']
d.save(out)
