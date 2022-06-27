import ventana_inicio 
import os
from gente.empleado import Empleado
from baseDatos.Serializador import Serializador
from baseDatos.Deserializador import Deserializador

#Comprobanmos si existen objetos creados anteriormente
if os.stat("Python/gestorAplicacion/baseDatos/temp/Empleado.txt").st_size == 0:
    p1 = Empleado(1, "Juan", 123)
    p2 = Empleado (2, "Villa", 456)
else:
    # Se cargan los objetos guardados
    Deserializador.deserializar("Empleado")
    print("Deserializaondo WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
ventana_inicio.Ventana_inicio()
Serializador.serializar("Empleado")

