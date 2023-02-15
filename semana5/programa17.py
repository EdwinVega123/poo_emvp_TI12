"""
    Programa17
    Nombre: Edwin MVP
    Fecha: 14/02/2023
    Descripción: Crear un Clase persona y Alumno, imprimiendo su nombre, pelicula y correo
"""
class Persona:
    __nombre = None
    __edad = None
    def __init__(self):
       print("Persona")

    def getNombre(self):
       return self._nombre

    def setNombre(self,nombre):
       self._nombre = nombre 

    def getEdad(self):
       return self._edad

    def setEdad(self,edad):
       self._edad = edad

objeto_persona = Persona()
#print(objeto_persona.nombre)
objeto_persona.nombre = "Hola"
print(objeto_persona.nombre)
objeto_persona.setNombre("Edwin")
print(objeto_persona.getNombre())
objeto_persona.setEdad("19")
print(objeto_persona.getEdad())


class Alumno(Persona):
    __nombre = None
    __matricula = None
    def __init__(self):
       print("Alumno")

    def getNombre(self):
       return self._nombre

    def setNombre(self,nombre):
       self._nombre = nombre 

    def getMatricula(self):
       return self._matricula

    def setMatricula(self,matricula):
       self._matricula = matricula

objeto_alumno = Alumno()
#print(objeto_alumno.nombre)
objeto_alumno.nombre = "Hola"
print(objeto_alumno.nombre)
objeto_alumno.setNombre("Dejah")
print(objeto_alumno.getNombre())
objeto_alumno.setMatricula("172212783")
print(objeto_alumno.getMatricula())


class Profesor(Persona):
    __nomina = None
    def __init__(self):
       print("Profesor")
    def getNomina(self):
       return self._nomina

    def setnomina(self,nomina):
       self._nomina = nomina

objeto_profesor = Profesor()
#print(objeto_profesor.nomina)
objeto_profesor.nomina = "5000$ al mes"
print(objeto_profesor.nomina)


class Coordinador:
    __numnomina = None
    __carrera_cordinador = None
    def __init__(self):
       print("Coordinador")
    def getNumNomina(self):
       return self._numnomina

    def setNumNomina(self,numnomina):
       self._numnomina = numnomina
      
    def getCarreraCor(self):
       return self._carrera_cordinador

    def setCarreraCor(self,carrera_cordinador):
       self._carrera_cordinador = carrera_cordinador
    
objeto_coordinador = Coordinador()
#print(objeto_coordinador.nomina)
objeto_coordinador.numnomina = "Ing. Salvador"
print(objeto_coordinador.numnomina)
objeto_coordinador.setNumNomina("5000 $")
print(objeto_coordinador.getNumNomina())
objeto_coordinador.setCarreraCor("Ing En Tecnolgias de la informacion")
print(objeto_coordinador.getCarreraCor())
