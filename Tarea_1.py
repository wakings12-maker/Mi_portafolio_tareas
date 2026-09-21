#Tarea 1 Ficha personal

print("Bienvenido a la ficha personal. Por favor, ingrese los siguientes datos:")
nombre = input("Ingrese su nombre: ") #declaro la variable nombre y le asigno su valor con el input
edad = int(input("Ingrese su edad: "))#declaro la variable edad y le asigno su valor con el input y lo convierto a entero con int()
ciudad = input("Ingrese su ciudad donde vive: ") #declaro la variable ciudad y le asigno su valor con el input

print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")#Imprimo el mensaje con los datos ingresados por el usuario.