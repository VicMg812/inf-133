# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn=sqlite3.connect("restaurante.db")

# Crear tabla de Platos
try:
    conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    categoria TEXT NOT NULL);
    """
)
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")
# Insertar datos de platos
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
try:
    conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")
#Insertar datos a mesas
conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(4)
    """
)
#Consultar datos platos
print("\nMESAS:")
cursor=conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
# Crear tabla de pedidos
try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla MATRICULAS ya existe")
# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 1, 25,'2024-01-12')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (2, 2, 4,'2024-01-23')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 5,'2024-01-31')
    """
)
# Listar datos de matriculación
print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)
# Consultar datos de matriculación INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, MESAS.numero, PEDIDOS.cantidad 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)
# Eliminar una fila de la tabla de matriculación
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)

for row in cursor:
    print(row)
# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE PEDIDOS
    SET fecha = '2024-01-28'
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)
for row in cursor:
    print(row)
#INNSER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)
#Left JOIN`
print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PEDIDOS.cantidad
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    """
)
for row in cursor:
    print(row)
# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()