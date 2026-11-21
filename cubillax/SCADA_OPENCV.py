# Developer Control GPIO
# SCADA OPENCV
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
import time

# crear ventana
v0=Tk()

v0.title("SCADA OPENCV")
v0.geometry("800x400+0+0")

img_on=PhotoImage(file="on.gif")
img_off=PhotoImage(file="off.gif")

def actualiza1():
                 pf=open("/home/cubillax/estado.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if (campof=="1"):
                                                  btn_imagen1=Button(v0,image=img_on).place(x=50,y=120)
                                                  v0.after(1000,actualiza1)

                                 if (campof=="0"):
                                                  btn_image2=Button(v0,image=img_off).place(x=50,y=120)

                                                  v0.after(1000,actualiza1)
# llamar funcion actualiza1
actualiza1()

def Activar_Monitoreo():
                        os.system("sudo /./home/cubillax/estadoD7.sh &")
                        messagebox.showinfo("INFO","SERVICIO DE MONITOREO ACTIVO")
                                                 
# Zona de funciones
def encender_D7():
                  os.system("sudo /./home/cubillax/onD7.sh &")
                  os.system("sudo /./home/cubillax/logON.sh &")
                  os.system("sudo /./home/cubillax/cargar_log.sh &")

                  messagebox.showinfo("INFO",message="ENCENDIDO")
                  

def apagar_D7():
                os.system("sudo /./home/cubillax/offD7.sh &")
                os.system("sudo /./home/cubillax/logOFF.sh &")
                os.system("sudo /./home/cubillax/cargar_log.sh &")
                messagebox.showinfo("INFO",message="APAGADO")

text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=16)

label_t1=Label(v0,text="SCADA OPENCV 2026",font=text1).place(x=150,y=10)

btn_on=Button(v0,text="ON",bg="green",fg="black",command=encender_D7).place(x=50,y=80)
btn_off=Button(v0,text="OFF",bg="red",fg="black",command=apagar_D7).place(x=120,y=80)
btn_monitor=Button(v0,text="ACTIVAR MONITOREO",bg="blue",command=Activar_Monitoreo).place(x=500,y=50)



v0.mainloop()
