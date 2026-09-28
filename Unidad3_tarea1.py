#Unidad 3 Tarea 1 Modelo de libro
#Utilizando POO vamos a diseñar una clase libro, con atributos y varios metodos

class Libro():
    def __init__(self, Titulo, Autor):
        self.Titulo=Titulo
        self.Autor=Autor
        self.Disponible=True

    def mostrar_info(self):
        return "Titulo:", self.Titulo, "Autor:", self.Autor, "Disponible:", self.Disponible

    def prestar(self, prestado):
        self.Disponible=prestado
        print("\n!Ha tomado el libro prestado de forma exitosa.!")
    
def pedir_opcion(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Debes ingresar un valor numérico válido.")


miLibro=Libro("Orgullo y prejuicio","Jane Austen")
print("Opcion 1.: ", miLibro.mostrar_info())
miLibro2=Libro("Cien años de soledad", "Gabriel García Márquez")
print("Opcion 2.: ", miLibro2.mostrar_info())
miLibro3=Libro("Harry Potter", "J.K. Rowling")
print("Opcion 3.: ", miLibro3.mostrar_info())


continuar = input("\n¿Desea tomar prestado algun libro?  Eliga (s/n)  ").strip().lower()

if continuar == "s":
    opcion = pedir_opcion("¿Cual de los 3 libros desea tomar prestado?  ")
    if opcion == 1:
        miLibro.prestar(False)
    elif opcion == 2:
         miLibro2.prestar(False)
    elif opcion == 3:
        miLibro3.prestar(False)
    else:
        print("❌ Error: Opción no válida. Intenta de nuevo.")
else:
    print("¡Gracias por usar la Biblioteca! Hasta luego.")
    
print("\nActualizando estado de los libros.")
print("Opcion 1.: ", miLibro.mostrar_info())
print("Opcion 2.: ", miLibro2.mostrar_info())
print("Opcion 3.: ", miLibro3.mostrar_info())