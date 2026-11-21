#!/bin/bash

CLAVE="cisco123"
USUARIO="admin"
IP="192.168.88.210"

sshpass -p "$CLAVE" ssh -T \
 -o KexAlgorithms=+diffie-hellman-group14-sha1 \
 -o HostKeyAlgorithms=+ssh-rsa \
 -o Ciphers=+aes128-cbc \
 -o StrictHostKeyChecking=accept-new \
 "$USUARIO@$IP" <<EOF

configure terminal
interface GigabitEthernet0/1
no ip address
ip address 192.168.70.230 255.255.255.0
no shutdown
end
write memory
show ip interface brief
exit
EOF
