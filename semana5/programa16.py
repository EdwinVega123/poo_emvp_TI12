"""
    Programa16
    Nombre: Edwin MVP
    Fecha: 14/02/2023
    Descripción: Crear un Clase persona y Alumno, imprimiendo su nombre, pelicula y correo
"""
class Persona:

    def __init__(self):
         __nombre = None
         print("Persona")

class Alumno(Persona):
    def __init__(self):
          super().__init__()
          print("Alumno")

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.nombre = "Dejah Thoris"
print(objeto_persona.nombre)

objeto_alumno.nombre = "John Carter"
print(objeto_alumno.nombre)

objeto_alumno.email = "John@gmail.com.mx"
print(objeto_alumno.email)

print(dir(objeto_persona))
print(dir(objeto_alumno))