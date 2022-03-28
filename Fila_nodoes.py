from Nodoenlazadosimple import NodoEnlazadoSimple
from Fila import Fila


class Fila_nodoES(NodoEnlazadoSimple):
  __fila = None  # Fila()

  def get_fila(self):
    return self.__fila

  def set_fila(self, fila):
    self.__fila = fila


  def imprimir(self, tipo):
    # muestra el título de la tabla
    if (tipo == "titulo"):
      self.__fila.imprimirTitulo()
    # muestra la celda de la tabla
    else: 
      self.__fila.imprimirCelda()