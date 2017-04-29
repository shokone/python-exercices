# definimos nuestra clase lista
class Lista:
	# inicializamos nuestra clase
	# como atributo utilizaremos una lista
	def __init__(self,lista):
		self.lista=lista


	# método para imprimir la lista
	def imprimir(self):
		print(self.lista)


	# redefinimos la suma
	def __add__(self,valor):
		n=[]
		for x in range(len(self.lista)):
			n.append(self.lista[x]+valor)
		return n

	# redefinimos la resta
	def __sub__(self,valor):
		n=[]
		for x in range(len(self.lista)):
			n.append(self.lista[x]-valor)
		return n


	# redefinimos el producto
	def __mul__(self,valor):
		n=[]
		for x in range(len(self.lista)):
			n.append(self.lista[x]*valor)
		return n


	# redefinimos la división
	def __floordiv__(self,valor):
		n=[]
		for x in range(len(self.lista)):
			n.append(self.lista[x]/valor)
		return n



# bloque principal
lista=Lista([5,8,15,23])
lista.imprimir()
print(lista+5)
print(lista-5)
print(lista*5)
print(lista//5)