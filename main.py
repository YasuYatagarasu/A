import json
from tkinter import *

from arbol import *

abb = ArbolBinario()
nombreslista = []
vehiculosLista= []
pagoTotal = []
categorias = []

def cargar_datos(ruta):
    with open(ruta) as contenido:
        arbolito = json.load(contenido)
        for arbolote in arbolito:
            nombreslista.append(arbolote.get('nombre'))
            abb.AgregarNodo(arbolote.get('nombre'), arbolote.get('valor'), arbolote.get('categoria'),
                            arbolote.get('valorBaseIzq'), arbolote.get('valorBaseDer'), arbolote.get('incrementeNocturno'))
            print(arbolote.get('nombre'), arbolote.get('valor'), arbolote.get('color'))


ruta = 'arbol.json'
cargar_datos(ruta)
ruta2 = 'categoria.json'
with open(ruta2) as contenido:
    cate = json.load(contenido)
    for arbolote in cate:
        print(arbolote.get("color"))
        categorias.append(arbolote)

raizTk = Tk()
raizTk.title("Carreteras")
raizTk.config(bg="Green")
##raizTk.attributes('-toolwindow', True)
raizTk.geometry("1150x650+0+0")
raizTk.resizable(False, False)

miImagen2 = PhotoImage(file="peaje.png")

Label(raizTk, image=miImagen2).pack(fill="both", expand="True")

label = Label(raizTk, text="Rutas de Colombia", font=("courier", 28, "bold"), bg="#D9FA6A").place(x=100, y=45)
##raizTk.wm_attributes('-transparentcolor','white')

def CrearFrameArbol():
      FrameArbol = Canvas()
      FrameArbol.config(bg="#D9FA6A") ##relief="groove"
      FrameArbol.pack()
      FrameArbol.config(width="950", height="500")
      FrameArbol.place(x=5, y=135)
      return FrameArbol

FrameA = CrearFrameArbol()

