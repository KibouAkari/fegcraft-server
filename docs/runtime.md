# Production inventory snapshot

**Captured from user-provided audit: November 2026.** Values may have changed since the audit.

| Item | Observed state |
| --- | --- |
| OS | Debian 13 (trixie) |
| CPU | Intel Core i7-7700, 4 physical cores / 8 logical CPUs |
| Memory | 62 GiB system RAM |
| Storage | two 3.6 TB HDDs with RAID1 arrays |
| Kernel after maintenance | `6.12.115+deb13.1-amd64` |
| Fabric launcher | `fabric-server-mc.26.2-loader.0.19.5-launcher.1.1.2.jar` |
| Java | Eclipse Temurin 25.0.4 |
| Java heap | `-Xms6G -Xmx24G` |
| Docker CPU cap (live) | 2.4 logical CPUs / 30% of host's 8 logical CPUs |
| Minecraft backend player maximum | 45 |
| Velocity advertised maximum (configured) | 777; status ping observed 69 |
| Distance settings staged | view=8, simulation=6 |
| Backup | daily around 03:00, incremental with restore probe |

**Known issues for maintainers:** startup error loading `minecraft:scoreboard` saved data and validation errors from `tru.e-ending`. These should be investigated before relying on a restored snapshot; neither is silently modified by this repo.

A 30% hard CPU cap is an upper limit, not an optimization, and may hurt peak TPS. No verified 100-player performance guarantee is made.
