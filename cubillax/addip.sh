#!/bin/bash
sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip address add address=192.168.30.1/24 interface=ether4 comment=192.168.10.1/24'
