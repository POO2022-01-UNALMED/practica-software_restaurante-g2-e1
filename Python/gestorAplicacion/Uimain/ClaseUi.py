import tkinter as tk
import os
import pathlib
from tkinter import messagebox
from tkinter import ttk

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana de inicio, es la primera ventana que se muestra al iniciar sesion

class ventana_inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana_inicio")
        self.geometry("500x400")
        self.configure(bg="red")

        #menu

        #cierra la aplicacion

        def eventosalir_aplicacion():
            self.destroy()

        #muestra un mensaje dando una pequeña descripcion del sistema

        def eventodescripcion(): 
            messagebox.showinfo("Descripcion del sistema","Este software se encarga de la gestion de un restaurante a nivel general, es decir, con el software para un restaurante se podran administrar diferentes aspectos como lo son ventas, nomina e inventario")


        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        self.menu1 = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="inicio", 
        menu=self.menu1,command=eventosalir_aplicacion)
        self.menu1.add_command(label="Salir de la aplicacion",command=eventosalir_aplicacion)
        self.menu1.add_command(label="Descripcion del sistema",command=eventodescripcion)

        #hojas de vida desarrolladores
        self.P5=tk.Frame(self,bg="white",width=1200) #en este frame van a ir las hojas de vida
        self.P5.pack(side="right",fill="y")
        self.hoja_vida=tk.Text(self.P5,width=90,height=10)
        self.hoja_vida.pack()
        self.hoja_vida.grid(row=0,column=0)

        #hoja de vida juan david villamizar
        self.hoja_vida_1=" \n hoja de vida desarrollador 1 \n \n nombres: Juan David\n apellidos: Villamizar Gelves\n edad: 21 años\n Ocupacion: Estudiante ingenieria electrica\n correo: juvillamizar@unal.edu.co"

        #hoja de vida Jorge Higuita
        self.hoja_vida_2=" \n hoja de vida desarrollador 2 \n \n nombres: Jorge Andres\n apellidos: Higuita Monsalve\n edad: 22 años\n Ocupacion: Estudiante ingenieria de sistemas\n correo: jhiguitam@unal.edu.co "

        #hola de vida Juan Sebastian

        self.hoja_vida_3=" \n hoja de vida desarrollador 3 \n \n nombres: Juan Sebastian\n apellidos: Zapata echeverry\n edad: 20 años\n Ocupacion: Estudiante ingenieria de sistemas\n correo: jzapatec@unal.edu.co"

        #imprimiendo la hoja de vida

        self.hoja_vida.insert(tk.END,self.hoja_vida_1)
        print(self.hoja_vida.get('1.0', 'end-1c'))  #se imprime la primera hoja de vida
        self.hoja_vida.configure(state='disabled')

        self.seleccion=1 #el numero de la hoja de vida que se muestra en el widget de las hojas de vida(1,2 o 3)
        def cambio():
            if self.seleccion<3:
                self.seleccion+=1
            else:
                self.seleccion=1

        def imprimir_hoja_vida():
            if self.seleccion==1:
                self.hoja_vida.configure(state='normal')
                self.hoja_vida.delete('1.0', 'end-1c')
                self.hoja_vida.insert(tk.END,self.hoja_vida_1)
                print(self.hoja_vida.get('1.0', 'end-1c'))  #se imprime la primera hoja de vida
                self.hoja_vida.configure(state='disabled')
            if self.seleccion==2:
                self.hoja_vida.configure(state='normal')
                self.hoja_vida.delete('1.0', 'end-1c')
                self.hoja_vida.insert(tk.END,self.hoja_vida_2)
                print(self.hoja_vida.get('1.0', 'end-1c'))  #se imprime la segunda hoja de vida
                self.hoja_vida.configure(state='disabled')
            if self.seleccion==3:
                self.hoja_vida.configure(state='normal')
                self.hoja_vida.delete('1.0', 'end-1c')
                self.hoja_vida.insert(tk.END,self.hoja_vida_3)
                print(self.hoja_vida.get('1.0', 'end-1c'))  #se imprime la tercera hoja de vida
                self.hoja_vida.configure(state='disabled')


        #fotos

        #fotos juan david
        self.foto_juan_d1 = tk.PhotoImage(file=path+"\juan_david1.png")
        self.foto_juan_d2 = tk.PhotoImage(file=path+"\juan_david1.png")
        self.foto_juan_d3 = tk.PhotoImage(file=path+"\juan_david1.png")
        self.foto_juan_d4 = tk.PhotoImage(file=path+"\juan_david1.png")

        #fotos juan sebastian
        self.foto_juan_s1 = tk.PhotoImage(file=path+"\juan_sebastian1.png")
        self.foto_juan_s2 = tk.PhotoImage(file=path+"\juan_sebastian2.png")
        self.foto_juan_s3 = tk.PhotoImage(file=path+"\juan_sebastian3.png")
        self.foto_juan_s4 = tk.PhotoImage(file=path+"\juan_sebastian4.png")

        #fotos jorge
        self.foto_jorge1 = tk.PhotoImage(file=path+"\jorge1.png")
        self.foto_jorge2 = tk.PhotoImage(file=path+"\jorge2.png")
        self.foto_jorge3 = tk.PhotoImage(file=path+"\jorge3.png")
        self.foto_jorge4 = tk.PhotoImage(file=path+"\jorge1.png")


        #espacio para las fotos que se muestran de un desarrollador en concreto
        self.P6 = tk.Label(self.P5)  
        self.P6.config(image=self.foto_juan_d1)
        self.P6.grid(row=1,column=0)

        #primera foto que se muestra del desarrollador
        self.foto1= tk.Label(self.P6)
        self.foto1.grid(row=0,column=0)
        self.foto1.config(image=self.foto_juan_d1)

        #segunda foto que se muestra del desarrollador
        self.foto2= tk.Label(self.P6)
        self.foto2.grid(row=0,column=1)
        self.foto2.config(image=self.foto_juan_d1)

        #tercera foto que se muestra del desarrollador
        self.foto3= tk.Label(self.P6)
        self.foto3.grid(row=1,column=0)
        self.foto3.config(image=self.foto_juan_d1)

        #cuarta foto que se muestra del desarrollador
        self.foto4= tk.Label(self.P6)
        self.foto4.grid(row=1,column=1)
        self.foto4.config(image=self.foto_juan_d1)

        def visualizacion_foto():
            #global seleccion
            if self.seleccion==1:
                self.foto1.config(image=self.foto_juan_d1)
                self.foto2.config(image=self.foto_juan_d1)
                self.foto3.config(image=self.foto_juan_d1)
                self.foto4.config(image=self.foto_juan_d1)
            if self.seleccion==2:
                self.foto1.config(image=self.foto_jorge1)
                self.foto2.config(image=self.foto_jorge2)
                self.foto3.config(image=self.foto_jorge3)
                self.foto4.config(image=self.foto_jorge1)
            if self.seleccion==3:
                self.foto1.config(image=self.foto_juan_s1)
                self.foto2.config(image=self.foto_juan_s2)
                self.foto3.config(image=self.foto_juan_s3)
                self.foto4.config(image=self.foto_juan_s4)
        
        def ejecucion(event):
            cambio() #primero realiza el cambio al numero de hoja de vida
            imprimir_hoja_vida() #imprime la hoja de vida
            visualizacion_foto() #imprime la foto del desarrollador

        #va a suceder cuando le demos click al espacio asignado para las hojas de vida de los desarrolladores(con el boton izquierdo del mouse)
        self.hoja_vida.bind("<Button-1>",ejecucion)

        #####################################################################

        #texto de bienvenida esquina superior izquierda
        self.frame1=tk.Frame(self,bg="red",width=1000)
        self.frame1.pack(side="top",anchor="w")
        self.P3=tk.Label(self.frame1,text=" bienvenido al sofware para un restaurante     ") #da un mensaje de bienvenida
        self.P3.grid(row=0,column=0)
        self.P3.config(fg="white",bg="gray",font=("italic",20,"italic"))
        self.sep = tk.Frame(self.frame1, bg="black", width=30,height=50)
        self.sep.grid(row=0,column=1)

        #imagenes asociadas al sistema, entre otros
        self.P4=tk.Frame(self,bg="red",width=1000)
        self.P4.pack(side="left",fill="both")

        #foto hamburguesa
        self.foto_hamburguesa = tk.PhotoImage(file=path+"\hamburguesa.png")

        #foto papas_fritas
        self.foto_papas_fritas = tk.PhotoImage(file=path+"\papas_fritas.png")

        #foto perro_caliente
        self.foto_perro_caliente = tk.PhotoImage(file=path+"\perro_caliente.png")

        #foto taco
        self.foto_taco = tk.PhotoImage(file=path+"\Taco.png")

        #foto burrito
        self.foto_burrito = tk.PhotoImage(file=path+"\Burrito.png")

        #nos va a servir para ver la foto de muestra de uno de los platillos
        self.numero_foto_platillo=1

        self.foto_muestra = tk.Label(self.P4)  
        self.foto_muestra.grid(row=0,column=0,padx=10,pady=10)
        self.foto_muestra.config(image=self.foto_hamburguesa)

        def visualizacion_foto_platillo(): #esta funcion es util para determinar cual es la foto que se va a ver
            if self.numero_foto_platillo==1:
                self.foto_muestra.config(image=self.foto_hamburguesa)
            if self.numero_foto_platillo==2:
                self.foto_muestra.config(image=self.foto_papas_fritas)
            if self.numero_foto_platillo==3:
                self.foto_muestra.config(image=self.foto_perro_caliente)
            if self.numero_foto_platillo==4:
                self.foto_muestra.config(image=self.foto_taco)
            if self.numero_foto_platillo==5:
                self.foto_muestra.config(image=self.foto_burrito)

        def cambio_platillo():
            if self.numero_foto_platillo<5:
                self.numero_foto_platillo+=1
            else:
                self.numero_foto_platillo=1
        
        def ejecucion_foto_platillo(event):
            cambio_platillo() #primero realiza el cambio al numero de hoja de vida
            visualizacion_foto_platillo() #imprime la foto del desarrollador

        #va a suceder cuando pasemos el mouse por encima de una imagen
        self.foto_muestra.bind("<Enter>",ejecucion_foto_platillo)

        #boton para ir a la siguiente ventana

        self.boton_i_sesion = tk.Button(self.P4,text="iniciar sesion",command=self.ventana_principal)

        self.boton_i_sesion.grid(row=1,column=0)

        self.boton_i_sesion.place(x=180,y=600,width=200, height=50)

        #self.boton_i_sesion.bind("<Button-1>",ingreso_ventana_usuario)

        #separador
        self.separador = tk.Frame(self.P4, bg="black", width=30,height=539)
        self.separador.grid(row=0,column=1)
        self.separador2 = tk.Frame(self.P4, bg="black", width=30,height=250)
        self.separador2.grid(row=1,column=1)

        self.mainloop()
    
    def ventana_principal(self):
        self.destroy()
        ventana_principal()

