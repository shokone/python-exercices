cant1=0
cant2=0
cant3=0
num=int(input("Ingrese la cantidad de triángulos: "))
for f in range(num):
    lado1=int(input("Ingrese lado primer lado: "))
    lado2=int(input("Ingrese lado segundo lado: "))
    lado3=int(input("Ingrese lado tercer lado: "))
    if lado1==lado2 and lado1==lado3:
        print("Es un triangulo equilatero.")
        cant1=cant1+1
    else:
        if lado1==lado2 or lado1==lado2 or lado2==lado3:
            print("Es un triángulo isosceles.")
            cant2=cant2+1
        else:
            print("Es un triángulo escaleno.")
            cant3=cant3+1

print("Cantidad de triángulos equilateros: ",cant1)
print("Cantidad de triángulos isósceles:   ",cant2)
print("Cantidad de triángulos escalenos:   ",cant3)
