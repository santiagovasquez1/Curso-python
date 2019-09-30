def fibonacciIterativo(n):
    a=0
    b=1

    if n==0:
        return 0
    for i in range(n-1):
        anterior=a
        a=b
        b=anterior+b
    return b

def fibonacciRecursivo(n): #Uso de funcion recursiva en python
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2)

calculados= {0:0,1:1}
def fibonaccirecursivo2(n):
    if n in calculados:
        return calculados[n]
    else:
        calculados[n]=fibonaccirecursivo2(n-1)+fibonaccirecursivo2(n-2)
        return calculados[n]




print ("Iterativo", fibonacciIterativo(35))
print ("Recursivo",fibonacciRecursivo(35))
print ("Memoizado",fibonaccirecursivo2(35))