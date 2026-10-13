#!/usr/bin/env python3
"""Conditional frozen-class compatibility of externally supplied candidates."""
from pathlib import Path
import argparse, json, re, unicodedata
from functools import lru_cache
ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT.parents[1] / 'verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_transcription.json'
LIMIT = 'Compatibility is not correctness. Unknown units consume 0–40 letters. Boundaries, spelling and segmentation may explain disagreement; no unique reading is certified.'

def projection(text):
    if 'non lu' in text:
        return None
    text = re.sub(r'\{[^}]*\}', '', text)
    text = unicodedata.normalize('NFKD', text).upper().replace('J', 'I').replace('V', 'U')
    return ''.join(c for c in text if 'A' <= c <= 'Z')

def exact_match(classes, text, ids, key):
    if text is None:
        return 'not_testable'
    options = [None if c not in key else [c] if c in ('QUE', 'QUI', 'POUR', 'ET') else list(key[c]) for c in classes]
    if ids == ['M8']:
        options[36] = list('FSGT')
    @lru_cache(None)
    def walk(i, j):
        if i == len(options):
            return j == len(text)
        choices = options[i] if options[i] is not None else [text[j:j+n] for n in range(min(40, len(text)-j)+1)]
        return any(text.startswith(s, j) and walk(i+1, j+len(s)) for s in choices)
    return 'compatible_conditional' if walk(0, 0) else 'not_compatible'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidates', type=Path, help='External JSON mapping physical row ID to text; clear script in braces')
    args = parser.parse_args()
    candidates = json.loads(args.candidates.read_text())
    records = json.loads((ROOT / 'line-records.json').read_text())['records']
    if not isinstance(candidates, dict) or any(not isinstance(v, str) for v in candidates.values()):
        parser.error('Expected an object mapping IDs to strings')
    known = {r['line'] for r in records}
    if set(candidates) - known:
        parser.error('Unknown physical row IDs')
    evidence = json.loads(EVIDENCE.read_text())
    runs = {r['id']: r['classes'] for r in evidence['rows']}
    results = {}
    for record in records:
        row = record['line']
        if row not in candidates:
            continue
        ids = record['code_runs']
        classes = [c for run in ids for c in runs[run]]
        results[row] = exact_match(classes, projection(candidates[row]), ids, evidence['key']) if ids else 'ordinary'
    print(json.dumps({'results': results, 'limit': LIMIT}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
