class Libro:
    def __init__(self, titulo,autor):
        self.titulo=titulo
        self.autor=autor

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre=nombre
        self.edad=edad
        self.pais=pais

libro1= Libro("Dune", "F. Herbet")
print(libro1.autor)

persona1 = Persona("waldo", 38, "STO DGO")
print(persona1.nombre)
#Usando POO