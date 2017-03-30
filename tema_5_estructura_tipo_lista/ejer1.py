lista=[213,44,578,123,100,56,78,1000,2345,1278]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1
    
print("La lista esta constituida por los elementos: ")
print(lista)
print("Hay un total de valores mayores a 100 de ")
print(cantidad)
