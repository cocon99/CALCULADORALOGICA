import tkinter as tk
import cv2
import numpy as np

# Principal
if __name__ == "__main__":
    print("Codigo principal")

    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("400x400")
    ventana.configure(background="indianred")

    input_text = tk.StringVar()

    tecla = ['p', 'q', 'r', 's', '~','->','v','<->','^','+']
    X_tecla = [10, 80, 160, 240, 10, 80, 160, 240, 10, 80]
    Y_tecla = [0, 0, 0, 0, 50, 50, 50, 50, 100, 100]

    for TeclaActual in range(len(tecla)):
        print(TeclaActual)
        TeclaFor = tk.Button(ventana)
        TeclaFor["height"] = 2
        TeclaFor["width"] = 7
        TeclaFor["text"] = tecla[TeclaActual]
        TeclaFor["bg"] = ("sandybrown")
        TeclaFor.place(x=X_tecla[TeclaActual], y=Y_tecla[TeclaActual])

    #
    # pollo = tk.Button(ventana)
    # pollo["height"] = 2
    # pollo["width"] = 7
    # pollo["text"] = tecla[0]
    # pollo["bg"] = ("sandybrown")
    # pollo.place(x=0,y=0)
    #
    #
    ventana.mainloop()
