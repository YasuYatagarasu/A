from nodo import *

class ArbolBinario:

    def __init__(self):
        self.raiz = None
        self.peso = 0
        self.altura = 0

    def ObtenerPeso(self):
        return self.peso

    def AgregarNodo(self, llave, valor, categoria, valorIzq, valorDer, incrementoNocturno):
        if self.raiz:
            # agregar nodo nuevo al árbol
            self._AgregarNodo(llave, valor, categoria, valorIzq, valorDer, incrementoNocturno, self.raiz)
        else:
            # agregar el nuevo nodo como raíz
            self.raiz = Nodo(llave, valor, 1, 0, categoria, valorIzq, valorDer, incrementoNocturno, 0, [], None)
            self.peso += 1
            print("El nodo ", llave, " se ha agregado como raíz en el nivel.", self.raiz.ObtenerNivel())

    def _AgregarNodo(self, llave, valor, categoria, valorIzq, valorDer, incrementoNocturno, nodo):
        # verificar sí es menor o mayor para ir por la izq o derecha respectivamente
        if (valor < nodo.valor):
            if (nodo.ObtenerHijoIzquierdo()):  # verifica si tiene hijo izq
                # se llama recursivamente al hijo implicado
                self._AgregarNodo(llave, valor, categoria, valorIzq, valorDer, incrementoNocturno, nodo.ObtenerHijoIzquierdo())
            else:
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(llave, valor, nodo.ObtenerNivel() + 1, nodo, categoria, valorIzq, valorDer, incrementoNocturno, 0, [], None)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                nodo.PonerValorIzq(nuevoNodo.valor)
                nuevoNodo.PonerCategoria(categoria)
                nuevoNodo.PonerPadre(nodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                print("Se ha agregado como hijo izquierdo de ", nodo.llave, " a ", nuevoNodo.llave, " en el nivel",
                      nuevoNodo.ObtenerNivel(), "Con el categoria", nuevoNodo.ObtenerCategoria(), nuevoNodo.ObtenerVehiculosRecorridos())
        else:
            if (valor > nodo.valor):
                if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                    # se llama recursivamente al hijo implicado
                    self._AgregarNodo(llave, valor, categoria, valorIzq, valorDer, incrementoNocturno, nodo.ObtenerHijoDerecho())
                else:
                    # se crea un nuevo nodo y se asigna como hijo
                    nuevoNodo = Nodo(llave, valor, nodo.ObtenerNivel() + 1, nodo, categoria, valorIzq, valorDer, incrementoNocturno, 0, [], None)
                    nodo.PonerHijoDerecho(nuevoNodo)
                    nodo.PonerValorDer(nuevoNodo.valor)
                    nuevoNodo.PonerCategoria(categoria)
                    nuevoNodo.PonerPadre(nodo)
                    self.peso += 1
                    if (self.altura < nuevoNodo.ObtenerNivel()):
                        self.altura = nuevoNodo.ObtenerNivel()
                    print("Se ha agregado como hijo derecho de ", nodo.llave, " a ", nuevoNodo.llave, " en el nivel",
                          nuevoNodo.ObtenerNivel(), "Con el categoria", nuevoNodo.ObtenerCategoria(), nuevoNodo.ObtenerVehiculosRecorridos())

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo):
        if (nodo):
            print(nodo.valor)
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho())

    # In-order (I-R-D)
    def imprimir_in_order(self, nodo):
        if (nodo):
            self.imprimir_in_order(nodo.ObtenerHijoIzquierdo())
            print(nodo.valor)
            self.imprimir_in_order(nodo.ObtenerHijoDerecho())

    # Post-order (I-D-R)
    def imprimir_post_order(self, nodo):
        if (nodo):
            self.imprimir_post_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_post_order(nodo.ObtenerHijoDerecho())
            print(nodo.valor)

    # Recorrido en Amplitud
    def imprimir_amplitud(self, nodo):
        if (nodo):
            cola = [nodo]
            recorrido = []
            while (len(cola) > 0):
                nodoActual = cola.pop(0)
                recorrido.append(nodoActual.valor)
                hijoIzq = nodoActual.ObtenerHijoIzquierdo()
                hijoDer = nodoActual.ObtenerHijoDerecho()
                if (hijoIzq):
                    cola.append(hijoIzq)
                if (hijoDer):
                    cola.append(hijoDer)
            print("El recorrido en amplitud es:")
            print(recorrido)
        else:
            print("El árbol está vacío.")

    # Verifica que un árbol sea impar
    def EsArbolImpar(self, nodo):
        if (nodo):
            cola = [nodo]
            valores = [0 for i in range(self.altura)]
            while (len(cola) > 0):
                nodoActual = cola.pop(0)

                valores[nodoActual.ObtenerNivel() - 1] += nodoActual.valor

                hijoIzq = nodoActual.ObtenerHijoIzquierdo()
                hijoDer = nodoActual.ObtenerHijoDerecho()
                if (hijoIzq):
                    cola.append(hijoIzq)
                if (hijoDer):
                    cola.append(hijoDer)
            print("Los Valores por niveles son:")
            print(valores)
            esImpar = True
            for v in valores:
                if (v % 2 == 0):
                    esImpar = False
                    break;
            if (esImpar):
                print("El árbol es impar")
            else:
                print("El árbol NO es impar")
        else:
            print("El árbol está vacío.")

    def buscarNodoPorValor(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorValor(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodoPorValor(self, busqueda, nodo):
        if not nodo:
            return None
        if (busqueda == nodo.valor):
            return nodo
        else:
            if (busqueda < nodo.valor):
                return self._buscarNodoPorValor(busqueda, nodo.ObtenerHijoIzquierdo())
            else:
                return self._buscarNodoPorValor(busqueda, nodo.ObtenerHijoDerecho())

    def buscarNodoPorValorRecorrido(self, busqueda, vehiculo, nodo, placa, horario):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorValorRecorrido(busqueda, nodo, "", 0, vehiculo, placa, 0, horario)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodoPorValorRecorrido(self, busqueda, nodo, texto, pago, vehiculo, placa, n, horario):

        if not nodo:
            return None
        if (busqueda == nodo.valor):
            if horario == "noche":
                  pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100)))
                  nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
                  money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
            elif horario == "dia":
                pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor))
                nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor)))
                money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor)))
            if nodo.ObtenerVehiculosRecorridos() == None:
                nodo.PonerVehiculosRecorridos([])
            nodo.ObtenerVehiculosRecorridos().append([placa, vehiculo, int(pago)])
            texto = texto + f"\n {nodo.llave} \n" \
                            f"valor: ${nodo.valor} \n" \
                            f"Porcentaje de vehiculo: {nodo.categoria.get(vehiculo)}% \n" \
                            f"Incremento nocturno: {nodo.incrementoNocturno}% \n" \
                            f"Pago total: {money} \n"

            n = n + 1
            lista = [texto, pago, n]
            return lista
        else:
            if (busqueda < nodo.valor):

                if horario == "noche":
                    pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100)))
                    nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
                    money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
                elif horario == "dia":
                    pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor))
                    nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor)))
                    money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor)))
                if nodo.ObtenerVehiculosRecorridos() == None:
                    nodo.PonerVehiculosRecorridos([])
                nodo.ObtenerVehiculosRecorridos().append([placa, vehiculo, int(pago)])
                texto = texto + f"\n {nodo.llave} \n " \
                                f"valor: ${nodo.valor} \n" \
                                f"Porcentaje de vehiculo: {nodo.categoria.get(vehiculo)}% \n" \
                                f"Incremento nocturno: {nodo.incrementoNocturno}% \n" \
                                f"Pago total: {money} \n" \

                n = n + 1
                return self._buscarNodoPorValorRecorrido(busqueda, nodo.ObtenerHijoIzquierdo(), texto, pago, vehiculo, placa, n, horario)
            else:

                if horario == "dia":
                    pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100)))
                    nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
                    money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100) + (nodo.valor * (nodo.incrementoNocturno / 100))))
                elif horario == "noche":
                    pago = pago + (nodo.valor * (nodo.categoria.get(vehiculo) / 100))
                    nodo.dinero = int(nodo.dinero + (nodo.valor * (nodo.categoria.get(vehiculo) / 100)))
                    money = int((nodo.valor * (nodo.categoria.get(vehiculo) / 100)))
                if nodo.ObtenerVehiculosRecorridos() == None:
                    nodo.PonerVehiculosRecorridos([])
                nodo.ObtenerVehiculosRecorridos().append([placa, vehiculo, int(pago)])
                texto = texto + f"\n {nodo.llave} \n" \
                                f"valor: ${nodo.valor} \n" \
                                f"Porcentaje de vehiculo: {nodo.categoria.get(vehiculo)}% \n" \
                                f"Incremento nocturno: {nodo.incrementoNocturno}% \n" \
                                f"Pago total: {money} \n" \

                n = n + 1
                return self._buscarNodoPorValorRecorrido(busqueda, nodo.ObtenerHijoDerecho(), texto, pago, vehiculo, placa, n, horario)

    def buscarNodoPorLlave(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorLlave(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodoPorLlave(self, busqueda, nodo):
        if (nodo):
            if (nodo.llave.upper() == busqueda.upper()):
                print("Si se encuentra la llave ", busqueda, " en el nodo con valor ", nodo.valor)
                return nodo
            return self._buscarNodoPorLlave(busqueda, nodo.ObtenerHijoIzquierdo()) or self._buscarNodoPorLlave(busqueda,
                                                                                                               nodo.ObtenerHijoDerecho())

    def EliminarNodo(self, busqueda):
        if (self.raiz):
            nodoPorEliminar = self.buscarNodoPorValor(busqueda)
            if (nodoPorEliminar):
                self._eliminarNodo(nodoPorEliminar)
        else:
            print("El árbol está vacío.")

    def _eliminarNodo(self, nodo):
        print(nodo.llave, "Es el hijo derecho de ",
              nodo.ObtenerHijoDerecho())
        print(nodo.llave, "Es el izquierdo de ", nodo.ObtenerHijoIzquierdo())
        if nodo:
            if nodo.EsNodoHoja():
                if nodo.EsHijoIzquierdo():
                    nodo.padre.PonerHijoIzquierdo(None)
                elif nodo.EsHijoDerecho():
                    nodo.padre.PonerHijoDerecho(None)
            else:
                # caso 2: tiene un solo hijo
                if (not (nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo())):

                    hijo = None
                    if (nodo.ObtenerHijoIzquierdo()):
                        print("5678")
                        hijo = nodo.ObtenerHijoIzquierdo()
                    else:
                        print(1234)
                        hijo = nodo.ObtenerHijoDerecho()
                    self.DisminuirNivel(hijo)
                    hijo.PonerPadre(nodo.padre)
                    if (nodo.EsHijoIzquierdo()):
                        print(1090)
                        nodo.padre.PonerHijoIzquierdo(hijo)
                    else:
                        print(2067)
                        nodo.padre.PonerHijoDerecho(hijo)
                    nodo.PonerHijoDerecho(None)
                    nodo.PonerPadre(None)
                else:
                    if nodo == self.raiz:

                        if nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho():
                            sucesor = nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho()
                            while sucesor.ObtenerHijoDerecho():
                                sucesor = sucesor.ObtenerHijoDerecho()
                            sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                            nodo.ObtenerHijoDerecho().PonerPadre(sucesor)
                        else:
                            nodo.ObtenerHijoIzquierdo().PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                        nodo.ObtenerHijoIzquierdo().PonerPadre(nodo.padre)
                        self.raiz = nodo.ObtenerHijoIzquierdo()
                    elif nodo.EsHijoIzquierdo():

                        nodo.padre.PonerHijoIzquierdo(None)
                        nodo.padre.PonerHijoIzquierdo(nodo.ObtenerHijoIzquierdo())
                        if nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho():
                            sucesor = nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho()
                            while sucesor.ObtenerHijoDerecho():
                                sucesor = sucesor.ObtenerHijoDerecho()
                            sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                            nodo.ObtenerHijoDerecho().PonerPadre(sucesor)
                            nodo.PonerPadre(None)
                        else:
                            nodo.ObtenerHijoIzquierdo().PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                            nodo.ObtenerHijoDerecho().PonerPadre(nodo.ObtenerHijoIzquierdo())
                        nodo.ObtenerHijoIzquierdo().PonerPadre(nodo.padre)

                    elif nodo.EsHijoDerecho():

                        nodo.padre.PonerHijoDerecho(None)
                        nodo.padre.PonerHijoDerecho(nodo.ObtenerHijoIzquierdo())
                        if nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho():
                            sucesor = nodo.ObtenerHijoIzquierdo().ObtenerHijoDerecho()
                            while sucesor.ObtenerHijoDerecho():
                                sucesor = sucesor.ObtenerHijoDerecho()
                            sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                            nodo.ObtenerHijoDerecho().PonerPadre(sucesor)
                            nodo.PonerPadre(None)
                        else:
                            nodo.ObtenerHijoIzquierdo().PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                            nodo.ObtenerHijoDerecho().PonerPadre(nodo.ObtenerHijoIzquierdo())
                        nodo.ObtenerHijoIzquierdo().PonerPadre(nodo.padre)

    def ObtenerSucesor(self, nodo):
        while (nodo.ObtenerHijoIzquierdo()):
            nodo = nodo.ObtenerHijoIzquierdo()
        return nodo

    def DisminuirNivel(self, nodo):
        if (nodo):
            nodo.nivel -= 1
            self.DisminuirNivel(nodo.ObtenerHijoIzquierdo())
            self.DisminuirNivel(nodo.ObtenerHijoDerecho())
