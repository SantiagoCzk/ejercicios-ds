'''
Ejercicio 1

Crear el archivo de configuración de la base de datos (puede ser 
SQLite en memoria o archivo) y definir el primer modelo 
Profesor con los campos: id, nombre, email y fecha_ingreso 
(Ver DateTime). 
Insertar un par de registros de prueba y mostrarlos por consola.

Ejercicio 2

1. Crear un nuevo modelo Departamento (id, nombre). 
2. Modificar el modelo Profesor para agregarle una clave 
foránea departamento_id. 
3. Utilizar relationship en el modelo Departamento para 
acceder a la lista de sus profesores.
Insertar un par de registros de prueba y mostrarlos por consola.

Ejercicio 3


'''

from conexionDB import Base, engine
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship
from sqlalchemy import DateTime, String, select, ForeignKey
from datetime import datetime

# Modelo de departamento
class Departamento(Base):
    __tablename__ = "departamentos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    profesores: Mapped[list["Profesor"]] = relationship()

# Modelo del profesor
class Profesor(Base):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))


if __name__ == "__main__":
    # Se crean las tablas en la base de datos
    
    Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    # Se inserta un par de registros de prueba
    with Session(engine) as session:

        departamento1 = Departamento(id= 1, nombre="Ingenieria")
        departamento2 = Departamento(id= 2, nombre="Economia")
            
        profesor1 = Profesor(id= 1, nombre="Juan Perez", email="juan.perez@example.com", fecha_ingreso=datetime(2024, 3, 1), departamento_id= 1)
        profesor2 = Profesor(id= 2, nombre="Maria Lopez", email="maria.lopez@example.com", fecha_ingreso=datetime(2024, 5, 15), departamento_id= 2)
        
        session.add_all([profesor1, profesor2, departamento1, departamento2])
        session.commit()

    # Se muestran los registros por consola
    with Session(engine) as session:
        print("\nPROFESORES\n")
        profesores = session.scalars(select(Profesor)).all()
        for p in profesores:
            print(f"ID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Fecha ingreso: {p.fecha_ingreso}") 

        print("\nDEPARTAMENTOS\n")
        departamentos = session.scalars(select(Departamento)).all()
        for d in departamentos:
            print(f"ID: {d.id} | Nombre: {d.nombre} | Profesores: ")
            for profe in d.profesores:
                print(profe.nombre)







