class Robot():
  __idRobot = 0
  __nombre = ""
  __tipo = ""
  __capacidad = 0
  
  def __init__(self):
    pass
  
  def get_idRobot(self):
    return self.__idRobot
  
  def get_nombre(self):
    return self.__nombre
  
  def get_tipo(self):
    return self.__tipo
  
  def get_capacidad(self):
    return self.__capacidad
  
  def set_idRobot(self, idRobot):
    self.__idRobot = idRobot
  
  def set_nombre(self, nombre):
    self.__nombre = nombre
  
  def set_tipo(self, tipo):
    self.__tipo = tipo
  
  def set_capacidad(self, capacidad):
    self.__capacidad = capacidad

  
  def imprimirTitulo(self):
    idRobot = "|" + "No".center(8, " ") + "|"
    nombre = "NOMBRE".center(28, " ") + "|"
    tipo = "TIPO".center(14, " ") + "|"
    capacidad = "CAPACIDAD".center(12, " ") + "|"
    borde = "=".ljust(70, "=")
    print(borde)
    print(idRobot, nombre, tipo, capacidad)
    print(borde)
  
  
  def imprimirCelda(self):
    idRobot = "|" + str(self.__idRobot).center(8, " ") + "|"
    nombre = self.__nombre.center(28, " ") + "|"
    tipo = str(self.__tipo).center(14, " ") + "|"
    capacidad = str(self.__capacidad).center(12, " ") + "|"
    borde = "-".ljust(70, "-")
    print(idRobot, nombre, tipo, capacidad)
    print(borde)
    