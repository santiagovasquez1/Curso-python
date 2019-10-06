#Sobrecarga de operadores
#+ _add_
#- _sub_
#** _pow_
#& _and_
#| _or_
#^ _xor_


import math

class Vector:

    def __init__(self, px=0, py=0):
        self.x=px
        self.y=py

    #Sobrecarfa +
    def __add__(self,operando):
        mx=self.x+operando.x
        my=self.y+operando.y
        return Vector(mx,my)

    #Calculamos la magnitud
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def __str__(self):
        return "(%.2f,%.2f)" %(self.x,self.y)

    #Sobrecarga de ==
    def __eq__(self, operando):
        return self.magnitud()==operando.magnitud()

    #Sobrecarga de >
    def __gt__(self, operando):
        return self.magnitud()>operando.magnitud()


#Uso en un programa

def Comparacion(val1,val2):
    if (val1==val2):
        print ("Ambos vectores son iguales")
    else:
        print ("Los vectores son diferente")

def Mayor(val1,val2):
    if (val1>val2):
        print("El vector1 es mayor que el vector2")
    else:
        print("El vector2 es mayor que el vector1")

a=Vector(5,3)
b=Vector(-1,2)
d=Vector(5,3)

print(a)
print(b)

#Suma de vectores
c=a+b
print (c)
print (a.magnitud())

Comparacion(a,b)
Comparacion(a,d)
Mayor(a,b)



    