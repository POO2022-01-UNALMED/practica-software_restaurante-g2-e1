import tkinter as tk
import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())

#esta es la clase en la que va a ir la interfaz y otros temas de interes

inicio = tk.Tk()
inicio.title("inicio")
inicio.geometry("500x400")
inicio.configure(bg="red")

#hojas de vida desarrolladores
P5=tk.Frame(inicio,bg="white",width=1200) #en este frame van a ir las hojas de vida
P5.pack(side="right",fill="y")
hoja_vida=tk.Text(P5,width=50,height=10)
hoja_vida.pack()
hoja_vida.grid(row=0,column=0)

#hoja de vida juan david villamizar
hoja_vida_1=" \n hoja de vida desarrollador 1 \n \n nombres: Juan David\n apellidos: Villamizar Gelves\n edad: 21 años\n Ocupacion: Estudiante ingenieria electrica\n correo: juvillamizar@unal.edu.co"

#hoja de vida Jorge Higuita
hoja_vida_2=" \n hoja de vida desarrollador 2 \n \n nombres: Jorge Andres\n apellidos: Higuita Monsalve\n edad: 22 años\n Ocupacion: Estudiante ingenieria de sistemas\n correo: jhiguitam@unal.edu.co "

#hola de vida Juan Sebastian

hoja_vida_3=" \n hoja de vida desarrollador 3 \n \n nombres: Juan Sebastian\n apellidos: Zapata echeverry\n edad: 20 años\n Ocupacion: Estudiante ingenieria de sistemas\n correo: jzapatec@unal.edu.co"

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

#fotos

#foto juan david
foto_juan_d = tk.PhotoImage(file=path+"\juan_david.png")

#foto juan sebastian
foto_juan_s = tk.PhotoImage(file=path+"\juan_sebastian.png")

#foto jorge
foto_jorge = tk.PhotoImage(file=path+"\jorge.png")


#foto que se muestra de un desarrollador en concreto
P6 = tk.Label(P5)  
P6.config(image=foto_juan_d)
P6.grid(row=1,column=0)
def visualizacion_foto():
    global seleccion
    if seleccion==1:
        P6.config(image=foto_juan_d)
    if seleccion==2:
        P6.config(image=foto_jorge)
    if seleccion==3:
        P6.config(image=foto_juan_s)
        
def ejecucion(event):
    cambio() #primero realiza el cambio al numero de hoja de vida
    imprimir_hoja_vida() #imprime la hoja de vida
    visualizacion_foto() #imprime la foto del desarrollador

#va a suceder cuando le demos click al espacio asignado para las hojas de vida de los desarrolladores(con el boton izquierdo del mouse)
hoja_vida.bind("<Button-1>",ejecucion)

#texto de bienvenida esquina superior derecha
frame1=tk.Frame(inicio,bg="red",width=1000)
frame1.pack(side="top",anchor="w")
P3=tk.Label(frame1,text=" bienvenido al sofware para un restaurante     ") #da un mensaje de bienvenida
P3.grid(row=0,column=0)
P3.config(fg="white",bg="gray",font=("italic",20,"italic"))
sep = tk.Frame(frame1, bg="black", width=30,height=50)
sep.grid(row=0,column=1)

#imagenes asociadas al sistema, entre otros
P4=tk.Frame(inicio,bg="red",width=1000)
P4.pack(side="left",fill="both")

#foto hamburguesa
foto_hamburguesa = tk.PhotoImage(file=path+"\hamburguesa.png")

#foto papas_fritas
foto_papas_fritas = tk.PhotoImage(file=path+"\papas_fritas.png")

#foto perro_caliente
foto_perro_caliente = tk.PhotoImage(file=path+"\perro_caliente.png")

#foto taco
foto_taco = tk.PhotoImage(file=path+"\Taco.png")

#foto burrito
foto_burrito = tk.PhotoImage(file=path+"\Burrito.png")

#nos va a servir para ver la foto de muestra de uno de los platillos
numero_foto_platillo=1

foto_muestra = tk.Label(P4)  
foto_muestra.grid(row=0,column=0,padx=10,pady=10)
foto_muestra.config(image=foto_hamburguesa)

def visualizacion_foto_platillo(): #esta funcion es util para determinar cual es la foto que se va a ver
    global numero_foto_platillo
    if numero_foto_platillo==1:
        foto_muestra.config(image=foto_hamburguesa)
    if numero_foto_platillo==2:
        foto_muestra.config(image=foto_papas_fritas)
    if numero_foto_platillo==3:
        foto_muestra.config(image=foto_perro_caliente)
    if numero_foto_platillo==4:
        foto_muestra.config(image=foto_taco)
    if numero_foto_platillo==5:
        foto_muestra.config(image=foto_burrito)

def cambio_platillo():
    global numero_foto_platillo
    if numero_foto_platillo<5:
        numero_foto_platillo+=1
    else:
        numero_foto_platillo=1
        
def ejecucion_foto_platillo(event):
    cambio_platillo() #primero realiza el cambio al numero de hoja de vida
    visualizacion_foto_platillo() #imprime la foto del desarrollador

#va a suceder cuando pasemos el mouse por encima de una imagen
foto_muestra.bind("<Enter>",ejecucion_foto_platillo)

#boton para ir a la siguiente ventana

boton_i_sesion = tk.Button(P4,text="iniciar sesion")
boton_i_sesion.grid(row=1,column=0)

boton_i_sesion.place(x=180,y=600,width=200, height=50)

#separador
separador = tk.Frame(P4, bg="black", width=30,height=539)
separador.grid(row=0,column=1)
separador2 = tk.Frame(P4, bg="black", width=30,height=250)
separador2.grid(row=1,column=1)
#separador.pack(fill="y")

inicio.mainloop()


