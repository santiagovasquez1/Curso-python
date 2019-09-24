# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:16:54 2019

@author: santi
"""

#Uso de shallow copy y deep copy (Superficiales y profundas)

from copy import deepcopy #Libreria necesaria para la copia profunda
import numpy as np



nombres1=["Nicosio","Susana"]
nombres2=nombres1

#Ambos a la misma instancia
print ("nombres1",nombres1)
print ("nombres2",nombres2)

nombres2[1]="Shago" #Cambia tambien la lista madre, ya que usan la misma instancia
print ("nombres1",nombres1)

nombres2=["Ana","Luis"] #No cambia el original, ya que nombres 2, es un nuevo objeto
print ("nombres1",nombres1)
print ("nombres2",nombres2)

#Copia con slice de un objeto que no es compuesto

letras1=["a","e","i","o","u"]
letras2=letras1[:] #Copia cada una de las referencias

print ("Letras1",letras1)
print ("Letras2",letras2)

#Cambios en letras2
letras2[1]="z"

#Copia con slice de un objeto compuesto
fonemas1=["a","e","i",["ba","be","bi"]]
fonemas2=fonemas1[:] #Como es compuesto, no recorre cada uno de los elementos de la lista dentro de la lista

fonemas2[3][0]="DA"

#Uso de copia profunda para evitar este incoveniente
fonemas2=deepcopy(fonemas1)
fonemas2[3][0]="PA"
fonemas2.append([1,5,6])

QR10 = [1, 2, 3]
QR20 = [1, 5, 3]
QR11 = [1, 2, 3]
QR21 = [1, 2, 3]

QR10 = np.array(QR10,dtype=float)
QR20 = np.array(QR20,dtype=float)
QR11 = np.array(QR11,dtype=float)
QR21 = np.array(QR21,dtype=float)

QR10.dot(QR20)

print (QR10)