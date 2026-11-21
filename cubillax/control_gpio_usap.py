# Developer: Universidad
from tkinter import *
from tkinter import font
from tkinter import ttk
import os
import subprocess
import time

# Crear ventana
v0=Tk()
v0.title("Control GPIO Microcontrolador")
v0.geometry("700x300+200+150")

img_on=PhotoImage(file="on.gif")
img_off=PhotoImage(file="off.gif")

def actualiza_D7():
                   pf=open("/home/cubillax/comp_unah/estado.txt","r")
                   for linea in pf:
                                   campo=linea.split("\n")
                                   campof=campo[0]
                                   if (campof=="1"):
                                                    btn_on=Button(v0,image=img_on).place(x=200,y=150)
                                                    v0.after(1000,actualiza_D7)
                                   if (campof=="0"):
                                                    btn_off=Button(v0,image=img_off).place(x=200,y=150)
                                                    v0.after(1000,actualiza_D7)                 
                                                    
                                
actualiza_D7()


def encenderD7():
                  os.system("sudo /./home/cubillax/comp_unah/onD7.sh &")
                  
def apagarD7():
               os.system("sudo /./home/cubillax/comp_unah/offD7.sh & ")
               
btn_encender=Button(v0,text="ON",bg="black",fg="white",command=encenderD7).place(x=10,y=50)
btn_apagar=Button(v0,text="OFF",bg="black",fg="white",command=apagarD7).place(x=130,y=50)

v0.mainloop()
