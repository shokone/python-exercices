# abrimos el fichero
# utilizamos la estructura with
with open("ejer-with.txt", "w+") as file:
	# escribimos en el
	file.write('Este es el ejercicio 3 con la estructura with')
	# mostramos los datos
	# y el fichero se cierra solo
	print(file.name)
	print(file.mode)
	print(file.encoding)