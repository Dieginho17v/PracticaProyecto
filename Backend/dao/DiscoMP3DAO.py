# dao/DiscoMP3DAO.py
from Datos import obtener_conexion

class DiscoMP3DAO:

    @staticmethod
    def insertarDisco(data, portada=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO DiscoMP3(nombre, genero, imagen_portada)
            VALUES (?, ?, ?)
        """, (data["nombre"], data.get("genero"), portada))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarDiscos():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_disco, nombre, genero FROM DiscoMP3")
        return cursor.fetchall()

    @staticmethod
    def consultarDisco(id_disco):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DiscoMP3 WHERE id_disco=?", (id_disco,))
        return cursor.fetchone()

    @staticmethod
    def obtenerPortada(id_disco):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT imagen_portada FROM DiscoMP3 WHERE id_disco=?", (id_disco,))
        f = cursor.fetchone()
        return f[0] if f else None

    @staticmethod
    def actualizarDisco(id_disco, data, portada=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE DiscoMP3
            SET nombre=?, genero=?, imagen_portada=?
            WHERE id_disco=?
        """, (data["nombre"], data.get("genero"), portada, id_disco))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarDiscoParcial(id_disco, data, portada=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        if portada is not None:
            campos.append("imagen_portada=?")
            valores.append(portada)

        valores.append(id_disco)
        cursor.execute(
            f"UPDATE DiscoMP3 SET {', '.join(campos)} WHERE id_disco=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarDisco(id_disco):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM DiscoMP3 WHERE id_disco=?", (id_disco,))
        conn.commit()
        return cursor.rowcount
