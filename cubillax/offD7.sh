#!/bin/bash
IParduino="192.168.88.100"
resp=$(curl -fsS --connect-timeout 3 --max-time 5 "http://${IParduino}/off")
if [ $? -eq 0 ]
               then
                   echo "Arduino : $resp"
                   echo 0 > /home/cubillax/estado.txt
else
    echo "Error no se puede conectar"

fi

