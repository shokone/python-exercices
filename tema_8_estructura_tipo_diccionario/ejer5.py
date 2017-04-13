# función para cargar los datos de los alumnos
def cargar():
    alumnos={}
    cont="s"
    while cont=="s":
        dni=int(input("Ingrese el código del alumno: "))
        nom=input("Ingrese el nombre del alumno: ")
        lista=[]
        cont2="s"
        while cont2=="s":
            materia=input("Ingrese el nombre de la materia: ")
            nota=int(input("Ingrese la nota: "))
            lista.append((materia,nota))
            cont2=input("Desea cargar otra materia [s/n]: ")
        alumnos[dni]=(nom,lista)
        cont=input("Desea cargar los datos de otro alumno [s/n]: ")
    return alumnos

# función para mostrar el listado de alumnos
def imprimir(alumnos):
    for dni in alumnos:
        print("Dni del alumno: ",dni)
        print("Nombre del alumno: ",alumnos[dni][0])
        print("Materias que cursa y notas obtenidas")
        for materia,nota in alumnos[dni][1]:
            print(materia,nota)

# función para consultar los datos de un alumno
def consulta(alumnos):
    dni=int(input("Ingrese el dni del alumno a consultar: "))
    if dni in alumnos:
        for materia,nota in alumnos[dni][1]:
            print(materia,nota)

# bloque principal
alumnos=cargar()
imprimir(alumnos)
consulta(alumnos)     
