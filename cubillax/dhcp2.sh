#!/bin/bash
sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip pool add name=pool_sistemas ranges=10.0.0.2-10.0.0.50'
sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip dhcp-server network add address=10.0.0.0/24 gateway=10.0.0.1 dns-server=8.8.8.8,1.1.1.1'
sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip dhcp-server add name=pool_sistemas interface=ether2 address-pool=pool_sistemas lease-time=1d disabled=no'
