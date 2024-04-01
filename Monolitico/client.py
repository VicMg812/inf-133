import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")

# print(response.text)
# #Buscar el post 2
# response2 = requests.get(f"{url}/post/2")
# print(response2.text)
newpost={
    "title":"Mi experiencia con dev",
    "content":"Esta es mi experiencia como dev",
}
response_new=requests.post(f"{url}/posts",data=newpost)
response = requests.get(f"{url}/posts")
print(response_new.text)
print(response.text)
