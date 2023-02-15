"""
    Programa15
    Nombre: Edwin MVP
    Fecha: 13/02/2023
    Descripción: Crear un Clase Alumno, imprimiendo su nombre, matricula y carrera
"""
class Alumno:
    __nombre = None
    __matricula = None
    __carrera= None
    def __init__(self):
          print("Alumno")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera

    def getNombre(self):
        return self.__nombre
    def getMatricula(self):
        return self.__matricula
    def getCarrera(self):
        return self.__carrera

dejah = Alumno()
dejah.setNombre("Dejah")
print(dejah.getNombre())
dejah.setMatricula("12109293")
print(dejah.getMatricula())
dejah.setCarrera("Ing. Informatica")
print(dejah.getCarrera())