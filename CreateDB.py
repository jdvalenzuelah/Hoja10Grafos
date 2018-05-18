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

#Connect to Neo4J server
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")

#Creamos los "labels" (Tipo de dato)
pacientes = db.labels.create("Pacientes")
doctores = db.labels.create("Doctores")
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

#Funcion para definir una visita de un paciente a un doctor
def visita(doctor, paciente):
	paciente.relationships.create("Visits", doctor)

	#Imprimimos los pacientes disponibles en la base de datos
	print("Estos son los pacientes disponibles, dentro de la sala\n")
	q = 'MATCH (u: Pacientes) RETURN u'
	resultados = db.query(q, returns=(client.Node, str, client.Node)) 
	#ciclo para recorrer la busqueda
	for r in resultados:
		print ("-")
#Funciona ara agregar una persona conocida
def conoce(persona1, persona2):
	persona1.relationships.create("Knows", persona2)

#Creacion de grafos de pruebas
doc = agregarDoctor("Marcos", "545454", "Internista", "24353026")
pac = agregarPaciente("Fernando", "35202766")
pac2 = agregarPaciente("David", "5454545")
prescribe(doc, pac, "Aspririna", "17/05/2018", "25/05/2018", "cada 8h")
visita(doc, pac)
conoce(pac, pac2)

