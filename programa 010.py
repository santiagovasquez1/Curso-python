#Uso de while de la forma general
"""
n=0

while n<10:
    print "Hola"
    print n
    n+=1

print "-"*20

#Uso de continue, fuerza la siguienta vuelta del ciclo, ignorando lo que siga

n=0

while n<10:
    print "Hola"
    print n
    n+=1
    if n%3==0:
        continue
    print "Esto solo se imprime a veces"

print "\nAfuera del while"
"""

#Uso del break, fuerza el ciclo a salir
"""
n=0

while n<10:
    print n
    if n==5:
        break

    print "Esto solo se imprime mientras se reccorra el ciclo"
    n+=1


print "\nAfuera del while"
"""

#Uso del else dentro del ciclo while

n=0
m=int(raw_input("Ingresa un numero "))

while n<10:
    print n
    if n==m:
        break

    n+=1
    print "Sigo imprimiendo"
else:
    print "No encontre el numero"

print "\nAfuera del while"
