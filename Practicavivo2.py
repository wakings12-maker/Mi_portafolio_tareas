#Practica en vivo Unidad 3

from abc import ABC, abstractclassmethod
class Libro(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def mostrar_info(self):
        estado = "disponible" if self.disponible else "prestado"
        print(f"{self.titulo} de {self.autor} - {estado}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, mb):
        super().__init__(titulo, autor)
        self.tamano_mb = mb

    def mostrar_info(self):
        print(f"{self.titulo} - Digital ({self.tamano_mb}MB)")

class LibroFisico(Libro):
    def __init__(self, titulo, autor, estante):
        super().__init__(titulo, autor)
        self.estante = estante

    def mostrar_info(self):
        print(f"{self.titulo} - Estante {self.estante}")
