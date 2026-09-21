# Unidad 2 Tarea 2 Agenda de contactos
# Usar diccionario para guardar los contactos. 
# Funciones para agregar, buscar y mostrar contactos guardados.

def agregar_contacto(contactos):
	#Agrega un contacto:
	nombre = input("Nombre: ").strip()

	if not nombre:
		print("El nombre no puede estar vacío.")
		return

	if nombre in contactos:
		print("Ese contacto ya existe.")
		return

	telefono = input("Teléfono: ").strip()
	correo = input("Correo: ").strip()
	contactos[nombre] = (telefono, correo)
	print("Contacto agregado correctamente.")


def buscar_contacto(contactos):
	#Busca y muestra un contacto por su nombre.
	nombre = input("Nombre del contacto que desea buscar: ").strip()
	contacto = contactos.get(nombre)

	if contacto is None:
		print("Contacto no encontrado.")
		return

	telefono, correo = contacto
	print(f"Nombre: {nombre}")
	print(f"Teléfono: {telefono}")
	print(f"Correo: {correo}")


def mostrar_contactos(contactos):
	#Muestra todos los contactos guardados.
	if not contactos:
		print("No hay contactos guardados.")
		return

	print("\nContactos guardados:")
	for nombre, (telefono, correo) in contactos.items():
		print(f"- {nombre}: teléfono {telefono}, correo {correo}")


def agenda():
	contactos = {}

	print("Bienvenido a su agenda de contactos")

	while True:
		print("\n1. Agregar contacto")
		print("2. Buscar contacto")
		print("3. Mostrar todos los contactos")
		print("4. Salir")
		opcion = input("Seleccione una opción: ").strip()

		if opcion == "1":
			agregar_contacto(contactos)
		elif opcion == "2":
			buscar_contacto(contactos)
		elif opcion == "3":
			mostrar_contactos(contactos)
		elif opcion == "4":
			print("Hasta luego.")
			break
		else:
			print("Opción no válida.")


if __name__ == "__main__": agenda()