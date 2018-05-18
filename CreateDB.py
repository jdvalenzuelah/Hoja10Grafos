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
<<<<<<< HEAD
pacientes = db.labels.create("Patient")
doctores = db.labels.create("Doctors")
=======
pacientes = db.labels.create("Pacientes")
doctores = db.labels.create("Doctores")
>>>>>>> 8eca3a90138e425f481d7737ff1ad3b148166c50
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
	 nombrePaciente = raw_input("Ingrese el nombre del Paciente que desea relacionar: ")
    print("Estos son los doctores disponibles dentro de la sala: ")
    q = 'MATCH (u: Doctores) RETURN u'
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        print(" - " + "%s" % (r[0]["name"]))
    nombreDoctor = raw_input("Ingrese el nombre del Doctor que desea relacionar: ")
    q = 'MATCH (u: Doctores) WHERE u.name="'+nombreDoctor+'" RETURN u'
    resultado_uno = db.query(q, returns=(client.Node))
    largo_uno = len(resultado_uno)
    q = 'MATCH (u: Pacientes) WHERE u.name="'+nombrePaciente+'" RETURN u'
    resultado_dos = db.query(q, returns=(client.Node))
    largo_dos = len(resultado_dos)
    if(largo_uno>0 and largo_dos>0):
        date = raw_input("Ingrese la Fecha de Vista(YYYYMMDD): ")
        medicia = raw_input("Ingrese la medicina: ")
        dateStart = raw_input("Ingrese la fecha de inicio del tratamiento (YYYYMMDD): ")
        dateFinish = raw_input("Ingrese la fecha de finalizacion del tratamiento (YYYYMMDD): ")
        dosisM = raw_input("Ingrese la dosis que el paciente debe de tomar: ")
        nuevaMedicina = db.nodes.create(name=medicina,desdeFecha=dateStart,hastaFecha=dateFinish,dosis=dosisM)
        Drogas.add(nuevaMedicina)
        for r in resultado_uno:
            for i in resultado_dos:
                i[0].relationships.create("VISITS",r[0],fecha=date) #el paciente visita al doctor en tal fecha
                i[0].relationships.create("TAKE",nuevaMedicina) #el paciente toma la medicina
                r[0].relationships.create("PRESCRIBE",nuevaMedicina) #el doctor prescribe la medicina 
        print("Se ha ingresado con exito la relacion\n")
    else:
        print("Algunos de los datos ingresados no estan dentro de la base de datos del Hospital\n Porfavor intentelo de nuevo")

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
	for result in query:
		results.append("Nombre: %s Telefono: %s" % (result[0]["name"], result[0]["phone"]))
	return results

#Creacion de grafos de pruebas
doc = agregarDoctor("Marcos", "545454", "Internista", "24353026")
pac = agregarPaciente("Fernando", "35202766")
pac2 = agregarPaciente("David", "5454545")
prescribe(doc, pac, "Aspririna", "17/05/2018", "25/05/2018", "cada 8h")
visita(doc, pac)
conoce(pac, pac2)
for i in buscarDoctor("Internista"):
	print(i)

