from random import randint

dado1=randint(1,6)
dado2=randint(1,6)
suma =dado1+dado2
print("El primer dado vale: ",dado1)
print("El segundo dado vale: ",dado2)
print("La suma de los dados es: ",suma)
if suma==9:
    print("Has ganado")
else:
    print("Has perdido")

