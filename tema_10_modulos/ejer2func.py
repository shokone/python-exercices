# importamos el modulo random
import random

# función para cargar un valor entero
def cargar():
    return int(input("Ingrese un valor entero: "))

# función para obtener un número aleatorio
def aleatorio():
    return random.randint(1,100)

# función para jugar a adivina el numerito
def adivina():
    num = aleatorio()
    imprimir("Bienvenido al juego de adivina el numerito")
    imprimir("A ver si eres capaz de adivinarlo")
    correcto=False
    while correcto == False:
        n = cargar()
        if num==n:
            imprimir("Has ganado")
            correcto=True
        elif num<n:
            imprimir("El valor introducido es menor")
        else:
            imprimir("El valor introducido es mayor")


# función para imprimir mensajes
def imprimir(texto):
    print(texto)
