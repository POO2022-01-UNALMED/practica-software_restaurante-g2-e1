import pickle

from gestorAplicacion.gente.cliente import Cliente
from gestorAplicacion.gente.empleado import Empleado
from gestorAplicacion.gente.gerente import Gerente
from gestorAplicacion.restaurante.ingredientes import Ingredientes

def serializar(cls,tipo):
    if tipo=="Cliente":
        pickfile = open("Python/baseDatos/temp/Cliente.txt","wb")
        serializa = Cliente._lista_socio
        pickle.dumps(serializa,pickfile)
        pickfile.close

    elif tipo=="Empleado":
         pickfile = open("Python/baseDatos/temp/Empleado.txt", "wb")
         serializa = Empleado._lista_empleado
         pickle.dumps(serializa,pickfile)
         pickfile.close
    
    elif tipo=="Gerente":
        pickfile = open("Python/baseDatos/temp/Gerente.txt", "wb")
        serializa = Gerente._list_gerente
        pickle.dumps(serializa, pickfile)
        pickfile.close
    
    elif tipo=="ingredientes":
         pickfile = open("Python/baseDatos/temp/ingredientes.txt", "wb")
         serializa = Ingredientes.getListaIngredientes
         pickle.dumps(serializa, pickfile)
         pickfile.close
    
    elif tipo=="NumEmple":
         pickfile = open("Python/baseDatos/temp/NumEmple.txt", "wb")
         serializa = Empleado.getNumero_empleados
         pickle.dumps(serializa, pickfile)
         pickfile.close