#!/bin/bash
iparduino="192.168.88.100"
resp=$(curl -fsS --connect-timeout 3 --max-time 5 "http://${iparduino}/off")
if [ $? -eq 0 ]; then
                 echo "Arduino $resp"
                 #echo $resp > /home/cubillax/comp_unah/estado.txt
else
    echo "Error de conexion con Arduino"
    exit 1

fi

