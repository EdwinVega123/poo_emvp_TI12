"""
    Programa8
    Nombre: Edwin MVP
    Fecha: 1/01/2023
    Descripción:11 Programa para Comparar 2 numeros enteros e imprimir el numero mayor usando def
"""
def mayor(numero1,numero2):
  if numero1 > numero2:
     print(numero1)
  elif numero2 > numero1:
    print (numero2)
  else:
    print("Iguales")

mayor(3,2)#3
mayor(2,3)#3
mayor(3,3)#None
