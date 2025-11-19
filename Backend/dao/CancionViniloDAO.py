# dao/CancionViniloDAO.py
from Datos import obtener_conexion

class CancionViniloDAO:

    @staticmethod
    def agregarCancionAVinilo(id_cancion, id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO CancionVinilo(id_cancion, id_vinilo)
            VALUES (?, ?)
        """, (id_cancion, id_vinilo))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def obtenerCancionesDeVinilo(id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_cancion FROM CancionVinilo WHERE id_vinilo=?
        """, (id_vinilo,))
        return cursor.fetchall()

    @staticmethod
    def eliminarCancionDeVinilo(id_cancion, id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM CancionVinilo
            WHERE id_cancion=? AND id_vinilo=?
        """, (id_cancion, id_vinilo))
        conn.commit()
        return cursor.rowcount
