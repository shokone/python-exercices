# definimos la función para cargar los datos y obtener las edades
def cantidad_mayores(edad,*edades):
    cant=0
    if edad>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant


# bloque principal

print("La cantidad de personas mayores a 18 son:", cantidad_mayores(5,18,21,47,16,32))
print("La cantidad de personas mayores a 18 son:", cantidad_mayores(22,17,32,8,24))
print("La cantidad de personas mayores a 18 son:", cantidad_mayores(45,12,25,8,19))
