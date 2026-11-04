# Mods

The [snapshot manifest](mods.lock.json) lists the exact JAR filenames observed in November 2026. These are **filename-derived version hints**, not cryptographically verified files or manually audited mod identities. The `sha256` fields are null until a read-only hash inventory is run against real JARs.

Run on the Minecraft host (no restarts):

```bash
python3 scripts/generate_mod_manifest.py --mods-dir /opt/fegcraft-updated/data/mods --output mods/mods.lock.json
```

This reads JAR contents locally, extracts Fabric metadata when possible, and records SHA-256 without copying JAR bytes. Review filenames, metadata, licenses and download sources before publication. The program does not invent download URLs or license grants.

`mods/jars/` stays empty in the public repository until redistribution rights are verified. If rebuilding, retrieve original exact artifacts from their authors and verify hashes.
