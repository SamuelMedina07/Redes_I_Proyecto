# Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from tkinter import messagebox
import subprocess
import os
import time

# Ventana
v0=Tk()
v0.title("Control y Gestion Router Mikrotik")
v0.geometry("900x500+200+100")

def clean_1():
            name.set('')
def Save():
        print("Salvado nombre de Router...")
        n=str(name.get())
        enc="#!/bin/bash"
        cs="'"
        tab=" "
        conexion='sshpass -p "1234567" ssh -l admin 192.168.88.200'
        comando="system identity set name="
        cadena=(str(conexion)+''+str(tab)+''+str(cs)+''+str(comando)+''+str(n)+''+str(cs))
        print (cadena)
        os.system("sudo touch /home/cubillax/routername.sh")
        os.system("sudo chmod -R 777 /home/cubillax/routername.sh")
        pf=open("/home/cubillax/routername.sh","w")
        pf.write(enc)
        pf.write("\n")
        pf.write(cadena)
        pf.write("\n")
        pf.close()

        time.sleep(0.1)
        os.system("sudo /./home/cubillax/routername.sh &")
        clean_1()
        messagebox.showinfo("INFO",message="Nombre Guardado con Exito")
                
def consulta_name():
                    os.system('sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 "system identity print" | head -n1 | cut -d " " -f4 > routername2.txt')
                    valor=subprocess.check_output("cat /home/cubillax/routername2.txt",shell=True)
                    area=scrolledtext.ScrolledText(v0,width=60,height=10,font=("Arial",11),fg="blue")
                    area.place(x=10,y=170)
                    area.insert(END,valor)
def consulta_ips():
                    os.system('sudo sshpass -p "1234567" ssh -l admin 192.168.88.200 "ip address print" > ipaddress.txt')
                    valor_ip=subprocess.check_output("cat /home/cubillax/ipaddress.txt",shell=True)
                    area=scrolledtext.ScrolledText(v0,width=60,height=10,font=("Arial",11),fg="green")
                    area.place(x=10,y=170)
                    area.insert(END,valor_ip)

# llamar funcion al load
#consulta_ips()

def consulta_dhcp_server():
                            os.system("sudo /./home/cubillax/c_dhcp_server.sh > c_dhcp_server.txt")
                            valor=subprocess.check_output("cat /home/cubillax/c_dhcp_server.txt",shell=True)
                            area=scrolledtext.ScrolledText(v0,width=60,height=10,fg="green")
                            area.place(x=10,y=170)
                            area.insert(END,valor)
    

def dhcp_network():
                    os.system("sudo /./home/cubillax/c_dhcp_server_net.sh > c_dhcp_server_net.txt")
                    valor=subprocess.check_output("cat /home/cubillax/c_dhcp_server_net.txt",shell=True)
                    area=scrolledtext.ScrolledText(v0,width=60,height=10,fg="green")
                    area.place(x=10,y=170)
                    area.insert(END,valor)

def Listar_BK():
                os.system("sudo /./home/cubillax/listar_bk.sh > listar_bk.txt")
                valor=subprocess.check_output("cat /home/cubillax/listar_bk.txt",shell=True)
                area=scrolledtext.ScrolledText(v0,width=80,height=10)
                area.place(x=10,y=170)
                area.insert(END,valor)


def Create_Backup():
                    os.system("sudo /./home/cubillax/mikrotik_respaldo.sh &")
                    messagebox.showinfo("INFO",message="Respaldo Creado")
                    

def clean_2():
           ipaddress.set('')
           interface.set('')
           comment.set('')

