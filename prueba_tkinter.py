#Se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#------------------------------------
# funciones de la app
#------------------------------------

#------------------------------------
# Ventana principal
#------------------------------------
#Se declara una variable llamada venta_principal, que adquiere las 
#carateristica de un objeto TK()
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------------
# Frame entrada datos
#------------------------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="yellow",width=500, height=250)
frame_entrada.place(x=0,y=0)

#----------------------------------
#frame operaciones
#----------------------------------
frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue",width=500, height=125)
frame_operaciones.place(x=0,y=250)

#----------------------------------
#frame resultados
#----------------------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="red",width=500, height=125)
frame_resultados.place(x=0,y=375)
#Run
#Se ejecuta la función (metodo) mainloop() de la clase Tk a través de la instancia 
#venta_principal. Este método despliega una ventana simple en la pantalla y queda 
#a la espera de lo que el usuario haga. cada acción del usuario se conoce como evento
# el método mainloop es un bucle "infinito" 
ventana_principal.mainloop()