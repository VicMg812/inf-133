import requests

query="""{
    hello
    goodbye
}"""
# queryB="""{
#     goodbye
# }"""

url='http://localhost:8000/graphql'

response=requests.post(url,json={'query':query})
# responseB=requests.post(url,json={'query':queryB})
print(response.text)
# print(responseB.text)
