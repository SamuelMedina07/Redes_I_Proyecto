from s7 import Client
from s7.type import Area

PLC_IP = "192.168.88.20"

plc = Client()

try:
    plc.connect(PLC_IP, 0, 1)
    print("Conectado al PLC")

    datos = plc.read_area(Area.PA, 0, 0, 1)

    print("Lectura correcta:", list(datos))

except Exception as e:
    print("ERROR:", e)

finally:
    if plc.get_connected():
        plc.disconnect()
