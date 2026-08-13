'''
Construir un modelo PerfilUsuario que combine:
    ● username: string alfanumérico en minúsculas usando el atributo pattern de Field y la expresión regular r"^[a-z0-9_]{3,20}$"
    ● biografia: opcional, con un máximo de 200 caracteres.
    ● redes_sociales: lista opcional de strings, URLs o nombres. (Ver Types/urls)
'''

from pydantic import BaseModel, Field, AnyUrl


# Modelo PerfilUsuario
class PerfilUsuario(BaseModel):
    username: str = Field(pattern=r"^[a-z0-9_]{3,20}$")
    biografia: str = Field(max_length=200, default="")
    redes_sociales: list[AnyUrl] = Field(default_factory=list)


# Prueba de perfiles de usuarios
try:
    redes = ["https://github.com/santiagoczk", "https://linkedin.com/in/santiagoczk"]

    perfil1 = PerfilUsuario(
        username="santiagoczk",
        biografia="Estudiante de desarrollo de software",
        redes_sociales=redes
    )
    print(f"\n> Mostrando Perfil: {perfil1}")

    redes = ["ig: pedro04", "X: pedro9004"]

    perfil2 = PerfilUsuario(username="USERNAME", redes_sociales=redes)
except ValueError as e:
        print(f"\n>>> Error en la Validacion: {e}")   

