"""
    Programa3
    Nombre: Edwin MVP
    Fecha: 31/01/2023
    Descripción:Area y Permietro de un triangulo
"""
lado_a = int(input("Ingrese el primer lado: "))#variable para imprimir o almacenar un numero
lado_b = int(input("Ingrese el segundo lado: "))#variable para imprimir  o almacenar un numero
lado_c = int(input("Ingrese el tercer lado: "))#variable para imprimir o almacenar  otro numero
altura = int(input("Ingrese la altura: "))#almacena una cadena de caracteres
base = int(input("Ingrese la base: "))#almacena una cadena de caracteres 

perimetro = lado_a+ lado_b + lado_c
area = int (base * altura / 2)

print("El perimetro es", perimetro)
print("El area es", area)