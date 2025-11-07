from Datos import get_conn

class ValoracionDAO:

    @staticmethod
    def insertarValoracion(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO valoracion (satisfaccion, comentario, pedido_id_pedido)
                VALUES (?, ?, ?)
            """, (
                data.get("satisfaccion"),
                data.get("comentario"),
                data.get("pedido_id_pedido")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarValoraciones():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM valoracion")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarValoracion(id_valoracion):
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM valoracion WHERE id_valoracion=?", (id_valoracion,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarValoracion(id_valoracion, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE valoracion
                SET satisfaccion=?, comentario=?, pedido_id_pedido=?
                WHERE id_valoracion=?
            """, (
                data.get("satisfaccion"),
                data.get("comentario"),
                data.get("pedido_id_pedido"),
                id_valoracion
            ))
            conn.commit()

    @staticmethod
    def actualizarValoracionParcial(id_valoracion, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_valoracion)
        with get_conn() as conn:
            conn.execute(f"UPDATE valoracion SET {', '.join(campos)} WHERE id_valoracion=?", valores)
            conn.commit()

    @staticmethod
    def eliminarValoracion(id_valoracion):
        with get_conn() as conn:
            conn.execute("DELETE FROM valoracion WHERE id_valoracion=?", (id_valoracion,))
            conn.commit()