def BotonPeaje(nodo):
    print(f"se presiono {nodo.llave}")
    raizPeaje = Tk()
    raizPeaje.title(nodo.llave)
    if nodo.creador != None:
       raizPeaje.geometry("322x239")
    else:
        raizPeaje.geometry("322x199")
    raizPeaje.resizable(False, False)

    def modificar():
        b= True
        if nodo.EsHijoDerecho() and cuadroValor.get().isdigit():

            if int(cuadroValor.get()) < nodo.padre.valor:
                b = False
        elif nodo.EsHijoIzquierdo() and cuadroValor.get().isdigit():
            if int(cuadroValor.get()) > nodo.padre.valor:
                b = False

        if nodo.ObtenerHijoIzquierdo() and nodo.ObtenerHijoIzquierdo().valor > int(cuadroValor.get()):
            b = False

        if nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoDerecho().valor < int(cuadroValor.get()):
            b = False

        if cuadroValor.get().isdigit() and cuadroIncrementoNoct.get().isdigit() and b:
            nuevoNombre = cuadroNombre.get()
            nombreslista.remove(nodo.llave)
            nombreslista.append(nuevoNombre)
            nodo.PonerLlave(nuevoNombre)
            print(f"Nuevo nombre {nodo.llave}")

            nuevoColor = colore.get()
            if nuevoColor == "blue":
               nuevoColor = categorias[0]
            elif nuevoColor == "red":
               nuevoColor = categorias[1]
            elif nuevoColor == "green":
               nuevoColor = categorias[2]
            elif nuevoColor == "purple":
               nuevoColor = categorias[3]
            nodo.PonerCategoria(nuevoColor)
            print(f"Nuevo color {nodo.categoria}")

            nuevoValor = cuadroValor.get()
            nuevoValor = int(nuevoValor)
            nodo.PonerValor(nuevoValor)
            print(f"Nuevo Valor Base {nodo.valor}")

            nuevoIncrementoNocturno = cuadroIncrementoNoct.get()
            nuevoIncrementoNocturno = int(nuevoIncrementoNocturno)
            nodo.PonerIncrementoNocturno(nuevoIncrementoNocturno)
            print(f"Nuevo incremento nocturno {nodo.incrementoNocturno}")

            ##FrameA.destroy()
            FrameArbol = CrearFrameArbol()
            ComponerArbol(FrameArbol, abb.raiz, 502, 30)
            CrearRecorrido()
            raizPeaje.destroy()
        else:
            raiz = Tk()
            raiz.title("Error")
            raiz.geometry("226x83")
            raiz.resizable(False, False)

            Label(raiz, text="Ingrese valores validos").place(x=50, y=30)

    def registro():
        raizRegistro = Tk()
        raizRegistro.title(f"Resgistro de {nodo.llave}")
        raizRegistro.geometry("322x699")
        raizRegistro.resizable(False, False)

        Label(raizRegistro, text="Registro de Vehiculos: ", font=('courier', 10)).grid(row=0, column=0)

        Label(raizRegistro, text="", font=('courier', 10)).grid(row=1, column=0)

        i = 2
        if nodo.ObtenerVehiculosRecorridos() != None:
            for pm in nodo.ObtenerVehiculosRecorridos():
               print(f"Numero {i}")
               Label(raizRegistro, text=f"Placa del Vehiculo: {pm[0]}\n"
                                        f"Tipo de Vehiculo: {pm[1]}\n"
                                        f"El total a pagar en el viaje es: \n ${pm[2]}").grid(row=i, column=0)
               i = i + 1
        else:
            Label(raizRegistro, text="Ningun vehiculo ha pasado por aquí").grid(row=2, column=0)

    ##FramePeajeModificar=Frame(raizPeaje, width=250, height=250)
    ##FramePeajeModificar.pack()

    n = 0

    if nodo.creador != None:
        creadorLabel = Label(raizPeaje, text=f"Peaje creado por: {nodo.creador}")
        creadorLabel.grid(row=n, column=1, sticky="e", padx=5, pady=5)
        n = n + 1

    NombreLabel = Label(raizPeaje, text="Nombre: ")
    NombreLabel.grid(row=n, column=0, sticky="w", padx=10, pady=10)
    cuadroNombre = Entry(raizPeaje)
    cuadroNombre.grid(row=n, column=1)
    cuadroNombre.config(justify="right")
    cuadroNombre.insert(0, nodo.llave)
    n = n + 1


    ColorLabel = Label(raizPeaje, text="Color: ")
    ColorLabel.grid(row=n, column=0, sticky="w", padx=10, pady=10)
    Colores = ["blue", "red", "purple", "green"]
    colore = StringVar()
    colore.set(nodo.categoria.get('color'))
    cuadroColor = OptionMenu(raizPeaje, colore, *Colores)
    cuadroColor.config(width=15, height=1)
    cuadroColor.grid(row=n, column=1)
    n = n + 1
    ##cuadroColor.insert(0, nodo.color)

    ValorLabel = Label(raizPeaje, text="Valor Base: ")
    ValorLabel.grid(row=n, column=0, sticky="w", padx=10, pady=10)
    cuadroValor = Entry(raizPeaje)
    cuadroValor.grid(row=n, column=1)
    cuadroValor.config(justify="right")
    cuadroValor.insert(0, nodo.valor)
    n = n + 1

    IncrementoNoctLabel = Label(raizPeaje, text="Incremento Nocturno(%): ")
    IncrementoNoctLabel.grid(row=n, column=0, sticky="w", padx=10, pady=10)
    cuadroIncrementoNoct = Entry(raizPeaje)
    cuadroIncrementoNoct.grid(row=n, column=1)
    cuadroIncrementoNoct.config(justify="right")
    cuadroIncrementoNoct.insert(0, nodo.incrementoNocturno)
    n = n + 1

    Label(raizPeaje, text=f"Cantidad de dinero acumulado: \n${nodo.dinero}").grid(row=n, column=0, sticky="e")

    Button(raizPeaje, text="Modificar", command=modificar).grid(row=n, column=1, sticky="w")
    Button(raizPeaje, text="Registro", command=registro).grid(row=n, column=1, sticky="e")

