lista=[]
cant=1
for x in range(50):
    lista.append([])
    valor=1
    for k in range(cant):
        lista[x].append(valor)
        valor=valor+1
    cant=cant+1

print(lista)
