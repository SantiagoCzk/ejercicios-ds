'''
Escriba un programa que simule un inicio de sesión. 
Definir una contraseña correcta en una constante (ej. 
"Admin1234"). 

    a. Permitir al usuario intentar ingresarla un máximo de 3 veces usando un bucle while. 
    b. Si acierta, muestra un mensaje de éxito y termina. 
    c. Si agota los intentos, muestra un mensaje de bloqueo y finaliza el programa
'''

# Importamos la función de validación de contraseña desde el archivo password.py
from password import validar_contrasena

# Definir la contraseña correcta
CONTRASENA_CORRECTA = "Admin1234"

# Variable para controlar el número de intentos
intentos = 0

while intentos < 3:
    # Solicitar al usuario que ingrese la contraseña
    contrasena = input(">> Ingrese la contraseña: ")
    validar_contrasena(contrasena)  # Validar la contraseña ingresada

    # Verificar si la contraseña ingresada es correcta
    if contrasena == CONTRASENA_CORRECTA:
        print("¡Inicio de sesión exitoso!")
        break  # Salir del bucle si la contraseña es correcta
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intentos restantes: {3 - intentos}")