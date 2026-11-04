# Integrations

## Discord

`dcintegration-fabric-MC26.2-3.2.1.jar`, `vcinteraction-fabric-1.0.8+26.2.jar` and `voicechat-fabric-2.6.23+26.2.jar` were present. No production token, channel mapping or bot credentials are exported. Validate login/linking and moderation events in a private test environment.

## Vector

The host runs `vector-fegcraft-assistant` alongside the separate Vector application stack. Exact integration API and service credentials have not been supplied for this starter. Document their *interface contracts* in a reviewed example file before claiming reproductions work.

## Velocity

Proxy to Fabric forwarding mode and authentication need to be preserved exactly, with secrets injected at deployment. Do not expose a Fabric backend directly before verifying proxy-only joins and authentication requirements.

## Player-facing services

Verify public Minecraft TCP status and join, voice UDP, web map, claims, permissions, world backups and webhook messages in the test deployment. A Docker `healthy` status alone is not a full functional test.
