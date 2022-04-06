import imp
from graphviz import Graph
from Mapa import Mapa
from Mapa_nodo import Mapa_nodo
from Mapa_matriz import Mapa_matriz

class ArchivoGraphviz():
  __directorio = ""

  def __init__(self):
    self.__directorio = "grafica/"


  def imprimirMapa(self, matrizMapa):
    if (matrizMapa.estaVacio()):
      print("GRAPHVIZ: no hay datos del mapa")
    else:
      # configuraciones del archivo graphviz
      graficaMapa = Graph(name = "Mapa", directory = self.__directorio, filename = "Mapa")
      graficaMapa.attr(rankdir = "LR")
      graficaMapa.attr(ranksep = "0.5")
      graficaMapa.attr("node", shape = "box", size = "0.5", style = "filled", fontsize = "12", fontcolor = "orange", nodesep = "0.5")
      graficaMapa.attr("edge", len = "0.1")
      # valores para recorrer la matriz
      noColumnas = matrizMapa.get_noColumnas()
      noFilas = matrizMapa.get_noFilas()
      # creación de los nodos y establecer sus propiedades
      # recorrido de filas
      for j in range(0, noFilas + 1, 1):
        # recorrido de columnas
        for i in range(0, noColumnas + 1, 1):
          matrizMapa.ubicarNodoActual(i, j)
          mapa = matrizMapa.get_mapa()
          estado = mapa.get_estado()
          if (estado == "*"): # celda intransitable
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "black")
          elif (estado == " "): # celda transitable
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "white")
          elif (estado == "E" or estado == "e"): # punto de entrada
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "darkseagreen3")
          elif (estado == "C" or estado == "c"): # unidad civil
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "cornflowerblue")
          elif (estado == "R" or estado == "r"): # recurso militar
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "darkgray")
          elif (estado == "M"): # unidad militar
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "crimson")
          else: # cabeceras
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "white", shape = "circle", fontcolor = "black")
      # conexiones por filas
      # recorrido de filas
      for j in range(0, noFilas + 1, 1):
        fila = []
        # recorrido de columnas
        for i in range(0, noColumnas, 1):
          tupla = (("nodo" + str(i) + str(j)), ("nodo" + str(i + 1)+ str(j)))
          fila.append(tupla)
        graficaMapa.edges(fila)
      # conexiones por columnas
      # recorrido por las filas
      for i in range(0, noColumnas + 1, 1):
        columna = []
        for j in range(0, noFilas, 1):
          tupla = (("nodo" + str(i) + str(j)), ("nodo" + str(i)+ str(j + 1)))
          columna.append(tupla)
        with graficaMapa.subgraph(name = ("nivel" + str(i))) as nivel:
          nivel.attr(rank = "same")
          nivel.edges(columna)
      graficaMapa.view()
