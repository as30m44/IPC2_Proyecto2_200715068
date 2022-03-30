import xml.etree.ElementTree as ET
import os
from Ciudad import Ciudad
from Ciudad_listaes import Ciudad_listaES
from Fila import Fila
from Fila_listaes import Fila_listaES
from Unidadmilitar import UnidadMilitar
from Unidadmilitar_listaes import UnidadMilitar_listaES
from Robot import Robot
from Robot_listaes import Robot_listaES

from Mapa import Mapa
from Mapa_matriz import Mapa_matriz


class ArchivoXML():
  __listaArchivosXML = []
  __listaCiudades = Ciudad_listaES()
  __listaRobots = Robot_listaES()

  def __init__(self, nombreCarpeta):
    carpeta = nombreCarpeta + "/"
    listaArchivos = os.listdir(carpeta) # muestra la lista de todos los archivos XML en la carpeta
    # Agregar todos los archivos con extensión XML en un arreglo
    for archivoXML in listaArchivos:
      if (os.path.isfile(os.path.join(carpeta, archivoXML)) and archivoXML.endswith(".xml")):
        self.__listaArchivosXML.append(carpeta + archivoXML)
  

  def get_listaCiudades(self):
    # **********************************************************************************************
    # Atributos del objeto Ciudad()
    idCiudad = 0
    nombre = ""
    noColumnas = 0
    noFilas = 0
    # Atributos del objeto Fila()
    estado = ""
    # Atributos dl objeto UnidadMilitar()
    posicion_X = 0
    posicion_Y = 0
    capacidadCombate = 0
    # **********************************************************************************************
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      raiz = arbol.getroot() # raiz[0] es <listaCiudades>
      # recorre el contenido dentro de las etiquetas <listaCiudades>
      for nivel_2 in raiz[0]: # nivel_2 es <ciudad>
        ciudad = Ciudad()
        listaFilas = Fila_listaES()
        listaUnidadesMilitares = UnidadMilitar_listaES()
        ciudad_i = 0
        filas_i = 0
        unidadesMilitares_i = 0
        # ----------------------------------------------------------------------------------------------
        # recorre el contenido dentro de las etiquetas <ciudad>
        for nivel_3 in nivel_2: # nivel_3 es <nombre>, <fila> y <unidadMilitar>
          # creación de objetos
          fila = Fila()
          unidadMilitar = UnidadMilitar()
          # ............................................................................................
          # caso 1: datos para el objeto Ciudad()
          if (nivel_3.tag == "nombre"):
            # busca si la ciudad está en la lista y devuelve su posición
            idCiudad = self.__listaCiudades.get_idCiudadxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
            # obtención de atributos de xml
            nombre = nivel_3.text
            noColumnas = int(nivel_3.attrib.get("columnas"))
            noFilas = int(nivel_3.attrib.get("filas"))
            # agregar atributos a objeto Ciudad()
            ciudad.set_nombre(nombre)
            ciudad.set_noColumnas(noColumnas)
            ciudad.set_noFilas(noFilas)
            ciudad_i += 1
          # ............................................................................................
          # caso 2: datos para el objeto Fila()|MAPA
          elif (nivel_3.tag == "fila"):
            # obtención de atributos de xml
            estado = ""
            estadoAux = nivel_3.text
            for i in range(0, len(estadoAux), 1):
              if (estadoAux[i] != "\""):
                estado += estadoAux[i]
            # agregar atributos a objeto Fila()
            fila.set_estado(estado)
            listaFilas.insertar(fila)
            filas_i += 1
          # ............................................................................................
          # caso 3: datos para el objeto UnidadMilitar()
          elif (nivel_3.tag == "unidadMilitar"):
            posicion_X = int(nivel_3.attrib.get("columna"))
            posicion_Y = int(nivel_3.attrib.get("fila"))
            capacidadCombate = int(nivel_3.text)
            # agregar atributos a objeto UnidadMilitar()
            unidadMilitar.set_posicion(posicion_X, posicion_Y)
            unidadMilitar.set_capacidadCombate(capacidadCombate)
            listaUnidadesMilitares.insertar(unidadMilitar)
            unidadesMilitares_i += 1
          # ............................................................................................
          # caso A: cuando ya es el último elemento del nivel_2
          totalNivel_2 = ciudad_i + filas_i + unidadesMilitares_i
          if (totalNivel_2 == len(nivel_2)):
            # __________________________________________________________________________________________
            # caso A.1: no hay datos de mapa y unidades militares
            if (filas_i == 0 and unidadesMilitares_i == 0):
              print("XML: no es posible almacenar datos, hace falta mapa")
            # __________________________________________________________________________________________
            # caso A.2: no hay datos de mapa
            elif (filas_i == 0 and unidadesMilitares_i != 0):
              print("XML: no es posible almacenar datos, hace falta mapa")
            # __________________________________________________________________________________________
            # caso A.3: hay únicamente datos de mapa
            elif (filas_i != 0 and unidadesMilitares_i == 0):
              ciudad.set_listaFilas(listaFilas)
              # caso A.3.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idCiudad == 0):
                self.__listaCiudades.insertar(ciudad)
              # caso A.3.2: cuando está la ciudad en la lista
              else:
                self.__listaCiudades.modificarCiudad(ciudad)
            # __________________________________________________________________________________________
            # caso A.4: hay datos de mapa y unidades militares
            else:
              ciudad.set_listaFilas(listaFilas)
              ciudad.set_listaUnidadesMilitares(listaUnidadesMilitares)
              # caso A.4.1: cuando la ciudad no está en la lista o la lista esta vacía
              if (idCiudad == 0):
                self.__listaCiudades.insertar(ciudad)
              # caso A.4.2: cuando está la ciudad en la lista
              else:
                self.__listaCiudades.modificarCiudad(ciudad)
    return self.__listaCiudades  


  def get_listaRobot(self):
    # **********************************************************************************************
    # Atributos del objeto Robot()
    idRobot = 0
    nombre = ""
    tipo = ""
    capacidad = 0
    # **********************************************************************************************
    # lee el contenido de cada archivo XML
    for archivoXML in self.__listaArchivosXML:
      arbol = ET.parse(archivoXML)
      raiz = arbol.getroot() # raiz[] es <robots>
      # recorre el contenido dentro de las etiquetas <robots>
      for nivel_2 in raiz[1]: # nivel_2 es <robot>
        robot = Robot()
        # ----------------------------------------------------------------------------------------------
        # recorre el contenido dentro de las etiquetas <robot>
        for nivel_3 in nivel_2: # nivel_3 es <nombre>
          # ............................................................................................
          # caso 1: datos para el objeto Robot()
          if (nivel_3.tag == "nombre"):
            # busca si el robot está en la lista y devuelve su posición
            idRobot = self.__listaRobots.get_idRobotxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
            # obtención de atributos de xml
            nombre = nivel_3.text
            tipo = nivel_3.attrib.get("tipo")
            if (tipo == "ChapinFighter"):
              capacidad = int(nivel_3.attrib.get("filas"))
            else: 
              capacidad = 0
            # agregar atributos a objeto Ciudad()
            robot.set_nombre(nombre)
            robot.set_tipo(tipo)
            robot.set_capacidad(capacidad)
            # insertar el robot en la lista
            # caso 1.1: cuando la ciudad no está en la lista o la lista esta vacía
            if (idRobot == 0):
              self.__listaRobots.insertar(robot)
            # caso 1.2: cuando está la ciudad en la lista
            else:
              self.__listaRobots.modificarCiudad(robot)
    return self.__listaRobots

  