def AddingIP():
             

               def save_ip():
                             print("Saving Tcp 2....")
                             ip=str(ipaddress.get())
                             i=str(interface.get())
                             c=str(comment.get())
                             enc="#!/bin/bash"
                             conexion='sudo sshpass -p "1234567" ssh -l admin 192.168.88.200'
                             tab=" "
                             cs="'"
                             comm1="ip address add address="
                             comm2="interface="
                             comm3="comment="

                             cadena=(str(conexion)+''+str(tab)+''+str(cs)+''+str(comm1)+''+str(ip)+''+str(tab)+''+str(comm2)+''+str(i)+''+str(tab)+''+str(comm3)+''+str(c)+''+str(cs))
                             print(cadena)

                             os.system("sudo touch /home/cubillax/addip.sh")
                             os.system("sudo chmod -R 777 /home/cubillax/addip.sh")
                             pf=open("/home/cubillax/addip.sh","w")
                             pf.write(enc)
                             pf.write("\n")
                             pf.write(cadena)
                             pf.write("\n")
                             pf.close()

                             time.sleep(0.1)
                             os.system("sudo /./home/cubillax/addip.sh &")
                             clean_2()
                             messagebox.showinfo("INFO",message="Ip Registrado",parent=v1)                           

               v1.config(bg="blue")
               text1=font.Font(family="Arial",size=12)
               text2=font.Font(family="Arial",size=18)
               label_t=Label(v1,text="Protocolo TCP/IP",font=text2,fg="white",bg="blue").place(x=100,y=10)    
               label_ip=Label(v1,text="IP ADDRESS:",font=text1,fg="white",bg="blue").place(x=50,y=50)
               label_ethe=Label(v1,text="INTERFACE",font=text1,fg="white",bg="blue").place(x=50,y=100)
               label_comm=Label(v1,text="COMMENT:",font=text1,fg="white",bg="blue").place(x=50,y=150)

               global ipaddress,comment,interface
               ipaddress=StringVar()
               interface=StringVar()
               comment=StringVar()

               txt_ip=Entry(v1,textvariable=ipaddress,width=15).place(x=150,y=50)
               txt_ether=Entry(v1,textvariable=interface,width=20).place(x=150,y=100)
               txt_comm=Entry(v1,textvariable=comment,width=20).place(x=150,y=150)

               btn_save=Button(v1,text="Save",bg="red",fg="White",command=save_ip).place(x=400,y=40)
                               
            

               v1.mainloop()

def dhcp_server():
                  v3=Toplevel()
                  v3.title("DHCP-SETTINGS")
                  v3.geometry("700x400+200+150")

                  def dhcp_save():
                                  print("Aplicar Dhcp_server...")
                                  # ---- Variables ------------
                                  #poolname,poolrange,dhcpnetwork,dhcpgateway,dhcpdns,dhcpname,dhcpether
                                  pn=str(poolname.get())
                                  pr=str(poolrange.get())
                                  d_net=str(dhcpnetwork.get())
                                  dg=str(dhcpgateway.get())
                                  d_dns=str(dhcpdns.get())
                                  d_name=str(dhcpname.get())
                                  de=str(dhcpether.get())
                                            
                                  # ----------- variables constantes -----------------"
                                  enc="#!/bin/bash"
                                  conexion='sudo sshpass -p "1234567" ssh -l admin 192.168.88.200'
                                  tab=" "
                                  cs="'"
                                  linea1_c1="ip pool add name="
                                  linea1_c2="ranges="
                                  linea2_c1="ip dhcp-server network add address="
                                  linea2_c2="gateway="
                                  linea2_c3="dns-server="
                                  linea3_c1="ip dhcp-server add name="
                                  linea3_c2="interface="
                                  linea3_c3="address="
                                  linea3_c4="lease_time=1d"
                                  linea3_c5="disabled=no"

                                  # Crear cadenas
                                  cadena1=(str(conexion)+''+str(tab)+''+str(cs)+''+str(linea1_c1)+''+str(pn)+''+str(tab)+''+str(linea1_c2)+''+str(pr)+''+str(cs))
                                  cadena2=(str(conexion)+''+str(tab)+''+str(cs)+''+str(linea2_c1)+''+str(d_net)+''+str(tab)+''+str(linea2_c2)+''+str(dg)+''+str(tab)+''+str(linea2_c3)+''+str(d_dns)+''+str(cs))                 
                                  cadena3=(str(conexion)+''+str(tab)+''+str(cs)+''+str(linea3_c1)+''+str(d_name)+''+str(tab)+''+str(linea3_c2)+''+str(de)+''+str(tab)+''+str(linea3_c3)+''+str(pn)+''+str(tab)+''+str(linea3_c4)+''+str(tab)+''+str(linea3_c5)+''+str(cs))                                                       

                                  # Crear,permisos y lectura
                                  os.system("sudo touch /home/cubillax/dhcp2.sh")
                                  os.system("sudo chmod -R 777 /home/cubillax/dhcp2.sh")
                                  pf=open("/home/cubillax/dhcp2.sh","w")
                                  pf.write(enc)
                                  pf.write("\n")
                                  pf.write(cadena1)
                                  pf.write("\n")
                                  pf.write(cadena2)
                                  pf.write("\n")
                                  pf.write(cadena3)
                                  pf.write("\n")
                                  pf.close()

                                  time.sleep(0.1)

                                  #ejecutar
                                  os.system("sudo /./home/cubillax/dhcp2.sh")
                                  messagebox.showinfo("INFO",message="Script dhcp ejecutado con exito")
                                            

                  # Captura de Datos
                  # variables globales
                  global poolname,poolrange,dhcpnetwork,dhcpgateway,dhcpdns,dhcpname,dhcpether
                  poolname=StringVar()
                  poolrange=StringVar()
                  dhcpnetwork=StringVar()
                  dhcpgateway=StringVar()
                  dhcpdns=StringVar()
                  dhcpname=StringVar()
                  dhcpether=StringVar()

                  txt_1=font.Font(family="Arial",size=12)

                  label_poolname=Label(v3,text="POOL NAME:",font=txt_1).place(x=5,y=100)
                  label_poolrange=Label(v3,text="POOL RANGE:",font=txt_1).place(x=5,y=140)
                  label_dhcpnetwork=Label(v3,text="DHCP NETWORK:",font=txt_1).place(x=5,y=180)
                  label_dhcpgateway=Label(v3,text="DHCP GATEWAY:",font=txt_1).place(x=5,y=220)
                  label_dhcpdns=Label(v3,text="DHCP DNS:",font=txt_1).place(x=5,y=260)
                  label_dhcpname=Label(v3,text="DHCP NAME:",font=txt_1).place(x=5,y=300)
                  label_dhcpether=Label(v3,text="DHCP ETHER:",font=txt_1).place(x=5,y=340)

                  
                  txt_poolname=Entry(v3,textvariable=poolname,width=30).place(x=180,y=100)
                  txt_poolrange=Entry(v3,textvariable=poolrange,width=30).place(x=180,y=140)
                  txt_dhcpnetwork=Entry(v3,textvariable=dhcpnetwork,width=30).place(x=180,y=180)
                  txt_dhcpgateway=Entry(v3,textvariable=dhcpgateway,width=20).place(x=180,y=220)
                  txt_dhcpdns=Entry(v3,textvariable=dhcpdns,width=20).place(x=180,y=260)
                  txt_dhcpname=Entry(v3,textvariable=dhcpname,width=20).place(x=180,y=300)
                  txt_dhcpether=Entry(v3,textvariable=dhcpether,width=10).place(x=180,y=340)

                  btn_save=Button(v3,text="SAVE",bg="red",fg="white",command=dhcp_save).place(x=150,y=370)
   
                  v3.mainloop()

