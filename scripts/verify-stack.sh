#!/usr/bin/env bash
set -euo pipefail
# Read-only production status: safe to run after installing on the intended host.
for service in fegcraft-updated velocity; do
  timeout 8 docker inspect "$service" --format '{{.Name}} {{.State.Status}} {{if .State.Health}}{{.State.Health.Status}}{{end}}'
done
for port in 25565; do
  if timeout 3 bash -c "</dev/tcp/127.0.0.1/$port"; then
    echo "Local TCP $port accepts connections"
  else
    echo "Local TCP $port not accepting connections"
  fi
done
