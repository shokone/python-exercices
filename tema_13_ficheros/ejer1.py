# abriremos el fichero para el ejercicio
# como no existe, lo creamos
archivo = open("ejercicio.txt", "w+")

# escribimos en el fichero
content = archivo.write('Este es el ejercicio 1')

# y lo cerramos
archivo.close()