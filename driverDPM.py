#******************************************************
#Universidad del Valle de Guatemala
#Algoritmos y Estructura de Datos
#David Valenzuela 171001
#Marcos Gutierrez 17
#Fernando Hengstenberg 17699
#Base de Datos y Grafos
#******************************************************	

#Import Graph Database
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Connect to Neo4J server
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")

#Creamos los "labels" (Tipo de dato)
pacientes = db.labels.create("Patient")
doctores = db.labels.create("Doctors")
drogas = db.labels.create("Drugs")

def agregarPaciente(nombre, telefono):
	"""
	Ingresar un nuevo paciente a la base de datos.

	Args:
		nombre (str): el nombre del paciente
		telefono (str): el numero de telefono del paciente

	Returns:
		client.Node: Nodo del paciente agregado a la db

	"""
	paciente = db.nodes.create(name=nombre, phone=telefono)
	pacientes.add(paciente)
	return paciente

def agregarDoctor(nombre, colegiado, especialidad, telefono):
	"""
	Ingresar un nuevo doctor a la base de datos.

	Args:
		nombre (str): el nombre del doctor
		colegiado (str): el numero de colegiado del doctor
		especialidad (str): la especialidad del doctor
		telefono (str): el numero de telefono del doctor

	Returns:
		client.Node: Nodo del doctor recien agregado a la db

	"""
	doctor = db.nodes.create(name=nombre, col=colegiado, esp=especialidad, phone=telefono)
	doctores.add(doctor)
	return doctor

def prescribe(doctor, paciente, nombreMedicina, desdeFecha, hastaFecha, dosisP):
	"""
	Recetar un medicamento a un paciente.
	
	Args:
		doctor (client.Node): Nodo del doctor que receta el medicamento
		paciente (client.Node): Nodo del paciente que recibe la reseta
		nombreMedicina (str): Nombre de la medicina que el doctor esta recetando
		desdeFecha (str): Fecha del comienzo de la receta
		hastaFecha (str): Fecha del final de la receta
		dosisP (str): Dosis de la medicina que la receta especifica

	"""
	medicina = db.nodes.create(name= nombreMedicina, desde = desdeFecha, hasta = hastaFecha, dosis = dosisP)
	drogas.add(medicina)
	doctor.relationships.create("Prescibes", medicina)
	paciente.relationships.create("Takes", medicina)

def visita(doctor, paciente, nombreMedicina, desdeFecha, hastaFecha, dosisP):
	"""
	Registrar la visita de un paciente a un doctor, en la visita tambien se registra la receta dada por el doctor
	
	Args:
		doctor (client.Node): Nodo del doctor que receta el medicamento
		paciente (client.Node): Nodo del paciente que recibe la reseta
		nombreMedicina (str): Nombre de la medicina que el doctor esta recetando
		desdeFecha (str): Fecha del comienzo de la receta
		hastaFecha (str): Fecha del final de la receta
		dosisP (str): Dosis de la medicina que la receta especifica


	"""
	paciente.relationships.create("Visits", doctor)
	prescribe(doctor, paciente, nombreMedicina, desdeFecha, hastaFecha, dosisP)

def visitaQ(queryD, queryP, nombreMedicina, desdeFecha, hastaFecha, dosisP):
	"""
	Registrar la visita de un paciente a un doctor, en la visita tambien se registra la receta dada por el doctor
		funcion baada en querys
	
	Args:
		doctor (client.Node[][]): Nodo del doctor que receta el medicamento
		paciente (client.Node[][]): Nodo del paciente que recibe la reseta
		nombreMedicina (str): Nombre de la medicina que el doctor esta recetando
		desdeFecha (str): Fecha del comienzo de la receta
		hastaFecha (str): Fecha del final de la receta
		dosisP (str): Dosis de la medicina que la receta especifica


	"""
	queryP[0][0].relationships.create("Visits", queryD[0][0])
	prescribe(queryD[0][0], queryP[0][0], nombreMedicina, desdeFecha, hastaFecha, dosisP)
			
def conoce(persona1, persona2):
	"""
	Definir una relacion entre dos personas. Persona1 conoce a Persona2

	Args:
		persona1 (client.Node): Nodo de la base de datos de la primera persona
		persona2 (client.Node): Nodo de la base de datos de la segunda persona

	"""
	persona1.relationships.create("Knows", persona2)

def conoceQ(query1, query2):
		"""
	Definir una relacion entre dos personas. Persona1 conoce a Persona2
		Funcion basada en querys

	Args:
		persona1 (client.Node[][]): matriz de nodos de la base de datos de la primera persona
		persona2 (client.Node[][]): matriz de nodos de la base de datos de la segunda persona

	"""
	query1[0][0].relationships.create("Knows", query2[0][0])

