"""
    Programa11
    Nombre: Edwin MVP
    Fecha: 1/02/2023
    Descripción:11 Programa para Comparar 2 numeros enteros e imprimir el numero mayor usando def
"""
def mayor(numero1,numero2): #Crea una clase en mayor y con dos variables
  if numero1 > numero2: #Condicion si entonces mayor q
     print(numero1) #Imprime numero1
  elif numero2 > numero1: #Condicion si entonces abreviado mayor que
    print (numero2)#Imprime numero 2
  else: #Condicion sino entonces
    print("Iguales")# Imprime Iguales

mayor(3,2)#Imprime 3
mayor(2,3)#Imprime 3
mayor(3,3)#Imprime None
