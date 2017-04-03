# realizamos la funcion
def calcular(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

# bloque principal
print("La suma de 2 y 4:")
print(calcular(1,2))
print("La suma de 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
print(calcular(1,2,3,4,5,6,7,8,9,10))

