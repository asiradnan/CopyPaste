#!/bin/bash

DB_NAME="copypasta_db"
DB_USER="postgres"
BACKUP_PATH="/root/DjangoApplications/CopyPaste/db_backups"
TIMESTAMP=$(date +"%F_%T")
BACKUP_FILE="$BACKUP_PATH/${DB_NAME}_backup_$TIMESTAMP.sql.gz"

# Create PostgreSQL backup
pg_dump -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_FILE"

# Upload to Dropbox
/root/Dropbox-Uploader/dropbox_uploader.sh upload "$BACKUP_FILE" /copypasta_db/

# Clean up
rm "$BACKUP_FILE"
