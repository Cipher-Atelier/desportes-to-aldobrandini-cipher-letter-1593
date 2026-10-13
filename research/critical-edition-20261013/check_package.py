#!/usr/bin/env python3
"""Portable metadata/text check, with optional locally supplied pixel provenance."""
from pathlib import Path
import argparse, hashlib, json, re
from build_reader import render
ROOT = Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

def load(name):
    return json.loads((ROOT / name).read_text())

def require(condition, message):
    if not condition:
        raise ValueError(message)

def pixels(local):
    from PIL import Image, ImageDraw
    recipe = load('row-window-recipe.json')
    frames = {f: Image.new('RGB', tuple(size), (255, 0, 255)) for f, size in recipe['dimensions'].items()}
    masks = {f: Image.new('L', tuple(size), 0) for f, size in recipe['dimensions'].items()}
    for item in load('primary-acquisition.json')['images']:
        path = local / item['file']
        require(sha(path.read_bytes()) == item['sha256'], 'Tile hash: ' + item['file'])
        image = Image.open(path).convert('RGB')
        x, y, w, h = item['region_xywh']
        require(image.size == (w, h) and item['native'], 'Tile dimensions')
        folio = path.name.split('-')[0]
        frames[folio].paste(image, (x, y))
        ImageDraw.Draw(masks[folio]).rectangle((x, y, x+w-1, y+h-1), fill=255)
    for item in recipe['windows']:
        folio = 'f347' if item['folio'] == '186r' else 'f348'
        box = item['bbox_xyxy']
        require(masks[folio].crop(box).getextrema() == (255, 255), 'Uncovered crop')
        crop = frames[folio].crop(box)
        saved = Image.open(local / item['file']).convert('RGB')
        require(saved.size == crop.size and saved.tobytes() == crop.tobytes(), 'Crop mismatch: ' + item['file'])
        require(sha(crop.tobytes()) == item['pixel_sha256'], 'Crop pixel hash')
    return {'status': 'PASS', 'tiles': 63, 'reconstructed_windows': 129, 'limit': 'Pixel provenance only; optical reading correctness not certified.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pixels', type=Path, help='Local edition directory with original sources/ and rows/ bytes')
    args = parser.parse_args()
    entries = {}
    for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        require(not rel.is_absolute() and '..' not in rel.parts and name not in entries, 'Unsafe or duplicate manifest path')
        require(sha((ROOT / rel).read_bytes()) == digest, 'Hash mismatch: ' + name)
        entries[name] = digest
    actual = {p.name for p in ROOT.iterdir() if p.is_file() and p.name != 'SHA256SUMS.txt'}
    require(set(entries) == actual, 'Manifest does not cover exact deliverable set')
    records = load('line-records.json')['records']
    expected = [f'r{i:02}' for i in range(52)] + [f'v{i:02}' for i in range(33)]
    require([r['line'] for r in records] == expected, '85 ordered physical IDs')
    runs = [run for r in records for run in r['code_runs']]
    evidence = json.loads((ROOT.parents[1] / 'verification/readings/evidence/Desportes_1593_evidence/Desportes_1593_evidence/letter_transcription.json').read_text())
    require(len(runs) == 76 and len(set(runs)) == 76 and set(runs) == {r['id'] for r in evidence['rows']}, 'Run coverage')
    gaps = load('open-loci.json')
    require(len(gaps) == 97 and {g['id'] for g in gaps} == {f'{r["id"]}:{a}-{b}' for r in evidence['rows'] for a,b in r.get('gaps', [])}, '97 frozen spans')
    uncertainties = load('additional-uncertainties.json')
    require(len(uncertainties) == 68 and len({g['id'] for g in uncertainties}) == 68, '68 unique additional uncertainties')
    require(len(load('primary-acquisition.json')['images']) == 63 and len(load('row-window-recipe.json')['windows']) == 129, 'Metadata inventory')
    require((ROOT / 'transcript-fr.md').read_text() == render(), 'Literal reader differs')
    for p in ROOT.iterdir():
        if p.suffix in ('.md', '.json', '.txt'):
            text = p.read_text()
            require(not re.search(r'/Users/|libfile_|library_file_id|critical_reading_proposal|consumed_by_position', text), 'Private or excluded field: ' + p.name)
    print(json.dumps({'status': 'PASS', 'scope': 'public metadata and text checks only', 'manifest_files': len(entries), 'physical_lines': 85, 'cipher_runs': 76, 'open_spans': 97, 'additional_uncertainties': 68, 'pixels': pixels(args.pixels) if args.pixels else {'status': 'SKIPPED', 'reason': 'No local image bytes supplied; scans and crops are excluded from public package.'}}, indent=2))

if __name__ == '__main__':
    main()
