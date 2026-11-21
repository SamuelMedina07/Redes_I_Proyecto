#!/bin/bash

ARDUINO="192.168.88.100"

respuesta=$(curl -fsS --connect-timeout 3 --max-time 5 \
    "http://${ARDUINO}/on")

if [ $? -eq 0 ]; then
    echo "Arduino: $respuesta"
else
    echo "Error: no se pudo encender D7."
    exit 1
fi

