#Uso de range y for

#Uso de range n elementos, de 0 a n-1

lista=range (10)
lista2=range (0,50,5) #Incremento en particular
nombres=["Shago","Susana","Pedro"]

# Uso de for con un rango, es un iterador para recorrer una lista,mas parecido al foreach en C#
sumatoria=0

for nombre in nombres:
    print ("El nombre es: ",nombre)
print ("-"*20)

for n in lista2:
    sumatoria+=n
    print (sumatoria)
print ("-"*20)

#Uso de manera similar en otros lenguajes
"""
for n in range (0,100):
    print (n)
"""

#Ciclos regresivo

"""
sumatoria=0
for n in range (100,-1,-5):
    sumatoria+=n
    print (n)
"""

#Uso del continue

for n in range(11):
    #print (n)
    if n%2!=0:
        continue
    print ("Este es un numero par ",n)
    
#Ejemplo usando el else y el breack
    
m=int(input ("Ingresa el numero "))

for n in range (11):
    print (n)
    if n==m:
        print ("Numero hayado con exito")
        break
else:
    print ("No se encontro el resultado")
    
print ("-"*20)