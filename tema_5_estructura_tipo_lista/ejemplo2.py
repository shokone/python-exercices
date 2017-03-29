# declaramos una lista vacia
lista=[]

# creamos un bucle para escribir cada elemento del array
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

# una vez rellenado el array, lo imprimimos
print(lista)

# y aprendemos una cosa nueva, como obtener la longitud del array
print(len(lista))

