# primera función para cargar los valores
def cargar():
    lista=[]
    for x in range(10):
        val=int(input("Ingrese un valor: "))
        lista.append(val)
    return lista

# función para retornar la mitad de la lista
def mitad(lista):
    return lista[:(len(lista)//2)]

# función para imprimir una lista
def imprimir(lista):
    print("La lista contiene")
    print(lista)

# bloque principal
lista=cargar()
lista2=mitad(lista)
imprimir(lista)
imprimir(lista2)
