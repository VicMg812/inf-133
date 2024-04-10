# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

#Crear la tabla Departamentos
try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")
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

# Consultar datos
print("DEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)

#Crear tabla de CARGOS
try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")
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
# Consultar datos
print("CARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)
#Crea tabla EMPLEADOS
try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTERGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")
# Insertar datos de empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion,departamento_id,cargo_id,fecha_creacion) 
    VALUES ('Juan','Gonzales','Perez','2023-05-15',1,1,'10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion,departamento_id,cargo_id,fecha_creacion) 
    VALUES ('Maria','Lopez','Martinez','2023-06-20',2,2,'11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion,departamento_id,cargo_id,fecha_creacion) 
    VALUES ('Carlos','Sanchez','Rodriguez','2023-03-9',1,3,'11-04-2020')
    """
)
# Consultar datos
print("EMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)
#Crea tabla SALARIOS
try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
    empleado_id INTEGER NOT NULL,
    salario INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    fecha_creacion TEXT NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")
conn.execute(
    """
    INSERT INTO SALARIOS (salario,fecha_inicio,fecha_fin,fecha_creacion,empleado_id) 
    VALUES (3000,'2024-04-01','2025-04-30','10-04-2020',1)
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS (salario,fecha_inicio,fecha_fin,fecha_creacion, empleado_id) 
    VALUES (3500,'2023-07-01','2024-04-30','11-04-2020',2)
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS (salario,fecha_inicio,fecha_fin,fecha_creacion, empleado_id) 
    VALUES (3500,'2023-05-05','2024-05-12','11-04-2020',3)
    """
)
# Consultar datos
print("SALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)

# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE CARGOS
    SET nombre = 'Representante de ventas'
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nCARGOS:")
cursor = conn.execute(
    "SELECT * FROM CARGOS"
)
# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nSALARIOS:")
cursor = conn.execute(
    "SELECT * FROM SALARIOS"
)
for row in cursor:
    print(row)

# Eliminar una fila de la tabla de matriculación
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nEMPLEADOS:")
cursor = conn.execute(
    "SELECT * FROM EMPLEADOS"
)

for row in cursor:
    print(row)

# Eliminar una fila de la tabla de matriculación
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

# Listar datos de matriculación
print("\nSALARIOS:")
cursor = conn.execute(
    "SELECT * FROM SALARIOS"
)

for row in cursor:
    print(row)

    

# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()