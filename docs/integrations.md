# Integrations

## Discord

Minecraft integration is provided by Discord Integration
3.2.1. Voice Chat Interaction is also installed.

Production configuration includes Discord commands,
messages and Minecraft account-linking state.

The public repository excludes live account mappings,
credentials, tokens and private identifiers.

The custom event schema and bot transport have not yet
been verified for third-party use.

## Vector

Vector is a separate application stack hosted alongside
the Minecraft environment.

A Vector-related bridge configuration exists in the
Minecraft integration data directory.

The authentication model, endpoints and message formats
remain private until their interfaces are reviewed.

## Velocity

Velocity is the Minecraft proxy. FabricProxy-Lite is
installed on the backend. Authentication and forwarding
configuration must remain consistent between both.

## Voice chat

Simple Voice Chat provides voice communication over UDP.
Voice Chat Interaction is installed alongside it.

## Web map

BlueMap provides the browser-accessible map.
Its local upstream is separate from public reverse
proxy routing.

## Gameplay systems

Open Parties and Claims provides party and claim
functionality. Its installed version is 0.31.6.
