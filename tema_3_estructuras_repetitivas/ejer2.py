personas=int(input("Cuantas personas hay:"))
x=1
suma=0
while x<=personas:
    altura=float(input("Ingrese la altura: "))
    suma=suma+altura
    x=x+1
promedio=suma/personas
print("El promedio es ")
print(promedio)