def ComponerArbol(Frame, nodo, h, w):
    if (nodo):
        def a():
            BotonPeaje(nodo)
        Button(Frame, text=f"{nodo.llave}\n"
                           f"(${nodo.valor})", font=('courier', 8),fg="white", bg=nodo.categoria.get('color'), command=a).place(x=h-35, y=w)
        if nodo.ObtenerNivel() < 2:
            if (nodo.ObtenerHijoDerecho() != None):
                Frame.create_line(h+255, w+30, h, w)
            if(nodo.ObtenerHijoIzquierdo() != None):
                Frame.create_line(h-255, w+30, h, w)
            ComponerArbol(Frame, nodo.ObtenerHijoIzquierdo(), h - 255, w + 30)
            ComponerArbol(Frame, nodo.ObtenerHijoDerecho(), h + 255, w + 30)
        elif nodo.ObtenerNivel() < 3:
            if (nodo.ObtenerHijoDerecho() != None):
                Frame.create_line(h+90, w+60, h, w)
            if(nodo.ObtenerHijoIzquierdo() != None):
                Frame.create_line(h-90, w+60, h, w)
            ComponerArbol(Frame, nodo.ObtenerHijoIzquierdo(), h - 90, w + 60)
            ComponerArbol(Frame, nodo.ObtenerHijoDerecho(), h + 90, w + 60)
        else:
            if (nodo.ObtenerHijoDerecho() != None):
                Frame.create_line(h + 60, w + 60, h, w)
            if (nodo.ObtenerHijoIzquierdo() != None):
                Frame.create_line(h - 60, w + 60, h, w)
            ComponerArbol(Frame, nodo.ObtenerHijoIzquierdo(), h - 60, w + 60)
            ComponerArbol(Frame, nodo.ObtenerHijoDerecho(), h + 60, w + 60)
        return


def crearPeaje():

    def crear():
        if cuadroValor.get().isdigit() and cuadroIncrementoNoct.get().isdigit():
           nombre = cuadroNombre.get()
           nuevoColor = colore.get()
           if nuevoColor == "blue":
               nuevoColor = categorias[0]
           elif nuevoColor == "red":
               nuevoColor = categorias[1]
           elif nuevoColor == "green":
               nuevoColor = categorias[2]
           elif nuevoColor == "purple":
               nuevoColor = categorias[3]
           print(categorias)
           abb.AgregarNodo(cuadroNombre.get(), int(cuadroValor.get()), nuevoColor, 0, 0, int(cuadroIncrementoNoct.get()))
           nodo = abb.buscarNodoPorLlave(cuadroNombre.get())
           nodo.PonerCreador(CuadroCreador.get())
           FrameArbol = CrearFrameArbol()
           ComponerArbol(FrameArbol, abb.raiz, 502, 30)
           raizPeaje.destroy()
           nombreslista.append(nombre)
           CrearRecorrido()
        else:
            raiz = Tk()
            raiz.title("Error")
            raiz.geometry("226x83")
            raiz.resizable(False, False)

            Label(raiz, text="Ingrese valores validos").place(x=50, y=30)

    raizPeaje = Tk()
    raizPeaje.title("Crear peaje")
    raizPeaje.geometry("310x235")
    raizPeaje.resizable(False, False)

    NombreLabel = Label(raizPeaje, text="Nombre: ")
    NombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    cuadroNombre = Entry(raizPeaje)
    cuadroNombre.grid(row=0, column=1)
    cuadroNombre.config(justify="right")


    ColorLabel = Label(raizPeaje, text="Color: ")
    ColorLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    Colores = ["blue", "red", "purple", "green"]
    colore = StringVar()
    cuadroColor = OptionMenu(raizPeaje, colore, *Colores)
    cuadroColor.config(width=15, height=1)
    cuadroColor.grid(row=1, column=1)
    ##cuadroColor.insert(0, nodo.color)

    ValorLabel = Label(raizPeaje, text="Valor Base: ")
    ValorLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    cuadroValor = Entry(raizPeaje)
    cuadroValor.grid(row=2, column=1)
    cuadroValor.config(justify="right")

    IncrementoNoctLabel = Label(raizPeaje, text="Incremento Nocturno(%): ")
    IncrementoNoctLabel.grid(row=5, column=0, sticky="w", padx=10, pady=10)
    cuadroIncrementoNoct = Entry(raizPeaje)
    cuadroIncrementoNoct.grid(row=5, column=1)
    cuadroIncrementoNoct.config(justify="right")

    creadorLabel = Label(raizPeaje, text="Creador: ")
    creadorLabel.grid(row=6, column=0, sticky="w", padx=10, pady=10)
    CuadroCreador = Entry(raizPeaje)
    CuadroCreador.grid(row=6, column=1)
    CuadroCreador.config(justify="right")

    Button(raizPeaje, text="Crear Peaje", command=crear).grid(row=7, column=1, sticky="e")

