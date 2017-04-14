# función para comprobar si la cadena es capicúa
def capicua(string):
    ind=-1
    cont=0
    for x in range(0,len(string)//2):
        if string[x]==string[ind]:
            cont+=1
        ind-=1
    print(string)
    if cont==len(string)//2:
        print("La cadena es capicúa")
    else:
        print("La cadena no es capicúa")

# bloque principal
string=input("Introduzca una cadena de texto: ")
capicua(string)
