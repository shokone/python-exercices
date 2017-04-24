# creamos la clase banco
class Banco:
	# inicializamos
	def __init__(self):
		self.cliente1=Cliente("Ivan")
		self.cliente2=Cliente("Marcos")
		self.cliente3=Cliente("Juan")

	# función para operar
	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)

	# función para obtener los depósitos totales
	def depositos(self):
		total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()



# creamos la clase Cliente
class Cliente:
	# inicializamos
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0

	# función para depositar dinero
	def depositar(self,cantidad):
		self.cantidad+=cantidad

	# función para extraer dinero
	def extraer(self,cantidad):
		self.cantidad-=cantidad

	# función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad

	# función para imprimir los datos del cliente
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)


# bloque principal
banco1=Banco()
banco1.operacion()
banco1.depositos()