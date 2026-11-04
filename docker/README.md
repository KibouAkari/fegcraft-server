# Docker image provenance

Production `fegcraft-updated` used a locally identified image (`e5166b077bb0` in the observed `docker ps` output). That ID does not reveal the source Dockerfile or all build inputs.

Before describing this repo as a complete production rebuild, export and review the exact Dockerfile, image tag/digest, base image, entrypoint, healthcheck, environment interfaces, installed Java/Fabric versions and mounts. Do not publish an invented Dockerfile claiming parity.

The sample `compose.example.yaml` deliberately does not claim full parity and must not be deployed against production unchanged.