def cambiarPeaje():

    def cambiar():
        nodo = abb.buscarNodoPorLlave(nombre.get())
        nodoB = abb.buscarNodoPorLlave(nombre2.get())

        if ((nodo.valor > abb.raiz.valor and nodoB.valor > abb.raiz.valor) or (nodo.valor < abb.raiz.valor and nodoB.valor < abb.raiz.valor)):
            b = True
        else:
            b = False

        if nodo.valor > nodoB.valor and nodoB.EsHijoIzquierdo() and nodoB.valor != abb.raiz.valor:
            if nodo.valor > nodoB.padre.valor:
                b = False

        if nodo.valor < nodoB.valor and nodoB.EsHijoDerecho() and nodoB.valor != abb.raiz.valor:
            if nodo.valor < nodoB.padre.valor:
                b = False


        if nodoB.valor == abb.raiz.valor:
                b = True

        if nodo.valor > nodoB.valor and b:
            abb.EliminarNodo(nodo.valor)
            nodo.PonerHijoDerecho(None)
            nodo.PonerHijoIzquierdo(None)
            if nodoB.ObtenerHijoDerecho():
                if nodoB.ObtenerHijoDerecho().valor > nodo.valor:
                    nodo.PonerHijoDerecho(nodoB.ObtenerHijoDerecho())
                    nodoB.ObtenerHijoDerecho().PonerPadre(nodo)
                elif nodoB.ObtenerHijoDerecho().valor < nodo.valor:
                    nodo.PonerHijoIzquierdo(nodoB.ObtenerHijoDerecho())
                    nodoB.ObtenerHijoDerecho().PonerPadre(nodo)
            nodoB.PonerHijoDerecho(nodo)
            nodo.PonerPadre(nodoB)
            FrameArbol = CrearFrameArbol()
            ComponerArbol(FrameArbol, abb.raiz, 502, 30)
            CrearRecorrido()
            raizEliminar.destroy()

        elif nodo.valor < nodoB.valor and b:
            abb.EliminarNodo(nodo.valor)
            nodo.PonerHijoDerecho(None)
            nodo.PonerHijoIzquierdo(None)
            if nodoB.ObtenerHijoIzquierdo().valor > nodo.valor:
                nodo.PonerHijoDerecho(nodoB.ObtenerHijoIzquierdo())
                nodoB.ObtenerHijoIzquierdo().PonerPadre(nodo)
            elif nodoB.ObtenerHijoIzquierdo().valor < nodo.valor:
                nodo.PonerHijoIzquierdo(nodoB.ObtenerHijoIzquierdo())
                nodoB.ObtenerHijoIzquierdo().PonerPadre(nodo)
            nodoB.PonerHijoIzquierdo(nodo)
            nodo.PonerPadre(nodoB)
            FrameArbol = CrearFrameArbol()
            ComponerArbol(FrameArbol, abb.raiz, 502, 30)
            CrearRecorrido()
            raizEliminar.destroy()
        else:
            raiz = Tk()
            raiz.title("Error")
            raiz.geometry("296x100")
            raiz.resizable(False, False)

            Label(raiz, text="No es posible ubicar el peaje aquí").place(x=50, y=30)

    raizEliminar = Tk()
    raizEliminar.title("Cambiar Peaje")
    raizEliminar.geometry("314x206")
    raizEliminar.resizable(False, False)

    NombreLabel = Label(raizEliminar, text="Seleccione el peaje que desea cambiar: ")
    NombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    nombreslista
    nombre = StringVar()
    cuadroNombre = OptionMenu(raizEliminar, nombre, *nombreslista)
    cuadroNombre.grid(row=1, column=0)
    cuadroNombre.config(width=25, height=1)
    cuadroNombre.config(justify="right")

    NombreLabel2 = Label(raizEliminar, text="Seleccione el peaje que donde desea porner el peaje: ")
    NombreLabel2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    nombreslista
    nombre2 = StringVar()
    cuadroNombre2 = OptionMenu(raizEliminar, nombre2, *nombreslista)
    cuadroNombre2.grid(row=3, column=0)
    cuadroNombre2.config(width=25, height=1)
    cuadroNombre2.config(justify="right")

    Label(raizEliminar, text="").grid(row=4, column=0, sticky="e")

    Button(raizEliminar, text="Cambiar ruta de peaje", command=cambiar).grid(row=5, column=0, sticky="e")

