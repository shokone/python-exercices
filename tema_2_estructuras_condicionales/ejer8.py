dia=int(input("Ingrese el dia: "))
mes=int(input("Ingrese el mes: "))
year=int(input("Ingrese el año: "))
if dia==1 and mes==1:
    print("Es el 1 de Enero de ",year)
elif dia==1 and mes==2:
    print("Es el 1 de Febrero de ",year)
else:
    print("Es "+dia+" - "+mes+" - "+year)
