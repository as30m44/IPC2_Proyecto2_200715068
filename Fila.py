class Fila():
  __idFila = 0
  __estado = ""

  def __init__(self):
    pass

  def get_idFila(self):
    return self.__idFila

  def get_estado(self):
    return self.__estado

  def set_idFila(self, idFila):
    self.__idFila = idFila

  def set_estado(self, estado):
    self.__estado = estado


  def imprimirTitulo(self):
    id = "|" + "No".center(8, " ") + "|"
    estado = "ESTADO".center(15, " ") + "|"
    borde = "-".ljust(26, "-")
    print(borde)
    print(id, estado)
    print(borde)
  
  
  def imprimirCelda(self):
    id = "|" + str(self.__idFila).center(8, " ") + "|"
    estado = self.__estado.center(15, " ") + "|"
    borde = "-".ljust(26, "-")
    print(id, estado)
    print(borde)