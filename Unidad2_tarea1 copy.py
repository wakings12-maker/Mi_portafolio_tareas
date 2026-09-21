#Unidad 2 Tarea 1 Analizador de Números

print("Bienvenido al Analizador de Números")

#declarando la funcion para guardar los numeros en una lista
def guardar_numeros():
    numeros = []
    cantidad_numeros = int(input("Ingrese la cantidad de números que desea analizar: "))
    for _ in range(cantidad_numeros):
        try:
            numero = int(input("Ingrese un número entero: "))
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            continue
     
        except KeyboardInterrupt:
            print("\nProceso interrumpido por el usuario.")
            break
        except EOFError:
            print("\nFin de entrada detectado.")
            break
    return numeros

numeros_ingresados = guardar_numeros()
print("Números ingresados:", numeros_ingresados)
print("El promedio de los números ingresados es:", sum(numeros_ingresados) / len(numeros_ingresados))
print("El número máximo ingresado es:", max(numeros_ingresados))
print("El número mínimo ingresado es:", min(numeros_ingresados))
