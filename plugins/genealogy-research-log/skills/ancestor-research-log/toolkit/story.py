# story.py - builds the Ancestor Story (.docx, .pdf, .md) from the "story" section of _data/data_<Full Name> <year>.json.
# Usage:
#   python3 story.py "<Full Name> <year>" [subfolder]        build the story (subfolder defaults to wherever the log is)
#   python3 story.py "<Full Name> <year>" --status N         story declined: records N, adds "Story declined <date>" to the
#                                                            log's Research Notes and rebuilds the log with make_log.sh
#   python3 story.py "<Full Name> <year>" --status awaiting  no answer yet: records "N – awaiting answer" (log unchanged)
# An existing story of the same name is first copied to Superseded with today's date (an existing copy is never overwritten).
# The .md copy (for the Claude Project) goes to _claude_staging. Research_Tracker.xlsx is refreshed at the end (tracker.py).
#
# "story" section of data.json (footnote markers [^1], [^2] ... match the order of "footnotes"):
#  "story": {
#   "living": false,
#   "title": "The Life of Louisa Butcher (Sims), 1882–1940",
#   "byline": "Louisa Butcher (Sims) · 12 Mar 1882 – 4 Jun 1940 · PID ABCD-123",      (" · Written <today>" is added)
#   "relationship": "Louisa Butcher is Mary Smith's 1st cousin 2x removed (FamilySearch, View My Relationship, accessed 16 Nov 2026).",
#   "sections": [ {"heading": "Origins and Parents", "paragraphs": ["Text with a footnote.[^1]", "..."]}, ... ],
#   "open_questions": "What is still unknown.[^4]",
#   "footnotes": [ ["England and Wales Census, 1881", "https://www.familysearch.org/ark:/61903/1:1:XXXX-XXX"], ["Short citation with no link"] ]
#  }
# A paragraph may also be a segment list like the log: [["bold text", true], ["plain text", false], {"link": "https://..."}]
import sys, os, re, json, shutil, subprocess, tempfile, datetime
T = os.path.dirname(os.path.abspath(__file__)); G = os.path.dirname(T)
sys.path.insert(0, T)
from helpers import today, _tz
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT

NAVY = RGBColor(0x1F, 0x38, 0x64); RED = RGBColor(0xC0, 0x00, 0x00)   # same navy as the log headings
MARK = re.compile(r'\[\^(\d+)\]')
LIVING = 'LIVING – do not upload to Memories'

def segs(v):
    if isinstance(v, str): return [[v, False]]
    if isinstance(v, dict): return [v]
    return v

# ---------- .docx ----------
def run(p, text, bold=False, italic=False, size=11, color=None, sup=False):
    r = p.add_run(text); f = r.font; f.name = 'Calibri'; f.size = Pt(size); f.bold = bold; f.italic = italic
    if color: f.color.rgb = color
    if sup: f.superscript = True
    return r

def link(p, url, text=None, size=11):
    rid = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); rp = OxmlElement('w:rPr')
    fn = OxmlElement('w:rFonts'); fn.set(qn('w:ascii'), 'Calibri'); fn.set(qn('w:hAnsi'), 'Calibri'); rp.append(fn)
    c = OxmlElement('w:color'); c.set(qn('w:val'), '0563C1'); rp.append(c)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size * 2))); rp.append(sz)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rp.append(u)
    r.append(rp); t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text or url; r.append(t)
    h.append(r); p._p.append(h)

def para(p, v, size=11):
    for s in segs(v):
        if isinstance(s, dict): link(p, s['link'], size=size); continue
        text, bold = s[0], bool(s[1])
        for i, part in enumerate(MARK.split(text)):
            if not part: continue
            if i % 2: run(p, part, size=size, sup=True)
            else: run(p, part, bold=bold, size=size)

def build_docx(s, byline, out):
    d = docx.Document(); sec = d.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)          # portrait, same page as the log
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(sec, m, Inches(0.75))
    st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(11)
    st.element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), 'Calibri')
    st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.15
    P = d.add_paragraph
    def heading(t):
        h = P(); h.paragraph_format.space_before = Pt(10); h.paragraph_format.keep_with_next = True
        run(h, t, bold=True, size=12, color=NAVY)
    if s.get('living'): run(P(), LIVING, bold=True, size=12, color=RED)
    run(P(), s['title'], bold=True, size=20, color=NAVY)
    run(P(), byline, bold=True)
    para(P(), s['relationship'])
    for sc in s['sections']:
        heading(sc['heading'])
        for v in sc['paragraphs']: para(P(), v)
    if s.get('open_questions'):
        heading('Open questions')
        for v in (s['open_questions'] if isinstance(s['open_questions'], list) and s['open_questions'] and not isinstance(s['open_questions'][0], (list, dict)) else [s['open_questions']]):
            para(P(), v)
    if s.get('footnotes'):
        heading('Notes')
        for i, f in enumerate(s['footnotes'], 1):
            p = P(); p.paragraph_format.space_after = Pt(2)
            run(p, f'{i}. ', size=9); run(p, f[0] + (', ' if len(f) > 1 and f[1] else ''), size=9)
            if len(f) > 1 and f[1]: link(p, f[1], size=9)
    d.core_properties.title = s['title']
    d.save(out)

