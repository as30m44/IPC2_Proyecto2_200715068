from Nodoenlazadosimple import NodoEnlazadoSimple
from Ciudad import Ciudad


class Ciudad_nodoES(NodoEnlazadoSimple):
  __ciudad = None # Ciudad()
  
  def get_ciudad(self):
    return self.__ciudad
  
  def set_ciudad(self, ciudad):
    self.__ciudad = ciudad