# creamos una función para cargar los datos
def cargar():
    nombre=input("Ingrese el nombre del pais: ")
    habitantes=int(input("Ingrese el total de habitantes: "))
    return (nombre,habitantes)

# creamos una función para imprimir los datos
def imprimir(data):
    for x in range(len(data)):
        print(data[x])

# una tercera función para comprobar que pais tiene más habitantes
def mayor(tupla):
    pos=0
    mayor=0
    for x in range(len(tupla)):
        if tupla[x][1]>mayor:
            mayor=tupla[x][1]
            pos=x
    print("El pais con más habitantes es ",tupla[x][0])


# bloque principal
pais1=cargar()
pais2=cargar()
pais3=cargar()
pais4=cargar()
pais5=cargar()
tupla=(pais1,pais2,pais3,pais4,pais5)
imprimir(tupla)
mayor(tupla)
