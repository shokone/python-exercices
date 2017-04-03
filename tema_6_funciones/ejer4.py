# declaramos la función para cargar los datos
def cargar():
    print("Cargamos los datos")
    nom=[]
    precio=[]
    for x in range(5):
        n=input("Ingrese el nombre del articulo: ")
        p=float(input("Ingrese el precio del articulo: "))
        nom.append(n)
        precio.append(p)
    
    return [nom,precio]

# creamos la función para imprimir cada articulo con sus datos
def mostrar(nom,precio):
    print("-"*len(nom))
    print("Listado de articulos")
    print("-"*len(nom))
    for x in range(len(nom)):
        print(nom[x]+": "+str(precio[x]))

# creamos la función para imprimir el nombre del artículo más caro
def mas_caro(nom,precio):
    print("-"*len(nom))
    print("Articulo mas caro")
    print("-"*len(nom))
    mayor=0
    for x in range(len(precio)):
        if precio[x]>mayor:
            mayor=precio[x]
            pos=x

    print(nom[x]+": "+str(precio[x]))

# creamos la función para obtener los articulos con un precio menor al insertado
def menores(nom,precio):
    print("-"*len(nom))
    print("Articulos superiores a")
    print("-"*len(nom))
    num=float(input("Ingrese el precio: "))
    for x in range(len(nom)):
        if precio[x]<num:    
            print(nom[x]+": "+str(precio[x]))

# bloque principal
nombre,precio=cargar()
mostrar(nombre,precio)
mas_caro(nombre,precio)
menores(nombre,precio)

