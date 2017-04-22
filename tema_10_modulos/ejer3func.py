# importamos el modulo random
import random

# función para generar la lista de valores aleatorio
def cargar():
    lista=[]
    for x in range(20):
        num=random.randint(0,100)
        lista.append(num)
    return lista

# función para imprimir 
def imprimir(lista):
    print(lista)

# función para ordenar la lista
def ordenar(lista):
    return lista.sort()
