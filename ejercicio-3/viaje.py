"""
Escriba un programa que solicite al usuario:

    a. El costo estimado de un pasaje, 
    b. El costo de alojamiento por noche, 
    c. La cantidad de noches que durará el viaje 
    d. El dinero disponible. 

El programa debe calcular el costo total del viaje y determinar (con un booleano) si el dinero disponible es suficiente. 
Muestra un resumen formateado con los resultados. Ver input() y f-strings.
"""

# Función para validar la entrada del usuario sea correcta y del tipo esperado
def entradaValida(msj, tipo=float):
    while True:
        try:
           return tipo(input(msj))
        except ValueError:
            print(f"Por favor, ingrese un valor válido.")


# Funcion para validar que el valor ingresado sea positivo
def entradaValidaPositiva(msj, tipo=float):
    while True:
        valor = entradaValida(msj, tipo)
        if valor >= 0:
            return valor
        else:
            print("Por favor, ingrese un valor numerico positivo.")

# Le pedimos al usuario que ingrese los datos necesarios para calcular el costo del viaje
print("\nCALCULO DE COSTO DE VIAJE\n") 

costo_pasaje = entradaValidaPositiva(">> Ingrese el costo estimado del pasaje: ")
costo_alojamiento = entradaValidaPositiva(">> Ingrese el costo de alojamiento por noche: ")
cantidad_noches = entradaValidaPositiva(">> Ingrese la cantidad de noches que durará el viaje: ", tipo=int)
dinero_disponible = entradaValidaPositiva(">> Ingrese el dinero disponible: ")

# Calculamos el costo total del viaje y verificamos si el dinero disponible es suficiente
costo_total = costo_pasaje + (costo_alojamiento * cantidad_noches)
dinero_suficiente = dinero_disponible >= costo_total

# Mostramos un resumen del viaje con los resultados obtenidos
print(f"\nRESUMEN DEL VIAJE\n")
print(f"Pasaje: ${costo_pasaje:.2f}")
print(f"Alojamiento: ${costo_alojamiento:.2f} por noche")
print(f"Noches: {cantidad_noches}")
print(f"Dinero Disponible: ${dinero_disponible:.2f}")
print(f"Costo Total: ${costo_total:.2f}")
print(f"Dinero Suficiente: { 'Sí' if dinero_suficiente else 'No' }")