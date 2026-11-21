#!/bin/bash
for dominio in laprensa.hn www.laprensa.hn; do
    echo "---- $dominio ----"
    echo "IPV4"
    dig +short "$dominio" A
    echo "IPV6"
    dig +short "$dominio" AAAA
done
