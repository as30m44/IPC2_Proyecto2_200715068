class Ciudad():
  __idCiudad = 0
  __nombre = ""
  __noColumnas = 0
  __noFilas = 0
  __listaFilas = None 
  __listaUnidadesMilitares = None 
  
  def __init__(self):
    pass
  
  def get_idCiudad(self):
    return self.__idCiudad
  
  def get_nombre(self):
    return self.__nombre
  
  def get_noColumnas(self):
    return self.__noColumnas
  
  def get_noFilas(self):
    return self.__noFilas
  
  def get_listaFilas(self):
    return self.__listaFilas
  
  def get_listaUnidadesMilitares(self):
    return self.__listaUnidadesMilitares
  
  def set_idCiudad(self, idCiudad):
    self.__idCiudad = idCiudad
  
  def set_nombre(self, nombre):
    self.__nombre = nombre
  
  def set_noColumnas(self, noColumnas):
    self.__noColumnas = noColumnas
  
  def set_noFilas(self, noFilas):
    self.__noFilas = noFilas
  
  def set_listaFilas(self, listaFilas):
    self.__listaFilas = listaFilas
  
  def set_listaUnidadesMilitares(self, listaUnidadesMilitares):
    self.__listaUnidadesMilitares = listaUnidadesMilitares
  
  
  def imprimirTitulo(self):
    id = "|" + "No".center(8, " ") + "|"
    nombre = "NOMBRE".center(28, " ") + "|"
    columnas = "COLUMNAS".center(8, " ") + "|"
    filas = "FILAS".center(8, " ") + "|"
    borde = "=".ljust(60, "=")
    print(borde)
    print(id, nombre, columnas, filas)
    print(borde)
  
  
  def imprimirCelda(self):
    id = "|" + str(self.__idCiudad).center(8, " ") + "|"
    nombre = self.__nombre.center(28, " ") + "|"
    columnas = str(self.__noColumnas).center(8, " ") + "|"
    filas = str(self.__noFilas).center(8, " ") + "|"
    borde = "-".ljust(60, "-")
    print(id, nombre, columnas, filas)
    print(borde)
    