#!/usr/bin/env python3
"""Read-only mod inventory. No downloads, uploads, modifications or server actions."""
import argparse
import hashlib
import json
import pathlib
import zipfile

def hash_file(path):
    h = hashlib.sha256()
    with path.open('rb') as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def metadata(path):
    try:
        with zipfile.ZipFile(path) as archive:
            if 'fabric.mod.json' in archive.namelist():
                data = json.loads(archive.read('fabric.mod.json'))
                return {'id': str(data.get('id', '')), 'name': str(data.get('name', '')), 'version': str(data.get('version', ''))}
    except (zipfile.BadZipFile, UnicodeDecodeError, ValueError, KeyError):
        return {}
    return {}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mods-dir', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    directory = pathlib.Path(args.mods_dir).resolve(strict=True)
    if not directory.is_dir():
        p.error('Not a directory')
    files = sorted(p for p in directory.iterdir() if p.is_file() and not p.is_symlink() and p.suffix.lower() == '.jar')
    mods = []
    for jar in files:
        info = metadata(jar)
        mods.append({'filename': jar.name, 'mod_id': info.get('id') or None,
                     'mod_name': info.get('name') or None,
                     'version': info.get('version') or None,
                     'sha256': hash_file(jar), 'source_url': None, 'license': None,
                     'redistribution_reviewed': False})
    result = {'minecraft_version': '26.2', 'fabric_loader_version': '0.19.5',
              'inventory_method': 'local JAR metadata and SHA256', 'mods': mods}
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Inventoried {len(mods)} JARs -> {out}')

if __name__ == '__main__':
    main()
