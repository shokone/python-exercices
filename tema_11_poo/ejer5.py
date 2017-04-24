# creamos nuestra clase agenda
class Agenda:
	# iniciamos nuestra clase
	def __init__(self):
		# crearemos una lista donde guardaremos los datos de nuestra agenda
		self.contactos=[]

	# menu del programa
	def menu(self):
		print()
		menu=[
			['Agenda Personal'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]

		for x in range(6):
			print(menu[x][0])

		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.anadir()
		elif opcion==2:
			self.lista()
		elif opcion==3:
			self.buscar()
		elif opcion==4:
			self.editar()
		elif opcion==5:
			print("Saliendo de la agenda ...")
			exit()

		# volvemos a llamar al menú
		self.menu()


	# función para añadir un contacto
	def anadir(self):
		print("---------------------")
		print("Añadir nuevo contacto")
		print("---------------------")
		nom=input("Introduzca el nombre: ")
		telf=int(input("Introduzca el teléfono: "))
		email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		

	# función para imprimir la lista de contactos
	# En este caso imprimiremos solo los nombres de los contactos
	# con ellos podremos buscar luego un contacto
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		

	# función para buscar un contacto a través del nombre
	def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telf'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
		


	# función para editar los datos de un contacto
	def editar(self):
		print("---------------")
		print("Editar contacto")
		print("---------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				nom=input("Introduzca el nuevo nombre: ")
				self.contactos[data]['nombre']=nom
			elif option==2:
				telf=input("Introduzca el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif option==3:
				email=input("Introduzca el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True



# bloque principal
agenda=Agenda()
agenda.menu()