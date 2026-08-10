'''
Crea una clase CuentaBancaria con los siguientes 
requisitos:
    a. Atributos de instancia: titular y saldo (por defecto en 0.0).
    b. Método depositar(monto): suma el monto al saldo si es mayor a 0.
    c. Método retirar(monto): resta el saldo si hay fondos suficientes, de lo contrario muestra un mensaje de error.
    d. Método mostrar_info(): imprime el titular y el saldo actual.

Crea un par de instancias y realizar operaciones para probarla.
'''

# Clase CuentaBancaria
class CuentaBancaria:

    # Metodo especial. Constructor
    def __init__(self, titular,saldo=0.0):  
        self.titular = titular
        self.saldo = saldo

    # Metodo para el deposito
    def depositar(self, monto): 
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto a depositar debe ser mayor a 0.")

    # Metodo para el retiro
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes para realizar el retiro.")

    # Metodo para mostrar la información de la cuenta
    def mostrar_info(self):
        print(f"Titular: {self.titular}, Saldo actual: {self.saldo:.2f}")



# Crear instancias de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Juan Pérez",500)
cuenta2 = CuentaBancaria("María López")

# Realizar operaciones en la cuenta 1
cuenta1.depositar(1000)
cuenta1.retirar(200)
cuenta1.mostrar_info()

# Realizar operaciones en la cuenta 2
cuenta2.depositar(500)
cuenta2.retirar(600)  # Intento de retiro con fondos insuficientes
cuenta2.mostrar_info()

