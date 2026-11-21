#!/bin/bash
cd /home/cubillax
ffplay triangulo_femenino.mp4 &
sleep 5
pkill -f triangulo_femenino.mp4
