import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("PoliSong.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def ensure_schema():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL,
                tipo_usuario TEXT NOT NULL,
                fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cancion (
                id_cancion INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio DECIMAL(10,2),
                duracion_segundos INT,
                tamano_mb DECIMAL(6,2),
                calidad_kbps INT,
                id_disco INT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS disco (
                id_disco INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                genero TEXT,
                imagen_portada TEXT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS vinilo (
                id_vinilo INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                artista TEXT,
                ano_salida INT,
                precio DECIMAL(10,2),
                inventario INT,
                id_proveedor INT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS recopilacion (
                id_recopilacion INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                publica INTEGER,
                id_usuario INT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cancion_recopilacion (
                id_recopilacion INT,
                id_cancion INT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cancion_vinilo (
                id_vinilo INT,
                id_cancion INT,
                duracion_segundos_vinilo INT
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS pedido (
                id_pedido INTEGER PRIMARY KEY,
                fecha_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado TEXT,
                metodo_pago TEXT,
                id_comprador INT,
                observacion_rechazo TEXT,
                fecha_envio_estimada DATE,
                fecha_recepcion DATE
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS detalle_pedido (
                id_pedido INT,
                tipo_producto TEXT,
                id_producto INT,
                cantidad INT,
                precio_unitario DECIMAL(10,2)
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS valoracion (
                id_valoracion INTEGER PRIMARY KEY,
                satisfaccion INTEGER,
                comentario TEXT,
                pedido_id_pedido INT
            );
        """)
        conn.commit()
