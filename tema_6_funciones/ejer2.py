# definimos una función para solicitar la carga del string
def carga():
    return input("Ingrese un string: ")

# definimos una función para comprobar el total de vocales
def comprobar(string):
    cant=0
    lista=["a","e","i","o","u"]
    for x in range(len(string)):
        for k in range(len(lista)):
            if string[x] == lista[k]:
                cant=cant+1
    print("El total de vocales es ",cant)

# bloque principal
string1=carga()
string2=carga()
string3=carga()
print(string1)
comprobar(string1)
print(string2)
comprobar(string2)
print(string3)
comprobar(string3)
