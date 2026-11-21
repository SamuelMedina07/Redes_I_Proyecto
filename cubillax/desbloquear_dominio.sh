#!/bin/bash

SITIO="$1"

DIR="/home/cubillax/$SITIO"
ARCHIVO="$DIR/ips.txt"

if [[ $EUID -ne 0 ]]; then
    echo "Ejecuta este script como root."
    exit 1
fi

if [[ ! -f "$ARCHIVO" ]]; then
    echo "No existe el archivo de IP: $ARCHIVO"
    exit 1
fi

while IFS= read -r ip; do
    [[ -z "$ip" ]] && continue

    echo "Desbloqueando IP: $ip"

    ufw --force delete deny out to "$ip" port 80 proto tcp
    ufw --force delete deny out to "$ip" port 443 proto tcp
    ufw --force delete deny out to "$ip" port 443 proto udp

done < "$ARCHIVO"

echo
echo "Verificando reglas restantes..."
ufw status numbered

echo
echo "Proceso de desbloqueo terminado."
