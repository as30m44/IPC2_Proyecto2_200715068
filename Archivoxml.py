import xml.etree.ElementTree as ET
import os
from Ciudad import Ciudad
from Ciudad_listaes import Ciudad_listaES
from Fila import Fila
from Fila_listaes import Fila_listaES
from Unidadmilitar import UnidadMilitar
from Unidadmilitar_listaes import UnidadMilitar_listaES
from Mapa import Mapa
from Mapa_matriz import Mapa_Matriz


class ArchivoXML():
  __directorio = ""

  def __init__(self, nombreArchivo):
    self.__directorio = "archivos/" + nombreArchivo
    try:
      raiz = ET.parse(self.__directorio)
    except NameError:
      print("XML: nombre incorrecto del archivo")
    except:
      print("XML: nombre incorrecto del archivo")
  
  
  # def 
# primer nivel
arbol = ET.parse("archivos/Entrada0.xml")
raiz = arbol.getroot()
for nivel_1 in raiz:
  print(nivel_1.tag)

print(".".ljust(50, "."))

arbol = ET.parse("archivos/Entrada0.xml")
raiz = arbol.getroot()
for nivel_1 in raiz:
  print(nivel_1.tag)
  for nivel_2 in nivel_1:
    print(nivel_2.tag.upper())
    for nivel_3 in nivel_2:
      print(nivel_3.tag)

print(".".ljust(50, "."))
      
for nivel_1 in raiz:
  listaCiudades = nivel_1.tag
  for nivel_2 in nivel_1:
    if (listaCiudades == "listaCiudades"):
      print(nivel_2.tag)

print(".".ljust(50, "."))

for nivel_2 in raiz[0]:
  print(nivel_2.tag.upper())
  for nivel_3 in nivel_2:
    mapaConfiguracion = nivel_3.tag
    if (nivel_3.tag == "nombre"):
      print(nivel_3.text)

# cargar todos los archivos en un arreglo.
carpeta = "archivos/"
listaArchivos = os.listdir(carpeta)
directorios = [] # lista de directorios
# Agregar todos los archivos con extensión xml en un arreglo
for archivo in listaArchivos:
  if (os.path.isfile(os.path.join(carpeta, archivo)) and archivo.endswith(".xml")):
    directorios.append(carpeta + archivo)


# crear la lista de ciudades obtenidas del arreglo de archivos
listaCiudades = Ciudad_listaES()
# Atributos del objeto Ciudad()
idCiudad = 0
noColumnas = 0
noFilas = 0
# Atributos del objeto Fila()
estado = ""
# Atributos dl objeto UnidadMilitar()
posicion_X = 0
posicion_Y = 0
capacidadCombate = 0
# examina cada directorio
for directorio in directorios:
  arbol = ET.parse(directorio)
  raiz = arbol.getroot()
  for nivel_2 in raiz[0]: # raiz[0] es <listaCiudades> y nivel_2 es <ciudad>
    ciudad = Ciudad()
    listaFilas = Fila_listaES()
    listaUnidadesMilitares = UnidadMilitar_listaES()
    ciudad_i = 0
    filas_i = 0
    unidadesMilitares_i = 0
    # ----------------------------------------------------------------------------------------------
    # lectura del archivo xml de un directorio k
    for nivel_3 in nivel_2: # nivel_3 es <nombre>, <fila> y <unidadMilitar>
      # creación de objetos
      fila = Fila()
      unidadMilitar = UnidadMilitar()
      # ............................................................................................
      # caso 1: datos para el objeto Ciudad()
      if (nivel_3.tag == "nombre"):
        # busca si la ciudad está en la lista y devuelve su posición
        idCiudad = listaCiudades.get_idCiudadxNombre(nivel_3.text) # 0: para nuevo o no existe ciudad
        # obtención de atributos de xml
        noColumnas = int(nivel_3.attrib.get("columnas"))
        noFilas = int(nivel_3.attrib.get("filas"))
        # agregar atributos a objeto Ciudad()
        ciudad.set_nombre(nivel_3.text)
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
        # caso 1: no hay datos de mapa y unidades militares
        if (filas_i == 0 and unidadesMilitares_i == 0):
          print("XML: no es posible almacenar datos, hace falta mapa")
        # __________________________________________________________________________________________
        # caso 2: no hay datos de mapa
        elif (filas_i == 0 and unidadesMilitares_i != 0):
          print("XML: no es posible almacenar datos, hace falta mapa")
        # __________________________________________________________________________________________
        # caso 3: hay únicamente datos de mapa
        elif (filas_i != 0 and unidadesMilitares_i == 0):
          ciudad.set_listaFilas(listaFilas)
          # caso 3.1: cuando la ciudad no está en la lista o la lista esta vacía
          if (idCiudad == 0):
            listaCiudades.insertar(ciudad)
          # caso 3.2: cuando está la ciudad en la lista
          else:
            listaCiudades.modificarCiudad(ciudad)
        # __________________________________________________________________________________________
        # caso 4: hay datos de mapa y unidades militares
        else:
          ciudad.set_listaFilas(listaFilas)
          ciudad.set_listaUnidadesMilitares(listaUnidadesMilitares)
          # caso 4.1: cuando la ciudad no está en la lista o la lista esta vacía
          if (idCiudad == 0):
            listaCiudades.insertar(ciudad)
          # caso 4.2: cuando está la ciudad en la lista
          else:
            listaCiudades.modificarCiudad(ciudad)
          
        
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