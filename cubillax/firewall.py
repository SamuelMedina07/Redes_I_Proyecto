# Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
import os
import time
import subprocess

v0=Tk()
v0.title("Control de puertos firewall")
v0.geometry("700x400+0+0")

def listports():
               print("activando firewall")
               os.system("sudo /./home/cubilalx/listport.sh > listadoports.txt")
               valor=subprocess.check_output




btn_list=Button(v0,text="List Port",command=listports).place(x=10,y=50)





v0.mainloop()
