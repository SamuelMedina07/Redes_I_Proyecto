# Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from tkinter import messagebox

import os
import time
import subprocess

v0=Tk()
v0.title("Control de puertos firewall")
v0.geometry("800x400+0+0")

text_gral=font.Font(family="Helvetica",size=12)

def Addports():
               v1=Toplevel()
               v1.title("Agregar Puertos")
               v1.geometry("550x200+250+150")

               def clean():
                           ports.set('')

               def Save_ports():
                                p=str(ports.get())
                                enc="#!/bin/bash"
                                com1="sudo ufw allow"
                                tab=" "
                                cadena=(str(com1)+''+str(tab)+''+str(p))
                                os.system("sudo touch /home/cubillax/seguridad/addports.sh")
                                os.system("sudo chmod -R 777 /home/cubillax/seguridad/addports.sh")
                                pf=open("/home/cubillax/seguridad/addports.sh","w")
                                pf.write(enc)
                                pf.write("\n")
                                pf.write(cadena)
                                pf.write("\n")
                                pf.close()

                                time.sleep(0.1)

                                os.system("sudo /./home/cubillax/seguridad/addports.sh &")
                                messagebox.showinfo("info",message="Puerto Agregado con exito",parent=v1)
                                

               text_v1=font.Font(family="Helvetica",size=12)
               label_port=Label(v1,text="Ingrese Numero de Puerto :",font=text_v1).place(x=10,y=80)
               global ports
               ports=StringVar()
               txt_port=Entry(v1,textvariable=ports,width=20).place(x=260,y=80)

               btn_save=Button(v1,text="Save",bg="green",fg="white",command=Save_ports).place(x=430,y=80)
               

               v1.mainloop()

def listports():
               print("activando firewall")
               os.system("sudo /./home/cubillax/seguridad/listports.sh > listadoports.txt")
               valor=subprocess.check_output("cat /home/cubillax/seguridad/listadoports.txt",shell=True)
               area1=scrolledtext.ScrolledText(v0,width=80,height=10)
               area1.place(x=10,y=100)
               area1.insert(END,valor)

listports()

def deleteport():
                 op=radio.get()
                 if (op==1):
                               action="allow"
                               p=str(puertodel.get())
                               enc="#!/bin/bash"
                               com1="sudo ufw delete"
                               tab=" "
                               cadena=(str(com1)+''+str(tab)+''+str(action)+''+str(tab)+''+str(p))
                               print(cadena)
                               os.system("sudo touch /home/cubillax/seguridad/deleteport.sh")
                               os.system("sudo chmod -R 777 /home/cubillax/seguridad/deleteport.sh")
                               pf=open("/home/cubillax/seguridad/deleteport.sh","w")
                               pf.write(enc)
                               pf.write("\n")
                               pf.write(cadena)
                               pf.write("\n")
                               pf.close()

                               time.sleep(0.1)

                               os.system("sudo /./home/cubillax/seguridad/deleteport.sh &")
                               messagebox.showinfo("info",message="Puerto Eliminado con exito",parent=v0)

