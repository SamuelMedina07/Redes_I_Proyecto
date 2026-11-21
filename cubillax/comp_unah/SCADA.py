# Developer: UNIVERSIDAD SCADA
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext
import os
import subprocess
import time

# Crear ventana
v0=Tk()
v0.title("CONTROL SCADA D7 ARDUINO")
v0.geometry("900x400+220+200")

# Zona de Funciones

img_on=PhotoImage(file="on.gif")
img_off=PhotoImage(file="off.gif")

def actualiza1():
                 pf=open("/home/cubillax/comp_unah/estado.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if (campof=="1"):
                                                  btn_on=Button(v0,image=img_on).place(x=390,y=50)
                                                  v0.after(1000,actualiza1)
                                                  
                                 if (campof=="0"):
                                                  btn_off=Button(v0,image=img_off).place(x=390,y=50)
                                                  v0.after(1000,actualiza1)

actualiza1()

def encender_D7_bash():
                       print("Encender D7 ...")
                       os.system("sudo /./home/cubillax/comp_unah/onD7.sh &")
                       
def apagar_D7_bash():
                       print("Apagar D7 ...")
                       os.system("sudo /./home/cubillax/comp_unah/offD7.sh &")

def EvaluarCheck_Bash():
                        ck1=str(check_bash.get())
                        if (ck1=="1"):
                                      encender_D7_bash()
                        if (ck1=="0"):
                                      apagar_D7_bash()

def EvaluarRadio():
                   rd=radio.get()
                   if (rd==1):
                               os.system("sudo /home/cubillax/comp_unah/estadoD7.sh &")
                               messagebox.showinfo("INFO",message="Monitor UP",parent=v0)
                   if (rd==2):
                              os.system("sudo /./home/cubillax/comp_unah/matar_monitoreo.sh &")
                              messagebox.showinfo("INFO",message="Monitor Down",parent=v0)

def tiempo_D7():
                v1=Toplevel()
                v1.title("Tiempo Proframado")
                v1.geometry("400x300+200+200")
                print ("Tiempo Programado.....")

                v1.mainloop()            


# Tipo de Fuente
text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=16)

# Zona de Etiquetas
label_t1=Label(v0,text="SCADA SYSTEM ARDUINO",font=text1).place(x=190,y=5)
label_t2=Label(v0,text="BASH",font=text2).place(x=10,y=50)

# Zona de botones
btn_onbash=Button(v0,text="ON",command=encender_D7_bash).place(x=10,y=120)
btn_offbash=Button(v0,text="OFF",command=apagar_D7_bash).place(x=100,y=120)
btn_tiempo=Button(v0,text="TIEMPO",command=tiempo_D7).place(x=500,y=120)

global check_bash,check_bash2
check_bash=StringVar()
c1=ttk.Checkbutton(v0,text="-ON-",variable=check_bash,command=EvaluarCheck_Bash)
c1.place(x=220,y=120)
c1=ttk.Checkbutton(v0,text="-OFF-",variable=check_bash,command=EvaluarCheck_Bash)
c1.place(x=320,y=120)

# Radio Button

global radio
radio=IntVar()
r1=ttk.Radiobutton(v0,text="Activar Monitoreo", variable=radio,value=1,command=EvaluarRadio)
r1.place(x=550,y=50)
r2=ttk.Radiobutton(v0,text="Desactivar Monitoreo",variable=radio,value=2,command=EvaluarRadio)
r2.place(x=710,y=50)

v0.mainloop()
