'''
Escriba un programa que permita hacer la conversión de 
valores de temperatura entre Celsius y Fahrenheit. Se 
debe solicitar al usuario que ingrese un valor numérico y 
la escala original. 

El programa deberá mostrar por pantalla el valor 
convertido incluyendo la escala final. Ver input(). 
Construya dos funciones, una para convertir datos a 
escala Celsius y otra para convertir los datos a escala 
Fahrenheit.
'''
# Funcion para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Funcion para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Funcion para validar la entrada del usuario sea correcta y del tipo esperado
def entrada_valida(msj, tipo=float):
    while True:
        try:
            return tipo(input(msj))
        except ValueError:
            print(f"Por favor, ingrese un valor válido.")

# Funcion para validar que el valor ingresado sea de una escala correcta (C o F)
def entrada_valida_escala(msj):
    while True:
        escala = input(msj).strip().upper()
        if escala in ['C', 'F']:
            return escala
        else:
            print("Por favor, ingrese una escala válida (C o F).")

print("\nCONVERSIÓN DE TEMPERATURA\n")

# Solicitamos al usuario que ingrese el valor de temperatura y la escala original
escala_original = entrada_valida_escala(">> Ingrese la escala original (C para Celsius, F para Fahrenheit): ")
valor_temperatura = entrada_valida(">> Ingrese el valor de temperatura: ")

# Realizamos la conversión según la escala original ingresada
if escala_original == 'C':
    valor_convertido = celsius_a_fahrenheit(valor_temperatura)
    escala_final = 'F'
else:
    valor_convertido = fahrenheit_a_celsius(valor_temperatura)
    escala_final = 'C'

# Mostramos el resultado de la conversión
print(f"\nRESULTADO DE LA CONVERSIÓN\n")
print(f"{valor_temperatura:.2f}°{escala_original} es igual a {valor_convertido:.2f}°{escala_final}")



