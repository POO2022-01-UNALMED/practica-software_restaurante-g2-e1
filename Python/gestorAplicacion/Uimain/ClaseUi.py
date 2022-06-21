#esta es la clase en la que va a ir la interfaz y demas vainas importantes
import tkinter as tk

inicio = tk.Tk()
inicio.title("inicio")
inicio.geometry("500x400")
inicio.configure(bg="red")

#hojas de vida desarrolladores
P5=tk.Frame(inicio,bg="white",width=500) #en este frame van a ir las hojas de vida
P5.pack(side="right",fill="y")

#texto de bienvenida esquina superior derecha
P3=tk.Label(inicio,text="bienvenido al sofware para un restaurante") #da un mensaje de bienvenida
P3.pack(side="top",anchor="w")
P3.config(fg="white",bg="red",font=("italic",20,"italic"))

inicio.mainloop()

#hoja de vida villamizar:
#Nombres: Juan David
#Apellidos: Villamizar Gelves
#edad: 21 años
