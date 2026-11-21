# Developer: VLA
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import scrolledtext
import os
import subprocess
import time
import shlex

# Crear ventana
v0=Tk()
v0.title("FIREWALL LINUX UFW")
v0.geometry("900x500+0+0")

# Zona de Funciones o metodos

def consultar_IPS():
                    st1=str(sitio1.get().strip())
                    st2=str(sitio2.get().strip())
                    os.system("sudo touch /home/cubillax/vla_consultaip.txt")
                    os.system("sudo chmod -R 777 /home/cubillax/vla_consultaip.txt")
                    resultado=subprocess.run(["sudo","/home/cubillax/vla_consultaip.sh",st1,st2],capture_output=True,text=True)

                    time.sleep(0.1)
                    
                    valor=subprocess.check_output("cat /home/cubillax/vla_consultaip.txt",shell=True)
                    area=scrolledtext.ScrolledText(v0,width=90,height=10)
                    area.place(x=20,y=170)
                    area.insert(END,valor)

def Bloquear():
               print("Dominio Bloqueado")
               d1=str(sitio1.get().strip())
               resultado=subprocess.run(["sudo","/home/cubillax/bloquear_dominio.sh",d1],capture_output=True,text=True)
               messagebox.showinfo("INFO",message="Dominio Bloqueado",parent=v0)

def Desbloquear():
                  print("Dominio Desbloqueado")
                  d1=str(sitio1.get().strip())
                  resultado=subprocess.run(["sudo","/home/cubillax/desbloquear_dominio.sh",d1],capture_output=True,text=True)
                  messagebox.showinfo("INFO",message="Dominio Desbloqueado",parent=v0)


def IPs_bloqueadas():
                       os.system("sudo ufw status > /home/cubillax/lista_bloqueados.txt")
                       valor=subprocess.check_output("cat /home/cubillax/lista_bloqueados.txt",shell=True)
                       area=scrolledtext.ScrolledText(v0,width=90,height=10)
                       area.place(x=20,y=170)
                       area.insert(END,valor)

def Evaluar_Tiempo_bloqueo():
                             v1=Toplevel()
                             v1.title("Control de Bloqueo por Tiempo")
                             v1.geometry("350x150+300+250")

                             def Save_tiempo():
                                               print("Tiempo de Bloqueo")
                                               dom1=str(dominio1.get())
                                               archivo="/home/cubillax/bloquear_dominio.sh"
                                               with open(archivo,"r") as f:
                                                    lineas=f.readlines()

                                               for i,linea in enumerate(lineas):     
                                                   if linea.strip()=='SITIO="$1"':
                                                       lineas[i]="SITIO=" + shlex.quote(dom1)+"\n"
                                                       break
                                               with open(archivo,"w") as f:
                                                    f.writelines(lineas)

                                               time.sleep(0.1)     
                                               #resultado=subprocess.run(["sudo","/home/cubillax/bloquear_dominio.sh",dom1],capture_output=True,text=True)
                                               hi=str(horai.get())
                                               mi=str(minini.get())
                                               tab=" "
                                               dia="*"
                                               mes="*"
                                               its="*"
                                               user="root"
                                               path1="/home/cubillax/bloquear_dominio.sh"

                                               
                                               cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(its)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                                               os.system("sudo chmod -R 777 /etc/cron.d/tiempo_bloqueo")
                                                
                                               pf=open("/etc/cron.d/tiempo_bloqueo","w")
                                               pf.write(cadena1)
                                               pf.write("\n")
                                               pf.close()

                                               time.sleep(0.1)
                                               os.system("sudo chmod -R 755 /etc/cron.d/tiempo_bloqueo")

                                               os.system("sudo /etc/init.d/cron restart")

                                               messagebox.showinfo("INFO",message="TIEMPO PROGRAMADO CON EXITO")
                                               
                                               
                            
                             
                             textv1=font.Font(family="Arial",size=13)
                             labeldom=Label(v1,text="Dominio :",font=textv1).place(x=20,y=5)
                             labelhi=Label(v1,text="Hora Inicial:",font=textv1).place(x=20,y=30)
                             labelmi=Label(v1,text="Minuto Inicial:",font=textv1).place(x=20,y=70)

                             global horai,minini,dominio1
                             horai=StringVar()
                             minini=StringVar()
                             dominio1=StringVar()

                             txt_dom=Entry(v1,textvariable=dominio1,width=20).place(x=140,y=5)
                             txt_horai=Entry(v1,textvariable=horai,width=10).place(x=140,y=30)
                             txt_minini=Entry(v1,textvariable=minini,width=10).place(x=140,y=70)

                             btn_save=Button(v1,text="Save",bg="red",fg="white",command=Save_tiempo).place(x=100,y=100)
                                                                                
                             
                             v1.mainloop()
# Definir tipos de fuente
text1=font.Font(family="Arial",size=22)
text2=font.Font(family="Helvetica",size=13)

# Zona de Etiquetas
label_t1=Label(v0,text="FIREWALL VLA",font=text1).place(x=350,y=10)

# consultas
label_sitio1=Label(v0,text="Dominio 1:",font=text2).place(x=20,y=80)
label_sitio2=Label(v0,text="Dominio 2:",font=text2).place(x=20,y=120)


# cajas de texto
global sitio1,sitio2
sitio1=StringVar()
sitio2=StringVar()

txt_sitio1=Entry(v0,textvariable=sitio1,width=25).place(x=150,y=80)
txt_sitio2=Entry(v0,textvariable=sitio2,width=25).place(x=150,y=120)


# botones
btn_consultaIP=Button(v0,text="Consultar IPs",bg="cyan",command=consultar_IPS).place(x=400,y=100)
btn_bloqueo=Button(v0,text="Bloquear",bg="cyan",command=Bloquear).place(x=530,y=100)
btn_desbloqueo=Button(v0,text="Desbloquear",bg="cyan",command=Desbloquear).place(x=640,y=100)
btn_listabl=Button(v0,text="IPs_Bloqueadas",bg="cyan",command=IPs_bloqueadas).place(x=400,y=60)

# Checkbox tiempo bloqueo
global check_bloqueo_t1
check_bloqueo_t1=StringVar()
ck1=ttk.Checkbutton(v0,text="Tiempo_Bloqueo",variable=check_bloqueo_t1,command=Evaluar_Tiempo_bloqueo)
ck1.place(x=530,y=130)




v0.mainloop()
