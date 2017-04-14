# función para invertir el string
def inverso(string):
    ind=-1
    for x in range(len(string)):
        print(string[ind],end="")
        ind-=1

# bloque principal
string=input("Ingresar una palabra:")
inverso(string)
