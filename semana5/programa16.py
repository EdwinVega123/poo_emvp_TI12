"""
    Programa16
    Nombre: Edwin MVP
    Fecha: 14/02/2023
    Descripción: Crear un Clase persona y Alumno, imprimiendo su nombre, pelicula y correo
"""
class Persona: #Crea la clase Persona
    __nombre = None #Variable Privada_nombre
    def __init__(self): #Constructor de la variable Persona 
         print("Persona")# Imprime Persona 

class Alumno(Persona): # Crea la clase alumno
    def __init__(self): #Constructor de la variable Alumno_Persona
          super().__init__() # Llama a la Clase  alumno 
          print("Alumno") #Imprime alumno 

objeto_persona = Persona() #Crea un objeto_persona
objeto_alumno = Alumno()#Crea un objeto_alumno

objeto_persona.nombre = "Dejah Thoris"
print(objeto_persona.nombre)

objeto_alumno.nombre = "John Carter"
print(objeto_alumno.nombre)

objeto_alumno.email = "John@gmail.com.mx"
print(objeto_alumno.email)

print(dir(objeto_persona))
print(dir(objeto_alumno))