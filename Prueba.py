import tkinter as tk
import cv2
import numpy as np

comandos = []

def ActualizarDisplay(Boton):
    global comandos
    print(f"comando es {Boton}")
    if(Boton == 'AC'):
        comandos = []
    elif(Boton == 'DEL'):
        if(len(comandos) > 0):
            comandos.pop()
    else:
        comandos.append(Boton)
    print(comandos)
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
