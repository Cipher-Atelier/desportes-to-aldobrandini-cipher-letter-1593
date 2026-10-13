#!/usr/bin/env python3
"""Render only curated literal working text; no modern candidate layer."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parent

def render():
    data = json.loads((ROOT / 'line-records.json').read_text())
    lines = ['# Desportes — literal French working transcript', '',
             '22 juillet 1593 — Illustrissime Monseigneur', '',
             'Editorial header; literal working choices, not a complete exact decipherment. Code labels and gaps remain unresolved. See README.md for credits and limits.', '']
    for record in data['records']:
        lines += [f"**{record['line']}** — {record['literal_working_text']}", '']
    lines += ['## Footer — retained literal reading', '']
    for item in data['footer']:
        lines += [item['diplomatic'], '']
        if item.get('note'):
            lines += [f"Editorial note: {item['note']}", '']
    return '\n'.join(lines).rstrip() + '\n'

if __name__ == '__main__':
    (ROOT / 'transcript-fr.md').write_text(render())
    print('Rendered 85 literal physical lines with header and footer.')
