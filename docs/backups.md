# Backup workflow

The production setup was observed running `/opt/fegcraft-updated/backup_minecraft.sh` and `/opt/fegcraft-updated/backup_minecraft.py`. Its host scheduler is `/etc/cron.d/vector-fegcraft-backup`. The Python script stages a consistent copy, briefly stops/restarts the same Minecraft container for final synchronization, writes an incremental restic snapshot and verifies a restore probe.

These production scripts were **not** supplied as source files in this chat and are therefore **not reproduced or invented** here. To publish them, use the private-review exporter and perform a line-by-line review of credentials, repository paths, restic passwords, webhook URLs, usernames, metadata, restore targets and side effects.

Do not commit any actual restic repository, snapshot state, backups or `verified-snapshot.json` from production. A structural example is available in `backups/examples/verified-snapshot.example.json`.

Always perform recovery tests on a separate instance. RAID1 is not a backup.
