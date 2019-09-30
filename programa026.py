def pares(n):
    assert(n%2==0) #Assert evalua una expresion, si esta es falsa levanta un exception de tipo assertionerror
    print ("Es par")

pares(4)
#pares(15)

"""
try:    
    print ("Vamos a intentar con impar")
    pares(5)
except AssertionError : #Si deseamos capturar todas, eliminamos el tipo que deseamos capturar
    
    print ("Fue un impar")
else:
    print ("Es par")
"""

#Uso de finally, se usa para poner codigo que se ejecuta independiente si dio o no una excepcion

try:    
    print ("Vamos a intentar con impar")
    pares(5)
except:   
    print ("Fue un impar")
else:
    print ("Es par")
finally:
    print ("Esto es el uso del finally")

#El argumento a info sobre la excepcion

"""
a="Hola"
try:
    x=int(a)
    print (x)
except ValueError as argumento:
    print ("El argumento es ",argumento)
"""

#Captura de multiples exepciones

class fue1(RuntimeError):
    def _init_(self): #Constructor
        print ("Desde la clase")
    
class fue2(RuntimeError):
    def _init_(self,argumento):
        self.args=argumento

def checar(n):
    if n==1:
        raise fue1
    if n==2:
        raise fue2("Error")
    print ("Todo bien")


try:
    checar(4)
except fue1:
    print ("Excepcion para el 1")
except fue2:
    print ("Exepcion para el 2")