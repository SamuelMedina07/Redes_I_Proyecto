# Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
import os
import subprocess

# crear una Ventana
v0=Tk()
v0.title("Control SCADA Router MiKrotik")
v0.geometry("760x400+200+200")
def salvar():
             print("registrando en MK...")

text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=14)

label_1=Label(v0,text="SCADA MIKROTIK ROUTER",font=text1).place(x=100,y=10)
label_1=Label(v0,text="Ingrese Nombre del Router",font=text2).place(x=50,y=100)

global name
name=StringVar()
txt_name=Entry(v0,textvariable=name,width=50).place(x=310,y=100)


btn_button=Button(v0,text="save", command=salvar).place(x=100,y=200)
v0.mainloop()
