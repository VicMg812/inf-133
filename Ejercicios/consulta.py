# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# Insertar datos de departamentos
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Marketing', '11-04-2020')
    """
)
print("DEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)
# Insertar datos de departamentos
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Gerente de Ventas','Senior', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Analista de Marketing','Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Representante de Ventas','Junior', '12-04-2020')
    """
)
print("CARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)
