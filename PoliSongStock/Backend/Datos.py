# Datos.py
import sqlite3

DB_NAME = "PoliSong.db"

def obtener_conexion():
    return sqlite3.connect(DB_NAME)


def crear_tablas():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DiscoMP3 (
        id_disco INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        genero TEXT,
        imagen_portada BLOB
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cancion (
        id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        duracion INTEGER NOT NULL,
        tamaño_mb REAL,
        calidad_kbps INTEGER,
        audio_blob BLOB,
        id_disco INTEGER,
        FOREIGN KEY(id_disco) REFERENCES DiscoMP3(id_disco)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vinilo (
        id_vinilo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rpm INTEGER NOT NULL,
        imagen_caratula BLOB
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recopilacion (
        id_recopilacion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        imagen_caratula BLOB
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CancionRecopilacion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cancion INTEGER,
        id_recopilacion INTEGER,
        FOREIGN KEY(id_cancion) REFERENCES Cancion(id_cancion),
        FOREIGN KEY(id_recopilacion) REFERENCES Recopilacion(id_recopilacion)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CancionVinilo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cancion INTEGER,
        id_vinilo INTEGER,
        FOREIGN KEY(id_cancion) REFERENCES Cancion(id_cancion),
        FOREIGN KEY(id_vinilo) REFERENCES Vinilo(id_vinilo)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Producto (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        tipo TEXT NOT NULL, 
        id_ref INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pedido (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        total REAL NOT NULL,
        id_usuario INTEGER,
        FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Valoracion (
        id_valoracion INTEGER PRIMARY KEY AUTOINCREMENT,
        puntuacion INTEGER NOT NULL,
        comentario TEXT,
        id_producto INTEGER,
        id_usuario INTEGER,
        FOREIGN KEY(id_producto) REFERENCES Producto(id_producto),
        FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario)
    )
    """)

    conn.commit()
    conn.close()


crear_tablas()
