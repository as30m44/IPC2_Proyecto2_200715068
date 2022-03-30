from Nodoenlazadosimple import NodoEnlazadoSimple
from Robot import Robot


class Robot_nodoES(NodoEnlazadoSimple):
  __robot = None # Robot()
  
  def get_robot(self):
    return self.__robot
  
  def set_robot(self, robot):
    self.__robot = robot


  def imprimir(self, tipo):
    # muestra el título de la tabla
    if (tipo == "titulo"):
      self.__robot.imprimirTitulo()
    # muestra la celda de la tabla
    else: 
      self.__robot.imprimirCelda()