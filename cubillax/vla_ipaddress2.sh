#!/bin/bash
sshpass -p "1234567" ssh -l admin 10.200.1.50 'ip address add address=192.168.50.1/24 interface=ether4 comm=LAN4'
