from Celda import Celda
from Celda_nodoes import Celda_nodoES


class Celda_listaES():
  __nodoInicio = None # Celda_nodoES()
  __nodoFinal = None # Celda_nodoES()
  __nodoActual = None # Celda_nodoES()
  __noCeldas = 0

  def __init__(self):
    pass

  def get_noCeldas(self):
    return self.__noCeldas

  def get_celda(self):
    return self.__nodoActual.get_celda()


  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None


  def insertar(self, celda):
    celda.set_idCelda(self.__noCeldas + 1)
    nodoNuevo = Celda_nodoES()
    nodoNuevo.set_celda(celda)
    # Caso 1: cuando la lista está vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__noCeldas = 1
    # Caso 2: cuando la lista tiene m elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noCeldas += 1
  

  def ubicar(self, idCelda):
    self.__nodoActual = self.__nodoInicio
    nodoPos_i = 1
    encontrado = False
    if (self.__nodoActual == None):
      print("CELDA: la lista está vacía")
    else:
      # caso 1: el id se encuentra dentro de la lista
      if (idCelda <= self.__noCeldas):
        while (encontrado == False):
          if (nodoPos_i == idCelda):
            encontrado = True
          else:
            nodoPos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      # caso 2: el id no está en la lista
      else:
        print("CELDA: no se encuentra el item que ha ingresado")


  def imprimir(self):
    if(self.estaVacio()):
      print("CELDA: la lista está vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()