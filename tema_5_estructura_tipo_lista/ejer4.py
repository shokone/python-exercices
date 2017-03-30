paises=[]
habitantes=[]
num=int(input("Ingrese el total de elmentos: "))
# solicitamos la carga de los datos
for x in range(num):
    pais=input("Ingrese el nombre del pais: ")
    hab=int(input("Ingrese el total de habitantes: "))
    paises.append(pais)
    habitantes.append(hab)

# imprimimos las listas
for x in range(num):
    print(paises[x]+" "+habitantes[x])

# ordenamos
for x in range(num):
    for k in range(num):
        if habitantes[k]<habitantes[k+1]:
            auxp=paises[k]
            auxh=habitantes[k]
            paises[k]=paises[k+1]
            habitantes[k]=habitantes[k+1]
            paises[k+1]=auxp
            habitantes[k+1]=auxh

for x in range(num):
    print(paises[x]+" "+habitantes[x])