def Sitios_Web():
                 v2=Toplevel()
                 v2.title("Sitios Web")
                 v2.geometry("500x400+200+200")

                 def bloquear_sitio():
                                      st=str(sitioweb.get().strip())
                                      resultado=subprocess.run(["pkexec","/home/cubillax/seguridad/bloquear2_uth.sh",st],capture_output=True,text=True)
                                      messagebox.showinfo("INFO",message="Sittio Bloqueado con exito",parent=v2)

                 text_sitio=font.Font(family="Helvetica",size=12)
                 def clean_tiempo():
                                    horai.set('')
                                    minini.set('')
                                    horaf.set('')
                                    minf.set('')

                 def Tiempo_sitio_uth():
                                        def save_tiempo_uth():
                                                              print("---Temporizador---")
                                                              hi=str(horai.get())
                                                              mi=str(minini.get())
                                                              hf=str(horaf.get())
                                                              mf=str(minf.get())
                                                              dia="*"
                                                              mes="*"
                                                              ism="*"
                                                              user="root"
                                                              path1="/home/cubillax/seguridad/bloquear_uth.sh"
                                                              path2="/home/cubillax/seguridad/desbloquear_uth.sh"
                                                              tab=" "

                                                              cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                                                              cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))                                      

                                                              os.system("sudo chmod -R 777 /etc/cron.d/task_uth_enable")
                                                              os.system("sudo chmod -R 777 /etc/cron.d/task_uth_disable")

                                                              pf1=open("/etc/cron.d/task_uth_enable","w")
                                                              pf1.write(cadena1)
                                                              pf1.write("\n")
                                                              pf1.close()

                                                              pf1=open("/etc/cron.d/task_uth_disable","w")
                                                              pf1.write(cadena2)
                                                              pf1.write("\n")
                                                              pf1.close()

                                                              # pausa

                                                              time.sleep(0.1)
                                                              # revertir permisos de full a 755 segun lo necesita el usuario root
                                                              
                                                              os.system("sudo chmod -R 755 /etc/cron.d/task_uth_enable")
                                                              os.system("sudo chmod -R 755 /etc/cron.d/task_uth_disable")

                                                              # Reiniciar el servicio cron

                                                              os.system("sudo /etc/init.d/cron restart")
                                                              clean_tiempo()

                                                              messagebox.showinfo("INFO",message="Tiempo Programado con exito",parent=v2)           
                                                              
                     
                                        print("Temporizador...")
                                        label_sitio=Label(v2,text="URL Sitio Web :",font=text_sitio).place(x=80,y=100)
                                        label_horai=Label(v2,text="Hora Inicial:",font=text_sitio).place(x=80,y=250)
                                        label_minini=Label(v2,text="Minuto Inicial:",font=text_sitio).place(x=80,y=280)
                                        label_horaf=Label(v2,text="Hora Final:",font=text_sitio).place(x=80,y=310)
                                        label_minif=Label(v2,text="Minuto Final:",font=text_sitio).place(x=80,y=340)

                                        global horai,minini,horaf,minf
                                        horai=StringVar()
                                        minini=StringVar()
                                        horaf=StringVar()
                                        minf=StringVar()
                                        

                                        txt_horai=Entry(v2,textvariable=horai,width=20).place(x=200,y=250)
                                        txt_minini=Entry(v2,textvariable=minini,width=20).place(x=200,y=280)
                                        txt_horaf=Entry(v2,textvariable=horaf,width=20).place(x=200,y=310)
                                        txt_minf=Entry(v2,textvariable=minf,width=20).place(x=200,y=340)
                                        txt_sitioweb=Entry(v2,textvariable=sitioweb,width=50).place(x=200,y=80)

                                        btn_save_tiempo=Button(v2,text="Save",command=save_tiempo_uth).place(x=400,y=300)
                                        

                 def Blockear_Sitios_Web():
                                           print("Bloqueo y Desbloquep de Sitios Web")
                                           cks2=str(check_sitio2.get())
                                           cks3=str(check_sitio3.get())
                                           if (cks2=="1"):
                                                          print("Activo")
                                                          os.system("sudo /./home/cubillax/bloquear.sh &")
                                                          messagebox.showinfo("INFO",message="Sitio Bloqueado",parent=v2)
                                                          label_permitido=Label(v2,text="BLOQUEADO",bg="black",fg="red",font=text_sitio).place(x=220,y=140)
                                                                                         
                                           if (cks2=="0"):
                                                          print("DESACTIVO")
                                                          os.system("sudo /./home/cubillax/desbloquear.sh &")
                                                          messagebox.showinfo("INFO",message="Sitio Desbloqueado",parent=v2)
                                                          label_permitido=Label(v2,text="PERMITIDO",bg="black",fg="green",font=text_sitio).place(x=220,y=140)

                                           if (cks3=="1"):
                                                          print("Bloqueo uth")
                                                          os.system("sudo /./home/cubillax/seguridad/bloquear_uth.sh")
                                                          messagebox.showinfo("INFO",message="Sitio Bloqueado",parent=v2)
                                                          label_permitido=Label(v2,text="BLOQUEADO",bg="black",fg="red",font=text_sitio).place(x=220,y=180)
                                                          
                                           if (cks3=="0"):
                                                          os.system("sudo /./home/cubillax/seguridad/desbloquear_uth.sh")
                                                          messagebox.showinfo("INFO",message="Sitio Desbloqueado",parent=v2)

                                                          label_permitido=Label(v2,text="PERMITIDO",bg="black",fg="green",font=text_sitio).place(x=220,y=180)
                                                          
                 def Evaluar_checkbox():
                                        print("Evaluar tiempo....")

                 text_sitio=font.Font(family="Helvetica",size=12)
                 global check_sitio1,check_sitio2,check_sitio3,sitioweb,cktime
                 check_sitio1=StringVar()
                 check_sitio2=StringVar()
                 check_sitio3=StringVar()
                 cktime=StringVar()
                 sitioweb=StringVar()
                 ck1=ttk.Checkbutton(v2,text="www.facebook.com",variable=check_sitio1,command=Blockear_Sitios_Web)
                 ck1.place(x=50,y=100)
                 ck2=ttk.Checkbutton(v2,text="www.diez.hn",variable=check_sitio2,command=Blockear_Sitios_Web)
                 ck2.place(x=50,y=140)
                 ck3=ttk.Checkbutton(v2,text="www.uth.hn",variable=check_sitio3,command=Blockear_Sitios_Web)
                 ck3.place(x=50,y=180)
                 label_sitios=Label(v2,text="Digitar URL del Sitio web",font=text_sitio).place(x=10,y=20)
                 txt_sitios=Entry(v2,textvariable=sitioweb,width=35).place(x=10,y=50)
                 btn_tiempo=Button(v2,text="Tiempo",bg="brown",fg="white",command=Tiempo_sitio_uth).place(x=200,y=180)
                 btn_blk_sitio=Button(v2,text="Bloquear",bg="red",command=bloquear_sitio).place(x=340,y=50)
                 btn_ch1=ttk.Checkbutton(v2,text="tiempo",command=Evaluar_checkbox,variable=cktime)
                 btn_ch1.place(x=450,y=50)
                 

                 v2.mainloop()

