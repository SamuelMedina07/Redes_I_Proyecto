# Developer: Universidad
from s7 import Client
from s7.type import Area

PLC_IP="192.168.88.20"
plc=Client()

try:
    plc.connect(PLC_IP,0,1)
   
    # Leer Salida QB0
    salida=plc.read_area(Area.PA,0,0,1)
    
    # Leer La Marca MB100
    marca=plc.read_area(Area.MK,0,100,1)

    # Extraer los bits
    q00=bool(salida[0] & 0b00000001)
    m100=bool(marca[0] & 0b00000001)

