#--------
#--------

#Import Graph Database
from neo4jrestclient.client import GraphDatabase

#Connect to Neo4J server
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")

#Create labels
pacientes = db.labels.create("Patient")
doctores = db.labels.create("Doctores")
drogas = db.labels.create("Drugs")

def agregarPaciente(nombre, telefono):
	paciente = db.nodes.create(name=nombre, phone=telefono)
	pacientes.add(paciente)
	return paciente

def agregarDoctor(nombre, colegiado, especialidad, telefono):
	doctor = db.nodes.create(name=nombre, col=colegiado, esp=especialidad, phone=telefono)
	doctores.add(doctor)
	return doctor

def prescribe(doctor, paciente, nombreMedicina, desdeFecha, hastaFecha, dosisP):
	medicina = db.nodes.create(name= nombreMedicina, desde = desdeFecha, hasta = hastaFecha, dosis = dosisP)
	drogas.add(medicina)
	doctor.relationships.create("Prescibes", medicina)
	paciente.relationships.create("Takes", medicina)

def visita(doctor, paciente):
	paciente.relationships.create("Visits", doctor)

#Creacion de grafos de pruebas
doc = agregarDoctor("Marcos", "545454", "Internista", "24353026")
pac = agregarPaciente("Fernando", "35202766")
prescribe(doc, pac, "Aspririna", "17/05/2018", "25/05/2018", "cada 8h")
visita(doc, pac)

