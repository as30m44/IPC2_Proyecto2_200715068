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
  __listaRobotsRescate = None # Robot_listaES()
  __listaRobotsExtraccion = None # Robot_listaES()
  __matrizMapa = None # Mapa_matriz()
  __mapaRescate = None # Mapa_matriz()
  __listaUnidadesCiviles = None # Celda_listaES()
  __mapaExtraccion = None # Mapa_matriz()
  __listaRecursosMilitares = None # Celda_listaES()
  __borde_1 = str("#").ljust(80,"#")
  __borde_2 = str("*").ljust(80,"*")
  __borde_3 = str("=").ljust(80,"=")
  
  def __init__(self):
    pass


  def __cargarDatosXML(self, nombreCarpeta):
    self.__archivoXML = ArchivoXML(nombreCarpeta)
    self.__listaCiudades = self.__archivoXML.get_listaCiudades()
    self.__listaRobotsRescate = self.__archivoXML.get_listaRobotsRescate()
    self.__listaRobotsExtraccion = self.__archivoXML.get_listaRobotsExtraccion()


  def __verArchivosXML(self):
    self.__archivoXML.imprimirListaXML()


  def __generarMapaRescate(self, idPuntoEntrada, idUnidadCivil):
    # dirección a seguir
    irDerecha = False
    irIzquierda = False
    irArriba = False
    irAbajo = False
    # punto de entrada seleccionado
    listaPuntoEntrada = self.__matrizMapa.get_listaPuntosEntrada()
    listaPuntoEntrada.ubicar(idPuntoEntrada)
    posicionE_X = listaPuntoEntrada.get_celda().get_posicion_X()
    posicionE_Y = listaPuntoEntrada.get_celda().get_posicion_Y()
    # unidad civil seleccionado
    self.__listaUnidadesCiviles.ubicar(idUnidadCivil)
    posicionC_X = self.__listaUnidadesCiviles.get_celda().get_posicion_X()
    posicionC_Y = self.__listaUnidadesCiviles.get_celda().get_posicion_Y()
    self.__mapaRescate = self.__matrizMapa
    self.__mapaRescate.ubicarNodoActual(posicionE_X, posicionE_Y)
    # AL INICIAR EL RECORRIDO
    # puede moverse entre 0<=direcciones <=2
    derecha = posicionE_X + 1
    izquierda = posicionE_X - 1
    arriba = posicionE_Y - 1
    abajo = posicionE_Y + 1
    # se mueve a la derecha o si no a la izquierda
    # antes de la última columna
    if (derecha < self.__mapaRescate.get_noColumnas()):
      irDerecha = True
    # después de la primera columna
    elif (izquierda != 0):
      irIzquierda = True
    # se mueve a abajo o si no a la arriba
    # antes de la última fila
    if (abajo < self.__mapaRescate.get_noFilas()):
      irAbajo = True
    # después de la primera fila
    elif (arriba != 0):
      irArriba = True
    # EN EL FINAL DEL RECORRIDO
    
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
    noCiudades = 0
    idCiudad = 0
    noRobotsRescate = 0
    idRobotRescate = 0
    while(noOpcion != 2):
      os.system("cls")
      # ********************************************************************************************
      # OPCIONES PARA ARCHIVOS XML
      print(self.__borde_1)
      print(str("MISIÓN DE RESCATE").center(80, " "))
      print(self.__borde_1)
      # --------------------------------------------------------------------------------------------
      # CIUDADES
      # Elegir ciudad
      print("\n\n")
      print("Lista de ciudades")
      print(self.__borde_2)
      self.__listaCiudades.imprimir()
      noCiudades = self.__listaCiudades.get_noCiudades()
      idCiudad = self.__inputEsNumero("Seleccione el número de la ciudad: ", 1, noCiudades)
      self.__matrizMapa = self.__archivoXML.get_matrizMapa(idCiudad)
      self.__archivoGraphviz = ArchivoGraphviz()
      self.__archivoGraphviz.imprimirMapa(self.__matrizMapa)
      self.__listaUnidadesCiviles = self.__matrizMapa.get_listaUnidadesCiviles()
      self.__listaRecursosMilitares = self.__matrizMapa.get_listaRecursosMilitares()
      # --------------------------------------------------------------------------------------------
      # hay unidades civiles para rescate
      if (self.__archivoXML.get_hayUnidadCivil()):
        # ..........................................................................................
        # ROBOT
        # caso 1: no hay robot
        if (self.__listaRobotsRescate.estaVacio()):
          print("MISIÓN RESCATE: no hay robot disponibles para realizar rescate")
        # caso 2: hay robot
        else:
          noRobotsRescate = self.__listaRobotsRescate.get_noRobots()
          print("\n")
          print("Lista de robots disponibles")
          print(self.__borde_2)
          self.__listaRobotsRescate.imprimir()
          # caso 2.1: para mas de 1 robot
          if (noRobotsRescate > 1):
            idRobotRescate = self.__inputEsNumero("Seleccione el número del robot: ", 1, noRobotsRescate)
          # caso 2.2: para un solo robot
          else:
            idRobotRescate = 1
          self.__listaRobotsRescate.ubicar(idRobotRescate)
          # ........................................................................................
          # PUNTOS DE ENTRADA
          print("\n")
          print("Lista de puntos de entrada")
          print(self.__borde_2)
          self.__matrizMapa.get_listaPuntosEntrada().imprimir()
          noPuntosEntrada = self.__matrizMapa.get_listaPuntosEntrada().get_noCeldas()
          idPuntoEntrada = self.__inputEsNumero("Seleccione el número del punto de entrada: ", 1, noPuntosEntrada)
          # ........................................................................................
          # UNIDAD CIVIL
          noUnidadesCiviles = self.__listaUnidadesCiviles.get_noCeldas()
          print("\n")
          print("Lista de unidades civiles")
          print(self.__borde_2)
          self.__listaUnidadesCiviles.imprimir()
          # caso 2.1: para mas de 1 unidad civil
          if (noUnidadesCiviles > 1):
            idUnidadCivil = self.__inputEsNumero("Seleccione el número de la unidad civil a rescatar: ", 1, noUnidadesCiviles)
          # caso 2.2: para un solo unidad civil
          else:
            idUnidadCivil = 1
          print("Generando mapa...")
          # self.__generarMapaRescate(idPuntoEntrada, idUnidadCivil)
      # --------------------------------------------------------------------------------------------
      # no hay unidades civiles para rescate
      else:
        print("MISIÓN RESCATE: no hay unidades civiles para rescatar")
      # --------------------------------------------------------------------------------------------
      self.__inputEsCualquierTecla()
      print("\n")
      print("Ingrese el número de la opción que desea realizar")
      print(self.__borde_2)
      print("1. Crear otra misión")
      print("2. Ir a GESTIONAR MISIÓN")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n")
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 2)
      if (noOpcion == 2):
        print("Regresando al GESTIONAR MISIÓN...")
        time.sleep(2)


  def __misionExtraccionRecursos(self):
    noOpcion = 1
    noCiudades = 0
    idCiudad = 0
    noRobotsRescate = 0
    idRobotRescate = 0
    while(noOpcion != 2):
      os.system("cls")
      # ********************************************************************************************
      # OPCIONES PARA ARCHIVOS XML
      print(self.__borde_1)
      print(str("MISIÓN DE EXTRACCIÓN DE RECURSOS").center(80, " "))
      print(self.__borde_1)
      # --------------------------------------------------------------------------------------------
      # CIUDADES
      # Elegir ciudad
      print("\n\n")
      print("Lista de ciudades")
      print(self.__borde_2)
      self.__listaCiudades.imprimir()
      noCiudades = self.__listaCiudades.get_noCiudades()
      idCiudad = self.__inputEsNumero("Seleccione el número de la ciudad: ", 1, noCiudades)
      self.__matrizMapa = self.__archivoXML.get_matrizMapa(idCiudad)
      self.__archivoGraphviz = ArchivoGraphviz()
      self.__archivoGraphviz.imprimirMapa(self.__matrizMapa)
      self.__listaUnidadesCiviles = self.__matrizMapa.get_listaUnidadesCiviles()
      self.__listaRecursosMilitares = self.__matrizMapa.get_listaRecursosMilitares()
      # --------------------------------------------------------------------------------------------
      # hay unidades civiles para rescate
      if (self.__archivoXML.get_hayRecursoMilitar()):
        # ..........................................................................................
        # ROBOT
        # caso 1: no hay robot
        if (self.__listaRobotsExtraccion.estaVacio()):
          print("MISIÓN EXTRACCIÓN DE RECURSOS: no hay robot disponibles para realizar rescate")
        # caso 2: hay robot
        else:
          noRobotsExtraccion = self.__listaRobotsExtraccion.get_noRobots()
          print("\n")
          print("Lista de robots disponibles")
          print(self.__borde_2)
          self.__listaRobotsExtraccion.imprimir()
          # caso 2.1: para mas de 1 robot
          if (noRobotsExtraccion > 1):
            idRobotExtraccion = self.__inputEsNumero("Seleccione el número del robot: ", 1, noRobotsExtraccion)
          # caso 2.2: para un solo robot
          else:
            idRobotExtraccion = 1
          self.__listaRobotsExtraccion.ubicar(idRobotExtraccion)
          # ........................................................................................
          # PUNTOS DE ENTRADA
          print("\n")
          print("Lista de puntos de entrada")
          print(self.__borde_2)
          self.__matrizMapa.get_listaPuntosEntrada().imprimir()
          noPuntosEntrada = self.__matrizMapa.get_listaPuntosEntrada().get_noCeldas()
          idPuntoEntrada = self.__inputEsNumero("Seleccione el número del punto de entrada: ", 1, noPuntosEntrada)
          # ........................................................................................
          # RECURSO MILITAR
          noRecursoMilitares = self.__listaRecursosMilitares.get_noCeldas()
          print("\n")
          print("Lista de recursos militares")
          print(self.__borde_2)
          self.__listaRecursosMilitares.imprimir()
          # caso 2.1: para mas de 1 recurso militar
          if (noRecursoMilitares > 1):
            idRecursoMilitar = self.__inputEsNumero("Seleccione el número del recurso militar para extracción: ", 1, noRecursoMilitares)
          # caso 2.2: para un solo recurso militar
          else:
            idRecursoMilitar = 1
          print("Generando mapa ...")
          # self.__generarMapaRescate(idPuntoEntrada, idRecursoMilitar)
      # --------------------------------------------------------------------------------------------
      # no hay recursos militares para rescate
      else:
        print("MISIÓN EXTRACCIÓN DE RECURSOS: no hay recursos militares para extracción")
      # --------------------------------------------------------------------------------------------
      self.__inputEsCualquierTecla()
      print("\n")
      print("Ingrese el número de la opción que desea realizar")
      print(self.__borde_2)
      print("1. Crear otra misión")
      print("2. Ir a GESTIONAR MISIÓN")
      # ********************************************************************************************
      # OPCIÓN DEL USUARIO
      print("\n")
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 2)
      if (noOpcion == 2):
        print("Regresando al GESTIONAR MISIÓN...")
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
      print("3. Salir del sistema")
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