def eliminarPeaje():

    def eliminar():
        nodoAEliminar = abb.buscarNodoPorLlave(nombre.get())
        ##print(nodoAEliminar.llave, nodoAEliminar.padre.llave, nodoAEliminar.ObtenerHijoIzquierdo().llave, nodoAEliminar.ObtenerHijoDerecho().llave)
        abb._eliminarNodo(nodoAEliminar)
        FrameArbol = CrearFrameArbol()
        ComponerArbol(FrameArbol, abb.raiz, 502, 30)
        raizEliminar.destroy()
        nombreslista.remove(nombre.get())
        CrearRecorrido()


    raizEliminar = Tk()
    raizEliminar.title("Eliminar Peaje")
    raizEliminar.geometry("254x126")
    raizEliminar.resizable(False, False)

    NombreLabel = Label(raizEliminar, text="Seleccione el peaje que desea eliminar: ")
    NombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    nombreslista
    nombre = StringVar()
    nombre.set(nombreslista[0])
    cuadroNombre = OptionMenu(raizEliminar, nombre, *nombreslista)
    cuadroNombre.grid(row=1, column=0)
    cuadroNombre.config(width=25, height=1)
    cuadroNombre.config(justify="right")

    Label(raizEliminar, text=" ").grid(row=2, column=0, sticky="e")

    Button(raizEliminar, text="Eliminar Peaje", command=eliminar).grid(row=3, column=0, sticky="e")

def estadisticas():
    pagoMayor = ["", 0, "", 0]
    pagoMenor = ["", 10000000000000000000000, "", 0]
    masRecorrido = ["", 0, "", 0]

    for pm in vehiculosLista:
        if pagoMayor[1] < pm[1]:
           pagoMayor = pm
        if pagoMenor[1] > pm[1]:
            pagoMenor = pm
        if masRecorrido[3] < pm[3]:
            masRecorrido = pm

    pagoTotalA = 0
    for pm in pagoTotal:
        pagoTotalA = pagoTotalA + pm

    if pagoMenor[1] != 0 and pagoMayor[1] !=0:
        raizEstadistica = Tk()
        raizEstadistica.title("Registro")
        raizEstadistica.geometry("354x323")
        raizEstadistica.resizable(False, False)

        Label(raizEstadistica, text="Registro de Vehiculos: ", font=('courier', 10)).grid(row=0, column=0)

        Label(raizEstadistica, text="", font=('courier', 10)).grid(row=1, column=0)

        Label(raizEstadistica, text="El vehiculo que más pagó fue: ").grid(row=2, column=0)
        Label(raizEstadistica, text=f"Placa: {pagoMayor[0]}\n"
                                    f"Tipo de vehiculo: {pagoMayor[2]}\n"
                                    f"Valor que pago: ${pagoMayor[1]}").grid(row=2, column=1)

        Label(raizEstadistica, text="", font=('courier', 10)).grid(row=3, column=0)

        Label(raizEstadistica, text="El vehiculo que menos pagó fue: ").grid(row=4, column=0)
        Label(raizEstadistica, text=f"Placa: {pagoMenor[0]}\n"
                                    f"Tipo de vehiculo: {pagoMenor[2]}\n"
                                    f"Valor que pago: ${pagoMenor[1]}").grid(row=4, column=1)

        Label(raizEstadistica, text="", font=('courier', 10)).grid(row=5, column=0)

        Label(raizEstadistica, text="El vehiculo que más peajes\n recorrio fue: ").grid(row=6, column=0)
        Label(raizEstadistica, text=f"Placa: {masRecorrido[0]}\n"
                                    f"Tipo de vehiculo: {masRecorrido[2]}\n"
                                    f"Peajes recorridos: {masRecorrido[3]}").grid(row=6, column=1)

        Label(raizEstadistica, text="", font=('courier', 10)).grid(row=7, column=0)
        Label(raizEstadistica, text="", font=('courier', 10)).grid(row=8, column=0)

        Label(raizEstadistica, text="Total de dinero recogido fue: ").grid(row=9, column=0)
        Label(raizEstadistica, text=f"${pagoTotalA}").grid(row=9, column=1)

    else:
        raiz = Tk()
        raiz.title("Error")
        raiz.geometry("400x100")
        raiz.resizable(False, False)

        Label(raiz, text="Ningun vehiculo ha hecho un recorrido.").place(x=50, y=30)


Button(raizTk, text="Crear Nuevo Peaje", font=('courier', 10), fg="black", command=crearPeaje).place(x=385, y=100)
Button(raizTk, text="Cambiar Posición", font=('courier', 10), fg="black", command=cambiarPeaje).place(x=540, y=100)
Button(raizTk, text="Eliminar Peaje", font=('courier', 10), fg="black", command=eliminarPeaje).place(x=687, y=100)
Button(raizTk, text="Ver Estadisticas", font=('courier', 10), fg="black", command=estadisticas).place(x=820, y=100)

