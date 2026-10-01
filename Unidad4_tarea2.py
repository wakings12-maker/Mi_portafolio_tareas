import json
import requests
respuesta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true" )    
datos_clima = respuesta.json()  # Convertir la respuesta a un diccionario de Python 

print("Codigo de estado: ", respuesta.status_code) #Imprimo el estatus de comunicacion de la API
print("Datos Recibidos")
print(datos_clima)  # Imprime el diccionario con los datos del clima
print(f"\nTemperatura actual: {datos_clima['current_weather']['temperature']}°C")  # Imprime la temperatura actual    
print(f"Velocidad del viento: {datos_clima['current_weather']['windspeed']} km/h")  # Imprime la velocidad del viento   
print(f"Dirección del viento: {datos_clima['current_weather']['winddirection']}°")  # Imprime la dirección del viento   
print(f"Hora de la medición: {datos_clima['current_weather']['time']}")  # Imprime la hora de la medición   
print(f"Condición del clima: {datos_clima['current_weather']['weathercode']}")  # Imprime el código de condición del clima  

with open("clima.json", "w") as archivo_json:
    json.dump(datos_clima, archivo_json)  # Guardar el diccionario en un archivo JSON
print("Datos del clima guardados en clima.json")  # Mensaje de confirmación
