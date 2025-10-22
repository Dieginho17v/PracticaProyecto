from Datos import get_conn

class ValoracionDAO:
    @staticmethod
    def insertarValoracion(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO valoracion(satisfaccion, comentario, pedido_id_pedido) VALUES (?,?,?)",
                (data["satisfaccion"], data.get("comentario"), data["pedido_id_pedido"])
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarValoraciones():
        with get_conn() as conn:
            filas = conn.execute("SELECT * FROM valoracion").fetchall()
            return [dict(f) for f in filas]
