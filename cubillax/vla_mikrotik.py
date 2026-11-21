# Developer: VLA
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext
import os
import subprocess
import time

# crear ventana
v0=Tk()
v0.title("VLA SYSTEM ROUTER MIKROTIK")
v0.geometry("800x400+0+0")
# Zona de Funciones
def Router_Name():
                  print("Estableciendo Nombre al Router....")
                  # Variables
                  n=(str(name.get()))
                  # Constantes
                  enc="#!/bin/bash"
                  tab=" "
                  cs="'"
                  conexion='sshpass -p "1234567" ssh -l admin 10.200.1.50'
                  com1="system identity set name="

                  # Variable de tipo cadena de texto
                  cadena=(str(conexion)+''+str(tab)+''+str(cs)+''+str(com1)+''+str(n)+''+str(cs))
                  # creando el archivo vacio vlaroutername.sh
                  os.system("sudo touch /home/cubillax/vlaroutername.sh")
                  # asignar full permisos al archivo vlaroutername.sh
                  os.system("sudo chmod -R 777 /home/cubillax/vlaroutername.sh")

                  # Aperturar Archivo

                  pf=open("/home/cubillax/vlaroutername.sh","w")
                  pf.write(enc)
                  pf.write("\n")
                  pf.write(cadena)
                  pf.write("\n")
                  pf.close()

                  # Pausa Estrategica
                  time.sleep(0.1)
                  
                  # Ejecutar script creado desde python
                  os.system("sudo /./home/cubillax/vlaroutername.sh")

                  messagebox.showinfo("INFO",message="NOMBRE GUARDADO CON EXITO")

def Consulta_Name():
                    os.system("sudo /./home/cubillax/vlaconsulta1.sh > /home/cubillax/vlaconsulta.txt")
                    valor=subprocess.check_output("cat /home/cubillax/vlaconsulta.txt",shell=True)
                    areatxt=scrolledtext.ScrolledText(v0,width=80,height=10)
                    areatxt.place(x=10,y=160)
                    areatxt.insert(END,valor)

def Consulta_IP():
                  os.system("sudo /./home/cubillax/vla_consulta_ip.sh > /home/cubillax/vlaconsultaip.txt")
                  valor=subprocess.check_output("cat /home/cubillax/vlaconsultaip.txt",shell=True)
                  areatxt=scrolledtext.ScrolledText(v0,width=80,height=10)
                  areatxt.place(x=10,y=160)
                  areatxt.insert(END,valor)
    

def IP_ADDRESS():
                 print("Agregando IPs...")
                 v1=Toplevel()
                 v1.title("IP ADDRESS")
                 v1.geometry("600x300+0+0")
                 v1.config(bg="blue")

                 text_v1=font.Font(family="Arial",size=20)
                 text2_v1=font.Font(family="Arial",size=13)

                 def clean():
                             ipaddress.set('')
                             interface.set('')
                             comment.set('')

                 def save_ip():
                                enc="#!/bin/bash"
                                conexion='sshpass -p "1234567" ssh -l admin 10.200.1.50'
                                tab=" "
                                cs="'"
                                com1="ip address add address="
                                com2="interface="
                                com3="comm="
                                ip=str(ipaddress.get())
                                ether=str(interface.get())
                                c=str(comment.get())

                                cadena=(str(conexion)+''+str(tab)+''+str(cs)+''+str(com1)+''+str(ip)+''+str(tab)+''+str(com2)+''+str(ether)+''+str(tab)+''+str(com3)+''+str(c)+''+str(cs))

                                os.system("sudo touch /home/cubillax/vla_ipaddress2.sh")
                                os.system("sudo chmod -R 777 /home/cubillax/vla_ipaddress2.sh")

                                pf=open("/home/cubillax/vla_ipaddress2.sh","w")
                                pf.write(enc)
                                pf.write("\n")
                                pf.write(cadena)
                                pf.write("\n")
                                pf.close()

                                time.sleep(0.1)
                                os.system("sudo /./home/cubillax/vla_ipaddress2.sh")

                                messagebox.showinfo("INFO",message="IP ADDRESS creado con exito")

                                # llamar funcion para limpiar campos
                                clean()

                                
                                
                                

                 label_v1=Label(v1,text="IP-ADDRESS MIKROTIK",fg="white",bg="blue",font=text_v1).place(x=150,y=10)
                 label_ip=Label(v1,text="IP ADDRESS :",fg="white",bg="blue",font=text2_v1).place(x=20,y=80)
                 label_ether=Label(v1,text="INTERFACE :",fg="white",bg="blue",font=text2_v1).place(x=20,y=120)
                 label_comm=Label(v1,text="COMMENT :",fg="white",bg="blue",font=text2_v1).place(x=20,y=160)

                 global ipaddress,interface,comment
                 ipaddress=StringVar()
                 interface=StringVar()
                 comment=StringVar()

                 txt_ip=Entry(v1,textvariable=ipaddress,width=30).place(x=200,y=80)
                 txt_inter=Entry(v1,textvariable=interface,width=20).place(x=200,y=120)
                 txt_comm=Entry(v1,textvariable=comment,width=30).place(x=200,y=160)

                 btn_save=Button(v1,text="Save",bg="red",fg="white",command=save_ip).place(x=300,y=200)

                 v1.mainloop()
                 
                 

# tipos fuentes
text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=14)

# Zona de Etiquetas
label_t1=Label(v0,text="SCADA MIKROTIK SYSTEM",font=text1).place(x=150,y=10)
label_name=Label(v0,text="Router Name :",font=text2).place(x=20,y=80)

# Cajas de texto
global name
name=StringVar()
txt_name=Entry(v0,textvariable=name,width=30).place(x=150,y=80)

btn_save=Button(v0,text="Save",bg="black",fg="white",command=Router_Name).place(x=410,y=80)
btn_consulta=Button(v0,text="Consulta",bg="green",fg="white",command=Consulta_Name).place(x=20,y=120)
btn_consulaIP=Button(v0,text="Consulta_IP",bg="green",fg="white",command=Consulta_IP).place(x=150,y=120)
btn_ip=Button(v0,text="IP-ADDRESS",bg="blue",fg="white",command=IP_ADDRESS).place(x=20,y=350)


v0.mainloop()
