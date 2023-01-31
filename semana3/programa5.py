"""
    Programa3
    Nombre: Edwin MVP
    Fecha: 31/01/2023
    Descripción:Area y Permietro de un triangulo
"""
A = input("Ingrese el primer lado: ")
B = input("Ingrese el segundo lado: ")
C = input("Ingrese el tercer lado: ")

Altura = int(input("Ingrese la altura: "))
Base = int(input("Ingrese la base:"))

Perimetro = (A) + (B) + (C)
Area = Base * Altura / 2

print(Perimetro)
print(Area)