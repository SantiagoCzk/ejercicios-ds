'''
Escribir un bloque de código que intente instanciar un modelo 
UsuarioSistema con campos: 

    ● email: utilizar EmailStr 
    ● nivel_acceso: entero entre 1 y 5 proveyendo datos incorrectos.

Capturar explícitamente la excepción ValidationError 
imprimiendo por pantalla los errores detallados. (Ver: try/except)
'''

from pydantic import BaseModel, EmailStr, ValidationError, Field


# Modelo Usuario
class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5)

# Prueba de usuario
try:
    
    data = {"email" : "santiagoczk04gmail.com", "nivel_acceso" : "0"}
    usuario1 = UsuarioSistema(**data)    
    
    usuario2 = UsuarioSistema(email="juanperez@gmail.com", nivel_acceso=3)
except ValidationError as e:
    print(f">>> Error: Se detectaron errores\n")
    for error in e.errors():    # e.error() muestra mas detalles de los errores que ocurrieron (devuelve una lista)
        print(f">> {error}\n")

