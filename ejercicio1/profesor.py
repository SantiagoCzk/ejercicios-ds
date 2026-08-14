'''
Crear el archivo de configuración de la base de datos (puede ser 
SQLite en memoria o archivo) y definir el primer modelo 
Profesor con los campos: id, nombre, email y fecha_ingreso 
(Ver DateTime). 
Insertar un par de registros de prueba y mostrarlos por consola.

'''

from conexionDB import Base, engine
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import DateTime, String, select, delete
from datetime import datetime


# Modelo del profesor
class Profesor(Base):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)


# Se crean las tablas en la base de datos
Base.metadata.create_all(engine)

# Se inserta un par de registros de prueba
''' '''
with Session(engine) as session:

    profesor1 = Profesor(nombre="Juan Perez", email="juan.perez@example.com", fecha_ingreso=datetime(2024, 3, 1))
    profesor2 = Profesor(nombre="Maria Lopez", email="maria.lopez@example.com", fecha_ingreso=datetime(2024, 5, 15))

    session.add_all([profesor1, profesor2])
    session.commit()

# Se muestran los registros por consola
with Session(engine) as session:
    profesores = session.scalars(select(Profesor)).all()
    for p in profesores:
        print(f"ID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Fecha ingreso: {p.fecha_ingreso}")


# Para borrar a todos los profesores
''' 
with Session(engine) as session:
    profesores = session.scalars(select(Profesor)).all()

    if profesores:
        for profesor in profesores:
            session.delete(profesor)

    session.commit()
'''






