import tkinter as tk
import os
import pathlib
from tkinter import Button, Frame, messagebox
from tkinter import ttk
from turtle import width
import turtle
import ventana_inicio

from gente.empleado import Empleado
from gente.gerente import Gerente

from excepciones.erroaplicacion import ErrorAplicacion
from excepciones.errorformato import *

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#ventana principal, donde se ejecuta el programa
class Ventana_principal_gerente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana_principal_gerente")
        self.geometry("1360x720")
        self.configure(bg="LightSteelBlue")

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
        self.frame_2=tk.Frame(self,bg="LightSteelBlue",height=700)
        self.frame_2.pack(side="top",fill="both")
        

       
        #frame de la parte de abajo, es meramente decorativo 
        self.frame_abajo=tk.Frame(self,bg="RoyalBlue",height=70)
        self.frame_abajo.pack(side="bottom",fill="both")

        #frames, botones de empleados ----------------------------------------------------------------------------------------------------------------------------------------------


        self.titl_label = tk.Label(self, text='Ver empleados', font=('Italic', 20))
        self.desp_frame = tk.Frame(self, bg= 'LightSteelBlue', height= 80, width= 1360)
        self.desp_exp = tk.Label(self.desp_frame, text = 'En esta ventana podremos visualizar la informacion de los empleados y despedir al que queramos,\nel despido inteligente despide al empleado menos eficiente, ademas podremos ver a nuestro mejor empleado.')


        self.despido = Button(self.frame_2, text='Despedir', width=15)
        self.info_emp = 'Aqui aparecera la informacion de los distintos empleados.'
        self.num_emp = 0
        self.textemp = tk.Text(self.frame_2, border= False, font=('Italic', 20))
        self.textemp.insert(tk.END, self.info_emp)
        self.textemp.configure(state='disabled')
        self.sig_emp = Button(self.frame_2, text='Siguiente', width=15)
        self.atr_emp = Button(self.frame_2, text='Anterior', width=15)
        self.desp_int = Button(self.frame_2, text='Despido inteligente', width=15)
        self.mas_ef = Button(self.frame_2, text= 'Mas eficiente',width=15)
        

        def buscar_empleado(event):
            x = Empleado.getListaEmpleado()
            if self.info_emp == 'Aqui aparecera la informacion de los distintos empleados.':
                self.num_emp = 0
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            elif self.num_emp >= len(x)-1:
                self.num_emp = 0
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            else:
                self.num_emp += 1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)


        def atras_empleado(event):
            x = Empleado.getListaEmpleado()
            if self.info_emp == 'Aqui aparecera la informacion de los distintos empleados.':
                self.num_emp = len(x)
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            elif self.num_emp == 0:
                self.num_emp = len(x)-1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

            else:
                self.num_emp -= 1
                try:
                    self.info_emp = x[self.num_emp].informacion()
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')
                except:
                    messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)
        
        def despido_emp(event):
            for i in Empleado.getListaEmpleado():
                 if i.informacion() == self.info_emp:
                    Gerente.despedir_Empleado(i.getNumero())
                    self.info_emp = 'Enhorabuena, despediste al empleado:\n\n' + self.info_emp + '\n\nAhora no tendras que verlo nunca mas'
                    self.textemp.configure(state='normal')
                    self.textemp.delete('1.0', 'end-1c')
                    self.textemp.insert(tk.END,self.info_emp)
                    self.textemp.configure(state='disabled')

        def desp_int(event):
            try:
                self.info_emp = 'Enhorabuena, despediste al empleado:\n\n' + Empleado.empleado_menos_eficiente().informacion() + '\n\nAhora no tendras que verlo nunca mas'
                Gerente.despido_inteligente()
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)
            self.textemp.configure(state='normal')
            self.textemp.delete('1.0', 'end-1c')
            self.textemp.insert(tk.END,self.info_emp)
            self.textemp.configure(state='disabled')

        def emp_efic(event):
            try:
                w = Empleado.empleado_mas_eficiente()
                self.info_emp = 'Nuestro mejor empleado es:\n\n' + w.informacion() + '\n\n deberias aumentarle el salario a este buen trabajador. '
                self.textemp.configure(state='normal')
                self.textemp.delete('1.0', 'end-1c')
                self.textemp.insert(tk.END,self.info_emp)
                self.textemp.configure(state='disabled')
            except:
                messagebox.showwarning(title="Aviso",message=ExcepcionEmpleado('').mensaje_error)

        self.sig_emp.bind('<ButtonRelease-1>',buscar_empleado)
        self.atr_emp.bind('<ButtonRelease-1>',atras_empleado)
        self.despido.bind('<ButtonRelease-1>', despido_emp)
        self.desp_int.bind('<ButtonRelease-1>', desp_int)
        self.mas_ef.bind('<ButtonRelease-1>',emp_efic)
        def show_empleados():
            self.frame_abajo.pack_forget()
            self.frame_2.pack_forget()
            self.titl_label.pack(pady = 10)
            self.desp_frame.pack(anchor='n')
            self.desp_exp.pack(pady= 10)
            self.frame_2.pack(side="top",fill="both")
            self.despido.place(relx = 0.4, rely = 0.9, anchor = 'c')
            self.desp_int.place(relx = 0.6,rely=0.9, anchor='c')
            self.textemp.place(relx=0.5,rely=0.5,relheight=0.6, relwidth= 0.6, anchor= 'c')
            self.sig_emp.place(relx = 0.7, rely = 0.9, anchor = 'c')
            self.atr_emp.place(relx = 0.3, rely = 0.9, anchor = 'c')
            self.mas_ef.place(relx = 0.5, rely = 0.9, anchor = 'c')
            
            

        ##---------------------------------------------------------------------------------------------------------------------------------
        #aqui va la parte de el inventario

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
            if self.p_y_c.get()=="Ver y despedir empleados":
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
        self.p_y_c = tk.ttk.Combobox(self.frame_1,values=["Ver y despedir empleados", "Caja", "Inventario"],textvariable=valorDefecto_p_y_c,state="readonly")
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
    emp3 = Empleado(7,"t",3)
    emp4 = Empleado(8, "david", 2)
    Ventana_principal_gerente()