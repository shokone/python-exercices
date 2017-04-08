# creamos la primera función para crear la tupla
def crear(d1,d2,d3):
    tupla=(d1,d2,d3)
    return tupla

# creamos una función para convertir a lista
def convertir_lista(tupla):
    return list(tupla)

# creamos una función para convertir a tupla
def convertir_tupla(lista):
    return tuple(lista)

# modificar lista
def modificar(lista,pos,data):
    lista[pos]=data
    return lista

# creamos una función para imprimir los datos
def imprimir(data):
    print(data)


# bloque principal
tupla=crear("hola",1,"mundo")
print("Imprimimos la tupla")
imprimir(tupla)
print("Convertimos a lista")
lista=convertir_lista(tupla)
imprimir(lista)
print("Modificamos la lista")
lista=modificar(lista,1," que tal ")
print("Imprimimos la lista")
imprimir(lista)
print("Volvemos a convertir en tupla")
tupla=convertir_tupla(lista)
imprimir(tupla)
