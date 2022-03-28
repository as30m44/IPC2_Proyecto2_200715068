from Nodoenlazadosimple import NodoEnlazadoSimple
from Ciudad import Ciudad


class Ciudad_nodoES(NodoEnlazadoSimple):
  __ciudad = None # Ciudad()
  
  def get_ciudad(self):
    return self.__ciudad
  
  def set_ciudad(self, ciudad):
    self.__ciudad = ciudad


  def imprimir(self, tipo):
    # muestra el título de la tabla
    if (tipo == "titulo"):
      self.__ciudad.imprimirTitulo()
    # muestra la celda de la tabla
    else: 
      self.__ciudad.imprimirCelda()