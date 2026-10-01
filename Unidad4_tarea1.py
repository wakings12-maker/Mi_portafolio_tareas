import requests
#Declaro la pagina web que voy a consultar
url = "https://jsonplaceholder.typicode.com/posts/1" 
#declaro la variable respuesta para que obtenga la info de la URL
respuesta = requests.get(url)

print("Codigo de estado: ", respuesta.status_code) #Imprimo el estatus de comunicacion de la API
print("Datos Recibidos")
print(respuesta.json()) #Imprimo la info de la URL

#Explicacion de la respuesta: el request me devuelve un arreglo o esquema con 4 datos. 
# UserID, ID, title y body. El status de la respuesta debe ser 200 que indica que la comunicacion fue exitosa.