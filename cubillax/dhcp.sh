#!/bin/bash
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip pool add name=pool_lan ranges=192.168.10.10-192.168.10.20'
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=8.8.8.8,1.1.1.1'
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip dhcp-server add name=dhcp_lan interface=ether2 address=pool_lan lease_time=1d disabled=no'
