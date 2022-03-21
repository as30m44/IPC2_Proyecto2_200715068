class Ciudad():
  __id = 0
  __nombre = ""
  __noColumnasMapa = 0
  __noFilasMapa = 0
  
  def __init__(self):
    pass
  
  def get_id(self):
    return self.__id
  
  def get_nombre(self):
    return self.__nombre
  
  def get_noColumnasMapa(self):
    return self.__noColumnasMapa
  
  def get_noFilasMapa(self):
    return self.__noFilasMapa
  
  def set_id(self, id):
    self.__id = id
  
  def set_nombre(self, nombre):
    self.__nombre = nombre
  
  def set_noColumnasMapa(self, noColumnasMapa):
    self.__noColumnasMapa = noColumnasMapa
  
  def set_noFilasMapa(self, noFilasMapa):
    self.__noFilasMapa = noFilasMapa
  
  
  def imprimirTitulo(self):
    id = "|" + "No".center(8, " ") + "|"
    nombre = "NOMBRE".center(15, " ") + "|"
    columnas = "COLUMNAS".center(8, " ") + "|"
    filas = "FILAS".center(8, " ") + "|"
    borde = "-".ljust(36, "-")
    print(borde)
    print(id, nombre, columnas, filas)
    print(borde)
  
  
  def imprimir(self):
    id = "|" + str(self.__id).center(8, " ") + "|"
    nombre = self.__nombre.center(15, " ") + "|"
    columnas = str(self.__noColumnasMapa).center(8, " ") + "|"
    filas = str(self.__noFilasMapa).center(8, " ") + "|"
    borde = "-".ljust(36, "-")
    print(id, nombre, columnas, filas)
    print(borde)
    