#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Desportes: reproduce compatibility, never infer the correct polyphonic choice.
d=E/'Desportes_1593_evidence/Desportes_1593_evidence'; j=js(d/'letter_transcription.json');key=j['key'];regions=assigned=letters=0
for row in j['rows']:
 seen=set();regions+=len(row['classes'])
 for span in row['readings']:
  units=[]
  for token in re.findall(r'\[[^]]+\]|[A-Z]+',span['text'].upper()):units.extend([token] if token.startswith('[') else list(token))
  k=0
  for index in range(span['start'],span['end']+1):
   assert index not in seen;seen.add(index);orig=row['classes'][index-1];cl=row.get('resolved_aliases',{}).get(orig,orig)
   if cl not in key:assert units[k]==f'[{orig.upper()}]';k+=1;continue
   n=len(cl) if cl in ('QUE','QUI','POUR','ET') else 1; chosen=''.join(units[k:k+n]);k+=n
   assert (chosen==cl if n>1 else chosen in key[cl]);assigned+=1;letters+=n
  assert k==len(units)
 assert seen=={x['position'] for x in row['choices']}
assert (regions,assigned,letters)==(4612,4108,4295)
for label in ['L05','L10']:
 assert next(r['classes'] for r in j['rows'] if r['id']==label)==js(d/f'validation/row_{label}_second_transcription.json')['classes']
record('desportes-1593',indexed_regions=regions,assigned_positions=assigned,expanded_letters=letters,second_arrays_matched=['L05','L10'],working_text_sha256=sha((d/'letter_reading_FR.txt').read_bytes()),limit='Compatibility is not a unique reading or historical accuracy; PAR addendum not merged into frozen text.')

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
