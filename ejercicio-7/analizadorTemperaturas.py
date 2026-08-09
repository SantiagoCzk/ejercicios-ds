'''
Escribe un programa con una función llamada analizar_temperaturas(registros) que reciba una 
lista de números (temperaturas). 

    a. La función debe retornar en una sola tupla: el valor 
    máximo, el valor mínimo y el promedio de las temperaturas. (ver operaciones con listas)
    b. Invocar a la función con datos de prueba e imprimir los resultados desmpaquetándolos.
'''

# Funcion para analizar temperaturas
def analizar_temperaturas(registros):
    if len(registros) == 0:
        print("La lista de registros está vacía.")
        return None

    max_temp = max(registros)
    min_temp = min(registros)
    avg_temp = sum(registros) / len(registros)


    return (max_temp, min_temp, avg_temp)


# Datos de prueba
temperaturas = [23.5, 25.0, 22.1, 24.8, 26.3, 21.9]

# Invocación de la función y desempaquetado de resultados
max_temp, min_temp, avg_temp = analizar_temperaturas(temperaturas)

print(f">> Temperatura máxima: {max_temp}")
print(f">> Temperatura mínima: {min_temp}")
print(f">> Temperatura promedio: {avg_temp}")
