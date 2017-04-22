# primero importaremos los modulos necesarios
from math import sqrt, pow

# cargaremos el valor entero
def cargar():
    return int(input("Ingrese un valor entero: "))

# calcularemos la raíz cuadrada
def raiz(num):
    return sqrt(num)

# calculamos el exponente
def exponente(num,exp):
    return pow(num,exp)

# bloque principal
num=cargar()
print("El valor utilizado es ",num)
r=raiz(num)
print("La raíz cuadrada da el resultado de ",r)
print("El valor elevado al cuadrado da el resultado de ",exponente(num,2))
print("El valor elevado al cubo da el resultado de ",exponente(num,3))
