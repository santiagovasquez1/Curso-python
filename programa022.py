#Operadores lambda, similares a las funciones lambdas en c#

"""
valor=lambda a,b: a*a+2*a*b+b*b #Trinomio cuadrado perfecto
print (valor(2,3))
"""

#Uso de map
#Invoca una funcion haciendo uso de una secuencia

def cuadrado(valor):
    return valor**2

def impares(valor):

    if valor%2 !=0:
        return(valor)

def suma(a,b):
    return a+b

valores=[2,5,10]
resultados= list (map (cuadrado,valores))
print (resultados)

#Uso de map con lambda

valores=[2,5,10]
resultados=list(map (lambda x: x*x,valores))
print (resultados)

valores=[1,4,7,8,9,10,25,32,15,99,2]
filtrados=list (filter(impares,valores))
print(filtrados)

#Filtrado con lambda
filtrados=list(filter(lambda x: x%2!=0,valores))
print(filtrados)

