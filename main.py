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
    

