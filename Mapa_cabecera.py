from Mapa import Mapa
from Mapa_nodo import Mapa_nodo



class Mapa_cabecera():
  __nodoInicio = None # Mapa_nodo()
  __nodoFinal = None # Mapa_nodo()
  __nodoActual = None # Mapa_nodo()
  __noNodos = 0
  __direccion = ""
  
  def __init__(self, noNodos, direccion):
    self.__noNodos = noNodos
    self.__direccion = direccion
  
  
  
  def __crearCabecera(self):
    posicion = [1, 1] # posicion[0] eje X, posicion[1], eje Y
    # agrega automáticamente todos los nodos en cierta dirección
    for i in range(1, self.__noNodos + 1, 1):
      nodoNuevo = Mapa_nodo()
      mapa = Mapa()
      mapa.set_estado(self.__direccion)
      mapa.set_posicion(posicion[0], posicion[1])
      nodoNuevo.set_mapa(mapa)
      if (self.__estaVacio()):
        self.__nodoInicio = nodoNuevo
        self.__nodoFinal = nodoNuevo
      else:
        # Agrega nodos según la dirección de la cabecera
        if (self.__direccion == "cabecera_columna"):
          self.__nodoFinal.set_derecha(nodoNuevo)
          nodoNuevo.set_izquierda(self.__nodoFinal)
          self.__nodoFinal = nodoNuevo
        else: # cabecera_fila
          self.__nodoFinal.set_abajo(nodoNuevo)
          nodoNuevo.set_arriba(self.__nodoFinal)
          self.__nodoFinal = nodoNuevo
      if (self.__direccion == "cabecera_columna"):
        posicion[0] += i
      else: # cabecera_fila
        posicion[1] += i
  
  
  
  def __estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None