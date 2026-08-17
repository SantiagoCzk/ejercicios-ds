'''
Ejercicio 9

Implementar una función de negocio transaccional (por ejemplo, 
"Matricular alumno") dentro de un bloque try-except. 

Si ocurre un error lógico o de integridad (como intentar inscribir a 
un alumno dos veces al mismo curso), invocar session.rollback() 
y capturar la excepción para cerrar la sesión de forma segura.

Crear las instancias requeridas para forzar la excepción. Verificar 
manualmente que el rollback ocurrió como se esperaba.
'''

from conexionDB import Base, engine
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship
from sqlalchemy import DateTime, String, select, ForeignKey, func
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
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="curso")

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

# Modelo de Estudiante
class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int] = mapped_column()
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="estudiante")

    def __str__(self):
        return f"\n> ID: {self.id} | Nombre: {self.nombre} | Legajo: {self.legajo}"
# Modelo de Inscripcion
class Inscripcion(Base):
    __tablename__ = "incripciones"
    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"))
    estudiante: Mapped[Estudiante] = relationship(back_populates="inscripciones")
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped[Curso] = relationship(back_populates="inscripciones")
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacion_final: Mapped[int] = mapped_column()

    def __str__(self):
        return super().__str__()


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

        estudiante1 = Estudiante(id= 1, nombre="Santiago Breczko", legajo=1004)
        estudiante2 = Estudiante(id= 2, nombre="Mateo Ruiz", legajo=1212)
        estudiante3 = Estudiante(id= 3, nombre="Tiziano Valentino", legajo=1111)

        clase1 = Clase(id= 1, tema="Variables", duracion_minutos=120, curso_id=1)
        clase2 = Clase(id= 2, tema="Funciones", duracion_minutos=180, curso_id=1)
        clase3 = Clase(id= 3, tema="Procedimientos", duracion_minutos=120, curso_id=1)

        curso1 = Curso(id= 1, titulo="Programacion", creditos=20, profesor_id= 1)
        curso2 = Curso(id= 2, titulo="Python", creditos=25, profesor_id= 1)
        
        inscripcion1 = Inscripcion(estudiante_id=1, curso_id=1, fecha_inscripcion=datetime(2024, 5, 5), calificacion_final=6)
        inscripcion2 = Inscripcion(estudiante_id=2, curso_id=1, fecha_inscripcion=datetime(2024, 5, 6), calificacion_final=7)
        inscripcion3 = Inscripcion(estudiante_id=1, curso_id=2, fecha_inscripcion=datetime(2024, 5, 7), calificacion_final=4)

        session.add_all([profesor1, profesor2, profesor3, departamento1, departamento2, curso1, curso2, clase1, 
                         clase2, clase3, estudiante1, estudiante2, estudiante3, inscripcion1, inscripcion2, inscripcion3])
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

        print("\nCURSOS QUE DICTA UN PROFESOR")
        profesor = session.scalar(select(Profesor).where(Profesor.id == 1))
        cursos_profesor = session.scalars(select(Curso).join(Profesor).where(Profesor.id == profesor.id)).all()

        cadena = f"\n> Profesor: {profesor.nombre} | Cursos que dicta: "
        for curso in cursos_profesor:
            cadena += f"{curso.titulo}, "
        print(cadena)  

        print("\nPROMEDIO DE CALIFICACION DE UN ESTUDIANTE")
        estudiante = session.scalar(select(Estudiante).where(Estudiante.legajo == 1004))
        promedio_estudiante = session.scalar(select(func.avg(Inscripcion.calificacion_final)).join(Estudiante).where(Estudiante.id == estudiante.id))

        print(f"\n> Promedio del estudiante {estudiante.nombre} es: {promedio_estudiante}")

        print("\nCANTIDAD DE ESTUDIANTES ANOTADOS POR CURSO")
        inscriptos_curso = session.execute(select(Curso.titulo, func.count(Inscripcion.id)).join(Inscripcion).group_by(Curso.id))

        print("\n>> Estudiantes anotados por curso: ")
        for titulo, cant in inscriptos_curso:
            print(f"    > {titulo}: {cant}")

        print("\nFUNCION TRASACCIONAL - INSCRIPCION ALUMNO A UN CURSO")
        try:
            # Valores Harcodeados
            legajo_estudiante = 1004
            id_curso = 1

            estudiante = session.scalar(select(Estudiante).where(Estudiante.legajo == legajo_estudiante))
            if not estudiante:
                raise ValueError(f"El estudiante con legajo {legajo_estudiante} no existe.")

            curso = session.scalar(select(Curso).where(Curso.id == id_curso))
            if not curso:
                raise ValueError(f"El curso con ID {id_curso} no existe.")

            inscripcion_existente = session.scalar(select(Inscripcion).where(Inscripcion.estudiante_id == estudiante.id).where(Inscripcion.curso_id == curso.id))

            if inscripcion_existente:
                raise ValueError(f"Error de Integridad: El estudiante {estudiante.nombre} ya está inscripto en '{curso.titulo}'.")

            nueva_inscripcion = Inscripcion(estudiante_id=estudiante.id, curso_id=curso.id, fecha_inscripcion=datetime.now(), calificacion_final=0)

            session.add(nueva_inscripcion)
            session.commit()

            print(f"\n>> {estudiante.nombre} fue matriculado en '{curso.titulo}'.")

        except ValueError as e:
            print(f"\n>>> Error Capturado: {e}")
            print(">> Ejecutando session.rollback()...")
            session.rollback() # Cancelamos cualquier operación pendiente

        finally:
            print(">> Transacción finalizada.")




    










