from Datos import get_conn

class RecopilacionDAO:

    @staticmethod
    def insertarRecopilacion(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO recopilacion (nombre, publica, id_usuario)
                VALUES (?, ?, ?)
            """, (
                data.get("nombre"),
                int(data.get("publica", 0)),
                data.get("id_usuario")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarRecopilaciones():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM recopilacion")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarRecopilacion(id_recopilacion):
        with get_conn() as conn:
            cursor = conn.execute(
                "SELECT * FROM recopilacion WHERE id_recopilacion=?",
                (id_recopilacion,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarRecopilacion(id_recopilacion, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE recopilacion
                SET nombre=?, publica=?, id_usuario=?
                WHERE id_recopilacion=?
            """, (
                data.get("nombre"),
                int(data.get("publica", 0)),
                data.get("id_usuario"),
                id_recopilacion
            ))
            conn.commit()

    @staticmethod
    def actualizarRecopilacionParcial(id_recopilacion, data):
        campos, valores = [], []
        for k, v in data.items():
            # Si el campo es 'publica', asegúrate de convertirlo a int (0 o 1)
            if k == "publica":
                v = int(v)
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_recopilacion)
        with get_conn() as conn:
            conn.execute(f"UPDATE recopilacion SET {', '.join(campos)} WHERE id_recopilacion=?", valores)
            conn.commit()

    @staticmethod
    def eliminarRecopilacion(id_recopilacion):
        with get_conn() as conn:
            conn.execute("DELETE FROM recopilacion WHERE id_recopilacion=?", (id_recopilacion,))
            conn.commit()
