#Uso de metaclases

#Una clase es un objeto, es en realidad una instancia de una metaclase
#La metaclase de default es type
#Instancia --InstanceOf--> Clase --instanceof-->metaclase

#HAcen uso de metodos magicos. Operadores y comportamiento a los que se les puede hacer override

opcion1=input("Desea colocar el duplicador en valores 1? 1.si 2.no")
opcion2=input("Desea colocar el duplicador en valores 2? 1.si 2.no")

def duplicador(self):
    self.a=self.a*2
    self.b=self.b*2
    print ("Estoy en duplicador")

class valores1:
    pass

    def __init__(self, pa, pb):
        self.a=pa
        self.b=pb

    def muestra(self):
        print ("El valor a es:",self.a)
        print ("El valor b es:",self.b)

    #Adicionamos el metodo dinamicamente a la clase
if opcion1==1:
    Valores1.duplicador=duplicador

class valores2:
    pass

    def __init__(self, pa, pb):
        self.a=pa
        self.b=pb

    def muestra(self):
        print ("El valor a es:",self.a)
        print ("El valor b es:",self.b)

if opcion2==1:
    valores2.duplicador=duplicador

#instanciamos
val1=valores1(5,3)
val2=valores2(10,22)

#Usamos las intancias
print("valores 1")
val1.muestra()

if opcion1==1:
    val1.duplicador()
    val1.muestra()

print("-"*20)

print("valores 2")
val2.muestra()

if opcion2==1:
    val2.duplicador()
    val2.muestra()