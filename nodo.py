class Nodo:
    # Constructor: (llave, valor, hijoIzquierdo, hijoDerecho, padre)
    def __init__(self, llave, valor, nivel, peso, categoria, valorIzq, valorDer, incrementoNocturno, dinero, padre=None, hijoIzquierdo=None, hijoDerecho=None, vehiculosRecorridos=None, creador=None):
        self.llave = llave
        self.valor = valor
        self.nivel = nivel
        self.peso = peso
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho
        self.padre = padre
        self.categoria = categoria
        self.valorIzq = valorIzq
        self.valorDer = valorDer
        self.incrementoNocturno = incrementoNocturno
        self.vehiculosRecorridos = vehiculosRecorridos
        self.dinero = dinero
        self.creador = creador

    def ObtenerCreador(self):
        return self.creador

    def PonerCreador(self, creador):
        self.creador = creador

    def ObtenerVehiculosRecorridos(self):
        return self.vehiculosRecorridos

    def PonerVehiculosRecorridos(self, vehiculosRecorridos):
        self.vehiculosRecorridos = vehiculosRecorridos

    def ObtenerDinero(self):
        return self.dinero

    def PonerDinero(self, dinero):
        self.dinero = dinero

    def ObtenerValor(self):
        return self.valor

    def PonerValor(self, valor):
        self.valor = valor

    def ObtenerPadre(self):
        return self.padre

    def PonerPadre(self, padre):
        self.padre = padre

    def ObtenerIncrementoNocturno(self):
        return self.incrementoNocturno

    def PonerIncrementoNocturno(self, incrementoNocturno):
        self.incrementoNocturno = incrementoNocturno

    def ObtenerValorIzq(self):
        return self.valorIzq

    def PonerValorIzq(self, valorIzq):
        self.valorIzq = valorIzq

    def ObtenerValorDer(self):
        return self.valorDer

    def PonerValorDer(self, valorDer):
        self.valorDer = valorDer

    def ObtenerLlave(self):
        return self.llave

    def PonerLlave(self, llave):
        self.llave = llave

    def ObtenerCategoria(self):
        return self.categoria

    def PonerCategoria(self, categoria):
        self.categoria = categoria

    # Retornar el nodo del hijo izquierdo [None cuando no tiene hijo]
    def ObtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    # Asignar el nodo del hijo izquierdo
    def PonerHijoIzquierdo(self, hijo):
        self.hijoIzquierdo = hijo

    # Retornar el nodo del hijo derecho [None cuando no tiene hijo]
    def ObtenerHijoDerecho(self):
        return self.hijoDerecho

    # Asignar el nodo del hijo derecho
    def PonerHijoDerecho(self, hijo):
        self.hijoDerecho = hijo

    def PonerPadre(self, padre):
        self.padre = padre

    # Validar sí el nodo es raíz
    def EsNodoRaiz(self):
        return not self.padre

    # Validar sí el nodo es hoja
    def EsNodoHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)

    # obtener el nivel del nodo
    def ObtenerNivel(self):
        return self.nivel

    def EsHijoIzquierdo(self):
        if (self.padre):
            if self.padre.ObtenerHijoIzquierdo() != None:
                print(f"{self.padre.valor} {self.padre.llave} y {self.valor} {self.llave}")
                return self.valor == self.padre.ObtenerHijoIzquierdo().valor

    def EsHijoDerecho(self):
        if (self.padre):
            if self.padre.ObtenerHijoDerecho() != None:
                print(f"{self.padre.valor} {self.padre.llave} y {self.valor} {self.llave}")
                return self.valor == self.padre.ObtenerHijoDerecho().valor
