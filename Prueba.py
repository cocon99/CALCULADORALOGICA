import tkinter as tk
import cv2
import numpy as np

comandos = []

def DibujarRespuesta(comandosActual):
    print(f"empezar operacion {comandosActual}")
    VentanaRespuesta=tk.Toplevel()
    VentanaRespuesta.geometry("400x400")
    VentanaRespuesta.configure(background="#437F97")
    Entradas = ""
    Entradas = []
    for comandoTemporal in comandosActual:
        SeEncuentra = False
        try:
            if(Entradas.index(comandoTemporal) >= 0 ):
                SeEncuentra = True
        except:
            print("No es lista")
        if(not SeEncuentra):
            if(comandoTemporal == 'P' or comandoTemporal == 'Q' or comandoTemporal == 'R' or comandoTemporal == 'S'):
                Entradas.append(comandoTemporal)
    print(f"Las estrados son: {Entradas}")
    for x in range(len(comandos)):
        CuadroTemporal = tk.Label(VentanaRespuesta)
        CuadroTemporal["text"] = comandos[x]
        CuadroTemporal["width"] = 10
        CuadroTemporal["height"] = 1
        CuadroTemporal.grid(row=0, column=x)

    for y in range(2 ** len(Entradas)):
        EntradaTable = []
        Y_Temporal = y
        for x in range(len(Entradas)):
            EntradaTable.append(Y_Temporal % 2)
            Y_Temporal = Y_Temporal // 2
            CuadroTemporal = tk.Label(VentanaRespuesta)
            CuadroTemporal["text"] = EntradaTable[x]
            CuadroTemporal["width"] = 10
            CuadroTemporal["height"] = 1
            CuadroTemporal.grid(row=y+1, column=x)


def ActualizarDisplay(Boton):
    global comandos
    print(f"comando es {Boton}")
    if(Boton == 'AC'):
        comandos = []
        print("Limpiando comandos ")
    elif(Boton == 'DEL'):
        if(len(comandos) > 0):
            comandos.pop()
            print("Elimiando ultimo")
        else:
            print("No hay que eliminar")
    elif(Boton == '='):
        if(len(comandos) > 0):
            print("Monstando respuesta")
            DibujarRespuesta(comandos)
    else:
        comandos.append(Boton)
        print(f"Imprimiendo comandos: {comandos}")
    CajaTexto.set(comandos)


# Dibujar
def DibujarBoton(pantalla, nombre, _x, _y):
    TeclaFor = tk.Button(pantalla)
    TeclaFor["height"] = 2
    if(nombre == "=" or nombre == "IZQUIERDA" or nombre == "DERECHA"):
        TeclaFor["width"] = 17
    else:
        TeclaFor["width"] = 7
    TeclaFor["text"] = nombre
    TeclaFor["bg"] = ("#242F40")
    TeclaFor["fg"] = ("#F6E8EA")
    TeclaFor.place(x=_x, y=_y)
    TeclaFor['command'] = lambda:ActualizarDisplay(nombre)

# Principal
if __name__ == "__main__":
    global CajaTexto
    print("Codigo principal")

    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("290x320")
    ventana.configure(background="#437F97")

    CajaTexto = tk.StringVar()
    entrada = tk.Entry(ventana, textvariable= CajaTexto, bg="#F6E8EA", fg="#242F40")
    entrada.pack(fill=tk.X,padx=10, pady=15, ipadx=5, ipady=4)

    tecla = ['AC', 'DEL', '=', 'P', 'Q','R','S','~','v','^','->','<->','+','(',')','IZQUIERDA','DERECHA',]
    X_tecla = [10,80,150,10,80,150,220,10,80,150,220,10,80,150,220,10,150]
    Y_tecla = [50,50,50,100,100,100,100,150,150,150,150,200,200,200,200,250,250]

    for TeclaActual in range(len(tecla)):
        DibujarBoton(ventana,tecla[TeclaActual], X_tecla[TeclaActual], Y_tecla[TeclaActual])

    ventana.mainloop()

# simple 2d table

# from tkinter import *
#
# for i in range(5):
#        for j in range(4):
#            l = Label(text='%d.%d' % (i, j), relief=RIDGE)
#            l.grid(row=i, column=j, sticky=NSEW)
#
# mainloop()
