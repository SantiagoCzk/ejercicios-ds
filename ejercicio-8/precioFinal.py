'''
Escribir un programa que contenga una función calcular_precio_final(precio_base, 
porcentaje_descuento=10, es_vip=False). 

    a. Si el client es VIP (es_vip=True), se le descuenta un 5% extra sobre el precio ya rebajado. 
    b. Validar que los valores ingresados sean positivos 
    
(lanzar una excepción ValueError si esto no es así).
Invocar a la función varias veces con diferentes parámetros para comprobar el funcionamiento correcto.
'''

# Funcion para calcular el precio final con descuento y condiciones VIP
def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base < 0 or porcentaje_descuento < 0:
        raise ValueError("Los valores ingresados deben ser positivos.")
    
    # Calcular el precio después del descuento
    precio_con_descuento = precio_base * (1 - porcentaje_descuento / 100)
    
    # Aplicar descuento adicional si es VIP
    if es_vip:
        precio_con_descuento *= 0.95  # Descuento adicional del 5%
    
    return precio_con_descuento


# Ejemplos de invocación de la función
try:
    print(calcular_precio_final(100))  # Precio base 100, descuento 10%, no VIP
    print(calcular_precio_final(200, 20))  # Precio base 200, descuento 20%, no VIP
    print(calcular_precio_final(150, es_vip=True))  # Precio base 150, descuento 10%, VIP
    print(calcular_precio_final(300, 15, True))  # Precio base 300, descuento 15%, VIP
    print(calcular_precio_final(250, 0, False))  # Precio base 250, sin descuento, no VIP
    print(calcular_precio_final(-50))  # Valor negativo para probar la excepción
except ValueError as e:
    print(f"Error: {e}")



