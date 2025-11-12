import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("PoliSong.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def ensure_schema():
    with get_conn() as conn:
        # --- Tabla Usuario ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Usuario (
                id_usuario INTEGER PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                correo VARCHAR(100) UNIQUE NOT NULL,
                contrasena VARCHAR(255) NOT NULL,
                tipo_usuario VARCHAR(20) NOT NULL,
                fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # --- Tabla Pedido ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Pedido (
                id_pedido INTEGER PRIMARY KEY,
                fecha_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado VARCHAR(20),
                metodo_pago VARCHAR(20),
                id_comprador INT,
                observacion_rechazo VARCHAR(255),
                fecha_envio_estimada DATE,
                fecha_recepcion DATE,
                FOREIGN KEY (id_comprador) REFERENCES Usuario(id_usuario)
            );
        """)

        # --- Tabla Valoracion ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Valoracion (
                id_pedido INT PRIMARY KEY,
                satisfaccion BOOLEAN,
                comentario VARCHAR(255),
                FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
            );
        """)

        # --- Tabla Producto ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Producto (
                id_producto INTEGER PRIMARY KEY,
                tipo_producto VARCHAR(20),
                id_pedido INT,
                cantidad INT,
                precio_unitario DECIMAL(10,2),
                FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
            );
        """)

        # --- Tabla Vinilo ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Vinilo (
                id_vinilo INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                artista VARCHAR(100),
                anio_salida YEAR,
                precio DECIMAL(10,2),
                inventario INT,
                id_proveedor INT
            );
        """)

        # --- Tabla Disco_MP3 ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Disco_MP3 (
                id_disco INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                genero VARCHAR(50),
                imagen_portada BLOB
            );
        """)

        # --- Tabla Cancion ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Cancion (
                id_cancion INTEGER PRIMARY KEY,
                id_disco INT,
                nombre VARCHAR(100),
                precio DECIMAL(11,2),
                duracion_segundos INT,
                tamano_mb DECIMAL(6,2),
                calidad_kbps INT,
                archivo_audio BLOB,
                FOREIGN KEY (id_disco) REFERENCES Disco_MP3(id_disco)
            );
        """)

        # --- Tabla Cancion_Vinilo ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Cancion_Vinilo (
                id_cancion INT,
                id_vinilo INT,
                duracion_segundos_vinilo INT,
                PRIMARY KEY (id_cancion, id_vinilo),
                FOREIGN KEY (id_cancion) REFERENCES Cancion(id_cancion),
                FOREIGN KEY (id_vinilo) REFERENCES Vinilo(id_vinilo)
            );
        """)

        # --- Tabla Recopilacion ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Recopilacion (
                id_recopilacion INTEGER PRIMARY KEY,
                id_usuario INT,
                nombre VARCHAR(100),
                publica BOOLEAN,
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
            );
        """)

        # --- Tabla Cancion_Recopilacion ---
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Cancion_Recopilacion (
                id_cancion INT,
                id_recopilacion INT,
                PRIMARY KEY (id_cancion, id_recopilacion),
                FOREIGN KEY (id_cancion) REFERENCES Cancion(id_cancion),
                FOREIGN KEY (id_recopilacion) REFERENCES Recopilacion(id_recopilacion)
            );
        """)

        conn.commit()
