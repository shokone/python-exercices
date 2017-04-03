# declaramos una función para mostrar el mensaje de bienvenida
def bienvenida(mensaje):
    print(mensaje)
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
def despedida(mensaje):
    print("********************************************************")
    print(mensaje)

# cargamos nuestras funciones
bienvenida("Bienvenido a nuestro programa")
suma()
despedida("Gracias por utilizar nuestro programa")

