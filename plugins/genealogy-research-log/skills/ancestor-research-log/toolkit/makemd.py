# makemd.py - turns the same data.json into the Project markdown copy of the log.
# Usage: python3 makemd.py "<data.json>" "<output.md>"
import json, sys
d=json.load(open(sys.argv[1]))
def c(v):
    if isinstance(v,dict): return '<'+v['link']+'>'
    if isinstance(v,list): return ''.join(('<'+x['link']+'>' if isinstance(x,dict) else ('**'+x[0].strip()+'** ' if x[1] else x[0])) for x in v)
    return v.replace('|','/')
def t(v): return ''.join(x[0] for x in v if not isinstance(x,dict)).strip() if isinstance(v,list) else v
o=['**Ancestor Research Log**','','*Genealogical Research & Source Tracking Worksheet*','','**Identification**','','|  |  |','|---|---|']
o+=['| **%s** | %s |'%(t(r[0]),c(r[1])) for r in d['ident']]
o+=['','**Vital Events**','','| **Event** | **Date** | **Location** |','|---|---|---|']+['| **%s** | %s | %s |'%(t(r[0]),c(r[1]),c(r[2])) for r in d['vitals']]
o+=['','**Spouse(s)**','','| **Spouse Name** | **Marriage Date / Location / FamilySearch ID / Notes** |','|---|---|']+['| **%s** | %s |'%(t(r[0]),c(r[1])) for r in d['spouses']]
o+=['','**Child(ren)**','','| **Child Name** | **Birth Date / Location** | **FamilySearch ID** | **Notes** |','|---|---|---|---|']+['| **%s** | %s | %s | %s |'%(t(r[0]),*map(c,r[1:])) for r in d['children']]
o+=['','**Sources**','','| **#** | **Source Citation** | **Repository / URL** | **Attached in FS? (Y/N)** | **Date Accessed** | **Findings / Notes** |','|---|---|---|---|---|---|']+['| '+' | '.join(map(c,r))+' |' for r in d['sources']]
o+=['','**Research Notes**','','|  |','|---|']+['| '+c(r)+' |' for r in d['notes']]
o+=['','**Tree Actions Suggested**','','|  |','|---|']+['| '+c(r)+' |' for r in d['actions']]
open(sys.argv[2],'w').write('\n'.join(o)+'\n')
