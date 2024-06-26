import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /tacos
response = requests.get(url)
print(response.json())

# POST /tacos 
mi_taco = {
    "base": "Pequeña",
    "guiso": "Poca",
    "salsa": "Normal",
    "toppings": ["Carne", "Papa"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# PUT /tacos/1
edit_taco = {
    "base": "Mediano",
    "guiso": "Mucha",
    "salsa": "Picante",
    "toppings": ["Carne","Tunta"]
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# DELETE /tacos/1

response = requests.delete(url + "/1")
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())