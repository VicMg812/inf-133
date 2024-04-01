import requests
query="""{
#    estudiantePorId(id:2){
#     nombre
#    }
#    estudiantePorNombreApellido(nombre:"Jose",apellido:"Lopez"){
#     nombre,apellido
#    }
   estudiantePorCarrera(carrera:"Arquitectura"){
    carrera
   }
}"""
query_crear="""
mutation{
    crearEstudiante(nombre:"Angel",apellido:"Gomez",carrera:"Sistemas"){
        estudiante{
            id
            nombre
            apellido
            carrera
        }
    }
}
"""
query_crear2="""
mutation{
    crearEstudiante(nombre:"Ben",apellido:"Gutierrez",carrera:"Arquitectura"){
        estudiante{
            id
            nombre
            apellido
            carrera
        }
    }
}
"""
query_crear3="""
mutation{
    crearEstudiante(nombre:"Maria",apellido:"Padilla",carrera:"Arquitectura"){
        estudiante{
            id
            nombre
            apellido
            carrera
        }
    }
}
"""
query_buscar="""
mutation{
    buscarCar(carrera:"Arquitectura"){
        estudiante{
            nombre
            carrera
        }
    }
}
"""

url='http://localhost:8000/graphql'


response_mutation=requests.post(url,json={'query':query_crear})
# print(response_mutation.text)
response_mutation=requests.post(url,json={'query':query_crear2})
# print(response_mutation.text)
response_mutation=requests.post(url,json={'query':query_crear3})
# print(response_mutation.text)
response_mutation=requests.post(url,json={'query':query_buscar})
print(response_mutation.text)
response=requests.post(url,json={'query':query})
print(response.text)