# Mod development reference

This document describes the existing runtime and systems
relevant to developing mods for FEGCRAFT.

## Target environment

| Component | Version |
| --- | --- |
| Minecraft | 26.2 |
| Fabric Loader | 0.19.5 |
| Java | 25 |
| Fabric API | 0.161.0+26.2 |
| Open Parties and Claims | 0.31.6 |
| FabricProxy-Lite | 2.12.0 |
| Simple Voice Chat | 2.6.23 |
| Discord Integration | 3.2.1 |
| Lithium | 0.25.3 |
| ServerCore | 1.5.19 |

The authoritative JAR inventory is
[`mods.lock.json`](../mods/mods.lock.json).

## Existing systems

### Claims and parties

Open Parties and Claims provides the existing party and
claim system. Mods modifying blocks, containers, entities
or territory must respect the deployed claim permissions.

Any OPAC API integration must target the installed version.

### Proxy and player identity

Minecraft connections enter through Velocity.
Player identity and forwarding behavior depend on
Velocity and FabricProxy-Lite configuration.

Mods must not bypass the proxy authentication boundary.

### Discord integration

Discord Integration is installed. Discord account linking,
commands and event handling depend on its configuration
and external components.

The exact custom integration protocol is not yet documented
as a stable public API.

### Voice communication

Simple Voice Chat and Voice Chat Interaction are present.
New voice features should account for these existing mods.

### World generation

Tectonic, Terralith, Structory and other generation mods
are installed. New world-generation features must be tested
against the existing stack and world compatibility.

### Performance

Existing optimization components include Lithium, C2ME,
FerriteCore, ModernFix, Noisium and ServerCore.

Avoid blocking operations on the tick thread, unnecessary
chunk loading and excessive synchronous disk writes.

## References

- [Full mod inventory](../mods/mods.lock.json)
- [Server architecture](architecture.md)
- [Networking](network.md)
- [External integrations](integrations.md)
- [Configuration](configuration.md)
