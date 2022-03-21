from Mapa_nodo import Mapa_nodo
from Mapa import Mapa



class Mapa_Matriz():
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
        self.__raiz = nodoNuevo
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
    for j in range (0, noFilas, 1):
      mapaNuevo = Mapa()
      nodoNuevo = Mapa_nodo()
      mapaNuevo.set_estado(str(j))
      mapaNuevo.set_posicion(0, j)
      nodoNuevo.set_mapa(mapaNuevo)
      self.__finCabeceraVer.set_abajo(nodoNuevo)
      nodoNuevo.set_arriba(self.__finCabeceraVer)
      self.__finCabeceraVer = nodoNuevo
  
  
  def ubicarNodoActual(self, posicion_X, posicion_Y):
    if (self.estaVacio()):
      print("MATRIZ: no contiente datos del mapa")
    else:
      # ubicar el nodo actual en la raiz
      self.__nodoActual = self.__raiz
      # recorre la cabecera horizontal y halla el índice buscado
      self.__nodoActual = self.__ubicarNodoActualCab(self.__nodoActual, posicion_X, "horizontal")
      # recorre las cabeceras verticales, desde el punto donde se quedó
      self.__nodoActual = self.__ubicarNodoActualCab(self.__nodoActual, posicion_Y, "vertical")
  
  
  def __ubicarNodo(self, nodo, posicion, direccion):
    nodoPos_i = 0
    encontrado = False
    if (self.estaVacio()):
      print("MATRIZ: no contiente datos del mapa")
    else:
      while (encontrado == False and nodo != None):
        mapaTemp = nodo.get_mapa()
        if (direccion == "horizontal"):
          nodoPos_i = mapaTemp.get_posicion_X()
        else: # direccion vertical
          nodoPos_i = mapaTemp.get_posicion_Y()
        if (nodoPos_i == posicion):
          encontrado = True
        else:
          if (direccion == "horizontal"):
            nodo = nodo.get_derecha()
          else: # direccion vertical
            nodo = nodo.get_abajo()
      return nodo
  
  
  def estaVacio(self):
    return self.__raiz == None


  def insertar(self, mapa):
    nodoNuevo = Mapa_nodo()
    nodoPos_i = mapa.get_posicion_X()
    nodoPos_j = mapa.get_posicion_Y()
    nodoNuevo.set_mapa(mapa)
    nodoTemp_i = None
    nodoTemp_ii = None
    nodoTemp_j = None
    nodoTemp_jj = None
    # ubicar al nodo actual en la raiz
    self.__nodoActual = self.__raiz
    # **********************************************************************************************
    # caso 1: para nodos en la última columna
    if (nodoPos_i == self.__noColumnas):
      # ............................................................................................
      # caso 1.1: ENLACES de nodo en la esquina inferior derecha, solo columna
      if (nodoPos_j == self.__noFilas):
        # mover el nodo temporal a la última cabecera horizontal
        nodoTemp_j = self.__ubicarNodo(self.__nodoActual, nodoPos_i, "horizontal")
        # baja y busca el último nodo de la columna
        while (nodoTemp_j.get_abajo() != None):
          nodoTemp_j = nodoTemp_j.get_abajo()
        # conecta los nodos
        nodoTemp_j.set_abajo(nodoNuevo)
        nodoNuevo.set_arriba(nodoTemp_j)
      # ............................................................................................
      # caso 1.2: ENLACES de nodo en la última columna entre dos nodos, solo columna
      else:
        # mover el nodo temporal 2 a la última cabecera horizontal
        nodoTemp_jj = self.__ubicarNodo(self.__nodoActual, nodoPos_i, "horizontal")
        # busca el nodo con primer id mayor a m de la columna
        while (nodoPos_j < nodoTemp_jj.get_mapa().get_posicion_Y):
          nodoTemp_jj = nodoTemp_jj.get_abajo()
        # selecciona el nodo con el último id menor a m de la columna
        nodoTemp_j = nodoTemp_jj.get_arriba()
        # conecta los nodos
        nodoTemp_j.set_abajo(nodoNuevo)
        nodoNuevo.set_arriba(nodoTemp_j)
        nodoNuevo.set_abajo(nodoTemp_jj)
        nodoTemp_jj.set_arriba(nodoNuevo)
      # ............................................................................................
      # ENLACES de nodo, para ambos casos, solo fila
      # mover el nodo temporal a la cabecera m vertical
      nodoTemp_i = self.__ubicarNodo(self.__nodoActual, nodoPos_j, "vertical")
      # se mueve a la derecha y busca el último nodo de la fila
      while (nodoTemp_i.get_derecha() != None):
        nodoTemp_i = nodoTemp_i.get_derecha()
      # conecta los nodos
      nodoTemp_i.set_derecha(nodoNuevo)
      nodoNuevo.set_izquierda(nodoTemp_i)
    # **********************************************************************************************
    # caso 2: para nodos antes de la última columna
    else:
      # ............................................................................................
      # caso 2.1: ENLACES de nodo en la última fila entre dos nodos, solo fila
      if (nodoPos_j == self.__noFilas):
        # mover el nodo temporal 2 a la última cabecera vertical
        nodoTemp_ii = self.__ubicarNodo(self.__nodoActual, nodoPos_j, "vertical")
        # busca el nodo con primer id mayor a m de la fila
        while (nodoPos_i < nodoTemp_ii.get_mapa().get_posicion_X):
          nodoTemp_ii = nodoTemp_ii.get_derecha()
        # selecciona el nodo con el último id menor a m de la fila
        nodoTemp_i = nodoTemp_ii.get_izquierda()
        # conecta los nodos
        nodoTemp_i.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(nodoTemp_i)
        nodoNuevo.set_derecha(nodoTemp_ii)
        nodoTemp_ii.set_izquierda(nodoNuevo)
        # ENLACES de nodo, solo columna
        # mover el nodo temporal a la cabecera m horizontal
        nodoTemp_j = self.__ubicarNodo(self.__nodoActual, nodoPos_i, "horizontal")
        # se mueve a la derecha y busca el último nodo de la fila
        while (nodoTemp_j.get_abajo() != None):
          nodoTemp_j = nodoTemp_j.get_abajo()
        # conecta los nodos
        nodoTemp_j.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(nodoTemp_j)
      # ............................................................................................
      # caso 2.2: ENLACES de nodo en el centro de la matriz
      else:
        # mover el nodo temporal 2 a la cabecera m horizontal
        nodoTemp_jj = self.__ubicarNodo(self.__nodoActual, nodoPos_i, "horizontal")
        # busca el nodo con primer id mayor a m de la columna
        while (nodoPos_j < nodoTemp_jj.get_mapa().get_posicion_Y):
          nodoTemp_jj = nodoTemp_jj.get_abajo()
        # selecciona el nodo con el último id menor a m de la columna
        nodoTemp_j = nodoTemp_jj.get_arriba()
        # conecta los nodos
        nodoTemp_j.set_abajo(nodoNuevo)
        nodoNuevo.set_arriba(nodoTemp_j)
        nodoNuevo.set_abajo(nodoTemp_jj)
        nodoTemp_jj.set_arriba(nodoNuevo)
      # ............................................................................................
        # mover el nodo temporal 2 a la cabecera m vertical
        nodoTemp_ii = self.__ubicarNodo(self.__nodoActual, nodoPos_j, "vertical")
        # busca el nodo con primer id mayor a m de la fila
        while (nodoPos_i < nodoTemp_ii.get_mapa().get_posicion_X):
          nodoTemp_ii = nodoTemp_ii.get_derecha()
        # selecciona el nodo con el último id menor a m de la fila
        nodoTemp_i = nodoTemp_ii.get_izquierda()
        # conecta los nodos
        nodoTemp_i.set_derecha(nodoNuevo)
        nodoNuevo.set_izquierda(nodoTemp_i)
        nodoNuevo.set_derecha(nodoTemp_ii)
        nodoTemp_ii.set_izquierda(nodoNuevo)
  
  
  def imprimir(self):
    self.__nodoActual = self.__raiz.get_abajo()
    nodo_m = self.__nodoActual.get_derecha()
    fila = ""
    # cambia de fila
    for j in range (0, self.__noFilas, 1):
      # concatena el contenido de cada celda en la fila k
      for i in range (0, self.__noColumnas, 1):
        nodoPos_i = nodo_m.get_mapa().get_posicion_X()
        # caso 1: para las celdas con información
        if (i == nodoPos_i):
          fila += nodo_m.imprimir()
          nodo_m = nodo_m.get_derecha()
        # caso 2: para las celdas vacías
        else:
          fila += "█"
      print(fila)
       # pasa a la siguiente fila
      self.__nodoActual = self.__nodoActual.get_abajo()
      nodo_m = self.__nodoActual.get_derecha()
