#Uso de if,elif y else
#Bloque de codigo


#Uso normal de if
a=float(raw_input("Ingrese un valor "))

if a>0:
    print "El numero es positivo"

if a<0:
    print "El numero es negativo"
    print "Esto tambien hace parte del bloque"
    
print "Fin ejemeplo1"



#Uso de if con else

b=float(raw_input("Ingresa el numero "))

if b>0:
    print "El numero es positivo"
else:
    print "El numero es negativo"

print "-"*20


#Uso de if con elseif

c=float(raw_input("Ingresa el numero "))

if c>0:
    print "El  numero es positivo"
elif  c==0:
    print "El numero es cero"
else:
    print "El numero es negativo"

print "-"*20
