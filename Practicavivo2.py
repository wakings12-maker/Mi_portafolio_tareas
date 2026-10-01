#Practica en vivo Unidad 3

from abc import ABC, abstractmethod
class Libro(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    @abstractmethod
    def mostrar_info(self)->str:
        pass

class LibroDigital(Libro):
    def __init__(self, titulo, autor, mb):
        super().__init__(titulo, autor)
        self.tamano_mb = mb

    def mostrar_info(self):
        return(f"{self.titulo} - Digital ({self.tamano_mb}MB)")

class LibroFisico(Libro):
    def __init__(self, titulo, autor, estante):
        super().__init__(titulo, autor)
        self.estante = estante

    def mostrar_info(self):
        return(f"{self.titulo} - Estante {self.estante}")


libro1 = Libro("Pantheon", "Neflix")
libro2 = Libro("La Mansion de Luis", "Luis Felipe")

biblio.agregar_libro()
