from Nodoenlazadosimple import NodoEnlazadoSimple
from Unidadmilitar import UnidadMilitar


class UnidadMilitar_nodoES(NodoEnlazadoSimple):
  __unidadMilitar = None # UnidadMilitar()
  
  def get_unidadMilitar(self):
    return self.__unidadMilitar
  
  def set_unidadMilitar(self, unidadMilitar):
    self.__unidadMilitar = unidadMilitar


  def imprimir(self, tipo):
    # muestra el título de la tabla
    if (tipo == "titulo"):
      self.__unidadMilitar.imprimirTitulo()
    # muestra la celda de la tabla
    else: 
      self.__unidadMilitar.imprimirCelda()