#Tarea 2 Calculadora de Propinas

print("Bienvenido a la calculadora de propinas.")
total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

while porcentaje_propina < 0 or porcentaje_propina > 100:
    print("El porcentaje de propina no puede ser negativo ni mayor a 100. Por favor, ingrese un valor válido.")
    porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

#fin del while
propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina

print(f"El total de la cuenta es: ${total_cuenta:.2f}")
print(f"La propina es: ${propina:.2f}")
print(f"El total con propina es: ${total_con_propina:.2f}")