# Developer: Universidad
from s7 import Client
from s7.type import Area

plc=Client()

try:
    plc.connect("192.168.88.20",0,1)
    datos=plc.read_area(Area.MK,0,100,1)
    datos[0]&=0xFE
    plc.write_area(Area.MK,0,100,bytes(datos))
    print("M100.0 APAGADA")

except Exception as e:
       print("ERROR:",e)
finally:
        if plc.get_connected():
           plc.disconnect()

