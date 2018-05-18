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

#Funcion para agregar el paciente
#Parametros: String nombre, String telefono
def agregarPaciente(nombre, telefono):
	paciente = db.nodes.create(name=nombre, phone=telefono)
	pacientes.add(paciente)
	return paciente

#Funcion para agregar un doctor
#Parametros: String nombre, colegiado, especialidad, telefono
def agregarDoctor(nombre, colegiado, especialidad, telefono):
	doctor = db.nodes.create(name=nombre, col=colegiado, esp=especialidad, phone=telefono)
	doctores.add(doctor)
	return doctor

#Funcion para recetar un medicamento
#Parametros: Doctor doctor (Elemento de la base de datos), Paciente paciente (Elemento de la base de datos). String nombre medicina, desdeFecha, hastaFecha, dosisP
def prescribe(doctor, paciente, nombreMedicina, desdeFecha, hastaFecha, dosisP):
	medicina = db.nodes.create(name= nombreMedicina, desde = desdeFecha, hasta = hastaFecha, dosis = dosisP)
	drogas.add(medicina)
	doctor.relationships.create("Prescibes", medicina)
	paciente.relationships.create("Takes", medicina)

#FUncion para definir una visita de un paciente a un doctor
def visita(doctor, paciente):
	paciente.relationships.create("Visits", doctor)

#Funciona ara agregar una persona conocida
def conoce(persona1, persona2):
	persona1.relationships.create("Knows", persona2)

#Funcion para buscar la especialidades
def getEspecialidades():
	cypher = 'MATCH (n: Doctors) RETURN n ORDER BY n.esp'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	results = []
	for result in query:
		results.append(result[0]["esp"])
	return eliminarRepetidos(results)

#Funcion para elminar repetidos en consultas
def eliminarRepetidos(list):
	newList = []
	for element in list:
		if(element not in newList):
			newList.append(element)
	return newList

#Funcion para buscar un doctor por especialidad
def buscarDoctor(especialidad):
	cypher = 'MATCH (n: Doctors) WHERE n.esp="' + especialidad +'" RETURN n'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	results = []
	return query

#Funcion para imprimir una lista de doctores
def imprimirDoctor(query):
	for result in query:
		print("Nombre: %s Telefono: %s" % (result[0]["name"], result[0]["phone"]))
		

#Funcion para buscar una persona
def buscarPersona(nombre):
	cypher = 'MATCH (n: Patient) WHERE n.name="' + nombre + '" RETURN n'
	query = db.query(cypher, returns=(client.Node, str, client.Node))
	return query

#Imprimir una lista de personas
def imprimirPersona(query):
	for r in query:
		print("Nombre: %s Telefono: %S" % (r[0]["name"], r[0]["phone"]))

