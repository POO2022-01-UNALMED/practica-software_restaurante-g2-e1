import tkinter as tk
import os
import pathlib
from tkinter import Button, Frame, messagebox
from tkinter import ttk
import ventana_inicio
import iniciar_sesion

from gente.empleado import Empleado

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Ventana_principal_gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana_principal_gerente")
        self.geometry("1360x720")
        self.configure(bg="white")

        #este frame(frame_0) corresponde al de la parte superior

        self.frame_0=tk.Frame(self,bg="RoyalBlue",height=80)
        self.frame_0.pack(side="top",fill="x")

        #una etiqueta que contiene al titulo del nombre del software

        self.titulo=tk.Label(self.frame_0,text=" software para un restaurante ")
        self.titulo.config(fg="white",bg="RoyalBlue",font=("italic",30,"italic"))
        self.titulo.pack(anchor="c")

        #este frame(frame_1) corresponde a la zona de menus

        self.frame_1=tk.Frame(self,bg="gray",height=80)
        self.frame_1.pack(side="top",fill="x")

        #se muestra una ventana de dialogo con la descripcion del software
        def descripcion_software(): 
            messagebox.showinfo("Descripcion del sistema","Este software se encarga de la gestion de un restaurante a nivel general, es decir, con el software para un restaurante se podran administrar diferentes aspectos como lo son ventas, nomina e inventario")
    
        #se muestra una ventana de dialogo con los nombres de los autores del software
        def autores_software(): 
            messagebox.showinfo("Autores del software","Autor 1:Juan David Billamizar Gelves\nAutor 2:Jorge Andres Higuita Monsalve\nAutor 3:Juan Sebastian echeverri Zapata")
        
        #en este frame(frame_2) se encuentra lo relacionado con los procesos y consultas
        self.frame_2=tk.Frame(self,bg="LightSteelBlue",height=580)
        self.frame_2.pack(side="top",fill="both")
       
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="RoyalBlue",height=70)
        self.frame_abajo.pack(side="bottom",fill="both")

        #frames, botones
        
        self.frameemp = tk.Frame(self.frame_2, bg='SteelBlue',width='340', height='720')
        self.despido = Button(self.frame_2, text='Despedir')
        self.info_emp = Empleado.getListaEmpleado()[0].informacion()
        self.num_emp = 0
        self.textemp = tk.Text(self.frame_2)
        self.textemp.place(relx=0.05, rely=0.1)
        self.textemp.insert(tk.END, self.info_emp)
        self.textemp.configure(state='disabled')

        def buscar_empleado(event):
            x = Empleado.getListaEmpleado()
            if self.num_emp == len(x):
                self.num_emp = 0
                self.info_emp = x[self.num_emp].informacion()
                self.textemp.configure(state='normal')
                self.textemp.delete('1.0', 'end-1c')
                self.textemp.insert(tk.END,self.info_emp)
                self.textemp.configure(state='disabled')
            else:
                self.num_emp += 1
                self.info_emp = x[self.num_emp].informacion()
                self.textemp.configure(state='normal')
                self.textemp.delete('1.0', 'end-1c')
                self.textemp.insert(tk.END,self.info_emp)
                self.textemp.configure(state='disabled')


        def show_empleados():
            self.frame_abajo.pack_forget()
            self.frameemp.pack(anchor='e')
            self.despido.place(relx = 0.375, rely = 0.9, anchor = 'c')
            self.textemp.place(relx=0.05,rely=0.1)
            


        #esta funcion ejecuta las opciones del combobox de Archivo
        def opciones_Archivo(event):
            if self.Archivo.get()=="Aplicacion":
                self.Archivo.set("Archivo")
                descripcion_software()
                
            elif self.Archivo.get()=="Salir":
                self.Archivo.set("Archivo")
                self.ventana_inicio()


        
        
            
        #esta funcion ejecuta las opciones del combobox de opciones_p_y_C(todavia faltan por definir bien las funciones)
        def opciones_p_y_c(event):
            if self.p_y_c.get()=="Mostrar empleados":
                show_empleados()
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Caja":
                self.p_y_c.set("Procesos y consultas")

            elif self.p_y_c.get()=="Inventario":
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
        self.p_y_c = tk.ttk.Combobox(self.frame_1,values=["Mostrar empleados", "Caja", "Inventario"],textvariable=valorDefecto_p_y_c,state="readonly")
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
if __name__ == "__main__":
    emp1 = Empleado(1,"andres", 23)
    emp2 = Empleado(3, "sofia", 4)
    Ventana_principal_gerente()