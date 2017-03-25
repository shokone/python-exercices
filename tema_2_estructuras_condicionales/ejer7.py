preguntas=int(input("Ingrese el total de preguntas:"))
correctas=int(input("Ingrese el total de preguntas correctas:"))
porcentaje=correctas * 100 / preguntas
if porcentaje>=90:
    print("Sobresaliente")
else:
    if porcentaje>=70:
        print("Notable")
    else:
        if porcentaje>=50:
            print("Aprobado")
        else:
            print("Suspendido")

