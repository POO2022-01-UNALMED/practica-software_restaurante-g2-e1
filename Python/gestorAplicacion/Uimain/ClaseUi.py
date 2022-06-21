import tkinter as tk
#esta es la clase en la que va a ir la interfaz y otros temas de interes

inicio = tk.Tk()
inicio.title("inicio")
inicio.geometry("500x400")
inicio.configure(bg="red")

#hojas de vida desarrolladores
P5=tk.Frame(inicio,bg="white",width=500) #en este frame van a ir las hojas de vida
P5.pack(side="right",fill="y")
hoja_vida=tk.Text(P5,width=40,height=10)
hoja_vida.pack()

#hoja de vida juan david villamizar
hoja_vida_1="nombres: Juan David\napellidos: Villamizar Gelves\nedad: 21 años"

#hoja de vida Jorge Higuita
hoja_vida_2="nombres: Jorge Andres\napellidos: Higuita\nedad: 22 años"

#hola de vida Juan Sebastian

hoja_vida_3="nombres: Juan Sebastian\napellidos: Zapata\nedad: 20 años"

#imprimiendo la hoja de vida

hoja_vida.insert(tk.END,hoja_vida_1)
print(hoja_vida.get('1.0', 'end-1c'))  #se imprime la primera hoja de vida
hoja_vida.configure(state='disabled')

seleccion=1 #el numero de la hoja de vida que se muestra en el widget de las hojas de vida(1,2 o 3)
def cambio():
    global seleccion
    if seleccion<3:
        seleccion+=1
    else:
        seleccion=1

def imprimir_hoja_vida():
    global seleccion
    if seleccion==1:
        hoja_vida.configure(state='normal')
        hoja_vida.delete('1.0', 'end-1c')
        hoja_vida.insert(tk.END,hoja_vida_1)
        print(hoja_vida.get('1.0', 'end-1c'))  #se imprime la primera hoja de vida
        hoja_vida.configure(state='disabled')
    if seleccion==2:
        hoja_vida.configure(state='normal')
        hoja_vida.delete('1.0', 'end-1c')
        hoja_vida.insert(tk.END,hoja_vida_2)
        print(hoja_vida.get('1.0', 'end-1c'))  #se imprime la segunda hoja de vida
        hoja_vida.configure(state='disabled')
    if seleccion==3:
        hoja_vida.configure(state='normal')
        hoja_vida.delete('1.0', 'end-1c')
        hoja_vida.insert(tk.END,hoja_vida_3)
        print(hoja_vida.get('1.0', 'end-1c'))  #se imprime la tercera hoja de vida
        hoja_vida.configure(state='disabled')

def ejecucion(event):
    cambio() #primero realiza el cambio al numero de hoja de vida
    imprimir_hoja_vida() #imprime la hoja de vida

#va a suceder cuando le demos click al espacio asignado para las hojas de vida de los desarrolladores(con el boton izquierdo del mouse)
P5.bind("<Button-1>",ejecucion)

#texto de bienvenida esquina superior derecha
P3=tk.Label(inicio,text="bienvenido al sofware para un restaurante") #da un mensaje de bienvenida
P3.pack(side="top",anchor="w")
P3.config(fg="white",bg="red",font=("italic",20,"italic"))

inicio.mainloop()
