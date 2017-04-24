# creamos la clase Cuenta
class Cuenta:
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad

	# imprimimos los datos
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)


# creamos la clase CajaAhorro
# esta clase hereda atributos de la clase Cuenta
class CajaAhorro(Cuenta):
	# iniciamos los atributos de la clase
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)

	# imprimimos los datos de la cuenta
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()


# creamos la clase PlazoFijo
# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes


	# calculamos la ganancia
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)


	# imprimimos los resultados
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()


# bloque principal
caja1=CajaAhorro("Manuel",5000)
caja1.imprimir()

plazo1=PlazoFijo("Isabel",8000,365,1.2)
plazo1.imprimir()
