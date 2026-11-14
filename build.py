#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'input'
DIST=ROOT/'dist'
with open(ROOT/'config.json',encoding='utf-8') as f: cfg=json.load(f)
if cfg['game']['version']!='1.4.3' or cfg['game']['build_id']!='277178B7DBA1B6D4':
    raise SystemExit('This prototype is locked to TOTK 1.4.3 (BID 277178B7DBA1B6D4).')
if not INPUT.exists() or not any(INPUT.rglob('*')):
    raise SystemExit('Put your own extracted TOTK 1.4.3 files under input/ before building.')
files=[p for p in INPUT.rglob('*') if p.is_file()]
DIST.mkdir(exist_ok=True)
manifest={'target':cfg['game'],'prototype':cfg['prototype'],'input_files':[{'path':str(p.relative_to(INPUT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
with open(DIST/'build-manifest.json','w',encoding='utf-8') as f: json.dump(manifest,f,indent=2)
print(f'Validated {len(files)} supplied files.')
