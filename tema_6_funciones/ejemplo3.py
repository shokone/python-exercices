# Primero la funcion para cargar el valor entero
def carga():
    num=int(input("Ingrese el valor: "))
    return num

# funcion para calcular la suma
def suma(num1,num2):
    sumar=num1+num2
    print("La suma de los valores es: ",sumar)

num1=carga()
num2=carga()
suma(num1,num2)

