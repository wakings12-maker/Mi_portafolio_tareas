# Unidad 2 tarea 3 Calculadora robusta
#Hacer funciones para cada operacion +-*/ y convertirla a reusable
#usar try/except para manejar errores

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


# Función para obtener un número válido ingresado por el usuario
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Debes ingresar un valor numérico válido.")


# Función principal de la calculadora con bucle continuo
def calculadora():
    while True:
        print("\n--- Bienvenido a la Calculadora de Waldo ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break  # Rompe el bucle principal y cierra el programa

        if opcion not in ["1", "2", "3", "4"]:
            print("❌ Error: Opción no válida. Intenta de nuevo.")
            continue  # Regresa al inicio del bucle para pedir la opción otra vez

        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        try:
            if opcion == "1":
                resultado = sumar(num1, num2)
                operacion = "+"
            elif opcion == "2":
                resultado = restar(num1, num2)
                operacion = "-"
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                operacion = "*"
            elif opcion == "4":
                resultado = dividir(num1, num2)
                operacion = "/"

            print(f"\n✅ Resultado: {num1} {operacion} {num2} = {resultado}")

        except ZeroDivisionError as e:
            print(f"\n❌ Error matemático: {e}")
        except Exception as e:
            print(f"\n❌ Ocurrió un error inesperado: {e}")

        # Preguntar al usuario si quiere hacer otra operación antes de continuar
        continuar = (
            input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        )
        if continuar != "s":
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break


# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()