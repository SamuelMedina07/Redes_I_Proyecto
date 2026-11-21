#!/bin/bash

CLAVE="cisco123"
USUARIO="admin"
IP="192.168.88.210"
NOMBRE="REDES_B"

sshpass -p "$CLAVE" ssh -T \
    -o KexAlgorithms=+diffie-hellman-group14-sha1 \
    -o HostKeyAlgorithms=+ssh-rsa \
    -o Ciphers=+aes128-cbc \
    -o StrictHostKeyChecking=accept-new \
    "$USUARIO@$IP" <<EOF
configure terminal
hostname $NOMBRE
end
write memory
exit
EOF