def CrearRecorrido():

    def viajar():
        if cuadroPlaca.get() != "":
            nodoInicio = abb.buscarNodoPorLlave(nombre.get())
            nodoBuscar = abb.buscarNodoPorLlave(nombre2.get())
            texto = abb.buscarNodoPorValorRecorrido(nodoBuscar.valor, (vehiculo.get()).lower(), nodoInicio, cuadroPlaca.get(), (nombrea.get()).lower())

            pago = texto[1]
            pagoTotal.append(pago)

            print(abb.raiz.ObtenerVehiculosRecorridos())

            n = texto[2]

            vehiculor = [cuadroPlaca.get(), pago, vehiculo.get(), n]
            vehiculosLista.append(vehiculor)

            raizViaje = Tk()
            raizViaje.geometry("350x650")
            FrameB = Canvas(raizViaje)
            Label(FrameB, text=texto[0]).grid(row=0, column=1, sticky="w")
            Label(FrameB, text=f"Placa del Vehiculo: {cuadroPlaca.get()}\n\n"
                                  f"Tipo de Vehiculo: {vehiculo.get()}\n\n"
                                  f"El total a pagar en el viaje es: \n ${pago}").grid(row=0, column=2)
            FrameB.pack(side=RIGHT)
            FrameB.config(width="950", height="500")
            scrollbar = Scrollbar(raizViaje, command=FrameB.yview)
            FrameB.config(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=LEFT, fill='y')

        else:
            raiz = Tk()
            raiz.title("Error")
            raiz.geometry("400x100")
            raiz.resizable(False, False)

            Label(raiz, text="Se debe ingresar la placa del vehiculo para hacer el viaje").place(x=50, y=30)

    FrameRecorrido = Frame()
    FrameRecorrido.config(bg="#D9FA6A")  ##relief="groove"
    FrameRecorrido.pack()

    Label(FrameRecorrido, text="Vehiculo: ", bg='#D9FA6A', font='courier').place(x=0, y=5)
    vehiculos = ["Camion", "Bus", "Camioneta", "Automovil", "Motocicleta", "Mototaxi"]
    vehiculo = StringVar()
    vehiculo.set(vehiculos[0])
    cuadroVehiculo = OptionMenu(FrameRecorrido, vehiculo, *vehiculos)
    cuadroVehiculo.place(x=10, y=30)
    cuadroVehiculo.config(width=15, height=1)
    cuadroVehiculo.config(justify="right")

    Label(FrameRecorrido, text="Ingrese la placa \n del vehiculo: ", bg='#D9FA6A', font='courier').place(x=0, y=70)
    cuadroPlaca = Entry(FrameRecorrido)
    cuadroPlaca.place(x=10, y=110)
    cuadroPlaca.config(justify="right")

    Label(FrameRecorrido, text="Punto de partida: ", bg='#D9FA6A', font='courier').place(x=0, y=135)
    nombre = StringVar()
    nombre.set(nombreslista[0])
    cuadroNombre = OptionMenu(FrameRecorrido, nombre, *nombreslista)
    cuadroNombre.place(x=10, y=160)
    cuadroNombre.config(width=15, height=1)
    cuadroNombre.config(justify="right")

    Label(FrameRecorrido, text="Destino: ", bg='#D9FA6A', font='courier').place(x=0, y=200)
    nombre2 = StringVar()
    nombre2.set(nombreslista[0])
    cuadroNombre2 = OptionMenu(FrameRecorrido, nombre2, *nombreslista)
    cuadroNombre2.place(x=10, y=225)
    cuadroNombre2.config(width=15, height=1)
    cuadroNombre2.config(justify="right")

    Label(FrameRecorrido, text="Horario: ", bg='#D9FA6A', font='courier').place(x=0, y=265)
    nombrea = StringVar()
    aas = ["Dia", "Noche"]
    nombrea.set(aas[0])
    cuadroHorario = OptionMenu(FrameRecorrido, nombrea, *aas)
    cuadroHorario.place(x=10, y=290)
    cuadroHorario.config(width=15, height=1)
    cuadroHorario.config(justify="right")

    Button(FrameRecorrido, text="Viajar", command=viajar).place(x=130, y=335)

    FrameRecorrido.config(width="181", height="370")
    FrameRecorrido.place(x=965, y=135)

ComponerArbol(FrameA, abb.raiz, 502, 30)
CrearRecorrido()

raizTk.mainloop()


