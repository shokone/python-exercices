# importamos la función factorial del modulo math
from math import factorial

#obtenemos el valor
valor=int(input("Ingrese un valor entero: "))
# calculamos el factorial
fac=factorial(valor)
# imprimimos
print("El valor factorial de ",valor," es ",fac)
