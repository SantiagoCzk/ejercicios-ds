'''
Crear un tipo reutilizable CoordenadaGPS con Annotated que 
sea un float entre -90.0 y 90.0. 

Luego, implementa un modelo  Ubicacion que use este tipo 
de dato para sus atributos: longitud y latitud y que además 
tenga un atributo opcional etiqueta (string).

Crear una instancia de este modelo para comprobar el uso del 
tipo reutilizable, mostrando por pantalla lo que tenga la 
instancia. 

Crear otra instancia para comprobar el error de validación al 
utilizar valores inválidos de latitud/longitud.
'''

from typing import Annotated
from pydantic import BaseModel, Field

# Definicion de tipo reutilizable
CoordenadaGPS = Annotated[float,Field(ge=-90.0, le=90.0)]

# Modelo Ubicacion
class Ubicacion(BaseModel):
    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: str = Field(max_length=300, default="")

try:
    data = {"longitud" : "70", "latitud" : "60", "etiqueta" : "ejemplo de prueba"}
    ubicacion1 = Ubicacion(**data)

    data = {"longitud" : "-95", "latitud" : "100"}
    ubicacion2 = Ubicacion(**data)
except ValueError as e:
    print(f"Error en la Validacion: {e}")





