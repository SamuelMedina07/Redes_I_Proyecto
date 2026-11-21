#!/bin/bash
while true
          do 
             valor=$(curl -s --max-time 3 http://192.168.88.100/estado | cut -d " " -f3)
             if [ $valor = "1" ]
                                then
                                     echo $valor > /home/cubillax/comp_unah/estado.txt
                                     echo $valor
             else
                 if [ $valor = "0" ]
                                    then
                                         echo $valor > /home/cubillax/comp_unah/estado.txt
                                         echo $valor
                 fi                          
             fi
             sleep 0.1
          done
