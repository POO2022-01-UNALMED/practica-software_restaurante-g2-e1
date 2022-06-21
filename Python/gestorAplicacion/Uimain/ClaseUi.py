#esta es la clase en la que va a ir la interfaz y demas vainas importantes
import tkinter as tk

inicio = tk.Tk()
inicio.title("inicio")
inicio.geometry("500x400")


P3=tk.Label(inicio,text="bienvenido") #da un mensaje de bienvenida
P3.pack(anchor="nw")

inicio.mainloop()

