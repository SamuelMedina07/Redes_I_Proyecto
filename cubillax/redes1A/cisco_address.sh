bash
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
interface GigabitEthernet 0/1
ip address 192.168.88.199 255.255.255.0
no shutdown
exit
end
write memory
exit
EOF

