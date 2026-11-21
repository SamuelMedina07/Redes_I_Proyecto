# Developer
from s7 import Client
from s7.type import Area

PLC_IP="192.168.88.20"

plc=Client()

try:
    plc.connect(PLC_IP,0,1)
    if not plc.get_connected():
       raise Exception("PLC no Conectado")
    datos=plc.read_area(Area.PA,0,0,1)
    datos[0] |= 0x02
    plc.write_area(Area.PA,0,0,bytes(datos))
    print("Q0.1 ENCENDIDA")
except Exception as e:
       print("ERROR:",e)
finally:
        if plc.get_connected():
           plc.disconnect()

