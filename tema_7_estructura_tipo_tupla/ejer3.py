# función para cargar el nombre y sueldo del empleado
def cargar():
    nombre=input("Ingrese el nombre: ")
    sueldo=float(input("Ingrese el sueldo: "))
    return (nombre,sueldo)

# función para comprobar quien tiene un sueldo mayor
def sueldo_mayor(emp1,emp2):
    if emp1[1]>emp2[1]:
        print("El empleado con nombre "+emp1[0]+" tiene un sueldo mayor")
    else:
        print("El empleado con nombre "+emp2[0]+" tiene un sueldo mayor")


# bloque principal
emp1=cargar()
emp2=cargar()
sueldo_mayor(emp1,emp2)