# ---------- .md ----------
def md(v):
    o = ''
    for s in segs(v):
        if isinstance(s, dict): o += '<' + s['link'] + '>'
        elif s[1] and s[0].strip():
            t = s[0]; lead = t[:len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
            o += lead + '**' + t.strip() + '**' + trail
        else: o += s[0]
    return o

def build_md(s, byline, out):
    o = []
    if s.get('living'): o += ['**' + LIVING + '**', '']
    o += ['# ' + s['title'], '', '**' + byline + '**', '', md(s['relationship']), '']
    for sc in s['sections']:
        o += ['## ' + sc['heading'], ''] + sum([[md(v), ''] for v in sc['paragraphs']], [])
    if s.get('open_questions'):
        oq = s['open_questions']
        oq = oq if isinstance(oq, list) and oq and not isinstance(oq[0], (list, dict)) else [oq]
        o += ['## Open questions', ''] + sum([[md(v), ''] for v in oq], [])
    for i, f in enumerate(s.get('footnotes', []), 1):
        o.append(f'[^{i}]: ' + f[0] + (', <' + f[1] + '>' if len(f) > 1 and f[1] else ''))
    open(out, 'w').write('\n'.join(o).rstrip() + '\n')

# ---------- checks ----------
def check(s):
    req = [k for k in ('title', 'byline', 'relationship', 'sections') if not s.get(k)]
    if req: sys.exit('story section is missing: ' + ', '.join(req))
    used = set(int(n) for n in MARK.findall(json.dumps(s, ensure_ascii=False)))
    nf = len(s.get('footnotes', []))
    bad = sorted(n for n in used if n < 1 or n > nf)
    if bad: sys.exit(f'footnote markers {bad} have no matching entry in "footnotes" ({nf} entries)')
    unused = [n for n in range(1, nf + 1) if n not in used]
    if unused: print('NOTE: footnotes never cited in the text:', unused)

def tracker():
    subprocess.run([sys.executable, os.path.join(T, 'tracker.py')], cwd=T, check=False)

def main():
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'): sys.exit(__doc__ or open(__file__).read().split('import sys')[0])
    B = a[0]; J = f'{G}/_data/data_{B}.json'
    if not os.path.exists(J): sys.exit('missing ' + J)
    data = json.load(open(J))
    status = a[a.index('--status') + 1] if '--status' in a and len(a) > a.index('--status') + 1 else None
    sub = a[1] if len(a) > 1 and not a[1].startswith('--') else \
        ('Not in my line' if os.path.exists(f'{G}/Not in my line/Ancestor_Research_Log_{B}.docx') else '.')

    if status:   # story declined or awaiting an answer
        st = {'N': 'N', 'n': 'N', 'awaiting': 'N – awaiting answer'}.get(status, status)
        data['story_status'] = st
        if st == 'N' and not any('Story declined' in json.dumps(n, ensure_ascii=False) for n in data['notes']):
            data['notes'].append([['STORY: ', True], [f'Story declined {today()}', False]])
        json.dump(data, open(J, 'w'), ensure_ascii=False, indent=1)
        if st == 'N': subprocess.run(['bash', os.path.join(T, 'make_log.sh'), B, sub], check=True)
        tracker(); print('story status:', st); return

    s = data.get('story') or sys.exit('no "story" section in ' + J)
    check(s)
    byline = s['byline'] + ' · Written ' + today()
    N = 'Ancestor_Story_' + B; D = datetime.datetime.now(_tz()).strftime('%F')
    os.chdir(G); os.makedirs('Superseded', exist_ok=True); os.makedirs('_claude_staging', exist_ok=True); os.makedirs(sub, exist_ok=True)
    for e in ('docx', 'pdf'):
        if os.path.exists(f'{sub}/{N}.{e}'):
            dst = f'Superseded/{N} ({D}).{e}'
            if os.path.exists(dst): print(f'NOTE: {dst} already exists - not overwritten')
            else: shutil.copy2(f'{sub}/{N}.{e}', dst)
    W = tempfile.mkdtemp()
    build_docx(s, byline, f'{W}/{N}.docx')
    build_md(s, byline, f'{W}/{N}.md')
    so = shutil.which('soffice') or shutil.which('libreoffice')
    if not so and os.access('/Applications/LibreOffice.app/Contents/MacOS/soffice', os.X_OK): so = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    if so: subprocess.run([so, '--headless', '--convert-to', 'pdf', '--outdir', W, f'{W}/{N}.docx'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy(f'{W}/{N}.docx', f'{G}/{sub}/'); shutil.copy(f'{W}/{N}.md', f'{G}/_claude_staging/')
    if os.path.exists(f'{W}/{N}.pdf'):
        shutil.copy(f'{W}/{N}.pdf', f'{G}/{sub}/')
        pg = subprocess.run(['pdfinfo', f'{W}/{N}.pdf'], capture_output=True, text=True).stdout
        print('pages:', (re.search(r'Pages:\s+(\d+)', pg) or [None, '?'])[1])
    else: print('NOTE: no PDF made (LibreOffice not found) - Claude will make the PDF another way')
    tracker()
    print(f'done: {G}/{sub}/{N}.docx')

if __name__ == '__main__':
    main()
