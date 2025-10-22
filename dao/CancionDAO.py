# dao/CancionDAO.py
from Datos import get_conn

class CancionDAO:

    @staticmethod
    def insertarCancion(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO cancion(nombre, precio, duracion_segundos, tamano_mb, calidad_kbps, id_disco) VALUES (?,?,?,?,?,?)",
                (data["nombre"], data.get("precio"), data.get("duracion_segundos"), data.get("tamano_mb"),
                 data.get("calidad_kbps"), data.get("id_disco"))
            )
            conn.commit()
            return cur.lastrowid


    @staticmethod
    def consultarCanciones():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM cancion")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarCancionPorId(id_cancion):
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM cancion WHERE id_cancion = ?", (id_cancion,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarCancion(id_cancion, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE cancion
                SET nombre=?, precio=?, duracion_segundos=?, tamano_mb=?, calidad_kbps=?, id_disco=?
                WHERE id_cancion=?
            """, (
                data.get("nombre"),
                data.get("precio"),
                data.get("duracion_segundos"),
                data.get("tamano_mb"),
                data.get("calidad_kbps"),
                data.get("id_disco"),
                id_cancion
            ))
            conn.commit()
            return True

    @staticmethod
    def actualizarCancionParcial(id_cancion, data):
        campos = []
        valores = []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        if not campos:
            return False
        valores.append(id_cancion)
        with get_conn() as conn:
            conn.execute(f"UPDATE cancion SET {', '.join(campos)} WHERE id_cancion=?", valores)
            conn.commit()
            return True

    @staticmethod
    def eliminarCancion(id_cancion):
        with get_conn() as conn:
            conn.execute("DELETE FROM cancion WHERE id_cancion=?", (id_cancion,))
            conn.commit()
            return True
