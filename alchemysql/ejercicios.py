'''
Ejercicio 5

Crea el modelo Clase (id, tema, duracion_minutos). 
Un curso se compone de muchas clases. 
Configurar la relación One-to-Many entre Curso y Clase. 
Escribir una consulta que devuelva todas las clases de un curso 
específico a través del ORM.

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

    def __str__(self):
        cadena = f"\nID: {self.id} | Nombre: {self.nombre} | Profesores: "
        for p in self.profesores:
            cadena += f"{p.nombre}, "
        return cadena


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

    def __str__(self):
        cadena = f"\nID: {self.id} | Nombre: {self.nombre} | Email: {self.email} | Fecha ingreso: {self.fecha_ingreso} | Departamento: {p.departamento.nombre} | Cursos: "
        for c in self.cursos:
            cadena += f"{c.titulo}, "
        return cadena

# Modelo de Curso
class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column(default=0)
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Profesor] = relationship(back_populates="cursos")
    clases: Mapped[list["Clase"]] = relationship(back_populates="curso")

    def __str__(self):
        cadena = f"\nID: {self.id} | Titulo: {self.titulo} | Creditos: {self.creditos} | Profesor: {self.profesor.nombre}"
        return cadena

# Modelo de Clase
class Clase(Base):
    __tablename__ = "clases"
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(100))
    duracion_minutos: Mapped[int] = mapped_column()
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped[Curso] = relationship(back_populates="clases")

    def __str__(self):
        cadena = f"ID: {self.id} | Tema: {self.tema} | Duracion(minutos): {self.duracion_minutos} | Curso: {self.curso.titulo}"
        return cadena


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

        clase1 = Clase(id= 1, tema="Variables", duracion_minutos=120, curso_id=1)
        clase2 = Clase(id= 2, tema="Funciones", duracion_minutos=180, curso_id=1)
        clase3 = Clase(id= 3, tema="Procedimientos", duracion_minutos=120, curso_id=1)

        curso1 = Curso(id= 1, titulo="Programacion", creditos=20, profesor_id= 1)
        curso2 = Curso(id= 2, titulo="Python", creditos=25, profesor_id= 2)
        
        session.add_all([profesor1, profesor2, profesor3, departamento1, departamento2, curso1, curso2, clase1, clase2, clase3])
        session.commit()

    # Se muestran los registros por consola
    with Session(engine) as session:
        print("\nPROFESORES")
        profesores = session.scalars(select(Profesor)).all()
        for p in profesores:
            print(p.__str__())

        print("\nDEPARTAMENTOS")
        departamentos = session.scalars(select(Departamento)).all()
        for d in departamentos:
            print(d.__str__())

        print("\nCURSOS")
        cursos = session.scalars(select(Curso)).all()
        for curso in cursos:
            print(curso.__str__())

        print("\nCLASES DE UN CURSO")
        curso = session.scalar(select(Curso).where(Curso.id == 1))
        cadena = f"\nCurso: {curso.titulo} | Clases: "
        for clase in curso.clases:
            cadena += f"{clase.tema}, "
        print(cadena)

    










