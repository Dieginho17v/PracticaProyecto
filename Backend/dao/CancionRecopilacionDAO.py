# dao/CancionRecopilacionDAO.py
from Datos import obtener_conexion

class CancionRecopilacionDAO:

    @staticmethod
    def agregarCancionARecopilacion(id_cancion, id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO CancionRecopilacion(id_cancion, id_recopilacion)
            VALUES (?, ?)
        """, (id_cancion, id_recopilacion))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def obtenerCancionesDeRecopilacion(id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_cancion FROM CancionRecopilacion WHERE id_recopilacion=?
        """, (id_recopilacion,))
        return cursor.fetchall()

    @staticmethod
    def eliminarCancionDeRecopilacion(id_cancion, id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM CancionRecopilacion
            WHERE id_cancion=? AND id_recopilacion=?
        """, (id_cancion, id_recopilacion))
        conn.commit()
        return cursor.rowcount
