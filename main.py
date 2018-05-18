#******************************************************
#Universidad del Valle de Guatemala
#Algoritmos y Estructura de Datos
#David Valenzuela 171001
#Marcos Gutierrez 17
#Fernando Hengstenberg 17699
#Base de Datos y Grafos

from CreateDB import *

#Contar para el ciclo
opcion = 0

print("Bienvenido al sistema de control del Hospital")
print("¿Que desea hacer?\n 1. Ingresar nuevo doctor\n 2. Ingresar nuevo paciente\n 3. Doctores con Especialidades\n 4.Una Persona Conoce a Otra\n 5. Recomendaciones de un Paciente\n 6.Recomendaciones de un doctor \n 7. Salir")
opcion = int(input("¿Cual es opcion a escoger?"))

#Ciclo para realizar el menu
while opcion !=5:
    #Opcion para agregar nuevo doctor
    if(opcion == 1):
        print("*****USTED INGRESARA UN NUEVO DOCTOR*****")
        nombre = raw_input("Ingrese el nombre del doctor") 
        colegiado = raw_input("Ingrese el numero del colegiado del doctor")
        especialidad = raw_input("Ingrese la especialidad del doctor")
        telefono = raw_input("Ingrse el nuero de telefono del doctor")
        #Llamamos a la funcion agregarDoctor
        agregarDoctor(nombre, colegiado, especialidad, telefono)

    #Opcion para agregar un nuevo paciente
    if(opcion == 2):
        print("*****USTED INGRESARA UN NUEVO PACIENTE")
        nombrePaciente = raw_input("Ingrese el nombre del paciente")
        telefonoPaciente = raw_input("Ingrese el numero telefonico del paciente")
        #Llamamos la funcion agregarPaciente
        agregarPaciente(nombrePaciente, telefonoPaciente)

    #Opcion para Doctores con Especialidades
    if(opcion == 3):
        #Llamamos la funcion que se encarga de lo solicitado
        getEspecialidades()

    #Opcion para si una persona conoce a otra persona
    if(opcion == 4):
        #Llamaos a la funcion
        

    #Opcion para recomendaciones de un paciente
    if(opcion == 5):

     
    

