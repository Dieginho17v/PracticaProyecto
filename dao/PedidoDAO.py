from Datos import get_conn

class PedidoDAO:
    @staticmethod
    def insertarPedido(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO pedido(estado, metodo_pago, id_comprador) VALUES (?,?,?)",
                (data["estado"], data["metodo_pago"], data["id_comprador"])
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarPedidos():
        with get_conn() as conn:
            filas = conn.execute("SELECT * FROM pedido").fetchall()
            return [dict(f) for f in filas]

    @staticmethod
    def actualizarEstado(id_pedido, estado):
        with get_conn() as conn:
            conn.execute("UPDATE pedido SET estado=? WHERE id_pedido=?", (estado, id_pedido))
            conn.commit()
