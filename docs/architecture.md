# Architecture

The Minecraft backend and Velocity proxy run in separate
Docker containers on a Debian 13 host.

```text
Minecraft client
       |
       | TCP 25565
       v
Velocity proxy
       |
       v
Fabric backend
       |
       +-- Gameplay and world generation
       +-- Open Parties and Claims
       +-- Discord Integration
       +-- Simple Voice Chat
       +-- BlueMap
       +-- Performance and utility mods

External systems

Discord <---- Minecraft integration
Vector  <---- Separate integration bridge
Backups <---- Host-side backup workflow
```

## Components

| Component | Role |
| --- | --- |
| `velocity` | Player-facing Minecraft proxy |
| `fegcraft-updated` | Fabric gameplay backend |
| FabricProxy-Lite | Backend integration with Velocity |
| Discord Integration | Minecraft-side Discord connectivity |
| Open Parties and Claims | Parties, territory and claim management |
| Simple Voice Chat | Player voice communication |
| BlueMap | Browser-based world map |
| Vector | Separately hosted application integration |

The exact Discord and Vector transport contracts are not
publicly established. Their presence does not imply an
available REST API or a particular webhook schema.

## Security boundary

The published Minecraft properties specify
`online-mode=false` for the backend. Authentication therefore
depends on the correctly configured proxy boundary.
Direct backend access requires appropriate restrictions.
