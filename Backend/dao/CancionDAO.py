# dao/CancionDAO.py
from Datos import obtener_conexion

class CancionDAO:

    @staticmethod
    def insertarCancion(data, audio=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Cancion(nombre, duracion, tamaño_mb, calidad_kbps, audio_blob, id_disco)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["nombre"], data["duracion"],
            data.get("tamaño_mb"), data.get("calidad_kbps"),
            audio, data.get("id_disco")
        ))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarCanciones():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_cancion, nombre, duracion, id_disco FROM Cancion")
        return cursor.fetchall()

    @staticmethod
    def consultarCancion(id_cancion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cancion WHERE id_cancion=?", (id_cancion,))
        return cursor.fetchone()

    @staticmethod
    def obtenerAudio(id_cancion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT audio_blob FROM Cancion WHERE id_cancion=?", (id_cancion,))
        f = cursor.fetchone()
        return f[0] if f else None

    @staticmethod
    def actualizarCancion(id_cancion, data, audio=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Cancion
            SET nombre=?, duracion=?, tamaño_mb=?, calidad_kbps=?, audio_blob=?, id_disco=?
            WHERE id_cancion=?
        """, (
            data["nombre"], data["duracion"],
            data.get("tamaño_mb"), data.get("calidad_kbps"),
            audio, data.get("id_disco"),
            id_cancion
        ))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarCancionParcial(id_cancion, data, audio=None):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        if audio is not None:
            campos.append("audio_blob=?")
            valores.append(audio)

        valores.append(id_cancion)
        cursor.execute(
            f"UPDATE Cancion SET {', '.join(campos)} WHERE id_cancion=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarCancion(id_cancion):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cancion WHERE id_cancion=?", (id_cancion,))
        conn.commit()
        return cursor.rowcount
