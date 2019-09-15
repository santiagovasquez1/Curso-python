#Pedir informacio al usuario
#Usano iput
#Usando raw input

#Al escribir cadenas hay que ponerlas con ""

"""
nombre = input ("Dame tu nombre ")
base_=input ("Dame la base " )
altura= input ("Dame la altura ")
area = base_*altura
perimetro = 2*(base_+altura)

#print "Hola %s  el area es  %.2f  y  el perimetro es %.2f" %(nombre,area,perimetro)
print "Hola ", nombre," el area es ",area, " y el perimetro es ",perimetro
"""

#Usando el raw_input mas recomendado
"""
nombre=str(raw_input("Dame tu nombre: "))
base=float(raw_input ("Dame la base : " ))
altura=float(raw_input("Dame la altura: "))
area = base*altura
perimetro = 2*(base+altura)
print "Hola %s  el area es  %.2f  y  el perimetro es %.2f" %(nombre,area,perimetro)
"""

#Funcion type, nos indica el tipo del objeto, cuando se use raw es mejor usar el constrructor para el ingreso de las variables
print "Con input"
a=input ("Un valor ")
print (a,type(a))

print "Ahora raw_input"
b=raw_input("mismo valor ")
print (b,type(b))

