#!/bin/bash
IPROUTER="10.105.148.110"
USER="admin"
PASSWORD="TU_PASSWORD"
PATHDEST="/home/cubillax/router"
DATE=$(date +%Y%m%d_%H%M)

sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$IPROUTER "/system backup save name=backup_$DATE"
sleep 2
sshpass -p "$PASSWORD" scp -O -o StrictHostKeyChecking=no $USER@$IPROUTER:
backup_$DATE.backup $PATH
