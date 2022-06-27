import pickle

from gente.cliente import Cliente
from gente.empleado import Empleado
from gente.gerente import Gerente
from restaurante.ingredientes import Ingredientes


class Serializador:
    @classmethod
    def serializar(cls,tipo):
        if tipo=="Cliente":
            pickfile = open("Python/gestorAplicacion/baseDatos/temp/Cliente.txt", "wb")
            serializa = Cliente._lista_socio
            pickle.dump(serializa, pickfile,)
            pickfile.close

        elif tipo=="Empleado":
            pickfile = open("Python/gestorAplicacion/baseDatos/temp/Empleado.txt", "wb")
            serializa = Empleado._lista_empleado
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="Gerente":
            pickfile = open("Python/gestorAplicacion/baseDatos/temp/Gerente.txt", "wb")
            serializa = Gerente._list_gerente
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="ingredientes":
            pickfile = open("Python/gestorAplicacion/baseDatos/temp/ingredientes.txt", "wb")
            serializa = Ingredientes.getListaIngredientes
            pickle.dump(serializa, pickfile)
            pickfile.close
        
        elif tipo=="NumEmple":
            pickfile = open("Python/gestorAplicacion/baseDatos/temp/NumEmple.txt", "wb")
            serializa = Empleado.getNumero_empleados
            pickle.dump(serializa, pickfile)
            pickfile.close
    
    def SerializarTodo():
        Serializador.serializar("Cliente")
        Serializador.serializar("Empleado")
        Serializador.serializar("Gerente")
        Serializador.serializar("ingredientes")
        Serializador.serializar("NumEmple")
