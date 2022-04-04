import os
import time
from Archivoxml import ArchivoXML
from Archivographviz import ArchivoGraphviz
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
  __archivoXML = None
  __archivoGraphviz = None
  __listaCiudades = None # Ciudad_listaES()
  __listaRobot = None # Robot_listaES()
  __matrizMapa = None # Mapa_matriz()
  __borde_1 = str("#").ljust(80,"#")
  __borde_2 = str("*").ljust(80,"*")
  __borde_3 = str("=").ljust(80,"=")
  
  def __init__(self):
    pass


  def __cargarDatosXML(self, nombreCarpeta):
    self.__archivoXML = ArchivoXML(nombreCarpeta)
    self.__listaCiudades = self.__archivoXML.get_listaCiudades()
    self.__listaRobot = self.__archivoXML.get_listaRobot()


  def __verArchivosXML(self):
    self.__archivoXML.imprimirListaXML()

  
  def __inputEsNumero(self, solicitud, opcionMin, opcionMax):
    esNumero = False
    numero = 0
    while (esNumero == False):
      valorIngresado = input(solicitud)
      if (str(valorIngresado).isdigit()):
        numero = int(valorIngresado)
        if (opcionMin <= numero and numero <= opcionMax):
          esNumero = True
        else:
          solicitud = "Esta opción no se encuentra, ingrese otra nuevamente: "
      else:
        solicitud = "únicamente se permiten números, ingrese otra nuevamente: "
    return numero
  
  
  def __inputEsCualquierTecla(self):
    solicitud = input("Presiona cualquier tecla para continuar: ")


  def __gestionarArchivoXML(self):
    noOpcion = 1
    while(noOpcion != 3):
      os.system("cls")
      # ********************************************************************************************
      # OPCIONES PARA ARCHIVOS XML
      print(self.__borde_2)
      print(str("ADMINISTRAR ARCHIVOS XML").center(80, " "))
      print(self.__borde_2)
      print("\n\n")
      print("Ingrese el número de la opción que desea realizar")
      print("1. Actualizar directorio de archivos")
      print("2. Ver lista de archivos cargados")
      print("3. Ir a MENÚ PRINCIPAL")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n\n")
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 3)
      if (noOpcion == 3):
        print("Regresando al MENÚ PRINCIPAL...")
        time.sleep(2)
      elif (noOpcion == 1):
        self.__cargarDatosXML("archivos")
        print("Actualizando directorio de archivos...")
        time.sleep(2)
      elif (noOpcion == 2):
        print("ARCHIVOS CARGADOS EN EL SISTEMA".center(80, " "))
        print("-".ljust(80, "-"))
        print("\n")
        self.__verArchivosXML()
        self.__inputEsCualquierTecla()


  def __gestionarMisiones(self):
    noOpcion = 1
    while(noOpcion != 3):
      os.system("cls")
      # ********************************************************************************************
      # OPCIONES PARA ARCHIVOS XML
      print(self.__borde_2)
      print(str("GESTIONAR MISIONES").center(80, " "))
      print(self.__borde_2)
      print("\n\n")
      print("Ingrese el número de la opción que desea realizar")
      print("1. Misión de rescate")
      print("2. Misión de extracción de recursos")
      print("3. Ir a MENÚ PRINCIPAL")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n\n")
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 3)
      if (noOpcion == 3):
        print("Regresando al MENÚ PRINCIPAL...")
        time.sleep(2)
      elif (noOpcion == 1):
        self.__misionRescate()
        print("Cargando datos...")
        time.sleep(2)
      elif (noOpcion == 2):
        self.__misionExtraccionRecursos()
        print("Cargando datos...")
        time.sleep(2)


  def __misionRescate(self):
    noOpcion = 1
    while(noOpcion != 3):
      os.system("cls")
      # ********************************************************************************************
      # OPCIONES PARA ARCHIVOS XML
      print(self.__borde_2)
      print(str("MISIÓN DE RESCATE").center(80, " "))
      print(self.__borde_2)
      print("\n\n")
      print("Lista de ciudades")
      print(self.__borde_3)
      self.__listaCiudades.imprimir()
      noCiudades = self.__listaCiudades.get_noCiudades()
      idCiudad = self.__inputEsNumero("Seleccione el número de la ciudad:", 1, noCiudades)
      self.__matrizMapa = self.__archivoXML.get_matrizMapa(idCiudad)
      self.__inputEsCualquierTecla()
      self.__archivoGraphviz = ArchivoGraphviz()
      self.__archivoGraphviz.imprimirMapa(self.__matrizMapa)
      print("Ingrese el número de la opción que desea realizar")
      print("1. Misión de rescate")
      print("2. Misión de extracción de recursos")
      print("3. Ir a GESTIONAR MISIÓN")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n\n")
      if (noOpcion == 3):
        print("Regresando al GESTIONAR MISIÓN...")
        time.sleep(2)
      elif (noOpcion == 1):
        self.__misionRescate()
        print("Cargando datos...")
        time.sleep(2)
      elif (noOpcion == 2):
        self.__misionExtraccionRecursos()
        print("Cargando datos...")
        time.sleep(2)


  def main(self) :
    noOpcion = 1
    self.__cargarDatosXML("archivos") # cargar los archivos XML
    while ( noOpcion != 3):
      os.system("cls")
      # ********************************************************************************************
      # MENÚ PRINCIPAL
      print(self.__borde_1)
      print(str("CHAPIN WARRIORS").center(80, " "))
      print(self.__borde_1)
      print("\n\n")
      print(str("MENÚ PRINCIPAL").center(80, " "))
      print(self.__borde_2)
      print("Ingrese el número de la opción que desea realizar")
      print("1. Administrar archivos XML")
      print("2. Gestionar misiones")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n\n")
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 3)
      if (noOpcion == 3):
        print("Gracias por utilizar nuestros servicios")
      elif (noOpcion == 1):
        self.__gestionarArchivoXML()
      elif (noOpcion == 2):
        self.__gestionarMisiones()



if __name__ == '__main__':
  centroOperacion = ChapinWarriors()
  centroOperacion.main()