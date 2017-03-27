string=input("Ingrese una cadena de caracteres: ")
texto=""
for x in range(len(string)):
    if x != len(string):
        texto=texto+string[x]+" "
    else:
        texto=texto+string[x]

print(string)
print(texto)
