num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))
if num1==num2 and num1==num3:
    total=num1+num2
    total=total*num3
    print("El resultado es: ",total)
else:
    print("Los numeros no son iguales")

