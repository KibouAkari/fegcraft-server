# FEGCRAFT

**Minecraft Server Infrastructure & Mod Development Reference**

FEGCRAFT is a community Minecraft server running Minecraft
26.2 with Fabric, Velocity and Docker. This repository documents
the server architecture, installed mods, configuration,
gameplay systems and external integrations.

![FEGCRAFT](docs/images/summit-party.png)

## Environment

| Component | Production environment |
| --- | --- |
| Minecraft | 26.2 |
| Fabric Loader | 0.19.5 |
| Java | Eclipse Temurin 25 |
| Operating system | Debian 13 |
| Deployment | Docker Compose |
| Proxy | Velocity |
| Installed mod JARs | 64 |
| JVM heap | 6 GiB initial / 24 GiB maximum |
| Voice | Simple Voice Chat |
| Web map | BlueMap |
| Parties and claims | Open Parties and Claims |

## Technical documentation

| Reference | Description |
| --- | --- |
| [Architecture](docs/architecture.md) | Server components and data flow |
| [Network](docs/network.md) | Domains, ports and network boundaries |
| [Mod development](docs/mod-development.md) | Runtime compatibility and existing systems |
| [Installed mods](mods/README.md) | Versions, mod IDs and SHA256 hashes |
| [Integrations](docs/integrations.md) | Discord, Vector, Velocity, voice and map |
| [Configuration](docs/configuration.md) | Published and private configuration |
| [Runtime](docs/runtime.md) | Hardware, resource allocation and performance |
| [Backups](docs/backups.md) | Backup architecture |

| [Integration reference](docs/integration-reference.md) | Discord, Vector and proxy configuration interfaces |

## Server gallery

<table>
<tr>
<td><img src="docs/images/fegleimental-sign.png" alt="Settlement" /></td>
<td><img src="docs/images/mountain-cross.png" alt="Mountain cross" /></td>
</tr>
<tr>
<td><img src="docs/images/night-settlement.png" alt="Night settlement" /></td>
<td><img src="docs/images/fortress-overview.png" alt="Fortress" /></td>
</tr>
</table>

## Repository scope

This repository provides technical documentation and a
production-derived mod inventory. Worlds, player identities,
credentials, forwarding secrets and private runtime data are
not distributed. Third-party mods retain their own licenses.
