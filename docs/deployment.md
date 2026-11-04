# Deployment

This is a **reproducibility blueprint**, not a complete unattended production installer. It will only become exact after the original Minecraft image build provenance, complete reviewed configuration, third-party JAR rights, world backup and integration contracts are added.

## Recommended workflow

1. Provision a **separate test host** with sufficient capacity and current security updates.
2. Install Docker Engine and the Compose plugin using official supported packages.
3. Clone this repository and copy `.env.example` to a local `.env`.
4. Rebuild or obtain the **original, trusted Fabric image**. The production `fegcraft-updated` image was observed by image ID, not a public build recipe. Do not substitute an arbitrary image as if it were identical.
5. Review your full, sanitized `server.properties`, Velocity config and any mod configs. Put credentials only into local secret files or an external secret manager.
6. Acquire the exact mods independently from their official sources and verify SHA-256 hashes against the generated manifest.
7. Supply world data via your approved backup restore procedure. **Never restore over the running production world.**
8. Adapt the illustrative `compose.example.yaml` to the actual image's environment interface, paths, forwarding mode, private network, healthchecks and integration endpoints. Validate with `docker compose -f compose.example.yaml config` after setting `MC_IMAGE`.
9. Test joins through Velocity, voice chat, Discord linking, Vector API flows, map, backups and recovery before going live.

## Production safety

No scripts in this repo restart, stop, remove or recreate production containers. No `docker compose down`, `prune` or destructive maintenance commands are supplied. The daily 03:00 backup job is **not** a generic maintenance window for arbitrary changes; it may briefly restart only Minecraft as part of its existing backup consistency procedure.
