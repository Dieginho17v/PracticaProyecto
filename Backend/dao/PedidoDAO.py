# dao/PedidoDAO.py
from Datos import obtener_conexion

class PedidoDAO:

    @staticmethod
    def insertarPedido(data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Pedido(fecha, total, id_usuario)
            VALUES (?, ?, ?)
        """, (data["fecha"], data["total"], data["id_usuario"]))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarPedidos():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido")
        return cursor.fetchall()

    @staticmethod
    def consultarPedido(id_pedido):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido WHERE id_pedido=?", (id_pedido,))
        return cursor.fetchone()

    @staticmethod
    def actualizarPedido(id_pedido, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Pedido SET fecha=?, total=?, id_usuario=?
            WHERE id_pedido=?
        """, (data["fecha"], data["total"], data["id_usuario"], id_pedido))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarPedidoParcial(id_pedido, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        valores.append(id_pedido)

        cursor.execute(
            f"UPDATE Pedido SET {', '.join(campos)} WHERE id_pedido=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarPedido(id_pedido):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pedido WHERE id_pedido=?", (id_pedido,))
        conn.commit()
        return cursor.rowcount
