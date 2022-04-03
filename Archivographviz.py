import imp
from multiprocessing.spawn import import_main_path
from turtle import fillcolor
from unicodedata import name
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
      graficaMapa.attr("node", shape = "box", size = 1, style = "filled", fontsize = "8", fontcolor = "orange")
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
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "aquamarine31")
          elif (estado == "C" or estado == "c"): # unidad civil
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "cornflowerblue")
          elif (estado == "R" or estado == "r"): # unidad civil
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "darkgray")
          elif (estado == "militar"): # unidad militar
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "crimson")
          else: # cabeceras
            graficaMapa.node(name = ("nodo" + str(i) + str(j)), label = estado, fillcolor = "white", shape = "circle")
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
          nivel._edge(columna)
      graficaMapa.view()

matriz = Graph(name = "Matriz", directory = "grafica/", filename = "Matriz")
matriz.attr(rankdir = "LR")
matriz.attr("node", shape = "box", style = "filled", size = "8.5")
matriz.attr("edge", len = "0.5")
for i in range(1, 13, 1):
  matriz.node(name = ("nodo" + str(i)), label = str(i), shape = "box", fillcolor = "orange")

contador = 1
for i in range(1, 5, 1): # filas
  fila = []
  for j in range(1,3,1): # columnas
    tupla = (("nodo" + str(contador)), ("nodo" + str(contador + 1)))
    fila.append(tupla)
    contador += 1
  matriz.edges(fila)
  contador += 1

for i in range(1, 4, 1): # columnas
  columna_n = []
  contador = i
  for j in range(1, 4, 1): # filas
    tupla = (("nodo" + str(contador)), ("nodo" + str(contador + 3)))
    columna_n.append(tupla)
    contador += 3
  with matriz.subgraph(name = ("hijo" + str(i))) as columna:
    columna.attr(rank = 'same')
    columna.edges(columna_n)

matriz.view()
  
print(type([('nodo1', 'nodo2'), ('nodo2', 'nodo3')]))
print(type(('1', '2')))