#Declaramos las listas
alumnos=[]
notas=[]

# Rellenamos los datos
for x in range(5):
    nombre=input("Ingrese el nombre del alumno: ")
    nota=int(input("Ingrese la nota del alumno: "))
    alumnos.append(nombre)
    notas.append(nota)

# imprimimos los datos
for x in range(5):
    print(alumnos[x]+" "+str(notas[x]))

