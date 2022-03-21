import xml.etree.ElementTree as ET


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
arbol = ET.parse("Entrada0.xml")
raiz = arbol.getroot()
for nivel_1 in raiz:
  print(nivel_1.tag)

print(".".ljust(50, "."))

arbol = ET.parse("Entrada0.xml")
raiz = arbol.getroot()
for nivel_1 in raiz:
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