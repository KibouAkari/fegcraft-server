# Velocity configuration

The production instance uses `itzg/mc-proxy` with `/opt/velocity/config` mounted at `/config`, and a separate Docker volume mounted at `/server`.

The November 2026 configuration contained `show-max-players = 777`, but the live status ping **still reported 69**. The cause was not established. `ping-passthrough.players` was `false`.

Do not publish the raw `velocity.toml` without reviewing modern forwarding secrets, backend endpoints, IPs, tokens and potentially unique identifiers. Export an approved template with placeholders and confirm that the runtime uses it.
