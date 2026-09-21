#exlicando funciones

#def multiplicador_por_tres(x:int)
   # return x*3

#print(multiplicador_por_tres(5))


"""def verificador_edad(edad:int):
    if edad >= 18:
        return "Aprobado. Usted es mayor de edad."
    else:
        return "Rechazado. Usted no es mayor de edad."
edad = int(input("Ingrese su edad: "))

resultado = verificador_edad(edad)
print(resultado)


#listas y tuplas

Listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Tuplas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
se comienza a contar en cero, por lo que el primer elemento de la lista es el índice 0, el segundo elemento es el índice 1, y así sucesivamente.
print(Listas[0])  # Imprime el primer elemento de la lista
print(Tuplas[0])  # Imprime el primer elemento de la tupla

Listas.append(11)  # Agrega un elemento al final de la lista
print(Listas)  # Imprime la lista actualizada
Listas.insert(0, 0)  # Inserta un elemento en la posición 0 de la lista
Listas.remove(5)  # Elimina el primer elemento con valor 5 de la lista
Listas.pop()  # Elimina el último elemento de la lista
Listas.clear()  # Elimina todos los elementos de la lista
Listas[-1] = 100  # Cambia el último elemento de la lista a 100

listas de varias dimensiones son listas que contienen otras listas como elementos. Se pueden crear listas de varias dimensiones utilizando corchetes anidados. Por ejemplo, una lista de dos dimensiones se puede crear de la siguiente manera:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printmatriz[0][0]  # Accede al primer elemento de la primera lista (1)


tuplas no se pueden modificar, por lo que no se pueden agregar, eliminar o cambiar elementos de una tupla después de que se ha creado. Sin embargo, se pueden realizar operaciones como concatenación y repetición para crear nuevas tuplas a partir de las existentes.
podemos cambiar de tupla a lista y viceversa, para poder modificar los elementos de la tupla. Para convertir una tupla en una lista, podemos usar la función list(). Por ejemplo:
tuplas_lista = list(Tuplas)  # Convierte la tupla en una lista
tuplas_lista.append(11)  # Agrega un elemento a la lista
print(tuplas_lista)  # Imprime la lista actualizada


Diccionarios son estructuras de datos que permiten almacenar pares de clave-valor. 
Cada elemento del diccionario se compone de una clave única y un valor asociado a esa clave.
Los diccionarios se definen utilizando llaves {} y los elementos se separan por comas. 

Por ejemplo:
mi_diccionario = {
    "nombre": "waldo
    "edad": 38
    "ciudad": "santo"
}

lista_diccionarios = [
    mi_diccionario,
    {"nombre": "Juan", "edad": 30, "ciudad": "Madrid    "},
    {"nombre": "María", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Valencia"}
]
print(mi_diccionario["nombre"])  # Imprime "maria
print(lista_diccionarios[0]["nombre"])  # Imprime "Juan"

print(lista_diccionarios[1]["edad"])  # Imprime 30
print(lista_diccionarios[0]["nombre"])


bucles for y while

lfor i in range(5):
    print(i)  # Imprime los números del 0 a 4  

while True:
     respuesta = input("Ingrese 'salir' para terminar el bucle: ")
     if respuesta == "salir":
     break  # Sale del bucle while
     
count =0
while (count < 5):
    print(count)
    count += 1  # Incrementa el contador en 1   

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)  # Imprime cada elemento de la lista  

  


    try:
        numero = int(input("Ingrese un número: "))
        print("El número ingresado es:", numero)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")  
        

"""
