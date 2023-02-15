"""
    Programa6
    Nombre: Edwin MVP
    Fecha: 31/01/2023
    Descripción:Area y Permietro de un Circulo
"""
radio = int(input("Ingrese el radio del circulo: "))#variable para imprimir  o almacenar un numero
pi = 3.14 #variable de tipo entero

perimetro_circulo = 2*pi*radio #Formula del perimetro del Circulo
area_circulo = pi*radio*radio #Formula del Area de un Circulo

print("El perimetro del circulo con un radio de {} es {} ".format(radio, perimetro_circulo)) #imprime el perimetro del circulo
print("El area del circulo con un radio de {} es {} ".format(radio, area_circulo))#imprime el area del circulo
