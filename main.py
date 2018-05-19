#******************************************************
#Universidad del Valle de Guatemala
#Algoritmos y Estructura de Datos
#David Valenzuela 171001
#Marcos Gutierrez 17
#Fernando Hengstenberg 17699
#Base de Datos y Grafos
#****************************************************** 

#Import the diriver
from driverDPM import *

print("Bienvenido al sistema de control del Hospital")
run = True


menu = """1. Ingresar nuevo doctor.
2. Ingresar nuevo paciente
3. Ver especialidades disponibles
4. Visita de un paciente a un doctor
5. Ver doctores con especialidad.
6. Una Persona Conoce a Otra
7. Recomendar doctor.
8. Recomendar un Paciente
9. Salir"""

#Ciclo para realizar el menu
while run:
    print(menu)
    opcion = raw_input("Cual es opcion a escoger?\n")
    #Opcion para agregar nuevo doctor
    if(opcion == "1"):
        print("---------------------------------------")
        print("*****USTED INGRESARA UN NUEVO DOCTOR*****")
        nombre = raw_input("Ingrese el nombre del doctor:\n") 
        colegiado = raw_input("Ingrese el numero del colegiado del doctor:\n")
        especialidad = raw_input("Ingrese la especialidad del doctor:\n")
        telefono = raw_input("Ingrse el numero de telefono del doctor:\n")
        #Llamamos a la funcion agregarDoctor
        agregarDoctor(nombre, colegiado, especialidad, telefono)
        print("---------------------------------------")

    #Opcion para agregar un nuevo paciente
    if(opcion == "2"):
        print("---------------------------------------")
        print("*****USTED INGRESARA UN NUEVO PACIENTE*****")
        nombrePaciente = raw_input("Ingrese el nombre del paciente:\n")
        telefonoPaciente = raw_input("Ingrese el numero telefonico del paciente:\n")
        #Llamamos la funcion agregarPaciente
        agregarPaciente(nombrePaciente, telefonoPaciente)
        print("---------------------------------------")

    #Opcion para ver Especialidades
    if(opcion == "3"):
        print(" ---- Especialidades disponibles: ----")
        #Llamamos la funcion que se encarga de lo solicitado
        for esp in getEspecialidades():
            print(esp)
        print("---------------------------------------")

    #Ingresar la visita de un paciente a un doctor
    if(opcion == "4"):
        print("---------------------------------------")
        nombreP = raw_input("Ingrese el nombre del paciente: ")
        nombreD = raw_input("Ingrese el nombre del doctor: ")
        qP = buscarPersona(nombreP)
        qD = buscarDoctorN(nombreD)
        if(len(qP) > 0 and len(qD) > 0):
            visitaQ(qD, qP, raw_input("Ingreser el nombre de la medicina prescrita: "), raw_input("Ingrese fecha de visita: "), raw_input("Ingrese fecha hasta tomar medicina: "), raw_input("Ingrese dosis de medicina: "))
        else:
            print("No se encontraron resultados!")
        print("---------------------------------------")

    #Buscar doctores con especialidad especifica
    if(opcion == "5"):
        print("---------------------------------------")
        #LLamamos a la funcion
        especialidad = raw_input("Ingrese especialidad: ")
        qE = buscarDoctor(especialidad)
        if(len(qE) > 0):
            imprimirDoctor(qE)
        else:
            print("No se encontraron resultados!")
        print("---------------------------------------")

    #Definir relacion de una persona con otra
    if(opcion == "6"):
        print("---------------------------------------")
        qP1 = buscarPersona(raw_input("Ingrese el nombre de la persona 1: "))
        qP2 = buscarPersona(raw_input("Ingrese el nombre de la persona 2: "))
        if(len(qP1)>0 and len(qP2) > 0):
            conoceQ(qP1, qP2)
        else:
            print("No se encontraron resultados!")
        print("---------------------------------------")

    #Recomendacion de un doctor
    if(opcion == "7"):
        print("-------- Doctores Recomendados --------")
        pac = raw_input("Ingrese nombre del paciente: ")
        esp = raw_input("Ingrese especialidad que busca: ")
        qR = recomendarDoctor(pac, esp)
        if(len(qR)>0):
            imprimirDoctor(eliminarRepetidos(qR))
        else:
            print("No se encontraron resultados!")
        print("---------------------------------------")

    #Recomendar paciente
    if(opcion == "8"):
        doc = raw_input("Ingrese nombre del doctor: ")
        esp = raw_input("Ingrese especialidad que busca: ")
        qP = recomendarPaciente(doc, esp)
        print("---------------------------------------")
        if(len(qP[0])>0):
            imprimirDoctor(eliminarRepetidos(qP[0]))
        if(len(qP[1])>0):
            imprimirDoctor(eliminarRepetidos(qP[1]))
        print("---------------------------------------")

    #Salir del programa
    if(opcion == "9"):
        print("Gracias por utilizar el programa!")
        run = False
    #Opcion invalida
    else:
        print("Ingrese una opcion valida!")
