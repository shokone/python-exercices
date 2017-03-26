n=int(input("Cuantos empleados tiene la empresa: "))
x=1
menor=0
mayor=0
coste=0
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo<=500:
        menor=menor+1
    else:
        mayor=mayor+1
    coste=coste+sueldo
    x=x+1
print("Cantidad de empleados con sueldos mayor a 500")
print(menor)
print("Cantidad de empleados con sueldos mayor a 500")
print(mayor)
print("Gastos total de la empresa en sueldos")
print(coste)
