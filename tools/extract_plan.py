# Reads Placement_DayWise_Plan.xlsx (Sufficient-resource columns only) and rebuilds index.html.
# Run from the repo root:  python tools/extract_plan.py
import openpyxl,re,json
wb=openpyxl.load_workbook('Placement_DayWise_Plan.xlsx',data_only=True)
def lines(s):
    out=[]
    for l in str(s).split('\n'):
        l=l.strip()
        if not l: continue
        out.append(re.sub(r'^\d+\.\s*','',l))
    return out
def build(name,kind):
    ws=wb[name]; res=[]
    for r in ws.iter_rows(min_row=7,values_only=True):
        if r[0] is None or r[1] is None: continue
        if kind=='c':
            num,date,track,topic,area,pri,resn,fol=r[:8]
        else:
            num,date,topic,area,pri,resn,fol=r[:7]; track=None
        rs=lines(resn); fs=lines(fol)
        groups=[]
        for i,(a,b) in enumerate(zip(rs,fs)):
            ext='[External]' in a
            a=a.replace('[External]','').strip()
            items=[x.strip() for x in re.split(r'\s+·\s+',b) if x.strip()]
            groups.append({'r':a,'x':ext,'s':items})
        tid=('T' if kind=='t' else 'C')+str(num)
        d={'id':tid,'d':date.strftime('%Y-%m-%d'),'t':topic,'a':area,'p':pri,'g':groups}
        if track: d['k']='DSA' if track.startswith('DSA') else 'ML'
        res.append(d)
    return res
data={'concept':build('Theory (day-wise)','t'),'coding':build('Coding (day-wise)','c')}

n=sum(len(g['s']) for k in data for t in data[k] for g in t['g'])
print(f'{n} tasks across {len(data["concept"])} conceptual + {len(data["coding"])} coding topics')

# Rebuild index.html from the template with the fresh data
tpl = open('tools/template.html', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':'))))
print('index.html rebuilt')
