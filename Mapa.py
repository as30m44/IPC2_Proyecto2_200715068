

class Mapa():
  __idCiudad = 0
  __estado = ""
  __posicion_X = 0
  __posicion_Y = 0
  
  def __init__(self):
    pass
  
  def get_idCiudad(self):
    return self.__idCiudad
  
  def get_estado(self):
    return self.__estado
  
  def get_posicion_X(self):
    return self.__posicion_X
  
  def get_posicion_Y(self):
    return self.__posicion_Y
  
  def set_idCiudad(self, idCiudad):
    self.__idCiudad = idCiudad
  
  def set_estado(self, estado):
    self.__estado = estado
  
  def set_posicion(self, posicion_X, posicion_Y):
    self.__posicion_X = posicion_X
    self.__posicion_Y = posicion_Y
  
  
  def imprimirCabecera(self):
    cabecera = str(self.__posicion_X).center(2," ")
    return cabecera
  
  
  def imprimirFila(self):
    fila = ""
    if (self.__estado == " "):
      pass
  
  
  def imprimirCelda(self):
    return self.__estado