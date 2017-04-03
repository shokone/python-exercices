# declaramos una función para mostrar el mensaje de bienvenida
def bienvenida():
    print("Bienvenido a nuestro programa")
    print("Este programa calculara la suma de dos valores enteros")
    print("********************************************************")

# la segunda funcion
# solicitara la carga de valores por teclado 
# y mostrara la suma de los valores
def suma():
    num1=int(input("Ingrese el primer valor:"))
    num2=int(input("Ingrese el segundo valor:"))
    suma=num1+num2
    print("La suma de los valores es: ",suma)

# por ultimo
# la funcion para mostrar el mensaje de despedida
def despedida():
    print("********************************************************")
    print("Gracias por utilizar nuestro programa")

# cargamos nuestras funciones
bienvenida()
suma()
despedida()

