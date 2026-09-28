#Unidad 3 Tarea 3 Herencia de libros 


from abc import ABC, abstractclassmethod

class Libro(ABC):

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  

    @abstractclassmethod
    def mostrar_info(self)->str:
        pass

class LibroDigital(Libro):
    def __init__(self, titulo, autor, mb):
        super().__init__(titulo, autor)
        self.tamano_mb = mb

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return(f"{self.titulo} - Autor: {self.autor} [{estado}]- Tamaño ({self.tamano_mb}MB)")

class LibroFisico(Libro):
    def __init__(self, titulo, autor, estante):
        super().__init__(titulo, autor)
        self.estante = estante

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return(f"{self.titulo} - Autor: {self.autor} [{estado}]- Estante {self.estante}")

class Biblioteca:
    """Clase que gestiona la colección de libros."""

    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        """Agrega un objeto de la clase Libro al catálogo."""
        self.catalogo.append(libro)
        print(f"✅ Libro '{libro.titulo}' agregado con éxito.")

    def buscar_por_titulo(self, titulo_buscar):
        """Busca libros cuyo título coincida o contenga el texto buscado."""
        encontrados = [
            l
            for l in self.catalogo
            if titulo_buscar.lower() in l.titulo.lower()
        ]
        return encontrados

    def prestar_libro(self, titulo_prestar):
        """Cambia el estado de un libro a no disponible si existe y está libre."""
        libros_coincide = self.buscar_por_titulo(titulo_prestar)

        if not libros_coincide:
            print("❌ No se encontró ningún libro con ese título.")
            return

        # Si hay coincidencias, intentamos prestar el primero que esté disponible
        for libro in libros_coincide:
            if libro.disponible:
                libro.disponible = False
                print(f" Has solicitado el préstamo de: '{libro.titulo}'.")
                return

        print("❌ Ese libro ya se encuentra prestado actualmente.")

    def mostrar_disponibles(self):
        """Muestra la lista de todos los libros que están disponibles."""
        libros_libres = [l for l in self.catalogo if l.disponible]

        if not libros_libres:
            print(" No hay libros disponibles en este momento.")
            return

        print("\n--- Libros Disponibles ---")
        for libro in libros_libres:
            print(libro.mostrar_info())


# Función principal con el menú interactivo y bucle continuo
def ejecutar_sistema():
    mi_biblioteca = Biblioteca()

    # Algunos libros iniciales de prueba
    mi_biblioteca.agregar_libro(
        LibroFisico("Cien años de soledad", "Gabriel García Márquez", "B5")
    )
    mi_biblioteca.agregar_libro(LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes", "B5"))
    mi_biblioteca.agregar_libro(LibroDigital("El Principito", "Antoine de Saint-Exupéry", 300))

    while True:
        print("\n=== GESTIÓN DE BIBLIOTECA ===")
        print("1. Agregar un nuevo libro")
        print("2. Buscar libro por título")
        print("3. Solicitar préstamo de un libro")
        print("4. Mostrar todos los libros disponibles")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        try:
            if opcion == "5":
                print("¡Gracias por usar el sistema de biblioteca! Saliendo...")
                break

            elif opcion == "1":
                titulo = input("Ingresa el título del libro: ").strip()
                autor = input("Ingresa el autor del libro: ").strip()
                tipo = input("Este libro es Digital. Elija s/n  ").strip().lower()
               

                if not titulo or not autor:
                    raise ValueError(
                        "El título y el autor no pueden estar vacíos."
                    )

                if tipo == "s":
                    tamano_mb = input("Ingrese el tamaño MB del libro.  ").strip()
                    nuevo_libro = LibroDigital(titulo, autor,tamano_mb)
                    mi_biblioteca.agregar_libro(nuevo_libro) 

                else:      
                    estante = input("Ingrese el estante donde estara ubicado el libro.  ").strip()
                    nuevo_libro = LibroFisico(titulo, autor, estante)
                    mi_biblioteca.agregar_libro(nuevo_libro)


                

            elif opcion == "2":
                busqueda = input("Ingresa el título (o parte de él) a buscar: ").strip()
                if not busqueda:
                    raise ValueError("Debes ingresar un término de búsqueda.")

                resultados = mi_biblioteca.buscar_por_titulo(busqueda)
                if resultados:
                    print("\n🔍 Resultados de la búsqueda:")
                    for libro in resultados:
                        print(libro)
                else:
                    print("❌ No se encontraron libros con ese criterio.")

            elif opcion == "3":
                titulo_p = input(
                    "Ingresa el título del libro que quieres prestar: "
                ).strip()
                if not titulo_p:
                    raise ValueError(
                        "Debes ingresar el título del libro a prestar."
                    )

                mi_biblioteca.prestar_libro(titulo_p)

            elif opcion == "4":
                mi_biblioteca.mostrar_disponibles()

            else:
                print("❌ Opción inválida. Por favor, selecciona del 1 al 5.")

        except ValueError as e:
            print(f"❌ Error de entrada: {e}")
        except Exception as e:
            print(f"💥 Ocurrió un error inesperado: {e}")


# Ejecución del programa
if __name__ == "__main__":
    ejecutar_sistema()