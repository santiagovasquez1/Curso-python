# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:51:24 2019

@author: svasquez
"""

#Uso del Tuple
#Secuencia de objetos inmutable (no se llevan acabo modificaciones)
#Se define en parentesis
#Los elementos se separan por comas, incluso si es un solo elemento
#El acceso a este es mas rapido que a las listas

#Creacion de un tuple
meses=("Enero","Febrero","Marzo")
unDato=(5,)

#Acceso igual a las listas
#Crear nuevo tuple a traves de concatenacion
nuevo=meses+unDato

#Elminacion del tuple
del nuevo

#Conversion de listas a tuples
milista=[":D",":C",":)"]
nuevo=tuple(milista)

#Conversion a listas
Lista1=list(nuevo)

#Operaciones similares como con las listas
