# Developer: Universidad
# user:admin pass:cisco123 192.168.88.210
# password enable es : 1234 como super usuario #
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext
import os
import subprocess
import time

# Crear Ventana
v0=Tk()
v0.title("SCADA ROUTER CISCO")
v0.geometry("700x350+200+150")
# Zona de Funciones
def save_name():
                 print("Save cisco name...")
                 # variables
                 n=str(name.get())
                 # Constantes
                 enc="#!/bin/bash"
                 tab=" "
                 CLAVE="cisco123"
                 USUARIO="admin"
                 IP="192.168.88.210"
                 linea1_sec="sshpass -p \"$CLAVE\" ssh -T \\"
                 linea2_sec=" -o KexAlgorithms=+diffie-hellman-group14-sha1 \\"
                 linea3_sec=" -o HostKeyAlgorithms=+ssh-rsa \\"
                 linea4_sec=" -o Ciphers=+aes128-cbc \\"
                 linea5_sec=" -o StrictHostKeyChecking=accept-new \\"
                 linea6_sec="\"$USUARIO@$IP\" <<EOF"
                 com1="configure terminal"
                 com2="hostname"
                 com3="end"
                 com4="write memory"
                 com5="exit"
                 com6="EOF"

                 # name
                 cadena_name=(str(com2)+''+str(tab)+''+str(n))
                 
                 os.system("sudo touch /home/cubillax/redes1A/cisco_name.sh")
                 os.system("sudo chmod -R 777 /home/cubillax/redes1A/cisco_name.sh")
                 pf=open("/home/cubillax/redes1A/cisco_name.sh","w")
                 pf.write(enc)
                 pf.write("\n")
                 pf.write('CLAVE="cisco123"')
                 pf.write("\n")
                 pf.write('USUARIO="admin"')
                 pf.write("\n")
                 pf.write('IP="192.168.88.210"')
                 pf.write("\n")
                 pf.write(linea1_sec)
                 pf.write("\n")
                 pf.write(linea2_sec)
                 pf.write("\n")
                 pf.write(linea3_sec)
                 pf.write("\n")
                 pf.write(linea4_sec)
                 pf.write("\n")
                 pf.write(linea5_sec)
                 pf.write("\n")
                 pf.write(linea6_sec)
                 pf.write("\n")
                 pf.write(com1)
                 pf.write("\n")
                 pf.write(cadena_name)
                 pf.write("\n")
                 pf.write(com3)
                 pf.write("\n")
                 pf.write(com4)
                 pf.write("\n")
                 pf.write(com5)
                 pf.write("\n")
                 pf.write(com6)
                 
                 pf.close()

                 time.sleep(0.1)

                 os.system("sudo /./home/cubillax/redes1A/cisco_name.sh &")

                 messagebox.showinfo("INFO",message="Success")
                                  
                 
                 
# Tipo de Fuente
text1=font.Font(family="Arial",size=22)
text2=font.Font(family="Arial",size=16)
# Zona de Etiquetas
label_t1=Label(v0,text="SCADA CISCO SYSTEM",font=text1).place(x=150,y=10)
label_name=Label(v0,text="Router_Name :",font=text2).place(x=20,y=75)

#Cajas de texto
global name
name=StringVar()
txt_name=Entry(v0,textvariable=name,width=30).place(x=190,y=75)

# Zona de botones
btn_save=Button(v0,text="Save",bg="black",fg="white",command=save_name).place(x=470,y=70)



v0.mainloop()
