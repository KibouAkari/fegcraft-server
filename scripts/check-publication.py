#!/usr/bin/env python3
"""Conservative repository guardrails; NOT a complete secrets audit."""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[1]
forbidden = [re.compile(p, re.I) for p in [
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'(?:discord[_-]?token|rcon[_-]?password|api[_-]?key|forwarding[_-]?secret)\s*[=:]\s*["\']?(?!<|REPLACE|CHANGEME|EXAMPLE)[a-z0-9_\-]{16,}',
]]
failures = []
for f in root.rglob('*'):
    if not f.is_file() or '.git' in f.parts or 'private-review' in f.parts:
        continue
    rel = f.relative_to(root).as_posix()
    if rel.startswith('mods/jars/') and f.suffix == '.jar':
        failures.append(f'Unexpected third-party JAR: {rel}')
    if f.name == '.env' or (f.name.startswith('.env.') and f.name != '.env.example'):
        failures.append(f'Private environment file: {rel}')
    if f.name in {'ops.json','whitelist.json','banned-ips.json','banned-players.json','forwarding.secret'}:
        failures.append(f'Potential sensitive runtime data: {rel}')
    if f.suffix.lower() in {'.md','.json','.yml','.yaml','.py','.sh','.toml','.example','.txt'}:
        try:
            content = f.read_text(encoding='utf-8')
        except UnicodeError:
            continue
        for pattern in forbidden:
            if pattern.search(content):
                failures.append(f'Possible private credential: {rel}')
if failures:
    print('\n'.join(failures), file=sys.stderr)
    sys.exit(1)
print('Repository guardrails passed. Manual secret and license review still required.')
