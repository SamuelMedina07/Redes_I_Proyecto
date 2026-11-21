#!/bin/bash
ARDUINO="192.168.88.100"
resp=$(curl -fsS --connect-timeout 3 --max-time 5 "http://${ARDUINO}/on")

if [ $? -eq 0 ]; then
     echo "Arduino $resp"
else
    echo "error no se puede Conectar"
    exit 1
fi
