'''
Escriba un programa que solicite al usuario una 
contraseña. Utilizar operadores lógicos y métodos de 
strings (.isupper(), .islower(), len()) para verificar si 
cumple con tres condiciones básicas:
    
    a. Tiene al menos 8 caracteres, 
    b. Contiene al menos una letra mayúscula 
    c. Al menos una minúscula. 

Imprimir un mensaje adecuado al caso.

'''

# Función para validar la contraseña ingresada por el usuario
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    if not any(char.isupper() for char in contrasena):  
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    
    if not any(char.islower() for char in contrasena):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False
    
    print("La contraseña es válida.")
    return True

# Variable para controlar el bucle de validación de la contraseña
resultado = False

while resultado != True:
    # Solicitar al usuario que ingrese una contraseña
    contrasena_usuario = input(">> Ingrese una contraseña: ")

    # Validar la contraseña
    resultado = validar_contrasena(contrasena_usuario)


