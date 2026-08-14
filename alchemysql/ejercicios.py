'''
Ejercicio 4

Crear el modelo Curso (id, titulo, creditos). 
Un profesor puede dictar muchos cursos, pero un curso es 
dictado por un único profesor. 
Añadir la clave foránea profesor_id en Curso y la relación 
correspondiente en ambos modelos (Profesor y Curso).

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
    profesores: Mapped[list["Profesor"]] = relationship(back_populates="departamento")

# Modelo del profesor
class Profesor(Base):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    departamento: Mapped[Departamento] = relationship(back_populates="profesores")
    cursos: Mapped[list["Curso"]] = relationship(back_populates="profesor")

# Modelo de Curso
class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(default=0)
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Profesor] = relationship(back_populates="cursos")


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
        profesor3 = Profesor(id= 3, nombre="Marcos Ruiz", email="marcos@gmail.com",fecha_ingreso=datetime(2024, 6, 20), departamento_id= 1)

        curso1 = Curso(id= 1, titulo="Programacion", creditos=20, profesor_id= 1)
        curso2 = Curso(id= 2, titulo="Python", creditos=25, profesor_id= 2)
        
        session.add_all([profesor1, profesor2, profesor3, departamento1, departamento2, curso1, curso2])
        session.commit()

    # Se muestran los registros por consola
    with Session(engine) as session:
        print("\nPROFESORES")
        profesores = session.scalars(select(Profesor)).all()
        for p in profesores:
            print(f"\nID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Fecha ingreso: {p.fecha_ingreso} | Departamento: {p.departamento.nombre} | Cursos: ")
            for c in p.cursos:
                print(c.titulo)

        print("\nDEPARTAMENTOS")
        departamentos = session.scalars(select(Departamento)).all()
        for d in departamentos:
            print(f"\nID: {d.id} | Nombre: {d.nombre} | Profesores: ")
            for profe in d.profesores:
                print(profe.nombre)

        print("\nCURSOS")
        cursos = session.scalars(select(Curso)).all()
        for curso in cursos:
            print(f"\nID: {curso.id} | Titulo: {curso.titulo} | Creditos: {curso.creditos} | Profesor: {curso.profesor.nombre}")






