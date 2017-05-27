archivo = open("ejemplo.txt", "r+")
content = archivo.read()
nombre=archivo.name
modo=archivo.mode
encoding=archivo.encoding
archivo.close()
print(nombre)
print(modo)
print(encoding)
