
#!/bin/bash

DIR="/home/cubillax/bloqueo-usap"
ARCHIVO="$DIR/ips.txt"

if [[ $EUID -ne 0 ]]; then
    echo "Ejecuta este script como root."
    exit 1
fi

mkdir -p "$DIR"
touch "$ARCHIVO"

# Consultar las IP actuales y guardarlas sin duplicados.
TEMP=$(mktemp)

for dominio in www.usap.edu usap.edu; do
    for tipo in A AAAA; do
        dig +short "$dominio" "$tipo"
    done
done |
grep -E '^[0-9a-fA-F:.]+$' |
sort -u > "$TEMP"

if [[ ! -s "$TEMP" ]]; then
    echo "No se encontraron IP. No se aplicó ningún bloqueo."
    rm -f "$TEMP"
    exit 1
fi

while IFS= read -r ip; do
    echo "Bloqueando USAP: $ip"

    ufw deny out to "$ip" port 80 proto tcp
    ufw deny out to "$ip" port 443 proto tcp
    ufw deny out to "$ip" port 443 proto udp

done < "$TEMP"

# Acumular IP nuevas y conservar las antiguas.
cat "$ARCHIVO" "$TEMP" |
sort -u > "$ARCHIVO.nuevo"

mv "$ARCHIVO.nuevo" "$ARCHIVO"
rm -f "$TEMP"

echo
echo "IP registradas en $ARCHIVO:"
cat "$ARCHIVO"

echo
ufw status numbered
