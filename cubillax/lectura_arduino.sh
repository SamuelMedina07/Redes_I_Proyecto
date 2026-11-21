#!/bin/bash
arduino="http://192.168.88.100"
estado=$(curl -fsS --connect-timeout 3 --max-time 5 "$arduino")
if [ $? -ne 0 ]; then 
    echo "error: no hay comunicacion con el Arduino"
    exit 1
fi

estado=$(echo "$estado" | tr -d '{:space}')

case "$estado" in
      1) 
         echo "GPIO D7 = Encendido"
         ;;
      0) 
        echo "GPIO D7 = Apagado"
        ;; 
      *)
        echo "Respueta Incorrecta"
        ;; 
esac
