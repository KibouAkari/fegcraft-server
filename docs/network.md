# Networking

## Known ports

| Port | Protocol | Component | Function |
| --- | --- | --- | --- |
| 25565 | TCP | Velocity | Public Minecraft entry point |
| 25566 | TCP | Fabric | Backend Minecraft listener |
| 24454 | UDP | Simple Voice Chat | Voice communication |
| 8100 | HTTP/TCP | BlueMap | Local map upstream |

## Domains

| Hostname | Service |
| --- | --- |
| `fegcraft.modsmp.ch` | Minecraft via Velocity |

The map's external URL depends on the reverse proxy
configuration and is not established by port 8100 alone.

## Exposure

Velocity is the intended player-facing entry point.

The backend has previously been observed with a published
host port. Backend reachability must be restricted to
trusted forwarding paths to prevent proxy bypass.

Ports listed here describe the known Minecraft stack;
they are not a host-wide firewall inventory.
