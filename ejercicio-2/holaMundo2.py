"""
Modifique el programa anterior para que muestre “¡Hola 
<arg 1>!”. Donde arg 1 proviene de la lista de 
argumentos al ejecutar el programa.
"""

import sys # Con esta libreria accedemos a los argumentos de la linea de comandos

def modificarCadena(cadena):
    return cadena.title()   # Con el método title() convertimos la primera letra de cada palabra en mayúscula (Capitalización de palabras)

print(f"¡Hola {modificarCadena(sys.argv[1])}!")
