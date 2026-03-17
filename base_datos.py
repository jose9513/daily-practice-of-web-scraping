import sqlite3

# 1. Creamos la CONEXIÓN (Si el archivo no existe, Python lo crea automáticamente)
conexion = sqlite3.connect("catalogo_bisuteria.db")

# 2. Creamos el CURSOR (Nuestro brazo robótico)
cursor = conexion.cursor()

print("🏗️ Construyendo la base de datos...")

# 3. Le damos la orden al cursor en lenguaje SQL puro
# Le decimos: "Crea una tabla llamada 'productos' con estas 3 columnas"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        nombre TEXT,
        precio REAL,
        comentario TEXT
    )
''')

# 4. Guardamos los cambios estructurales
conexion.commit()

# 5. Cerramos la puerta por seguridad
conexion.close()

print("✅ Base de datos 'catalogo_bisuteria.db' creada exitosamente.")