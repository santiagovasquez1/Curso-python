# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:37:45 2019

@author: santi
"""

#Definicion de funciones

def mostrar(numero): #Variable de entrada
    "Esta funcion imprime el numero" #Dockstring opcional, descripcion de la funcion
    print (numero)
    
def adicionar(nombre):
    nombre="Hola "+nombre
    print(nombre)
    
def sumar2(a,b):
    r=a+b
    print(r)
  
def multi(a,b=3): #b es un parametro opcional, que se debe de inicializar
    r=a*b
    print (r)    

def muestra(a=1,b=2,c=3):
    print ("A es ", a)
    print ("B es ", b)
    print ("C es ", c)

    
#Codigo del programa
mostrar(1)
mostrar(2)
mostrar(3)
print(mostrar.__doc__)


adicionar("Shago")
sumar2(100,2)

multi(5)
multi(4,8)

#Uso de los keywords
muestra(b=6,a=8,c=20) #No importa el orden de como se entran las variables a la funcion
muestra(b=20)

