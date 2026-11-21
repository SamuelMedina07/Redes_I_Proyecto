# Developer: UNIVERSIDAD
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import scrolledtext
import os

# crear Ventana Principal

v0=Tk()
v0.title("Control de Router Mikrotik")
v0.geometry("700x400+200+200")

# zona de f.unciones
def salvar():
             print("Saving Router Name....")
             
text1=font.Font(family="Ari-al",size=18)
text2=font.Font(family="Arial",size=13)
label_t=Label(v0,text="CONTROL SCADA TIPO MIKROTIK",font=text1).place(x=50,y=10)
labe_name=Label(v0,text="Ingrese Nombre",font=text2).place(x=20,y=100)

global name
name=StringVar()
txt_name=Entry(v0,textvariable=name,width=50).place(x=180,y=100)

btn_save=Button(v0,text="SAVE",command=salvar).place(x=600,y=100)




v0.mainloop()
