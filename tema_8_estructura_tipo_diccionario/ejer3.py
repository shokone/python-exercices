# función para cargar los productos
def cargar():
    productos={}
    continuar="s"
    while continuar=="s":
        cod=int(input("Ingrese el código de producto: "))
        nom=input("Ingrese el nombre del producto: ")
        precio=float(input("Ingrese el precio del producto: "))
        stock=int(input("Ingrese el total de stock del producto: "))
        productos[cod]=(nom,precio,stock)
        continuar=input("Desea cargar otro producto[s/n]?")
    return productos

# función para imprimir el listado de productos
def imprimir(productos):
    print("Listado de productos")
    for cod in productos:
        print(cod,productos[cod][0],productos[cod][1],productos[cod][2])

# función para consultar un producto mediante su clave
def consulta(productos):
    cod=int(input("Ingrese el código de articulo: "))
    if cod in productos:
        print(productos[cod][0],productos[cod][1],productos[cod][2])

# función para mostrar el listado de productos con stock 0
def listado_cero(productos):
    print("Listado de productos con stock 0")
    for cod in productos:
        if productos[cod][2]==0:
            print(cod,productos[cod][0],productos[cod][1],productos[cod][2])

# bloque principal
productos=cargar()
imprimir(productos)
consulta(productos)
listado_cero(productos)
