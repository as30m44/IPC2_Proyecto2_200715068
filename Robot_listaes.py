from Robot_nodoes import Robot_nodoES


class Robot_listaES():
  __nodoInicio = None # Robot_nodoES()
  __nodoFinal = None # Robot_nodoES()
  __nodoActual = None # Robot_nodoES()
  __noRobots = 0

  def __init__(self):
    pass

  def get_idRobotxNombre(self, nombre):
    idRobot = 0
    if(self.estaVacio()):
      print("ROBOT: la lista está vacía")
    else:
      encontrado = False
      self.__nodoActual = self.__nodoInicio
      while (encontrado == False and self.__nodoActual != None):
        robot = self.__nodoActual.get_robot()
        if (robot.get_nombre() == nombre):
          encontrado = True
          idRobot = robot.get_idRobot()
        else:
          self.__nodoActual = self.__nodoActual.get_siguiente()
    return idRobot

  def get_noRobots(self):
    return self.__noRobots

  def get_robot(self):
    return self.__nodoActual.get_robot()

  
  def modificarRobot(self, robot):
    if (self.estaVacio() or self.__nodoActual == None):
      print("ROBOT: la lista está vacía o no hay una ciudad seleccionada")
    else:
      idRobot = self.__nodoActual.get_robot().get_idRobot()
      robot.set_idRobot(idRobot)
      self.__nodoActual.set_robot(robot)

  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFinal == None
  
  
  def insertar(self, robot):
    robot.set_idRobot(self.__noRobots + 1)
    nodoNuevo = Robot_nodoES()
    nodoNuevo.set_robot(robot)
    # Caso 1: cuando la lista está vacía
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__noRobots = 1
    # Caso 2: cuando la lista tiene m elementos
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noRobots += 1
  

  def ubicar(self, idRobot):
    self.__nodoActual = self.__nodoInicio
    nodoPos_i = 1
    encontrado = False
    if (self.estaVacio()):
      print("ROBOT: la lista está vacía")
    else:
      # caso 1: el id se encuentra dentro de la lista
      if (idRobot <= self.__noRobots):
        while (encontrado == False):
          if (nodoPos_i == idRobot):
            encontrado = True
          else:
            nodoPos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      # caso 2: el id no está en la lista
      else:
        print("ROBOT: no se encuentra el item que ha ingresado")
        self.__nodoActual = None


  def imprimir(self):
    if (self.estaVacio()):
      print("ROBOT: la lista está vacía")
    else:
      nodo_m = self.__nodoInicio
      nodo_m.imprimir("titulo")
      while (nodo_m != None):
        nodo_m.imprimir("celda")
        nodo_m = nodo_m.get_siguiente()