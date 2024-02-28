from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Victor")
print(result)

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
client = Client(wsdl_url)
number_to_convert = 100
result = client.service.NumberToDollars(number_to_convert)
print(f"{number_to_convert} en dólares es: {result}")