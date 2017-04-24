# creamos nuestra clase
class Triangulo:
	# inicializamos
	def inicializar(self):
		self.lado1=int(input("Ingrese el valor del primer lado: "))
		self.lado2=int(input("Ingrese el valor del segundo lado: "))
		self.lado3=int(input("Ingrese el valor del tercer lado: "))

	# imprimimos 
	def imprimir(self):
		print("Los lados del triángulo tienen el valor de")
		print("Lado 1: ",self.lado1)
		print("Lado 2: ",self.lado2)
		print("Lado 3: ",self.lado3)

	# comprobamos el lado mayor
	def mayor(self):
		print("El lado mayor es")
		if self.lado1>self.lado2 and self.lado1>self.lado3:
			print("Lado 1: ",self.lado1)
		elif self.lado2>self.lado3:
			print("Lado 2: ",self.lado2)
		else:
			print("Lado 3: ",self.lado3)

	# comprobamos el tipo de triángulo
	# equilátero -> todos los lados iguales
	# isósceles -> dos lados iguales
	# escaleno -> todos los lados desiguales
	def tipo(self):
		if self.lado1==self.lado2 and self.lado1==self.lado3:
			print("Es un triángulo equilátero")
		elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
			print("Es un triángulo escaleno")
		else:
			print("Es un triángulo isósceles")

# bloque principal
figura=Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()
