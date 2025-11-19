# dao/ViniloDAO.py
from Datos import obtener_conexion

class ViniloDAO:

    @staticmethod
    def insertarVinilo(data, caratula=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Vinilo(nombre, rpm, imagen_caratula)
            VALUES (?, ?, ?)
        """, (data["nombre"], data["rpm"], caratula))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarVinilos():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_vinilo, nombre, rpm FROM Vinilo")
        return cursor.fetchall()

    @staticmethod
    def consultarVinilo(id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vinilo WHERE id_vinilo=?", (id_vinilo,))
        return cursor.fetchone()

    @staticmethod
    def obtenerCaratula(id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT imagen_caratula FROM Vinilo WHERE id_vinilo=?", (id_vinilo,))
        result = cursor.fetchone()
        return result[0] if result else None

    @staticmethod
    def actualizarVinilo(id_vinilo, data, caratula=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Vinilo SET nombre=?, rpm=?, imagen_caratula=?
            WHERE id_vinilo=?
        """, (data["nombre"], data["rpm"], caratula, id_vinilo))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarViniloParcial(id_vinilo, data, caratula=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        if caratula is not None:
            campos.append("imagen_caratula=?")
            valores.append(caratula)

        valores.append(id_vinilo)

        cursor.execute(
            f"UPDATE Vinilo SET {', '.join(campos)} WHERE id_vinilo=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarVinilo(id_vinilo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Vinilo WHERE id_vinilo=?", (id_vinilo,))
        conn.commit()
        return cursor.rowcount
