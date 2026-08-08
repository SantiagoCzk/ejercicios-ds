'''
Cree un programa que muestre un menú interactivo utilizando la estructura match.
    a. Calcular la suma de los primeros N números naturales (usando un for).
    b. Encontrar todos los números divisibles por 3 en un rango dado por el usuario. (Ver range())
    c. Salir.
'''

# Funcion para validar la entrada del usuario sea correcta y del tipo esperado
def entradaValida(msj, tipo=float):
    while True:
        try:
           return tipo(input(msj))
        except ValueError:
            print(f"\n>>> ERROR: Por favor, ingrese un valor válido.")

# Funcion para validar que el valor ingresado sea positivo
def entradaValidaPositiva(msj, tipo=float):
    while True:
        valor = entradaValida(msj, tipo)
        if valor > 0:
            return valor
        else:
            print("\n>>> ERROR: Por favor, ingrese un valor numerico positivo.")

# Funcion para calcular la suma de los primeros N números naturales
def calcular_suma_numeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Funcion para encontrar todos los números divisibles por 3 en un rango dado
def encontrar_divisibles_por_3(inicio, fin):
    divisibles = []

    rango_inicio = min(inicio, fin)
    rango_fin = max(inicio, fin)

    for i in range(rango_inicio, rango_fin + 1):
        if i % 3 == 0:
            divisibles.append(i)
    return divisibles

# Funciones para cada opción del menú
def opcion_a():
    print("\nCálculo de la suma de los primeros N números naturales")
    n = entradaValidaPositiva("\n>> Ingrese el valor de N: ", int)
    suma = calcular_suma_numeros_naturales(n)
    print(f"\nRESULTADO: La suma de los primeros {n} números naturales es: {suma}")

def opcion_b():
    print("\nEncontrar todos los números divisibles por 3 en un rango dado")
    inicio = entradaValida("\n>> Ingrese el inicio del rango: ", int)
    fin = entradaValida("\n>> Ingrese el final del rango: ", int)
    divisibles = encontrar_divisibles_por_3(inicio, fin)
    print(f"\nRESULTADO: Los números divisibles por 3 en el rango [{inicio}, {fin}] son: {divisibles}")


while True:
    # Mostramos el menú de opciones
    print("\n--- Menú Interactivo ---")
    print("a. Calcular la suma de los primeros N números naturales")
    print("b. Encontrar todos los números divisibles por 3 en un rango dado")
    print("c. Salir")

    # Obtenemos la opción del usuario
    opcion = input("\n>> Seleccione una opción (a, b, c): ")

    match opcion:
        case "a": opcion_a()
        case "b": opcion_b()
        case "c": 
            print("\n>>> Saliendo del programa...")
            break
        case _:
            print("\n>>> ERROR: Opción no válida. Por favor, seleccione una opción válida.")  

