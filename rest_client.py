import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Ben",
    "apellido": "Pérez",
    "carrera": "Ingeneria Sistemas",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET elimina todos los estudiantes por la ruta /eliminar_estudiante
ruta_eliminar = url + "eliminar_estudiante"
eliminar_response = requests.request(method="GET"
                                , url=ruta_eliminar)
print(eliminar_response.text)

# Agregar estudiante carrera Economia
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Lucas",
    "carrera": "Economia",
}

post_response = requests.request(method="POST", 
                                url=ruta_post, 
                                json=nuevo_estudiante)
print(post_response.text)


#Agregar estudiantes con carrera de Economia
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Pablo",
    "apellido": "Rojas",
    "carrera": "Economia",
}

post_response = requests.request(method="POST", 
                                url=ruta_post, 
                                json=nuevo_estudiante)
print(post_response.text)

#buscar estudiante con carrera Economia
ruta_buscar_Economia=url+"/carreras/"
buscar_Economia_response=requests.request(method="GET",url=ruta_buscar_Economia)
print(buscar_Economia_response.text)
#mostrar todos los estudiantes
post_response = requests.request(method="POST", 
                                url=ruta_post, 
                                json=nuevo_estudiante)
print(post_response.text)
