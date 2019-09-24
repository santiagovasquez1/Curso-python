#En este programa hacemos uso del modulo

#Donde busca los modulos python
#Directorio actual
#Variable dentro PYTHONPATH
#Path de default

import Modulo1 as md1 #Importacion normal
#from Modulo1 import multi #importacion de una funcion desde un modulo
from Modulo1 import *

m=3
n=5

c=suma(m,n)
print (c)
p=multi(n,m)
print (p)

#Variable local y luego la del modulo
print(x)
x=50
print(x)
imprimir()

#Uso de dir
Contenido_modulo=dir(md1)
print(Contenido_modulo)

"""
Hacemos que se ejecute nuevamente el codigo del modulo
y se carga nuevamente
reload(md1)
"""
import Paquete_modulos
Paquete_modulos.adios()
Paquete_modulos.Hola()
