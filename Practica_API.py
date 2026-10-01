import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)

print("Codigo de estado: ", respuesta.status_code)
print("Datos Recibidos")
print(respuesta.json())