#Se importa la libreria tkinter con todas sus funciones 
from tkinter import *


ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("750x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana
ventana_principal.config(bg="blue")



frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red",width=200, height=175)
frame_entrada.place(x=0,y=0)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red",width=200, height=175)
frame_entrada.place(x=0,y=325)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red",width=400, height=175)
frame_entrada.place(x=350,y=0)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red",width=400, height=175)
frame_entrada.place(x=350,y=325)



frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white",width=37.5, height=212.5)
frame_entrada.place(x=200,y=0)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white",width=37.5, height=212.5)
frame_entrada.place(x=200,y=287.5)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white",width=37.5, height=212.5)
frame_entrada.place(x=312.5,y=0)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white",width=37.5, height=212.5)
frame_entrada.place(x=312.5,y=287.5)

frame_entrada2=Frame(ventana_principal)
frame_entrada2.config(bg="white",width=212.5, height=37.5)
frame_entrada2.place(x=0,y=325)

frame_entrada1=Frame(ventana_principal)
frame_entrada1.config(bg="white",width=212.5, height=37.5)
frame_entrada1.place(x=0,y=287.5)

ventana_principal.mainloop()