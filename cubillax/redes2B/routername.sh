#!/bin/bash
IP="192.168.88.230"
sshpass -p "1234567" ssh -l admin 192.168.88.230 'system identity print'