def getEspecialidades():
	"""
	Mostrar las especialidades de los doctores que se encuentran el la base de datos

	"""
	cypher = 'MATCH (n: Doctors) RETURN n ORDER BY n.esp'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	results = []
	for result in query:
		results.append(result[0]["esp"])
	return eliminarRepetidos(results)

def eliminarRepetidos(list):
	"""
	Eliminar los elementos repetidos en una lista de datos

	Args:
		list (list): la lista de datos que se quieren eliminar los registros repetidos

	"""
	newList = []
	for element in list:
		if(element not in newList):
			newList.append(element)
	return newList

def buscarDoctor(especialidad):
	"""
	Buscar doctores con una especialidad especifica en la base de datos

	Args:
		especialidad (str): Especialidad que se quieren buscar los doctores

	Returns:
		clien.Node[][]: Nodos de la base de datos de los doctores encontrados con la especialidad especificada

	"""
	cypher = 'MATCH (n: Doctors) WHERE n.esp="' + especialidad +'" RETURN n'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	return query

def buscarDoctorN(nombre):
	"""
	Buscar un doctor en la base de datos con el nombre:¿.

	Args:
		nombre (str): Nombre del doctor que se quiere buscar en la base de datos

	Returns:
		client.Node[][]: Nodos de la base de dato con los doctores con el nombre ingresado

	"""
	cypher = 'MATCH (n: Doctors) WHERE n.name="' + nombre +'" RETURN n'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	return query

def imprimirDoctor(query):
	"""
	Imprimir lista de doctores en la base de datos

	Args:
		query (clien.Node[][]): Lista de nodos de doctores a mostrar en pantalla.

	"""
	for result in query:
		print("Nombre: %s Telefono: %s" % (result[0]["name"], result[0]["phone"]))
		
def buscarPersona(nombre):
	"""
	Buscar una persona en la base de datos a partir del nombre.

	Args:
		nombre (str): Nombre de la persona a buscar en la base de datos

	Returns:
		client.Node[][]: Nodos de la base de dato con las personas con el nombre ingresado

	"""
	cypher = 'MATCH (n) WHERE n.name="' + nombre + '" RETURN n'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	return query

def imprimirPersona(query):
	"""
	Imprimir lista de personas en la base de datos

	Args:
		query (clien.Node[][]): Lista de nodos de pacientes a mostrar en pantalla.

	"""
	for r in query:
		print("Nombre: %s Telefono: %s" % (r[0]["name"], r[0]["phone"]))

def recomendarDoctor(paciente, especialidad):
	"""
	Dada una persona específica:
	Quiere buscar un doctor que tenga una especialidad específica, pero que haya sido visitado por alguien 
	que él conoce, o que un conocido de un conocido ha visitado.

	Args:
		paciente (str): Nombre del paciente que quiere ser recomendado un doctor
		especialidad (str): Especialidad del doctor que quiere ser recomendado

	Returns:
		client.Node[][]: Nodos de la base de dato con los doctores recomendados.

	"""
	cypher = 'MATCH (paciente:Patient)-[:Knows]->(kp:Patient), (kp)-[:Knows]->(kkp:Patient),(kp)-[:Visits]->(doc:Doctors), (kpp)-[:Visits]->(docp:Doctors)  WHERE paciente.name="' + paciente + '" AND doc.esp="' + especialidad +'" AND docp.esp="' + especialidad +'" RETURN doc, docp'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	return query

def recomendarPaciente(nombre, especialidad):
	"""
	Dado un doctor específico:
	Quiere referir a su paciente a otro doctorcon una especialidad específica. Pero el doctor nuevo debe ser 
	conocido por el doctor original, o ser un conocido de un conocido del doctor original.

	Args:
		nombre (str): Nombre del doctor que quiere referir el paciente a otro doctor.
		especialidad (str): Especialidad de los doctores a ser recomendados.

	Returns:
		client.Node[][]: Nodos de la base de dato con los doctores recomendados.

	"""
	cypher = 'MATCH (doctor:Doctors)-[:Knows]->(kd:Doctors) WHERE doctor.name="' +  nombre + '" AND kd.esp="' + especialidad + '" RETURN kd'
	query1 = db.query(cypher, returns=(client.Node, str, client.Node))
	cypher = 'MATCH (doctor:Doctors)-[:Knows]->(conocidos), (conocidos)-[:Knows]->(doc:Doctors) WHERE doctor.name="' +  nombre + '" AND doc.esp="' + especialidad + '" RETURN doc'
	query2 = db.query(cypher, returns=(client.Node, str, client.Node))
	return [query1, query2]
