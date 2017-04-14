# función para obtener los meses
def meses(num):
    lista=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return lista[num:]

# bloque principal
print("Imprimir los meses restantes hasta fin de año")
print(meses(int(input("Ingrese el número del mes actual: "))))
