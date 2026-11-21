#!/bin/bash
IP="192.168.88.200"
sudo sshpass -p "1234567" ssh -l admin $IP 'system identity print'

