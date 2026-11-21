#!/bin/bash
IPROUTER="192.168.88.200"
USER="admin"
PASS="1234567"
DATE=$(date +%Y%m%d_%H%M)
PATHFINAL="/home/cubillax/RESPALDOMK"
sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$IPROUTER "/system backup save name=respaldo_$DATE"
sshpass -p "$PASS" scp -O -o StrictHostKeyChecking=no $USER@$IPROUTER:respaldo_$DATE.backup $PATHFINAL
