# Architecture

```text
Minecraft client -> Velocity proxy (public TCP 25565)
                         |
                         v
                  Fabric server (private backend)
                     |      |      |
                   mods  world  optional integrations
                                  | Discord / Vector / map / voice chat
```

Production used a `velocity` container and `fegcraft-updated` Fabric server container; the latter also published a UDP voice chat port and an HTTP map port bound to localhost. A backend TCP port was publicly bound in the observed setup; this is not recommended as a default for a fresh deployment. Proxy forwarding mode and protection must be reviewed before reproduction.

The project is hosted on a shared Debian 13 / Docker / libvirt machine with other unrelated production services. This repository **does not** export those other services or promise host-wide reproducibility.

## Integration boundaries

- **Discord:** `dcintegration` and voice integration mods were observed. Bot tokens, channel IDs and webhook URLs stay outside Git.
- **Vector:** the host runs a separate Vector application and a `vector-fegcraft-assistant` service. Their source, credentials and service contracts have not been exported, so integration cannot be assumed to work from the example Compose file.
- **Voice:** Simple Voice Chat is present; observed UDP port 24454.
- **Map:** observed localhost HTTP port 8100; nginx rules and upstream service need a separate approved export.
- **Backups:** separate host-side incremental restic workflow. See [backups.md](backups.md).
