# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)

# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")


# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()

