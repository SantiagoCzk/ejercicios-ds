from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import prestamo_libro, devolver_libro, consultar_libro

# Crear un libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("1984", "George Orwell", "978-0-452-28423-4")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-06-112241-5")


# Consultar el estado del libro
consultar_libro(libro1)
consultar_libro(libro2)
consultar_libro(libro3)

# Prestar el libro
prestamo_libro(libro1)

# Consultar el estado del libro después del préstamo
consultar_libro(libro1)

# Devolver el libro
devolver_libro(libro1)

# Consultar el estado del libro después de la devolución
consultar_libro(libro1)

