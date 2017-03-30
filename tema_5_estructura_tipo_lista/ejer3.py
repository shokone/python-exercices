paises=[]
num=int(input("Ingrese el total de paises: "))
for x in range(num):
    pais=input("Ingrese el nombre del pais: ")
    paises.append(pais)

paises.sort()
print(paises)
