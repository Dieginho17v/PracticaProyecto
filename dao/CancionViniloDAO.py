from Datos import get_conn

class CancionViniloDAO:

    @staticmethod
    def insertarCancionVinilo(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO cancion_vinilo (id_vinilo, id_cancion, duracion_segundos_vinilo)
                VALUES (?, ?, ?)
            """, (
                data.get("id_vinilo"),
                data.get("id_cancion"),
                data.get("duracion_segundos_vinilo")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarCancionesVinilo():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM cancion_vinilo")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarCancionVinilo(id_cancion_vinilo):
        with get_conn() as conn:
            cursor = conn.execute(
                "SELECT * FROM cancion_vinilo WHERE id_cancion_vinilo=?",
                (id_cancion_vinilo,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarCancionVinilo(id_cancion_vinilo, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE cancion_vinilo
                SET id_vinilo=?, id_cancion=?, duracion_segundos_vinilo=?
                WHERE id_cancion_vinilo=?
            """, (
                data.get("id_vinilo"),
                data.get("id_cancion"),
                data.get("duracion_segundos_vinilo"),
                id_cancion_vinilo
            ))
            conn.commit()

    @staticmethod
    def actualizarCancionViniloParcial(id_cancion_vinilo, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_cancion_vinilo)
        with get_conn() as conn:
            conn.execute(f"UPDATE cancion_vinilo SET {', '.join(campos)} WHERE id_cancion_vinilo=?", valores)
            conn.commit()

    @staticmethod
    def eliminarCancionVinilo(id_cancion_vinilo):
        with get_conn() as conn:
            conn.execute("DELETE FROM cancion_vinilo WHERE id_cancion_vinilo=?", (id_cancion_vinilo,))
            conn.commit()
