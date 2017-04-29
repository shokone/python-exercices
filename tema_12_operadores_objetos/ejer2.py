# creamos nuestra clase Rectangulo
class Rectangulo():
	# inicializamos los atributos
	def __init__(self,menor,mayor):
		self.menor=menor
		self.mayor=mayor

	# devolvemos el valor de la superficie del rectángulo
	def superficie(self):
		return self.menor*self.mayor

	# redefinimos el operador ==
	def __eq__(self,obj):
		if self.superficie()==obj.superficie():
			return True
		else:
			return False

	# redefinimos el operador !=
	def __ne__(self,obj):
		if self.superficie()!=obj.superficie():
			return True
		else:
			return False

	# redefinimos el operador >
	def __gt__(self,obj):
		if self.superficie()>obj.superficie():
			return True
		else:
			return False

	# redefinimos el operador >=
	def __ge__(self,obj):
		if self.superficie()>=obj.superficie():
			return True
		else:
			return False

	# redefinimos el operador <
	def __lt__(self,obj):
		if self.superficie()<obj.superficie():
			return True
		else:
			return False

	# redefinimos el operador <=
	def __le__(self,obj):
		if self.superficie()<=obj.superficie():
			return True
		else:
			return False

	

# bloque principal
rectangulo1=Rectangulo(5,5)
rectangulo2=Rectangulo(8,20)
if rectangulo1==rectangulo2:
	print("La superficie de los rectángulos es igual")
else:
	print("La superficio de los rectángulos es diferente")