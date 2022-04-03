import imp


import os
from Archivoxml import ArchivoXML
from Ciudad import Ciudad
from Ciudad_nodoes import Ciudad_nodoES
from Ciudad_listaes import Ciudad_listaES
from Robot import Robot
from Robot_nodoes import Robot_nodoES
from Robot_listaes import Robot_listaES
from Fila import Fila
from Fila_nodoes import Fila_nodoES
from Fila_listaes import Fila_listaES
from Unidadmilitar import UnidadMilitar
from Unidadmilitar_nodoes import UnidadMilitar_nodoES
from Unidadmilitar_listaes import UnidadMilitar_listaES
from Mapa import Mapa
from Mapa_nodo import Mapa_nodo
from Mapa_matriz import Mapa_matriz


class ChapinWarriors():
  __listaCiudades = None # Ciudad_listaES()
  __listaRobot = None # Robot_listaES()
  __matrizMapa = None # Mapa_matriz()
  
  def __init__(self):
    pass


  def __cargarDatosXML(self, nombreCarpeta):
    archivoXML = ArchivoXML(nombreCarpeta)
    self.__listaCiudades = archivoXML.get_listaCiudades()
    self.__listaRobot = archivoXML.get_listaRobot()


  # def __
  def main(self) :
    salir = False
    # Ejecución principal del programa
    while ( salir == False):
      

 
if __name__ == '__main__':
  centroOperacion = ChapinWarriors()
  centroOperacion.main()