#ventana principal, donde se ejecuta el programa

class ventana_principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana_principal")
        self.geometry("500x400")
        self.configure(bg="white")

        #este frame(frame_0) corresponde al de la parte superior

        self.frame_0=tk.Frame(self,bg="red",height=80)
        self.frame_0.pack(side="top",fill="x")

        #una etiqueta que contiene al titulo del nombre del software

        self.titulo=tk.Label(self.frame_0,text=" software para un restaurante ")
        self.titulo.config(fg="white",bg="red",font=("italic",30,"italic"))
        self.titulo.pack(anchor="c")

        #este frame(frame_1) corresponde a la zona de menus

        self.frame_1=tk.Frame(self,bg="gray",height=80)
        self.frame_1.pack(side="top",fill="x")

        #se muestra una ventana de dialogo con la descripcion del software
        def descripcion_software(): 
            messagebox.showinfo("Descripcion del sistema","Este software se encarga de la gestion de un restaurante a nivel general, es decir, con el software para un restaurante se podran administrar diferentes aspectos como lo son ventas, nomina e inventario")
    
        #se muestra una ventana de dialogo con los nombres de los autores del software
        def autores_software(): 
            messagebox.showinfo("Autores del software","Autor 1:Juan David Villamizar Gelves\nAutor 2:Jorge Andres Higuita Monsalve\nAutor 3:Juan Sebastian Echeverry Zapata")
        
        #en este frame(frame_2) se encuentra lo relacionado con los procesos y consultas
        self.frame_2=tk.Frame(self,bg="pink",height=650)
        self.frame_2.pack(side="top",fill="both")
        
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="red",height=80)
        self.frame_abajo.pack(side="bottom",fill="both")

        #esta funcion ejecuta las opciones del combobox de Archivo
        def opciones_Archivo(event):
            if self.Archivo.get()=="Aplicacion":
                self.Archivo.set("Archivo")
                descripcion_software()
                
            if self.Archivo.get()=="Salir":
                self.Archivo.set("Archivo")
                self.ventana_inicio()
               
        #esta funcion ejecuta las opciones del combobox de opciones_p_y_C(todavia faltan por definir bien las funciones)
        def opciones_p_y_c(event):
            if self.p_y_c.get()=="agregar socio":
                self.p_y_c.set("Procesos y consultas")

            if self.p_y_c.get()=="tomar orden":
                self.p_y_c.set("Procesos y consultas")
        
        #esta funcion ejecuta las opciones del combox de ayuda
        def opciones_ayuda(event):
            if self.Ayuda.get()=="acerca de":
                self.Ayuda.set("Ayuda")
                autores_software()


        #Archivo
        valorDefecto_archivo = tk.StringVar(value='Archivo')
        self.Archivo = tk.ttk.Combobox(self.frame_1,values=["Aplicacion","Salir"],textvariable=valorDefecto_archivo,state="readonly")
        self.Archivo.grid(row=0,column=0)
        self.Archivo.bind("<<ComboboxSelected>>",opciones_Archivo)


        #Procesos y consultas
        valorDefecto_p_y_c = tk.StringVar(value='Procesos y consultas')
        self.p_y_c = tk.ttk.Combobox(self.frame_1,values=["tomar orden","agregar socio"],textvariable=valorDefecto_p_y_c,state="readonly")
        self.p_y_c.grid(row=0,column=1)
        self.p_y_c.bind("<<ComboboxSelected>>",opciones_p_y_c)

        #Ayuda
        valorDefecto_ayuda = tk.StringVar(value='Ayuda')
        self.Ayuda = tk.ttk.Combobox(self.frame_1,values=["acerca de"],textvariable=valorDefecto_ayuda,state="readonly")
        self.Ayuda.grid(row=0,column=2)
        self.Ayuda.bind("<<ComboboxSelected>>",opciones_ayuda)

        self.mainloop()

    #vuelve a la ventana de inicio   
    def ventana_inicio(self):
        self.destroy()
        ventana_inicio()

ventana_inicio()
