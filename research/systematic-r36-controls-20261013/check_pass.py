#!/usr/bin/env python3
"""Verify native IIIF tile provenance and fully covered raw RGB crop reconstruction."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse
from PIL import Image


def digest(data):
    return hashlib.sha256(data).hexdigest()


def confined(root, name):
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Unsafe relative path: ' + str(name))
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Path escapes root: ' + str(name))
    return path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(manifest, base, source_root=None, baseline=None):
    errors = []
    require(isinstance(manifest, dict), 'Manifest must be an object')
    for field in ('sources', 'windows', 'freezes'):
        require(isinstance(manifest.get(field), list), 'Manifest requires array: ' + field)
    require(manifest['sources'] and manifest['windows'], 'Source and window inventories must not be empty')
    if baseline is not None:
        require(isinstance(baseline, dict), 'Baseline must map relative paths to hashes')
    tiles = {}
    counts = {'sources': 0, 'windows': 0, 'freezes': 0, 'baseline_files': 0}
    for item in manifest.get('sources', []):
        name = item.get('file', '<missing>')
        try:
            require(name not in tiles, 'Duplicate source file')
            path = confined(base, name)
            require(digest(path.read_bytes()) == item['sha256'], 'Source file hash mismatch')
            region = item['region']
            require(len(region) == 4 and all(isinstance(n, int) and not isinstance(n, bool) for n in region), 'Invalid region')
            x, y, w, h = region
            require(x >= 0 and y >= 0 and w > 0 and h > 0, 'Invalid region bounds')
            image = Image.open(path).convert('RGB')
            require(image.size == (w, h) == tuple(item['native_dimensions']), 'Source is not exact native region size')
            url = urlparse(item['url'])
            require(url.scheme == 'https' and url.hostname == 'gallica.bnf.fr', 'Non-official IIIF URL')
            match = re.search(r'/iiif/ark:/[^/]+/[^/]+/(f\d+)/(\d+),(\d+),(\d+),(\d+)/(\d+),/0/native\.(?:jpg|png)$', url.path)
            require(match is not None, 'Unsupported or non-native IIIF URL')
            require(match[1] == item['folio'], 'URL folio mismatch')
            require(tuple(map(int, match.group(2, 3, 4, 5))) == tuple(region), 'URL region mismatch')
            require(int(match[6]) == w, 'URL documented output width differs from native region width')
            tiles[name] = (item['folio'], region, image)
            counts['sources'] += 1
        except Exception as exc:
            errors.append({'kind': 'source', 'id': name, 'error': str(exc)})
    ids = set()
    for item in manifest.get('windows', []):
        name = item.get('id', '<missing>')
        try:
            require(name not in ids, 'Duplicate window ID')
            ids.add(name)
            box = item['box']
            require(len(box) == 4 and all(isinstance(n, int) and not isinstance(n, bool) for n in box), 'Invalid crop coordinates')
            x0, y0, x1, y1 = box
            require(x0 >= 0 and y0 >= 0 and x1 > x0 and y1 > y0, 'Invalid crop bounds')
            size = (x1-x0, y1-y0)
            require(tuple(item['dimensions']) == size and item['scale'] == 1 and item['coverage'] == 'full', 'Crop dimensions/scale/coverage mismatch')
            path = confined(base, item['raw_file'])
            require(digest(path.read_bytes()) == item['file_sha256'], 'Crop file hash mismatch')
            saved = Image.open(path).convert('RGB')
            require(saved.size == size, 'Saved crop dimensions mismatch')
            output = bytearray(size[0]*size[1]*3)
            covered = bytearray(size[0]*size[1])
            source_files = item['source_files']
            require(source_files and len(source_files) == len(set(source_files)), 'Missing or duplicate tile membership')
            for source in source_files:
                require(source in tiles, 'Unavailable source tile: ' + source)
                folio, region, image = tiles[source]
                require(folio == item['folio'], 'Tile folio mismatch')
                tx, ty, tw, th = region
                a, b, c, d = max(tx,x0), max(ty,y0), min(tx+tw,x1), min(ty+th,y1)
                require(c > a and d > b, 'Listed tile does not overlap crop')
                pixels = image.crop((a-tx,b-ty,c-tx,d-ty)).tobytes()
                for row in range(d-b):
                    for col in range(c-a):
                        target = (b-y0+row)*size[0]+a-x0+col
                        offset = (row*(c-a)+col)*3
                        value = pixels[offset:offset+3]
                        if covered[target]:
                            require(output[target*3:target*3+3] == value, 'Overlapping tile pixels disagree')
                        else:
                            output[target*3:target*3+3] = value
                            covered[target] = 1
            require(all(covered), 'Crop has missing pixel coverage; padding forbidden')
            require(bytes(output) == saved.tobytes(), 'Reconstructed crop RGB bytes differ')
            require(digest(output) == item['rgb_sha256'], 'Reconstructed RGB hash mismatch')
            counts['windows'] += 1
        except Exception as exc:
            errors.append({'kind': 'window', 'id': name, 'error': str(exc)})
    for item in manifest.get('freezes', []):
        try:
            require(digest(confined(base,item['file']).read_bytes()) == item['sha256'], 'Freeze hash mismatch')
            counts['freezes'] += 1
        except Exception as exc:
            errors.append({'kind': 'freeze', 'id': item.get('file'), 'error': str(exc)})
    git = None
    if baseline is not None:
        if source_root is None:
            errors.append({'kind': 'baseline', 'error': '--baseline requires --source-root'})
        else:
            for name, expected in baseline.items():
                try:
                    require(digest(confined(source_root,name).read_bytes()) == expected, 'Baseline file hash mismatch')
                    counts['baseline_files'] += 1
                except Exception as exc:
                    errors.append({'kind': 'baseline', 'id': name, 'error': str(exc)})
    if source_root is not None:
        git = {}
        for field, arguments in [('head',['rev-parse','HEAD']),('status',['status','--porcelain'])]:
            result = subprocess.run(['git','-C',str(source_root),*arguments],capture_output=True,text=True)
            git[field] = result.stdout.strip() if result.returncode == 0 else None
            if result.returncode:
                errors.append({'kind': 'git', 'id': field, 'error': result.stderr.strip()})
    return {'status': 'FAIL' if errors else 'PASS', 'counts': counts, 'failures': errors, 'source_git': git, 'limit': 'Native bytes, coverage and immutability only; no optical interpretation or historical correctness certified.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--base-dir', type=Path, default=Path('.'))
    parser.add_argument('--report', type=Path, default=Path('verification.json'))
    parser.add_argument('--source-root', type=Path)
    parser.add_argument('--baseline', type=Path)
    args = parser.parse_args()
    base = args.base_dir.resolve()
    try:
        report_path = args.report.resolve() if args.report.is_absolute() else confined(base,str(args.report))
        require(report_path.is_relative_to(base), 'Report must stay within base directory')
        require(report_path != args.manifest.resolve(), 'Report would overwrite manifest')
        manifest = json.loads(args.manifest.read_text())
        protected = {confined(base,s['file']) for s in manifest.get('sources',[])} | {confined(base,w['raw_file']) for w in manifest.get('windows',[])} | {confined(base,f['file']) for f in manifest.get('freezes',[])}
        require(report_path not in protected, 'Report would overwrite evidence')
        baseline = json.loads(args.baseline.read_text()) if args.baseline else None
        report = verify(manifest,base,args.source_root,baseline)
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    except Exception as exc:
        report = {'status':'FAIL','failures':[{'kind':'input','error':str(exc)}]}
    print(json.dumps(report,indent=2))
    return 0 if report['status']=='PASS' else 1

if __name__ == '__main__':
    raise SystemExit(main())