def listas_ip_dominios():

                         def Cosultar_IP_dominios():
                                 print("Consultar....Ip...Dominios ...")
                                 s1=str(sitio1.get().strip())
                                 s2=str(sitio2.get().strip())
                                 resultado=subprocess.run(["sudo","/home/cubillax/seguridad/consultar_dominio.sh",s1,s2],capture_output=True,text=True)
                                 time.sleep(0.1)
                                 valor=subprocess.check_output("cat /home/cubillax/seguridad/listarip_dominio.txt",shell=True)
                                 area5=scrolledtext.ScrolledText(v0,width=80,height=10)
                                 area5.place(x=10,y=100)
                                 area5.insert(END,valor)

                                 
                             
                         text20=font.Font(family="Helvetica",size=13)
                         label_sitio1=Label(v0,text="Dominio 1:",font=text20).place(x=50,y=350)
                         label_sitio2=Label(v0,text="Dominio 2:",font=text20).place(x=350,y=350)
                                            
                         global sitio1,sitio2
                         sitio1=StringVar()
                         sitio2=StringVar()

                         txt_s1=Entry(v0,textvariable=sitio1,width=20).place(x=160,y=350)
                         txt_s2=Entry(v0,textvariable=sitio2,width=20).place(x=450,y=350)

                         btn_c5=Button(v0,text="Consultar",command=Cosultar_IP_dominios).place(x=630,y=350)
                         

                                
btn_list=Button(v0,text="List Port",command=listports).place(x=10,y=50)
btn_add=Button(v0,text="Add_ports",bg="green",fg="white",command=Addports).place(x=100,y=50)
btn_sitio=Button(v0,text="Sitios_Webs",bg="orange",fg="white",command=Sitios_Web).place(x=10,y=300)
btn_listarIP=Button(v0,text="Listar IP Publicas del Dominio",bg="orange",fg="white",command=listas_ip_dominios).place(x=200,y=300)
label_port=Label(v0,text="Puerto :", font=text_gral).place(x=300,y=50)
global puertodel
puertodel=StringVar()
txt_del=Entry(v0,textvariable=puertodel,width=10).place(x=380,y=50)
global radio
radio=IntVar()
r1=ttk.Radiobutton(v0,text="allow",variable=radio,value=1,command=deleteport).place(x=500,y=50)
r2=ttk.Radiobutton(v0,text="deny",variable=radio,value=2,command=deleteport).place(x=590,y=50)
label_t2=Label(v0,text="Eliminar",font=text_gral).place(x=550,y=20)
v0.mainloop()
