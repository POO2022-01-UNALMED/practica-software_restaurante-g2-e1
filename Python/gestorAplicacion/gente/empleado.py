from csv import list_dialects
from persona import Persona
class Empleado(Persona):
    numero_empleados=0
    lista_empleado=[]
    def __init__(self,cedula,nombre,telefono):
        super.__init__(self,cedula,nombre,telefono)
        self.numero_ventas=0
        numero_empleados+=1
        self._numero_asignado=numero_empleados
        self._numero_ventas=0
        lista_empleado.append(self)
    
    #metodos get
    def getNumero(self):
        return self._numero_asignado
    
    @classmethod
    def getNumero_empleados(self):
        return numero_empleados
    
    def getNumero_ventas(self):
        return self._numero_ventas
    
    #metodos set
    def setNumero_asignado(self,numero_asignado):
        self._numero_asignado=numero_asignado
    
    #otros metodos
    def nuevaVenta(self):
        self._numero_ventas+=1
    
    @classmethod
    def empleado_mas_eficiente(cls):
        ventasporempleado=[]
        for i in lista_empleado:
            ventasporempleado.append(i.getNumero_ventas())
        maximo_ventas=max(ventasporempleado)
        for e in ventasporempleado:
            if ventasporempleado(e)==maximo_ventas:
                return lista_empleado[e]
    
    @classmethod
    def empleado_menos_eficiente(cls):
        ventasporempleado=[]
        for i in lista_empleado:
            ventasporempleado.append(i.getNumero_ventas())
        minimo_ventas=min(ventasporempleado)
        for e in ventasporempleado:
            if ventasporempleado(e)==minimo_ventas:
                return lista_empleado[e]
    
    def informacion(self):
        return f"nombre del Empleado: {self._nombre} \ncedula: {self._cedula} \ntelefono: {self._telefono}\nnumero asignado: {self._numero_asignado} \nnumero de ventas: {self._numero_ventas}"
    
    def info_basi(self):
	    super().informacion()