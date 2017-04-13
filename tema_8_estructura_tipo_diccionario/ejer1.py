# función para añadir valores al diccionario
def cargar(dic):
    en=input("Ingrese un string en inglés: ")
    es=input("Ingrese un string en español: ")
    dic[en]=es
    return dic
  
# creamos una función para listar el diccionario
def imprimir(dic):
    for key in dic:
        print(key+": "+dic[key])

# creamos una función para buscar
def buscar(dic,string):
    if string in dic.keys():
        print(dic[string])
    else:
        print("Esa key no existe")

# bloque principal
dic={}
dic=cargar(dic)
dic=cargar(dic)
imprimir(dic)
print("Buscar una palabra")
buscar(dic,"house")
