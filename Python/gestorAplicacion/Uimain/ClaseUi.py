#esta es la clase en la que va a ir la interfaz y demas vainas importantes
import tkinter as tk

inicio = tk.Tk()
inicio.title("inicio")
inicio.geometry("500x400")
inicio.configure(bg="red")

P3=tk.Label(inicio,text="bienvenido al sofware para un restaurante") #da un mensaje de bienvenida
P3.pack(anchor="nw")
P3.config(fg="white",bg="red",font=("Arial",20))

inicio.mainloop()

#hoja de vida villamizar:
#Nombres: Juan David
#Apellidos: Villamizar Gelves
#edad: 21 años
