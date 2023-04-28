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
ventana_principal.config(bg="red")

frame_balnco=Frame(ventana_principal)
frame_balnco.config(bg="white",width=150, height=500)
frame_balnco.place(x=200,y=0)

frame_balnco=Frame(ventana_principal)
frame_balnco.config(bg="white",width=750, height=150)
frame_balnco.place(x=0,y=175)

frame_azul=Frame(ventana_principal)
frame_azul.config(bg="blue",width=100, height=500)
frame_azul.place(x=225,y=0)

frame_azul=Frame(ventana_principal)
frame_azul.config(bg="blue",width=750, height=100)
frame_azul.place(x=0,y=200)

ventana_principal.mainloop()