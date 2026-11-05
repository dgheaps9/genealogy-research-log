# extract.py - turns an existing research log .docx back into data.json (the reverse of refill.py).
# Usage: python3 extract.py "<log.docx>" "<data.json>"
# Cells become segment lists: [text, bold] runs and {"link": url} hyperlinks. A cell holding only one link becomes {"link": url}.
import sys, json, os, docx
from docx.oxml.ns import qn
def cell(tc, rels):
    segs = []
    paras = [p for p in tc.findall(qn('w:p')) if ''.join(t.text or '' for t in p.iter(qn('w:t'))).strip()]
    for i, p in enumerate(paras):
        if i: segs.append([' ', None])
        for ch in p:
            if ch.tag == qn('w:r'):
                txt = ''.join(t.text or '' for t in ch.iter(qn('w:t')))
                if not txt: continue
                b = ch.find(qn('w:rPr') + '/' + qn('w:b'))
                bold = None if b is None else (b.get(qn('w:val')) not in ('0', 'false'))
                if segs and isinstance(segs[-1], list) and segs[-1][1] == bold: segs[-1][0] += txt
                else: segs.append([txt, bold])
            elif ch.tag == qn('w:hyperlink'):
                rid = ch.get(qn('r:id'))
                url = rels[rid].target_ref if rid in rels else ''.join(t.text or '' for t in ch.iter(qn('w:t')))
                segs.append({'link': url})
    if len(segs) == 1 and isinstance(segs[0], dict): return segs[0]
    if len(segs) == 1 and segs[0][1] is None: return segs[0][0]
    return segs
def rows(table, rels, header=1, single=False):
    out = []
    for tr in table._tbl.findall(qn('w:tr'))[header:]:
        vals = [cell(tc, rels) for tc in tr.findall(qn('w:tc'))]
        out.append(vals[0] if single else vals)
    return out
def extract(path):
    d = docx.Document(path); t = d.tables; rels = d.part.rels
    name = os.path.splitext(os.path.basename(path))[0]
    data = {'title': name.replace('Ancestor_Research_Log_', 'Research Log – '), 'layout': 'current' if len(t) == 7 else 'old',
            'ident': rows(t[0], rels, 0), 'vitals': rows(t[1], rels), 'spouses': rows(t[2], rels),
            'children': rows(t[3], rels), 'sources': rows(t[4], rels),
            'sources_header': [c.text for c in t[4].rows[0].cells], 'notes': rows(t[5], rels, 0, True)}
    data['actions'] = rows(t[6], rels, 0, True) if len(t) > 6 else []
    return data
if __name__ == '__main__':
    json.dump(extract(sys.argv[1]), open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
