class Celda():
  __idCelda = 0
  __posicion_X = 0
  __posicion_Y = 0

  def __init__(self):
    pass

  def get_idCelda(self):
    return self.__idCelda

  def get_posicion_X(self):
    return self.__posicion_X

  def get_posicion_Y(self):
    return self.__posicion_Y

  def set_idCelda(self, idCelda):
    self.__idCelda = idCelda

  def set_posicion(self, posicion_X, posicion_Y):
    self.__posicion_X = posicion_X
    self.__posicion_Y = posicion_Y


  def imprimirTitulo(self):
    idCelda = "|" + "No".center(16," ") + "|"
    posicionX = "COLUMNA".center(15, " ") + "|"
    posicionY = "FILA".center(8, " ") + "|"
    borde = "-".ljust(45, "-")
    print(borde)
    print(idCelda, posicionX, posicionY)
    print(borde)
  
  
  def imprimirCelda(self):
    idCelda = "|" + str(self.__idCelda).center(16, " ") + "|"
    posicionX = str(self.__posicion_X).center(15, " ") + "|"
    posicionY = str(self.__posicion_Y).center(8, " ") + "|"
    borde = "-".ljust(45, "-")
    print(idCelda, posicionX, posicionY)
    print(borde)
    