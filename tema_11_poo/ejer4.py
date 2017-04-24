# creamos la clase
class Calculadora:
	# iniciamos con el método __init__
	def __init__(self):
		self.valor1=int(input("Ingrese el primer valor: "))
		self.valor2=int(input("Ingrese el segundo valor: "))

	# función para sumar
	def suma(self):
		suma=self.valor1+self.valor2
		print("El resultado de la suma de los valores es: ",suma)

	# función para restar
	def resta(self):
		resta=self.valor1-self.valor2
		print("El resultado de la resta de los valores es: ",resta)

	# función para calcular el producto
	def multiplicacion(self):
		pro=self.valor1*self.valor2
		print("El resultado de la multiplicación de los valores es: ",pro)

	# función para dividir
	def division(self):
		div=self.valor1/self.valor2
		print("El resultado de la división de los valores es: ",div)

	# función para imprimir
	def imprimir(self):
		print("Los valores son: ")
		print("Valor 1: ",self.valor1)
		print("Valor 2: ",self.valor2)


# bloque principal
calcular=Calculadora()
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()