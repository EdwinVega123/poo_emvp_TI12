"""
    Programa10
    Nombre: Edwin MVP
    Fecha: 1/02/2023
    Descripción:11 Programas para Comparar 2 numeros enteros e imprimir el numero mayor
"""

def mayor(numero1: int, numero2: int) -> int: #crea una clase llamada mayor
  mayor = None # Variable para almacenar una cadena de caracteres
  if numero1 > numero2: # Condicion si entonces mayor que
    mayor = numero1 # Variable para almacenar una cadena de carac
  elif numero2 > numero1: # Condicion si entonces abreviado mayor que
    mayor = numero2 #Variable para almacenar una cadena de caracteres
  else: # Condicion sino entonces
    mayor = None # Varibale para almacenar una cadena de caracteres
  return mayor # retorna a la variable mayor 


print(mayor(3, 2))  #Imprime 3
print(mayor(2, 3))  #Imprime 3
print(mayor(3, 3))  #Imprime None
