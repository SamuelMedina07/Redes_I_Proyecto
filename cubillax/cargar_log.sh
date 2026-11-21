#!/bin/bash
# Parametros globales
DB_NAME="TEORIACOMP"
DB_USER="unah"
DB_PASS="Developer+2026"
DB_TABLE="log"
DATA_FILE="final_log.txt"

# verificar si exite el file .txt
if [ ! -f "$DATA_FILE" ]; then
     echo "Error: El Archivo $DATA_FILE no existe"
     exit 1
fi

# conexion con Mysql
mysql --local-infile=1 -u$DB_USER -p$DB_PASS $DB_NAME <<EOF
-- Vaciar la tabla log
DELETE FROM $DB_TABLE;
-- Cargar los Datos desde el archivo .txt
LOAD DATA LOCAL INFILE '$DATA_FILE'
INTO TABLE $DB_TABLE
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
(USUARIO,FECHA,HORA,PROCESO,IPCLIENTE,IPSERVER,UPSERVER,ESTADO,OBS);
EOF
echo "DATOS CARGADOS CON EXITO"
