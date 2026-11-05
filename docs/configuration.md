# Configuration reference

## Published configuration

| Path | Description |
| --- | --- |
| `config/minecraft/server.properties` | Selected production Minecraft settings |
| `mods/mods.lock.json` | Exact observed mod versions and checksums |
| `mods/mods.csv` | Tabular mod inventory |

## Production configuration locations

| Component | Host location |
| --- | --- |
| Minecraft | `/opt/fegcraft-updated/data/server.properties` |
| Fabric mods | `/opt/fegcraft-updated/data/config/` |
| Minecraft Compose | `/opt/fegcraft-updated/docker-compose.yml` |
| Velocity Compose | `/opt/velocity/docker-compose.yaml` |
| Velocity | `/opt/velocity/config/velocity.toml` |
| Discord Integration | `/opt/fegcraft-updated/data/config/Discord-Integration.toml` |
| Discord commands and messages | `/opt/fegcraft-updated/data/DiscordIntegration-Data/` |
| Backup scripts | `/opt/fegcraft-updated/` |

These paths describe the production host, not files
that must exist in a developer's local workspace.

## Private configuration

Proxy forwarding secrets, Discord credentials, Vector
tokens, account mappings, player data and backup secrets
are excluded.

The existing illustrative Compose example does not
represent a complete production deployment.
