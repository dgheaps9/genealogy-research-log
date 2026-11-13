# tracker.py - rebuilds Research_Tracker.xlsx from Genealogy/_data, keeping what you typed
# in the yellow columns (Tree Actions done, Uploaded to Memories?).  Usage: python3 tracker.py
import json,glob,os,re,datetime,time
_f=os.path.join(os.path.dirname(os.path.abspath(__file__)),'timezone.txt')   # your time zone (the shell may run in UTC)
os.environ['TZ']=(open(_f).read().strip() if os.path.exists(_f) else '') or 'UTC'; time.tzset()
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
G=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=G+'/Research_Tracker.xlsx'
fl=lambda c: c['link'] if isinstance(c,dict) else (c if isinstance(c,str) else ''.join(s['link'] if isinstance(s,dict) else s[0] for s in c))
keep={}
if os.path.exists(OUT):
    old=openpyxl.load_workbook(OUT)['Tracker']
    for r in old.iter_rows(min_row=2,values_only=True):
        if r[0] and r[2]: keep[(r[0],str(r[2]))]=(r[7],r[9])
rows=[]
for f in sorted(glob.glob(G+'/_data/data_*.json')):
    b=os.path.basename(f)[5:-5]; d=json.load(open(f))
    docx=f'Ancestor_Research_Log_{b}.docx'
    inline=os.path.exists(f'{G}/{docx}')
    path=f'{G}/{docx}' if inline else f'{G}/Not in my line/{docx}'
    if not os.path.exists(path): continue
    date=datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
    idr=[fl(r[1]) for r in d['ident'] if 'ID' in fl(r[0])]
    m2=re.search(r'[A-Z0-9]{4}-[A-Z0-9]{3,4}',idr[0]) if idr else None; pid=m2.group() if m2 else ''
    m=re.match(r'(.*) ((?:abt )?\d{4})$',b); name,yr=m.group(1),m.group(2)
    still=''
    for n in d['notes']:
        t=fl(n); k=t.lower().find('still to search')
        if k>=0: still=t[k+15:k+415].lstrip(' :.-–').strip(); break
    done,mem=keep.get((name,yr),(None,None))
    rows.append([name,pid,yr,'Yes' if inline else 'No',date,'Current' if d.get('layout','current')=='current' else 'Old – rebuild',len(d['actions']),done,None,mem,still,f'https://www.familysearch.org/tree/person/details/{pid}' if pid else ''])
wb=Workbook(); ws=wb.active; ws.title='Tracker'
ws.append(['Person (log name)','FamilySearch PID','Birth year','In my line?','Log date','Log layout','Tree Actions in log','Tree Actions done','Tree Actions open','Uploaded to Memories?','Still to search','FamilySearch profile'])
F=Font(name='Arial',size=10); LF=Font(name='Arial',size=10,color='0563C1',underline='single')
for i,r in enumerate(rows, start=2):
    ws.append(r); ws.cell(i,9).value=f'=IF(G{i}="","",G{i}-N(H{i}))'; ws.cell(i,5).number_format='d mmm yyyy'
    for c in ws[i]: c.font=F; c.alignment=Alignment(vertical='top',wrap_text=c.column==11)
    if r[11]: ws.cell(i,12).hyperlink=r[11]; ws.cell(i,12).font=LF
for c in ws[1]: c.fill=PatternFill('solid',fgColor='1F4E78'); c.font=Font(name='Arial',size=10,bold=True,color='FFFFFF'); c.alignment=Alignment(wrap_text=True,vertical='center')
for i in range(2,len(rows)+2):
    for col in (8,10): ws.cell(i,col).fill=PatternFill('solid',fgColor='FFF2CC')
for col,w in zip('ABCDEFGHIJKL',[38,12,9,9,12,14,10,10,10,12,60,48]): ws.column_dimensions[col].width=w
ws.freeze_panes='B2'; last=len(rows)+1; ws.auto_filter.ref=f'A1:L{last}'
dv=DataValidation(type='list',formula1='"Yes,No"',allow_blank=True); ws.add_data_validation(dv); dv.add(f'J2:J{last}')
n=last+2
ws.cell(n,1,'Totals'); ws.cell(n,7,f'=SUM(G2:G{last})'); ws.cell(n,8,f'=SUM(H2:H{last})'); ws.cell(n,9,f'=SUM(I2:I{last})')
ws.cell(n+1,1,'Logs uploaded to Memories'); ws.cell(n+1,10,f'=COUNTIF(J2:J{last},"Yes")')
for c in list(ws[n])+list(ws[n+1]): c.font=Font(name='Arial',size=10,bold=c.column==1)
lg=wb.create_sheet('How to use')
for t in ['How to use this tracker','','Yellow cells are yours to fill in:',"  • Tree Actions done – how many of the log's Tree Actions you have finished in FamilySearch.","  • Uploaded to Memories? – Yes once the PDF is attached to the person's Memories.",'','Everything else is filled in by Claude from the logs (the _data folder) and refreshed each time a log is made or replaced; your yellow entries are kept.','Tree Actions open is a formula: Tree Actions in log minus Tree Actions done.','Log layout "Old – rebuild" marks logs made with an older layout.','In my line? = No for logs kept in the Not in my line folder.',"Still to search is copied from each log's Research Notes.",'',f'Last rebuilt {datetime.datetime.now():%d %b %Y} from {len(rows)} research logs.']:
    lg.append([t])
for r in lg.iter_rows():
    for c in r: c.font=Font(name='Arial',size=12 if c.row==1 else 10,bold=c.row==1)
lg.column_dimensions['A'].width=110
wb.calculation.fullCalcOnLoad=True
wb.save(OUT); print(len(rows),'rows')
