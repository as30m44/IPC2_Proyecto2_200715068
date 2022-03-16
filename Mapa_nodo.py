from Mapa import Mapa



class Mapa_nodo():
  __mapa = Mapa()
  __derecha = None # MapaNodo()
  __izquierda = None # MapaNodo()
  __arriba = None # MapaNodo()
  __abajo = None # MapaNodo()
  
  def __init__(self):
    pass
  
  def get_mapa(self):
    return self.__mapa
  
  def get_derecha(self):
    return self.__derecha
  
  def get_izquierda(self):
    return self.__izquierda
  
  def get_arriba(self):
    return self.__arriba
  
  def get_abajo(self):
    return self.__abajo
  
  def set_mapa(self, mapa):
    self.__mapa = mapa
  
  def set_derecha(self, derecha):
    self.__derecha = derecha
  
  def set_izquierda(self, izquierda):
    self.__izquierda = izquierda
  
  def set_arriba(self, arriba):
    self.__arriba = arriba
  
  def set_abajo(self, abajo):
    self.__abajo = abajo
  
  
  
  def imprimirPrueba(self):
    celda = self.__mapa.imprimirPrueba()
    return celda