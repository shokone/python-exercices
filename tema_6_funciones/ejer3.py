# creamos la función para solicitar la carga de un valor entero
def carga():
    return int(input("Ingrese un valor entero: "))

# creamos la función para calcular la suma
def sumar(num1,num2):
    return num1+num2

# creamos la función para calcular la resta
def resta(num1,num2):
    return num1-num2

# creamos la función para mostrar los valores
def mostrar(num1,num2):
    print("Los valores son "+str(num1)+" y "+str(num2))

# bloque principal
num1=carga()
num2=carga()
mostrar(num1,num2)
print(sumar(num1,num2))
print(resta(num1,num2))
