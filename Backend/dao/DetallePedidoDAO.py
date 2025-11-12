from Datos import get_conn

class DetallePedidoDAO:
    @staticmethod
    def insertarDetallePedido(data):
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO detalle_pedido(id_pedido,tipo_producto,id_producto,cantidad,precio_unitario) VALUES (?,?,?,?,?)",
                (data["id_pedido"], data["tipo_producto"], data["id_producto"], data["cantidad"], data["precio_unitario"])
            )
            conn.commit()
