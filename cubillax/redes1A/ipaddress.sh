#!/bin/bash
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip address add address=192.168.20.1/24 interface=ether3 comment=LAN3'
