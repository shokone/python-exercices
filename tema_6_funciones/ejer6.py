# creamos una funcion para la tabla de multiplicar
def tabla(num,terminos=10):
    for x in range(terminos):
        n=x*num
        # añadimos los parametros sep y end a la funcion print
        # con sep podemos añadir un caracter separando cada elemento, en este caso separaría 
        # el valor de n con la ","
        # con end incluimos un caracter al final de la impresión
        # esto también es útil para mostrar todos los datos en una única linea
        print(n,",",sep="",end="")
    print()

# bloque principal
print("Tabla del 3")
tabla(3)
print("Tabla del 2 con 7 terminos")
tabla(2,7)
print("Tabla del 5 con 20 terminos")
tabla(terminos=20,num=5)
