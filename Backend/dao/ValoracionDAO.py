# dao/ValoracionDAO.py
from Datos import obtener_conexion

class ValoracionDAO:

    @staticmethod
    def insertarValoracion(data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Valoracion(puntuacion, comentario, id_producto, id_usuario)
            VALUES (?, ?, ?, ?)
        """, (data["puntuacion"], data.get("comentario"), data["id_producto"], data["id_usuario"]))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarValoraciones():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Valoracion")
        return cursor.fetchall()

    @staticmethod
    def consultarValoracion(id_valoracion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Valoracion WHERE id_valoracion=?", (id_valoracion,))
        return cursor.fetchone()

    @staticmethod
    def actualizarValoracion(id_valoracion, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Valoracion
            SET puntuacion=?, comentario=?, id_producto=?, id_usuario=?
            WHERE id_valoracion=?
        """, (
            data["puntuacion"], data.get("comentario"),
            data["id_producto"], data["id_usuario"],
            id_valoracion
        ))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarValoracionParcial(id_valoracion, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        valores.append(id_valoracion)

        cursor.execute(
            f"UPDATE Valoracion SET {', '.join(campos)} WHERE id_valoracion=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarValoracion(id_valoracion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Valoracion WHERE id_valoracion=?", (id_valoracion,))
        conn.commit()
        return cursor.rowcount
