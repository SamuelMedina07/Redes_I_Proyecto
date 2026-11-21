# Developer: Universidad
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
import cv2
import numpy as np


# Crear ventana
v0=Tk()
v0.title("Control de Estado GPIO")
v0.geometry("700x600+590+200")

img_t=PhotoImage(file="triangulof.png")
img_c=PhotoImage(file="cuadradof.png")
img_r=PhotoImage(file="circulof.png")

text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Helvetica",size=14)
text3=font.Font(family="Arial",size=100)
text5=font.Font(family="Arial",size=65)
# Zona de Funciones
def encender():
               print("Encendido")
               os.system("sudo /./home/cubillax/on.sh")
          
def apagar():
             print("Apagado")
             os.system("sudo /./home/cubillax/off.sh")

def actualizar():
                  pf=open("/home/cubillax/estado.txt","r")
                  for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text3).place(x=250,y=40)
                                                   v0.after(1000,actualizar)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text3).place(x=250,y=40)
                                                   v0.after(1000,actualizar)

# llamar funcion
actualizar()

def triangulo():
                pf=open("/home/cubillax/triangulo.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=100,y=350)
                                                   v0.after(1000,triangulo)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=100,y=350)
                                                   v0.after(1000,triangulo)
    
triangulo()

def cuadrado():
                pf=open("/home/cubillax/cuadrado.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=300,y=350)
                                                   v0.after(1000,cuadrado)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=300,y=350)
                                                   v0.after(1000,cuadrado)
    
cuadrado()

def circulo():
                pf=open("/home/cubillax/circulo.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=500,y=350)
                                                   v0.after(1000,circulo)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=500,y=350)
                                                   v0.after(1000,circulo)
    
circulo()

# --------------------------- Funciones Recursivas para la deteccion de colores ------------------------------
def red():
                pf=open("/home/cubillax/red.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=100,y=500)
                                                   v0.after(1000,red)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=100,y=500)
                                                   v0.after(1000,red)

red()

def green():
                pf=open("/home/cubillax/green.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=300,y=500)
                                                   v0.after(1000,green)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=300,y=500)
                                                   v0.after(1000,green)

green()

def yellow():
                pf=open("/home/cubillax/yellow.txt","r")
                for linea in pf:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   label_on=Label(v0,text="1",font=text5).place(x=500,y=500)
                                                   v0.after(1000,yellow)

                                  if (campof=="0"):
                                                   label_off=Label(v0,text="0",font=text5).place(x=500,y=500)
                                                   v0.after(1000,yellow)
yellow()

# zona de Etiquetas
label_t=Label(v0,text="CONTROL GPIO MICROPROCESADOR IA",font=text1).place(x=10,y=5)

btn_on=Button(v0,text="ON",command=encender).place(x=100,y=100)
btn_off=Button(v0,text="OFF",command=apagar).place(x=100,y=150)

# Figuras Geometricas
btn_t=Button(v0,image=img_t).place(x=100,y=250)
btn_c=Button(v0,image=img_c).place(x=300,y=250)
btn_r=Button(v0,image=img_r).place(x=500,y=250)


# ------------------Camara y Opencv ----------------------
cap = None

def abrir_camara():
    global cap

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la camara")
        return

    def procesar():
        global cap

        ret, frame = cap.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7,7), 1)
        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        figura_detectada = None
        max_area = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 4000 and area > max_area:
                max_area = area

                approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
                lados = len(approx)

                if lados == 3:
                    figura_detectada = "triangulo"
                elif lados == 4:
                    figura_detectada = "cuadrado"
                else:
                    figura_detectada = "circulo"

        if figura_detectada == "triangulo":
            os.system("sudo /./home/cubillax/triangulo.sh &")
            os.system("sudo /./home/cubillax/triangulo_sonido.sh &")

        elif figura_detectada == "cuadrado":
            os.system("sudo /./home/cubillax/cuadrado.sh &")
            os.system("sudo /./home/cubillax/cuadrado_sonido.sh &")
            

        elif figura_detectada == "circulo":
            os.system("sudo /./home/cubillax/circulo.sh &")

        cv2.imshow("Camara - Deteccion Figuras", frame)

        cv2.waitKey(1)   

        v0.after(30, procesar)

    procesar()

def close_camara():
                   os.system("sudo /./home/cubillax/closecamara.sh")


# ------------------Camara y Opencv Colores----------------------
#cap = None
ultimo_color = None

def abrir_camara_colores():
    global cap
    global ultimo_color
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la camara")
        return

    def procesar():
        global cap
        global ultimo_color
        ret, frame = cap.read()
        if not ret:
            return

        # Convertir a HSV para detectar colores
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Rangos de colores

        # ROJO (tiene dos rangos en HSV)
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        # VERDE
        lower_green = np.array([40, 70, 70])
        upper_green = np.array([80, 255, 255])

        # AMARILLO
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        # Crear máscaras
        mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask_red = mask_red1 + mask_red2

        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Contar pixeles detectados
        red_pixels = cv2.countNonZero(mask_red)
        green_pixels = cv2.countNonZero(mask_green)
        yellow_pixels = cv2.countNonZero(mask_yellow)

        color_detectado = None

        if red_pixels > 5000:
            color_detectado = "rojo"

        elif green_pixels > 800:
            color_detectado = "verde"

        elif yellow_pixels > 800:
            color_detectado = "amarillo"

      # Ejecutar scripts según color


        if color_detectado != ultimo_color:

           # Ejecutar scripts según color
           if color_detectado == "rojo":
              os.system("sudo /./home/cubillax/red.sh &")

           elif color_detectado == "verde":
                os.system("sudo /./home/cubillax/green.sh &")

           elif color_detectado == "amarillo":
                os.system("sudo /./home/cubillax/yellow.sh &")

           ultimo_color = color_detectado     

        cv2.imshow("Camara - Deteccion Color", frame)

        cv2.waitKey(1)

        v0.after(80, procesar)

    procesar()

def setred():
              os.system("sudo /./home/cubillax/setred.sh &")

btn_cam = Button(v0, text="ABRIR CAMARA", bg="white",command=abrir_camara)
btn_cam.place(x=100, y=200)
btn_cam2=Button(v0,text="CERRAR CAMARA", bg="white", command=close_camara).place(x=230,y=200)
btn_camcolor=Button(v0,text="ABRIR CAMARA_COLORES",bg="white",command=abrir_camara_colores).place(x=380,y=200)

# Botones Colores
btn_red=Button(v0,text="ROJO",bg="red").place(x=100,y=460)
btn_red=Button(v0,text="VERDE",bg="green").place(x=300,y=460)
btn_red=Button(v0,text="AMARILLO",bg="yellow").place(x=500,y=460)
btn_setred=Button(v0,text="SETRED",bg="white",command=setred).place(x=590,y=200)





v0.mainloop()
