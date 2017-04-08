# creamos una función para cargar los valores
def cargar():
    dia=int(input("Ingrese el día: "))
    mes=int(input("Ingrese el mes: "))
    year=int(input("Ingrese el año: "))
    tupla=(dia,mes,year)    
    return tupla

# creamos una función para imprimir la tupla
def imprimir(tupla):
    print(tupla[0],tupla[1],tupla[2],sep=" - ",end=" ")

# bloque principal
tupla=cargar()
imprimir(tupla)
