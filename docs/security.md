# Publication policy

**Assume the repository will become public.** Publication is a separate decision; no auto-push is implemented.

- Never commit `.env`, cookies, JWTs, API keys, forwarding secrets, RCON passwords, restic passwords, recovery keys, private TLS keys or production databases.
- Do not commit player profile JSON, whitelists, bans, ops, live worlds, chat logs or raw logs (player IPs and UUIDs may be present).
- Treat real addresses, Discord IDs, internal service endpoints and cloud resource identifiers as deployment-specific; use placeholders where appropriate.
- Never assume a regex sanitizer can identify every secret. Review every diff manually, run a dedicated secret scanner, and prefer explicit field allowlists.
- Mod JARs are not included because license terms differ. Review individual licenses before redistribution.
- Never publish full raw Docker inspect outputs: they frequently expose environment variables and internal mounts.
- Running `scripts/check-publication.py` is a guardrail, **not a guarantee** that secrets are absent.
