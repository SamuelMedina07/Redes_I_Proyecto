#!/bin/bash
IPROUTER="192.168.88.200"
USER="admin"
PASSWORD="1234567"
PATHDEST="/home/cubillax/res_router"
DATE=$(date +%Y%m%d_%H%M)

sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$IPROUTER "/system backup save name=backup_$DATE"
sleep 2
sshpass -p "$PASSWORD" scp -O -o StrictHostKeyChecking=no $USER@$IPROUTER:backup_$DATE.backup $PATHDEST
