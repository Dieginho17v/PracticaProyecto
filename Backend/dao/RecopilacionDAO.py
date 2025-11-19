# dao/RecopilacionDAO.py
from Datos import obtener_conexion

class RecopilacionDAO:

    @staticmethod
    def insertarRecopilacion(data, imagen=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Recopilacion(nombre, descripcion, imagen_caratula)
            VALUES (?, ?, ?)
        """, (data["nombre"], data.get("descripcion"), imagen))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarRecopilaciones():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_recopilacion, nombre FROM Recopilacion")
        return cursor.fetchall()

    @staticmethod
    def consultarRecopilacion(id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Recopilacion WHERE id_recopilacion=?", (id_recopilacion,))
        return cursor.fetchone()

    @staticmethod
    def obtenerCaratula(id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT imagen_caratula FROM Recopilacion WHERE id_recopilacion=?", (id_recopilacion,))
        r = cursor.fetchone()
        return r[0] if r else None

    @staticmethod
    def actualizarRecopilacion(id_recopilacion, data, imagen=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Recopilacion
            SET nombre=?, descripcion=?, imagen_caratula=?
            WHERE id_recopilacion=?
        """, (
            data["nombre"], data.get("descripcion"),
            imagen, id_recopilacion
        ))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarRecopilacionParcial(id_recopilacion, data, imagen=None):
        conn = obtener_conexion()
        cursor = conn.cursor()

        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        if imagen is not None:
            campos.append("imagen_caratula=?")
            valores.append(imagen)

        valores.append(id_recopilacion)

        cursor.execute(
            f"UPDATE Recopilacion SET {', '.join(campos)} WHERE id_recopilacion=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarRecopilacion(id_recopilacion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Recopilacion WHERE id_recopilacion=?", (id_recopilacion,))
        conn.commit()
        return cursor.rowcount
