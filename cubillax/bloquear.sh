#!/bin/bash

for dominio in www.laprensa.hn laprensa.hn; do
    for tipo in A AAAA; do
        dig +short "$dominio" "$tipo" |
        grep -E '^[0-9a-fA-F:.]+$' |
        sort -u |
        while read -r ip; do
            [ -z "$ip" ] && continue

            echo "Bloqueando $dominio -> $ip"

            sudo ufw deny out to "$ip" port 80 proto tcp
            sudo ufw deny out to "$ip" port 443 proto tcp
            sudo ufw deny out to "$ip" port 443 proto udp
        done
    done
done

sudo ufw status numbered
