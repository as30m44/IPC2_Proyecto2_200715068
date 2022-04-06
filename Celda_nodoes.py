import imp
from Nodoenlazadosimple import NodoEnlazadoSimple
from Celda import Celda


class Celda_nodoES(NodoEnlazadoSimple):
  __celda = None # Celda()

  def get_celda(self):
    return self.__celda

  def set_celda(self, celda):
    self.__celda = celda


  def imprimir(self, tipo):
    # muestra el título de la tabla
    if (tipo == "titulo"):
      self.__celda.imprimirTitulo()
    # muestra la celda de la tabla
    else: 
      self.__celda.imprimirCelda()