import tkinter as tk
import os
import pathlib
from tkinter import messagebox
from tkinter import ttk
import ventana_inicio
import iniciar_sesion

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Ventana_principal_empleado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana_principal_empleado")
        self.geometry("1360x720")
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
            messagebox.showinfo("Autores del software","Autor 1:Juan David Villamizar Gelves\nAutor 2:Jorge Andres Higuita Monsalve\nAutor 3:Juan Sebastian echeverri Zapata")
        
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
        
        #esta funcion se ejecuta al seleccionar la opcion agragar socio del combobox de p y c
        def agregar_socio():
            print("no se ejecuta")

            self.boton_anadir_platillo.grid_forget()

            self.boton_retirar_platillo.grid_forget()

            self.boton_revisar_pedido.grid_forget()

            self.boton_terminar_orden.grid_forget()

            self.boton_cancelar_orden.grid_forget()
        
        #esta funcion se ejecuta al seleccionar la opcion tomar orden del combobox de p y c
        def tomar_orden():
            print("se ejecuta")
            self.boton_anadir_platillo.grid()

            self.boton_retirar_platillo.grid()

            self.boton_revisar_pedido.grid()

            self.boton_terminar_orden.grid()

            self.boton_cancelar_orden.grid()
        
        #botones de tomar orden

        self.boton_anadir_platillo = tk.Button(self.frame_2,text="anadir platillo")

        self.boton_retirar_platillo = tk.Button(self.frame_2,text="retirar platillo")

        self.boton_revisar_pedido = tk.Button(self.frame_2,text="revisar pedido")

        self.boton_terminar_orden = tk.Button(self.frame_2,text="terminar orden")

        self.boton_cancelar_orden = tk.Button(self.frame_2,text="cancelar orden")

        ############################################################################

        self.boton_anadir_platillo.grid(row=0,column=0, padx=10, pady=10)

        self.boton_retirar_platillo.grid(row=1,column=0, padx=10, pady=10)

        self.boton_revisar_pedido.grid(row=2,column=0, padx=10, pady=10)

        self.boton_terminar_orden.grid(row=3,column=0, padx=10, pady=10)

        self.boton_cancelar_orden.grid(row=4,column=0, padx=10, pady=10)

        ############################################################################

        self.boton_anadir_platillo.grid_forget()

        self.boton_retirar_platillo.grid_forget()

        self.boton_revisar_pedido.grid_forget()

        self.boton_terminar_orden.grid_forget()

        self.boton_cancelar_orden.grid_forget()
               
        #esta funcion ejecuta las opciones del combobox de opciones_p_y_C(todavia faltan por definir bien las funciones)
        def opciones_p_y_c(event):
            if self.p_y_c.get()=="agregar socio":
                agregar_socio()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="tomar orden":
                tomar_orden()
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
        ventana_inicio.Ventana_inicio()