def bloquear_dominios():

                         v1=Toplevel()
                         
                         v1.title("Bloquear Sitios Web")
                         v1.geometry("600x400+350+150")

                         def Evaluar_Checkbox():
                                                print("Bloaquear sitio1....")



                         # Checkbox
                         global chksitio1,chksitio2,chksitio3
                         chksitio1=StringVar()
                         chksitio2=StringVar()
                         chksitio3=StringVar()
                         ck1=ttk.Checkbutton (v1,text="www.unah.edu.hn",variable=chksitio1,command=Evaluar_Checkbox)
                         ck1.place(x=100,y=50)
                                        


                         v1.mainloop()

               
text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=13)

label_t=Label(v0,text="MIROTIK ROUTER",font=text1).place(x=50,y=10)
label_name=Label(v0,text="Ingrese Nombre:",font=text2).place(x=50,y=80)
label_opc=Label(v0,text="Network Settings",font=text1).place(x=10,y=355)
global name
name=StringVar()

txt_name=Entry(v0,textvariable=name,width=50).place(x=50,y=100)
btn_save=Button(v0,text="Save",bg="red",command=Save).place(x=50,y=130)
# ----------------------------- Query-----------------------------------------------
btn_cname=Button(v0,text="Routername",bg="cyan",command=consulta_name).place(x=200,y=50)
btn_ip=Button(v0,text="IP-Address",bg="cyan",command=consulta_ips).place(x=310,y=50)
btn_dhcp1=Button(v0,text="DHCP-SERVER",bg="cyan",command=consulta_dhcp_server).place(x=410,y=50)
btn_dhcp_net=Button(v0,text="DHCP-NETWORK",bg="cyan",command=dhcp_network).place(x=540,y=50)
btn_list=Button(v0,text="LISTAR_BK",bg="cyan",command=Listar_BK).place(x=680,y=50)
btn_bk=Button(v0,text="Make_Backup",bg="Black",fg="white",command=Create_Backup).place(x=10,y=50)
#----------------------------------------- Create --------------------------------------
btn_IPS=Button(v0,text="IP-ADDRESS",bg="blue",fg="white",command=AddingIP).place(x=10,y=390)
btn_dhcp=Button(v0,text="DHCP-SERVER",bg="blue",fg="white",command=dhcp_server).place(x=110,y=390)
btn_bloquear=Button(v0,text="BLOQUEAR-SITIOS",bg="blue",fg="white",command=bloquear_dominios).place(x=240,y=390)



v0.mainloop()








