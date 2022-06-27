import pickle

from gestorAplicacion.gente.cliente import Cliente
from gestorAplicacion.gente.empleado import Empleado
from gestorAplicacion.gente.gerente import Gerente
from gestorAplicacion.restaurante.ingredientes import Ingredientes

def deserializar(cls, tipo):
    if tipo == "Cliente":
        pickfile = open("Python/baseDatos/temp/Cliente.txt", "rb")
        Cliente._lista_socio = pickle.load(pickfile)
        pickfile.close

    elif tipo == "Empleado":
        pickfile = open("Python/baseDatos/temp/Empleado.txt", "rb")
        Empleado._lista_empleado = pickle.load(pickfile)
        pickfile.close

    elif tipo == "Gerente":
        pickfile = open("Python/baseDatos/temp/Gerente.txt", "rb")
        Gerente._list_gerente = pickle.load(pickfile)
        pickfile.close

    elif tipo == "ingredientes":
        pickfile = open("Python/baseDatos/temp/ingredientes.txt", "rb")
        Ingredientes._listaIngredientes = pickle.load(pickfile)
        pickfile.close

    elif tipo == "NumEmple":
        pickfile = open("Python/baseDatos/temp/NumEmple.txt", "rb")
        Empleado._numero_empleados = pickle.load(pickfile)
        pickfile.close
