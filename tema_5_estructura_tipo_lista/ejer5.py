paises=[]
habitantes=[]
num=int(input("Ingrese el total de paises: "))
x=0
#rellenamos las listas
for x in range(num):
    p=input("Ingrese el nombre del pais: ")
    h=int(input("Ingrese el total de habitantes: "))
    paises.append(p)
    habitantes.append(h)

# imprimimos las listas
for x in range(num):
    print(paises[x]+" "+str(habitantes[x]))

