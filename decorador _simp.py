@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    print(f,"Hola,{name}!")

greet("Juan")
print(greet.__name__)
print(greet.__doc__)