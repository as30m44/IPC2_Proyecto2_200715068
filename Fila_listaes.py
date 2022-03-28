from Fila_nodoes import Fila_nodoES


class Fila_listaES():
  __nodoInicio = None # Fila_nodoES()
  __nodoFinal = None # Fila_nodoES()
  __nodoActual = None # Fila_nodoES()
  __noFilas = 0

  def get_noFilas(self):
    return self.__noFilas

  def get_fila(self):
    return self.__nodoActual.get_fila()

  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None
  
  
  def insertar(self, fila):
    fila.set_idFila(self.__noFilas + 1)
    nodoNuevo = Fila_nodoES()
    nodoNuevo.set_fila(fila)
    # Caso 1: cuando la lista está vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__noFilas = 1
    # Caso 2: cuando la lista tiene m elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noFilas += 1
  

  def ubicar(self, idFilas):
    self.__nodoActual = self.__nodoInicio
    nodoPos_i = 1
    encontrado = False
    if (self.estaVacio()):
      print("FILA: la lista está vacía")
    else:
      # caso 1: el id se encuentra dentro de la lista
      if (idFilas <= self.__noFilas):
        while (encontrado == False):
          if (nodoPos_i == idFilas):
            encontrado = True
          else:
            nodoPos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      # caso 2: el id no está en la lista
      else:
        print("FILA: no se encuentra el item que ha ingresado")


  def imprimir(self):
    if (self.estaVacio()):
      print("FILA: la lista está vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()