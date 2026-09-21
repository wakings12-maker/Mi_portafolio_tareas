#Tarea 3 validador de mayor de edad  
print("Bienvenido al validador de mayor de edad.")

edad_usuario = int(input("Ingrese su edad: "))
count = 0
while (edad_usuario < 0 or edad_usuario > 100):
    count += 1
    print(f"Tiene {count} intento. Le quedan {3-count} intentos.")
    print("Edad inválida. Por favor, ingrese un valor entre 0 y 100.")
    edad_usuario = int(input("Ingrese su edad: "))

    if  edad_usuario >= 18 and edad_usuario <= 100:
            print("Aprobado. Usted es mayor de edad.")
    else:
            if count >= 2 :
                print("Ha excedido el número máximo de intentos. Saliendo del programa.")
                exit()
            print("Rechazado. Usted no es mayor de edad.")

    

    
        





