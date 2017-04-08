# creamos una primera función para cargar una lista de n string
def cargar(cant):
    lista=[]
    for x in range(cant):
        string=input("Ingrese un string: ")
        lista.append(string)
    return lista

# creamos una función para mostrar las palabras con más de 5 caracteres
def comprobar(lista):
    for x in range(len(lista)):
         if len(lista[x])>5:
             print(lista[x],"",sep=" - ",end="")


# bloque principal
lista=cargar(5)
comprobar(lista)

