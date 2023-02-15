"""
    Programa14
    Nombre: Edwin MVP
    Fecha: 13/02/2023
    Descripción: Crear un Clase Persona, imprimiendo su nombre y correo
"""
class Persona:
    __email = None
    __nombre = None
    def __init__(self):
          print("Persona")
    def setEmail(self,email):
        self.__email = email
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getEmail(self):
       return self.__email
    def getNombre(self):
       return self.__nombre


dejah = Persona()
dejah.setNombre("Dejah")
print(dejah.getNombre())
dejah.setEmail("Dejah@utectulancingo.edu.mx")
print(dejah.getEmail())