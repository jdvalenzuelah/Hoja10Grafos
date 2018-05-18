#******************************************************
#Universidad del Valle de Guatemala
#Algoritmos y Estructura de Datos
#David Valenzuela 171001
#Marcos Gutierrez 17
#Fernando Hengstenberg 17699
#Base de Datos y Grafos
#******************************************************


print ("************************menu************************")
print ("1. ingresar nuevo Doctor")
print ("2. ingresar nuevo Paciente")
print ("3. Doctores con tipos de Especialidades")
print ("4. una persona conoce a otra")
print ("5. salir")
print ("****************************************************")

menu=input("")

while menu != "salir" or menu != "5":

    if menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5":
        print ("intente de nuevo")
        menu = input("")

    if menu == "1" or menu == "ingresar nuevo doctor":
        print ("ingrese un doctor")
    
    if menu == "2" or menu == "ingresar nuevo paciente":
        print ("ingrese un nuevo paciente")

    if menu == "3" or menu == "doctores con tipos de especialidades":
        print ("doctores con tipos de especialidades")

    if menu == "4" or menu == "una persona conoce a otra":
        print ("una persona conoce a otra")


     
    

