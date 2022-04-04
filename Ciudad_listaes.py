from Ciudad_nodoes import Ciudad_nodoES


class Ciudad_listaES():
  __nodoInicio = None # Ciudad_nodoES()
  __nodoFinal = None # Ciudad_nodoES()
  __nodoActual = None # Ciudad_nodoES()
  __noCiudades = 0

  def __init__(self):
    pass

  def get_noCiudades(self):
    return self.__noCiudades
  
  def get_idCiudadxNombre(self, nombre):
    idCiudad = 0
    if(self.estaVacio()):
      print("CIUDAD: la lista está vacía")
    else:
      encontrado = False
      self.__nodoActual = self.__nodoInicio
      while (encontrado == False and self.__nodoActual != None):
        ciudad_m = self.__nodoActual.get_ciudad()
        if (ciudad_m.get_nombre() == nombre):
          encontrado = True
          idCiudad = ciudad_m.get_idCiudad()
        else:
          self.__nodoActual = self.__nodoActual.get_siguiente()
    return idCiudad


  def get_ciudad(self):
    return self.__nodoActual.get_ciudad()

  
  def modificarCiudad(self, ciudad):
    if (self.estaVacio() or self.__nodoActual == None):
      print("CIUDAD: la lista está vacía o no hay una ciudad seleccionada")
    else:
      # el idCiudad se crea automaticamente en la lista de ciudades
      idCiudad_m = self.__nodoActual.get_ciudad().get_idCiudad()
      ciudad.set_idCiudad(idCiudad_m)
      self.__nodoActual.set_ciudad(ciudad)

  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None
  
  
  def insertar(self, ciudad):
    ciudad.set_idCiudad(self.__noCiudades + 1)
    nodoNuevo = Ciudad_nodoES()
    nodoNuevo.set_ciudad(ciudad)
    # Caso 1: cuando la lista está vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__noCiudades = 1
    # Caso 2: cuando la lista tiene m elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noCiudades += 1
  

  def ubicar(self, idCiudad):
    self.__nodoActual = self.__nodoInicio
    nodoPos_i = 1
    encontrado = False
    if (self.estaVacio()):
      print("CIUDAD: la lista está vacía")
    else:
      # caso 1: el id se encuentra dentro de la lista
      if (idCiudad <= self.__noCiudades):
        while (encontrado == False):
          if (nodoPos_i == idCiudad):
            encontrado = True
          else:
            nodoPos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      # caso 2: el id no está en la lista
      else:
        print("CIUDAD: no se encuentra el item que ha ingresado")
        self.__nodoActual = None


  def imprimir(self):
    if (self.estaVacio()):
      print("CIUDAD: la lista está vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()