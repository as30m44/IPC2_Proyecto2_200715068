from platform import node
from tkinter.ttk import Style
from turtle import fillcolor
from unicodedata import name
from xml.etree.ElementTree import Comment
from graphviz import Digraph, Graph


dot = Digraph(comment="Tabla")
dot.node('0','a1')
dot.node('1','b1')
dot.node('2','c1')
dot.node('3','d1')

dot.edges(['01','12', '23'])
# dot.edge('0','2',constraint='false')
print(dot.source)
# dot.render('test-output/tabla.svg',view=True)

tabla = Graph(name = "Matriz", directory = "grafica/", filename = "Prueba", engine = 'patchwork')
# engine='patchwork'
# tabla.attr("layout = patchwork")
# nodos
tabla.attr(rankdir = "TB")
tabla.node(name = "nodo1", label = "1", shape = "box")
tabla.node(name = "nodo2", label = "2")
tabla.node(name = "nodo3", label = "3")
tabla.node(name = "nodo4", label = "4")
tabla.node(name = "nodo5", label = "5")
tabla.node(name = "nodo6", label = "6")
tabla.edges([('nodo1','nodo4')])
tabla.edges([('nodo2','nodo5')])
tabla.edges([('nodo3','nodo6')])
# tabla.attr(rank = 'same')
with tabla.subgraph(name="hijo") as fila:
  fila.attr(rank = 'same')
  fila.edges([('nodo1', 'nodo2'), ('nodo2', 'nodo3')])
  
with tabla.subgraph(name="hijo2") as fila:
  fila.attr(rank = 'same')
  fila.edges([('nodo4', 'nodo5'), ('nodo5', 'nodo6')])
  
# tabla.edge(head_name="nodo2", tail_name = "nodo4")
tabla.view()
print(tabla.source)


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