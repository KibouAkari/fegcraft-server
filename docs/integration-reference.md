# Integration reference

This document describes the configuration interfaces observed
in the FEGCRAFT production installation.

Configuration keys establish available settings, not necessarily
their enabled state or a stable public API.

## Discord Integration

**Installed version:** 3.2.1

The Minecraft integration exposes the following configuration
areas.

| Configuration section | Purpose |
| --- | --- |
| `general` | Bot and server settings |
| `messages` | Minecraft and Discord message configuration |
| `commands` | Command integration |
| `ingameCommand` | In-game command handling |
| `linking` | Minecraft and Discord account linking |
| `linking.personalSettingsDefaults` | Default linked-account preferences |
| `embedMode.*` | Embedded messages for gameplay events |
| `commandLog` | Command logging configuration |
| `advanced` | Advanced behavior |
| `compatibility` | Compatibility settings |
| `bungee` | Proxy-related settings |
| `webhook` | Webhook configuration |

### Account linking

The configuration defines `enableLinking`, `globalLinking`,
`requiredRoles`, `shouldNickname` and `unlinkOnLeave`.

The message configuration contains successful-link,
failed-link and account lookup messages.

A supported custom linking protocol or Discord ID to
Minecraft UUID API has not been established.

Live account mappings are not distributed.

### Custom commands

`DiscordIntegration-Data/Commands.toml` exposes these fields:

| Field | Meaning |
| --- | --- |
| `name` | Command name |
| `args` | Argument definitions |
| `optional` | Optional argument setting |
| `adminOnly` | Administrative restriction setting |
| `mcCommand` | Minecraft command field |
| `textToSend` | Message output field |

This describes configuration keys, not a confirmed external
command API. Actual commands and their permissions depend
on the production configuration.

### Gameplay message types

Configured message templates include:

- Player joins and leaves
- Player deaths
- Advancements
- Minecraft chat
- Server startup and shutdown
- Discord chat and replies

These are configuration categories. Runtime activation has
not been independently verified.

## Vector bridge

Production configuration:
`DiscordIntegration-Data/vector/bridge.properties`

Observed setting names:

| Setting | Role |
| --- | --- |
| `enabled` | Bridge activation setting |
| `discordInputEnabled` | Discord input setting |
| `introductionEnabled` | Introduction feature setting |
| `ownerWelcomeEnabled` | Owner welcome feature setting |
| `logoTexture` | Logo texture setting |

The presence of these settings does not establish the bridge
transport, request schema or authentication model.

No public REST API, webhook or message payload contract
is currently confirmed.

## Velocity and FabricProxy-Lite

The Velocity configuration defines these backend labels:

- `fegcraft-updated`
- `fegcraft-test`
- `lobby`
- `nicolassmp`

These are configured backend entries, not an inventory
of currently running servers.

Relevant Velocity settings include `online-mode`,
`player-info-forwarding-mode`, `bind`, `try` and
`show-max-players`.

FabricProxy-Lite exposes:

- `hackOnlineMode`
- `hackEarlySend`
- `hackMessageChain`
- `disconnectMessage`

Authentication behavior depends on the actual configuration
values and the relationship between Velocity and Fabric.

Forwarding secrets and backend addresses are excluded.

## Mod integration boundaries

New FEGCRAFT mods should use established server-side APIs
where available and respect existing proxy, claim, permission
and identity handling.

The existence of a configuration key does not guarantee a
supported Java API or stable external protocol.
