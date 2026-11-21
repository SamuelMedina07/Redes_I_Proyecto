# Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext
import subprocess
import os
import time

# Crear ventana
v0=Tk()
v0.title("MIKROTIK SYSTEM")
v0.geometry("1000x500+0+0")

# zona de funciones
def clean():
            name.set('')

def save_name():
                print("Routername...")
                n=str(name.get())
                enc="#!/bin/bash"
                conexion='sshpass -p "1234567" ssh -l admin 192.168.88.200'
                tab=" "
                com1="system identity set name="
                cs="'"

                cadena1=(str(conexion)+''+str(tab)+''+str(cs)+''+str(com1)+''+str(n)+''+str(cs))
                os.system("sudo touch /home/cubillax/redes1A/routername.sh")
                os.system("sudo chmod -R 777 /home/cubillax/redes1A/routername.sh")
                pf=open("/home/cubillax/redes1A/routername.sh","w")
                pf.write(enc)
                pf.write("\n")
                pf.write(cadena1)
                pf.write("\n")
                pf.close()

                time.sleep(0.1)
                os.system("sudo /./home/cubillax/redes1A/routername.sh")

                messagebox.showinfo("INFO",message="Nombre Registrado con Exito",parent=v0)

                # llamar funcion clean
                clean()
                
                
                
def Query_name():
                 os.system("sudo /./home/cubillax/redes1A/consulta_mk.sh > /home/cubillax/redes1A/routername.txt")
                 valor=subprocess.check_output("cat /home/cubillax/redes1A/routername.txt",shell=True)
                 area1=scrolledtext.ScrolledText(v0,width=100,height=10)
                 area1.place(x=10,y=120)
                 area1.insert(END,valor)     

# Tipo de Fuente
text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=12)

# Zona de Etiquetas
label_t=Label(v0,text="MIKROTIK SYSTEM",font=text1).place(x=100,y=10)
label_name=Label(v0,text="ROUTER NAME:",font=text2).place(x=10,y=50)
label_ip=Label(v0,text="IP ADDRESS :",font=text2).place(x=10,y=100)
label_inter=Label(v0,text="INTERFACE :",font=text2).place(x=10,y=130)
label_comm=Label(v0,text="COMMENT:",font=text2).place(x=10,y=160)

# Caja de texto
global name,ipaddress,interface,comment
name=StringVar()
ipaddress=StringVar()
interface=StringVar()
comment=StringVar()
txt_name=Entry(v0,textvariable=name,width=30).place(x=160,y=50)

txt_ip=Entry(v0,textvariable=ipaddress,width=20).place(x=160,y=100)
txt_inter=Entry(v0,textvariable=interface,width=10).place(x=160,y=130)
txt_com=Entry(v0,textvariable=comment,width=20).place(x=160,y=160)



# Boton
btn_name=Button(v0,text="Consultar_name",bg="blue",fg="white",command=Query_name).place(x=850,y=40)
btn_save_name=Button(v0,text="Save",bg="red",command=save_name).place(x=430,y=50)
# IP ADDRESS







v0.mainloop()
