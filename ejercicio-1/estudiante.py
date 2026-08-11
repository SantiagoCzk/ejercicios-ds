'''
Crear un modelo Estudiante que contenga:
    ● legajo: entero positivo
    ● nombre_completo: string de al menos 5 caracteres
    ● email: string con formato de correo electrónico
    ● promedio: float entre 0.0 y 10.0 con valor por defecto de 0.0
Crear una instancia por cada posible error de validación para 
observar el mensaje que nos da Python al utilizar valores 
inválidos.
'''

from typing import Annotated
from pydantic import BaseModel, EmailStr, Field

# Clase estudiante
class Estudiante(BaseModel):
    legajo: Annotated[int, Field(gt=0)]
    nombre_completo: Annotated[str, Field(min_length=5)]
    email: EmailStr
    promedio: Annotated[float, Field(ge=0.0, le=10.0)] = 0.0


# Instancia con legajo inválido (negativo)
try:
    datos = {"legajo": -1, "nombre_completo": "Juan Pérez", "email": "juanperez@example.com", "promedio": 8.5}
    estudiante1 = Estudiante(**datos)
except Exception as e:
    print(f"Error al crear estudiante1: {e}")

# Instancia con nombre_completo inválido (menos de 5 caracteres)
try:
    datos = {"legajo": 123, "nombre_completo": "Ana", "email": "ana@example.com", "promedio": 9.0}
    estudiante2 = Estudiante(**datos)
except Exception as e:
    print(f"Error al crear estudiante2: {e}")

# Instancia con email inválido (formato incorrecto)
try:
    datos = {"legajo": 456, "nombre_completo": "Carlos López", "email": "carlos.lopezexample.com", "promedio": 7.5}
    estudiante3 = Estudiante(**datos)
except Exception as e:
    print(f"Error al crear estudiante3: {e}")

# Instancia con promedio inválido (mayor a 10.0)
try:
    datos = {"legajo": 789, "nombre_completo": "María García", "email": "mariagarcia@example.com", "promedio": 11.0}
    estudiante4 = Estudiante(**datos)
except Exception as e:
    print(f"Error al crear estudiante4: {e}")



