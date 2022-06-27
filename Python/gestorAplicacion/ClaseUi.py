import ventana_inicio 
import os
from gente.empleado import Empleado
from baseDatos.Serializador import Serializador
from baseDatos.Deserializador import Deserializador
from restaurante.ingredientes import Ingredientes
from gente.cliente import Cliente
from gente.gerente import Gerente

#Comprobanmos si existen objetos creados anteriormente
Vacio=True
dirtemp = "gestorAplicacion/baseDatos/temp"
for filename in os.listdir(dirtemp):
    f = os.path.join(dirtemp, filename)
    if os.stat(f).st_size == 0:
        Vacio = True
    else:
        Vacio = False
if Vacio == True: # Si alguna de las carpetas esta vacia
    p1 = Empleado(1, "Juan", 123)
    p2 = Empleado (2, "Villa", 456)
    ing1 = Ingredientes(2, 30, 'carne de res')
    ing2 = Ingredientes(2, 30, 'leche')
    g1 = Gerente(10, "Jorge", 4820249, 1111)
    c1 = Cliente(20, "Franlo el jefe", 318383)
    print("Instanciando objetos")
    
else:
    # Se cargan los objetos guardados
    Deserializador.DeserializarTodo()
    print("cargando informacion")  
ventana_inicio.Ventana_inicio()
Serializador.SerializarTodo()

