# abrimos el fichero creado previamente
archivo = open("ejercicio.txt", "r+")

# obtenemos los datos del fichero
nombre=archivo.name
modo=archivo.mode
encoding=archivo.encoding

# lo cerramos
archivo.close()

# e imprimimos la información
print(nombre)
print(modo)
print(encoding)