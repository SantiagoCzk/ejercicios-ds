'''
Crear un modelo Dispositivo que contenga:
    ● id_dispositivo: puede ser un entero o una cadena
    ● tipo: Literal que solo acepte los valores “sensor”, “actuador” o “gateway”.
Crear una instancia de este modelo para comprobar el uso del 
atributo id_dispositivo como Union de dos tipos de datos y 
otra instancia para comprobar el error de validación al utilizar 
valores inválidos.

'''

from typing import Literal, Union
from pydantic import BaseModel, field_validator
from enum import Enum

# Enumerado de tipos de valores
class TipoValores(Enum):
    SENSOR = "Sensor",
    ACTUADOR = "Actuador",
    GATEWAY = "Gateway"


# Modelo dispositivo
class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal[TipoValores.SENSOR,TipoValores.ACTUADOR,TipoValores.GATEWAY]


    @field_validator("tipo")
    def validar_tipo(cls, value):
        if value not in TipoValores:
            raise ValueError
        return value
    

try:
    # Instancia válida del modelo dispositivo
    dispositivo_valido = Dispositivo(id_dispositivo=123, tipo="sensor")

    # Error de validación al utilizar valor inválido en tipo
    dispositivo_invalido = Dispositivo(id_dispositivo="456", tipo="ejemplo123")
except ValueError as e:
    print(f"Error de validación: {e}")

