#!/bin/bash

# archivo donde se van ha registrar la bitacora de eventos
ARCHIVO="/var/log/estado_servidor.txt"

echo $ARCHIVO

# Usuario que inicia sesion
USUARIO="${PAM_USER:-${SUDO_USER:-$(whoami)}}"

echo ${USUARIO}

# Fecha y Hora del Servidor
FECHA=$(date '+%Y-%m-%d')

echo ${FECHA}

HORA=$(date '+%H:%M:%S')

echo ${HORA}

# PROCESO QUE EJECUTA EL SCRIPT
PID=$$

echo ${PID}

# IP DEL CLIENTE
IPCLIENTE=$(who | tail -n1 | awk -F'[()]' '/pts/ {print $2; exit}')

echo ${IPCLIENTE}
# VER IP DEL SERVIDOR

IP_SERVER=$(hostname -I | awk '{print $1}')

echo ${IP_SERVER}

# RECORD TIEMPO ARRIBA DE SERVER

UPSERVER=$(uptime | cut -d " " -f5)

echo ${UPSERVER}

ESTADO=1

echo ${ESTADO}

OBS="ENCENDIDO"

echo ${OBS}

# GENERANDO ARCHIVO TEXTO

echo "${USUARIO};${FECHA};${HORA};${PID};${IPCLIENTE};${IP_SERVER};${UPSERVER};${ESTADO};${OBS}" >> final_log.txt
