from Datos import get_conn

class PedidoDAO:

    @staticmethod
    def insertarPedido(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pedido (estado, metodo_pago, id_comprador)
                VALUES (?, ?, ?)
            """, (
                data.get("estado"),
                data.get("metodo_pago"),
                data.get("id_comprador")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarPedidos():
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM pedido")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarPedido(id_pedido):
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM pedido WHERE id_pedido=?", (id_pedido,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarPedido(id_pedido, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE pedido
                SET estado=?, metodo_pago=?, id_comprador=?
                WHERE id_pedido=?
            """, (
                data.get("estado"),
                data.get("metodo_pago"),
                data.get("id_comprador"),
                id_pedido
            ))
            conn.commit()

    @staticmethod
    def actualizarPedidoParcial(id_pedido, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_pedido)
        with get_conn() as conn:
            conn.execute(f"UPDATE pedido SET {', '.join(campos)} WHERE id_pedido=?", valores)
            conn.commit()

    @staticmethod
    def actualizarEstado(id_pedido, estado):
        with get_conn() as conn:
            conn.execute("UPDATE pedido SET estado=? WHERE id_pedido=?", (estado, id_pedido))
            conn.commit()

    @staticmethod
    def eliminarPedido(id_pedido):
        with get_conn() as conn:
            conn.execute("DELETE FROM pedido WHERE id_pedido=?", (id_pedido,))
            conn.commit()
