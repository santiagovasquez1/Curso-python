dias=["Lunes","Mates","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#Invocacion de iter
mi_iterador=iter(dias)

#Usamos el iterable next para obtener el elemento siguiente
"""
print (next (mi_iterador))
print (next(mi_iterador))
"""

"""
while mi_iterador:
    try:
        d=next(mi_iterador)
        print(d)
    except StopIteration as identifier:
        print ("No hay mas elementos, forzamos la salida")
        break
print("-"*20)
"""

"""
def dias_generador():
    yield("Lunes")
    yield("Martes")
    yield ("Miercoles")
    yield ("Jueves")
    yield ("Viernes")

dias=dias_generador

while mi_iterador:
    try:
        d=next(mi_iterador)
        print(d)
    except StopIteration as identifier:
        print ("No hay mas elementos, forzamos la salida")
        break
print("-"*20)

"""

#Generador para potencias de 2

def potencias2():
    b=1
    while b>0:
        yield b
        b+=b
        if b>300:
            raise StopIteration #Establecer una excepcion dentro de nuestra funcion

binarios=potencias2()

for x in binarios:
    print(x)

