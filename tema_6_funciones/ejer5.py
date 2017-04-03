# creamos una función para cargar los datos
def cargar(total):
    lista=[]
    for x in range(total):
        num=int(input("Ingrese un valor entero: "))
        lista.append(num)
    return lista

# creamos una función para separar las listas de numeros positivos y negativos
def separar(lista):
    pos=[]
    neg=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            pos.append(lista[x])
        else:
            neg.append(lista[x])

    return [pos,neg]

# declaramos una tercera función para imprimir los valores
def imprimir(mensaje,lista):
    print("-"*10)    
    print(mensaje)
    print(lista)
    print("-"*10)

# bloque principal
lista=cargar(10)
pos,neg=separar(lista)
imprimir("Imprimimos la lista original",lista)
imprimir("Imprimimos la lista de numeros positivos",pos)
imprimir("Imprimimos la lista de numeros negativos",neg)

