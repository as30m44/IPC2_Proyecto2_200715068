from Mapa_nodo import Mapa_nodo
from Mapa import Mapa


class Mapa_matriz():
  __raiz = None # Mapa_nodo()
  __finCabeceraHor = None # Mapa_nodo()
  __finCabeceraVer = None # Mapa_nodo()
  __nodoActual = None # Mapa_nodo()
  __noColumnas = 0
  __noFilas = 0
  # __noPasos = 0
  
  def __init__(self, noColumnas, noFilas):
    self.__noColumnas = noColumnas
    self.__noFilas = noFilas
    # creación de cabecera horizontal
    for i in range (0, noColumnas + 1, 1):
      mapaNuevo = Mapa()
      nodoNuevo = Mapa_nodo()
      if (i == 0):
        mapaNuevo.set_estado("raiz")
        mapaNuevo.set_posicion(0, 0)
        nodoNuevo.set_mapa(mapaNuevo)
        self.__nodoActual = nodoNuevo
        self.__finCabeceraHor = nodoNuevo
        self.__finCabeceraVer = nodoNuevo
      else:
        mapaNuevo.set_estado(str(i))
        mapaNuevo.set_posicion(i, 0)
        nodoNuevo.set_mapa(mapaNuevo)
        self.__finCabeceraHor.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(self.__finCabeceraHor)
        self.__finCabeceraHor = nodoNuevo
    # creación de las cabeceras verticales
    for j in range (1, noFilas + 1, 1):
      mapaNuevo = Mapa()
      nodoNuevo = Mapa_nodo()
      mapaNuevo.set_estado(str(j))
      mapaNuevo.set_posicion(0, j)
      nodoNuevo.set_mapa(mapaNuevo)
      self.__finCabeceraVer.set_abajo(nodoNuevo)
      nodoNuevo.set_arriba(self.__finCabeceraVer)
      self.__finCabeceraVer = nodoNuevo

  def get_noColumnas(self):
    return self.__noColumnas

  def get_noFilas(self):
    return self.__noFilas
  
  def get_mapa(self):
    return self.__nodoActual.get_mapa()

  
  def ubicarNodoActual(self, posicion_X, posicion_Y):
    if (self.estaVacio()):
      print("MATRIZ: no contiente datos del mapa")
    else:
      # ubicar el nodo actual en la raiz
      self.__nodoActual = self.__raiz
      # recorre la cabecera horizontal y halla el índice buscado
      self.__nodoActual = self.__unicarNodoAux(self.__nodoActual, posicion_X, "horizontal")
      # recorre las cabeceras verticales, desde el punto donde se quedó
      self.__nodoActual = self.__unicarNodoAux(self.__nodoActual, posicion_Y, "vertical")
  
  
  def __ubicarNodoAux(self, nodo, posicion, direccion):
    nodoPos_i = 0
    encontrado = False
    if (self.estaVacio()):
      print("MATRIZ: no contiente datos del mapa")
    else:
      if (direccion == "horizontal"):
        if (posicion <= self.__noColumnas):
          mapa = nodo.get_mapa()
          nodoPos_i = mapa.get_posicion_X()
          while (encontrado == False):
            if (nodoPos_i == posicion):
              encontrado = True
            else:
              nodoPos_i += 1
              nodo = nodo.get_derecha()
        else:
          print("MAPA: la posición indicada está fuera de los límites")
      else: # direccion == vertical
        if (posicion <= self.__noFilas):
          mapa = nodo.get_mapa()
          nodoPos_i = mapa.get_posicion_Y()
          while (encontrado == False):
            if (nodoPos_i == posicion):
              encontrado = True
            else:
              nodoPos_i += 1
              nodo = nodo.get_abajo()
        else:
          print("MAPA: la posición indicada está fuera de los límites")
    return nodo
  
  
  def estaVacio(self):
    return self.__raiz == None


  def insertar(self, mapa):
    if (self.estaVacio()):
      self.__raiz = self.__nodoActual
      self.__insertarAux(mapa)
    else:
      self.__insertarAux(mapa)


  def __insertarAux(self, mapa):
    nodoNuevo = Mapa_nodo()
    nodoNuevo.set_mapa(mapa)
    nodoPos_i = mapa.get_posicion_X()
    nodoPos_j = mapa.get_posicion_Y()
    print(nodoPos_i, nodoPos_j)
    self.__nodoActual = self.__raiz
    print(self.__nodoActual.get_derecha()==None)
    nodoVer = self.__ubicarNodoAux(self.__nodoActual, nodoPos_i, "horizontal")
    nodoHor = self.__ubicarNodoAux(self.__nodoActual, nodoPos_j, "vertical")
    nodoVerMax = None
    nodoHorMax = None
    # ______________________________________________________________________________________________
    # inserción VERTICAL
    # caso 1: para las cabeceras vacías
    if (nodoVer.get_abajo() == None):
      nodoVer.set_abajo(nodoNuevo)
      nodoNuevo.set_arriba(nodoVer)
    # caso 2: para las cabeceras con 1 o más nodos
    else:
      while (nodoVer.get_abajo() != None):
        nodoVer = nodoVer.get_abajo()
      # caso 2.1: si la posicion del último nodo es menor a la posicion del nuevo nodo
      if (nodoPos_j > nodoVer.get_mapa().get_posicion_Y()):
        nodoVer.set_abajo(nodoNuevo)
        nodoNuevo.set_arriba(nodoVer)
      # caso 2.2: si la posicion del último nodo es mayor a la posicion del nuevo nodo
      else:
        # como el nodo está en la última posición, entonces ahora debe subir
        # {a,b,d,e}, si insertamos el "nodo c", encontramos el "nodo b" y "nodo d"
        while (nodoPos_j < nodoVer.get_mapa().get_posicion_Y()):
          nodoVerMax = nodoVer # nodo d
          nodoVer = nodoVer.get_arriba() # nodo b
        nodoVer.set_abajo(nodoNuevo)
        nodoNuevo.set_arriba(nodoVer)
        nodoVerMax.set_arriba(nodoNuevo)
        nodoNuevo.set_abajo(nodoVerMax)
    # ______________________________________________________________________________________________
    # inserción HORIZONTAL
    # caso 1: para las cabeceras vacías
    if (nodoHor.get_derecha() == None):
      nodoHor.set_derecha(nodoNuevo)
      nodoNuevo.set_izquierda(nodoHor)
    # caso 2: para las cabeceras con 1 o más nodos
    else:
      while (nodoHor.get_derecha() != None):
        nodoHor = nodoHor.get_derecha()
      # caso 2.1: si la posicion del último nodo es menor a la posicion del nuevo nodo
      if (nodoPos_i > nodoHor.get_mapa().get_posicion_X()):
        nodoHor.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(nodoHor)
      # caso 2.2: si la posicion del último nodo es mayor a la posicion del nuevo nodo
      else:
        # como el nodo está en la última posición, entonces ahora debe subir
        # {a,b,d,e}, si insertamos el "nodo c", encontramos el "nodo b" y "nodo d"
        while (nodoPos_i < nodoHor.get_mapa().get_posicion_X()):
          nodoHorMax = nodoHor # nodo d
          nodoHor = nodoHor.get_arriba() # nodo b
        nodoHor.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(nodoHor)
        nodoHorMax.set_izquierda(nodoNuevo)
        nodoNuevo.set_derecha(nodoHorMax)

  
  def imprimir(self):
    if (self.estaVacio()):
      print("MAPA: la matriz está vacía")
    else:
      self.__nodoActual = self.__raiz
      # lectura de fila
      for j in range (0, self.__noFilas + 1, 1):
        nodo = self.__nodoActual # .get_derecha() # pasa a la siguiente columna
        fila = ""
        # lectura de columnas
        for i in range (0, self.__noColumnas + 1, 1):
          fila += nodo.imprimir("celda") # concatena cada celda horizontal
          nodo = nodo.get_derecha()
        print(fila)
        self.__nodoActual = self.__nodoActual.get_abajo() # pasa a la siguiente fila
