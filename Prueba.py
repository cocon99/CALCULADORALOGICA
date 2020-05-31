import tkinter as tk
import cv2
import numpy as np

# Principal
if __name__ == "__main__":
    print("Codigo principal")

    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("340x380")
    ventana.configure(background="indianred")

    input_text = tk.StringVar()
    entrada=tk.Entry(ventana,textvariable=input_text,bg="sandybrown")
    entrada.pack(fill=tk.X,padx=10,pady=15,ipadx=5,ipady=4)

    tecla = ['p', 'q', 'r', 's', '~','+','v','^','->','<->','(',')','IZQUIERDA','DERECHA','AC','=']
    X_tecla = [30, 100, 170, 240, 30, 100, 170, 240, 30, 100, 170, 240, 30, 100, 170, 240]
    Y_tecla = [80, 80, 80, 80, 130, 130, 130, 130, 180, 180, 180, 180, 230, 230, 230, 230]

    for TeclaActual in range(len(tecla)):
        print(TeclaActual)
        TeclaFor = tk.Button(ventana)
        TeclaFor["height"] = 2
        TeclaFor["width"] = 7
        TeclaFor["text"] = tecla[TeclaActual]
        TeclaFor["bg"] = ("sandybrown")
        TeclaFor.place(x=X_tecla[TeclaActual], y=Y_tecla[TeclaActual])


    ventana.mainloop()
