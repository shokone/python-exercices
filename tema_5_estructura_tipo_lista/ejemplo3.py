# declaramos una lista vacia
lista=[]

# creamos un bucle para escribir cada elemento del array
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

# creamos una variable en la que guardamos el primer elemento
mayor=lista[0]

#utilizamos un bucle para recorrer el array
for x in range(1,5):
    # comprobamos si es mayor al almacenado
    if lista[x]>mayor:
        mayor=lista[x]

#imprimimos la lista completa
print(lista)
# imprimimos el numero mayor
print(mayor)

