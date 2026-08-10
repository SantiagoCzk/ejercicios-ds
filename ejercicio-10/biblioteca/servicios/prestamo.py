from biblioteca.modelos.libro import Libro


def prestamo_libro(libro: Libro):
    if libro.disponible:
        libro.disponible = False
        print(f"El libro '{libro.titulo}' ha sido prestado.")
    else:
        print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

def devolver_libro(libro: Libro):
    if not libro.disponible:
        libro.disponible = True
        print(f"El libro '{libro.titulo}' ha sido devuelto.")
    else:
        print(f"El libro '{libro.titulo}' no estaba prestado.")


def consultar_libro(libro: Libro):
    estado = "disponible" if libro.disponible else "prestado"
    print(f"El libro '{libro.titulo}' está {estado}.")