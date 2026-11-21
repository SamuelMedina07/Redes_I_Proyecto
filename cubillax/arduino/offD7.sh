#!/bin/bash
IParduino="192.168.88.100"
resp=$(curl -fsS --connect-timeout 3 --max-time 5 "http://${IParduino}/off")
if [ $? -eq 0 ]
               then
                    echo "Arduino : $resp"
else
     echo "error no se conectar al microcontrolador Arduini uno r4 wifi"
     exit 1
fi

