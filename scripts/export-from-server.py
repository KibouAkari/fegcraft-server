#!/usr/bin/env python3
"""Safe, read-only limited export from a production FEGCRAFT host.

Does not copy secrets, restart containers, change production files or push to GitHub.
Backup scripts and any extra config require independent manual review.
"""
import argparse
import json
from pathlib import Path

ALLOWED_SERVER_PROPERTIES = {
    'view-distance', 'simulation-distance', 'max-players',
    'network-compression-threshold', 'entity-broadcast-range-percentage',
    'sync-chunk-writes', 'pause-when-empty-seconds', 'server-port'
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--production-root', default='/opt/fegcraft-updated/data')
    parser.add_argument('--output', default='private-review/host-export')
    args = parser.parse_args()
    src = Path(args.production_root)
    dst = Path(args.output)
    if not src.is_dir() or src.is_symlink():
        parser.error('Production data root not available or is a symbolic link')
    if not str(dst.resolve()).startswith(str(Path.cwd().resolve()) + '/'):
        parser.error('Export destination must be inside the current working directory')
    dst.mkdir(parents=True, exist_ok=True)
    result = {}
    properties = src/'server.properties'
    if properties.is_file() and not properties.is_symlink():
        for line in properties.read_text(encoding='utf-8').splitlines():
            if '=' not in line or line.lstrip().startswith('#'):
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            if key in ALLOWED_SERVER_PROPERTIES:
                result[key] = value.strip()
    (dst/'minecraft-safe-properties.json').write_text(json.dumps(result, indent=2)+'\n')
    print('Exported allowlisted server.properties values only.')
    print('Not exported: Docker inspect, environment, Velocity secrets, backup scripts, world, player data or tokens.')
    print('NEXT: Review all additional production files manually in private review and run publication safety checks.')

if __name__ == '__main__':
    main()
