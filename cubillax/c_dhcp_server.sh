#!/bin/bash
sshpass -p "1234567" ssh -l admin 192.168.88.200 'ip dhcp-server print'