listaCiudades.imprimir()
listaCiudades.ubicar(3)
listaFilas = listaCiudades.get_ciudad().get_listaFilas()
listaFilas.imprimir()
listaUnidadesMilitares = listaCiudades.get_ciudad().get_listaUnidadesMilitares()
listaUnidadesMilitares.imprimir()


noFilas = listaFilas.get_noFilas()
ciudad = listaCiudades.get_ciudad()
columnas = ciudad.get_noColumnas()
filas = ciudad.get_noFilas()
print(type(columnas))
print(type(noFilas))
matrizMapa = Mapa_Matriz(listaCiudades.get_ciudad().get_noColumnas(), listaCiudades.get_ciudad().get_noFilas())
contador = 1
for idFila in range(1, noFilas + 1, 1):
  listaFilas.ubicar(idFila) # sitúo el apuntador en cada tupla
  fila = listaFilas.get_fila() # obtengo el objeto de la tupla seleccionada
  estado = fila.get_estado()
  for idColumna in range(0, len(estado), 1):
    print("recorrido: ", str(contador))
    contador += 1
    mapa = Mapa()
    mapa.set_estado(estado[idColumna])
    mapa.set_posicion(idColumna + 1, idFila)
    matrizMapa.insertar(mapa)

matrizMapa.imprimir()

