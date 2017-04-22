# importamos el modulo random
import random

# función para cargar valores aleatorios
def cargar():
    lista=[]
    for x in range(10):
        num=random.randint(1,1000)
        lista.append(num)
    return lista

# función para imprimir la lista
def imprimir(lista):
    print(lista)
