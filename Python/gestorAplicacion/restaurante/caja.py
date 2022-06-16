class Caja:

    #constructor
    def __init__(self, efectivo = 0, ingresos = None, egresos = None):
        if ingresos is None:
            ingresos = []
        if egresos is None:
            egresos = []
        self._efectivo = efectivo
        self._ingresos = ingresos
        self._egresos = egresos

    #metodos get 
    def getEfectivo(self):
        return self._efectivo

    def getIngresos(self):
        return self._ingresos

    def getEgresos(self):
        return self._egresos

    #metodos set
    def setEfectivo(self, efectivo):
        self._efectivo += efectivo

    def setIngresos(self, ingresos):
        self._ingresos.append(ingresos)

    def setEgresos(self, egresos):
        self._egresos.append(egresos)

    #metodos
    def devuelta(self, n, orden):
        if n > orden.getPrecio_total():
            w = n - orden.getPrecioTotal()
            return w + ""
        else:
            return "cantidad insuficiente"

    def arqueo(self):
        x = 0
        for i in self._ingresos:
            x += i
        for i in self._egresos:
            x -= i
        return x