# función para cargar datos en el diccionario
def cargar(dic):
    dni=input("Ingrese un dni: ")
    nombre=input("INgrese el nombre: ")
    dic[dni]=nombre
    return dic

# función para imprimir los datos
def imprimir(dic):
    for key in dic:
        print(key+": "+dic[key])

# función para buscar 
def buscar(dic,dni):
    if dni in dic.keys():
        print(dic[dni])
    else:
        print("No existe nadie con ese dni")


# bloque principal
dic={}
dic=cargar(dic)
dic=cargar(dic)
dic=cargar(dic)
dic=cargar(dic)
imprimir(dic)
print("Buscar una persona")
dni=input("Introduzca el dni: ")
buscar(dic,dni)
