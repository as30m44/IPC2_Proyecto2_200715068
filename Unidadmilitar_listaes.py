from Unidadmilitar_nodoes import UnidadMilitar_nodoES


class UnidadMilitar_listaES():
  __nodoInicio = None # UnidadMilitar_nodoES()
  __nodoFinal = None # UnidadMilitar_nodoES()
  __nodoActual = None # UnidadMilitar_nodoES()
  __noUnidadesMilitares = 0

  def __init__(self):
    pass
  
  def get_noUnidadesMilitares(self):
    return self.__noUnidadesMilitares

  def get_unidadMilitar(self):
    return self.__nodoActual.get_unidadMilitar()

  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None
  
  
  def insertar(self, unidadMilitar):
    unidadMilitar.set_idUnidadMilitar(self.__noUnidadesMilitares + 1)
    nodoNuevo = UnidadMilitar_nodoES()
    nodoNuevo.set_unidadMilitar(unidadMilitar)
    # Caso 1: cuando la lista está vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__noUnidadesMilitares = 1
    # Caso 2: cuando la lista tiene m elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noUnidadesMilitares += 1
  

  def ubicar(self, idUnidadMilitar):
    self.__nodoActual = self.__nodoInicio
    nodoPos_i = 1
    encontrado = False
    if (self.__nodoActual == None):
      print("UNIDAD MILITAR: la lista está vacía")
    else:
      # caso 1: el id se encuentra dentro de la lista
      if (idUnidadMilitar <= self.__noUnidadesMilitares):
        while (encontrado == False):
          if (nodoPos_i == idUnidadMilitar):
            encontrado = True
          else:
            nodoPos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      # caso 2: el id no está en la lista
      else:
        print("UNIDAD MILITAR: no se encuentra el item que ha ingresado")


  def imprimir(self):
    if(self.estaVacio()):
      print("UNIDAD MILITAR: la lista está vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()