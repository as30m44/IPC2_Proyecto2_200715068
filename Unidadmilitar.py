class UnidadMilitar():
  __idUnidadMilitar = 0
  __posicion_X = ""
  __posicion_Y = 0
  __capacidadCombate = 0
  
  def __init__(self):
    pass
  
  def get_idUnidadMilitar(self):
    return self.__idUnidadMilitar
  
  def get_posicion_X(self):
    return self.__posicion_X
  
  def get_posicion_Y(self):
    return self.__posicion_Y
  
  def get_capacidadCombate(self):
    return self.__capacidadCombate
  
  def set_idUnidadMilitar(self, idUnidadMilitar):
    self.__idUnidadMilitar = idUnidadMilitar
  
  def set_posicion(self, posicion_X, posicion_Y):
    self.__posicion_X = posicion_X
    self.__posicion_Y = posicion_Y
  
  def set_capacidadCombate(self, capacidadCombate):
    self.__capacidadCombate = capacidadCombate
  
  
  def imprimirTitulo(self):
    idUnidadMilitar = "|" + "UNIDAD MILITAR".center(16," ") + "|"
    posicionX = "COLUMNA".center(15, " ") + "|"
    posicionY = "FILA".center(8, " ") + "|"
    capacidadCombate = "CAPACIDAD COMBATE".center(20, " ") + "|"
    borde = "-".ljust(65, "-")
    print(borde)
    print(idUnidadMilitar, posicionX, posicionY, capacidadCombate)
    print(borde)
  
  
  def imprimirCelda(self):
    idUnidadMilitar = "|" + str(self.__idUnidadMilitar).center(16, " ") + "|"
    posicionX = str(self.__posicion_X).center(15, " ") + "|"
    posicionY = str(self.__posicion_Y).center(8, " ") + "|"
    capacidadCombate = str(self.__capacidadCombate).center(20, " ") + "|"
    borde = "-".ljust(65, "-")
    print(idUnidadMilitar, posicionX, posicionY, capacidadCombate)
    print(borde)
    