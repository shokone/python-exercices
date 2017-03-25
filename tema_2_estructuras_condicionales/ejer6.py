num=int(input("Ingresa un valor entero:"))
if num<10:
    print("Es un numero de 1 digito")
else:
    if num<100:
        print("Es un numero de 2 digitos")
    else:
        if num<1000:
            print("Es un numero de 3 digitos")
        else:
            print("El numero tiene mas de 3 digitos")

