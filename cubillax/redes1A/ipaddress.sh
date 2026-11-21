#!/bin/bash
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip address add address=192.168.10.1/24 interface=ether2 comm=LAN2'
