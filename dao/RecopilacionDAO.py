from Datos import get_conn

class RecopilacionDAO:
    @staticmethod
    def insertarRecopilacion(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO recopilacion(nombre, publica, id_usuario) VALUES (?,?,?)",
                (data["nombre"], int(data.get("publica", 0)), data["id_usuario"])
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarRecopilaciones():
        with get_conn() as conn:
            filas = conn.execute("SELECT * FROM recopilacion").fetchall()
            return [dict(f) for f in filas]

    @staticmethod
    def obtenerPorId(id_recopilacion):
        with get_conn() as conn:
            fila = conn.execute("SELECT * FROM recopilacion WHERE id_recopilacion=?", (id_recopilacion,)).fetchone()
            return dict(fila) if fila else None
