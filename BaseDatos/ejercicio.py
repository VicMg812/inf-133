# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn=sqlite3.connect("restaurante.db")

# Crear tabla de Platos
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    categoria TEXT NOT NULL);
    """
)
# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES('Pizza',10.99,'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES('Hamburguesa',8.99,'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES('Shushi',12.99,'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES('Ensalada',6.99,'Vegetariana')
    """
)
#Consultar datos
print("PLATOS:")
cursor=conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

#Crear tabla mesas
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)
#Insertar datos a estudiantes
conn.execute(
    """
    INSERT INTO PLATOS(numero)
    VALUES(1)
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(numero)
    VALUES(2)
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(numero)
    VALUES(3)
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(numero)
    VALUES(4)
    """
)
#Consultar datos platos
print("\nPLATOS:")
cursor=conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)