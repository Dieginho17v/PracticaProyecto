from Datos import get_conn

class CancionRecopilacionDAO:

    @staticmethod
    def insertarCancionRecopilacion(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO cancion_recopilacion (id_recopilacion, id_cancion)
                VALUES (?, ?)
            """, (
                data.get("id_recopilacion"),
                data.get("id_cancion")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarCancionesRecopilacion():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM cancion_recopilacion")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarCancionRecopilacion(id_cancion_recopilacion):
        with get_conn() as conn:
            cursor = conn.execute(
                "SELECT * FROM cancion_recopilacion WHERE id_cancion_recopilacion=?",
                (id_cancion_recopilacion,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarCancionRecopilacion(id_cancion_recopilacion, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE cancion_recopilacion
                SET id_recopilacion=?, id_cancion=?
                WHERE id_cancion_recopilacion=?
            """, (
                data.get("id_recopilacion"),
                data.get("id_cancion"),
                id_cancion_recopilacion
            ))
            conn.commit()

    @staticmethod
    def actualizarCancionRecopilacionParcial(id_cancion_recopilacion, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_cancion_recopilacion)
        with get_conn() as conn:
            conn.execute(f"UPDATE cancion_recopilacion SET {', '.join(campos)} WHERE id_cancion_recopilacion=?", valores)
            conn.commit()

    @staticmethod
    def eliminarCancionRecopilacion(id_cancion_recopilacion):
        with get_conn() as conn:
            conn.execute("DELETE FROM cancion_recopilacion WHERE id_cancion_recopilacion=?", (id_cancion_recopilacion,))
            conn.commit()
