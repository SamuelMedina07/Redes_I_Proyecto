#!/bin/bash
sitio1="www.usap.edu"
sitio2="usap.edu"
for dominio in "$sitio1" "$sitio2"; do
    echo "---- $dominio ----"
    echo "IPV4"
    dig +short "$dominio" A
    echo "IPV6"
    dig +short "$dominio" AAAA
done
