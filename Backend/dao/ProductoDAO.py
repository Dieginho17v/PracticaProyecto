# dao/ProductoDAO.py
from Datos import obtener_conexion

class ProductoDAO:

    @staticmethod
    def insertarProducto(data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Producto(nombre, precio, tipo, id_ref)
            VALUES (?, ?, ?, ?)
        """, (data["nombre"], data["precio"], data["tipo"], data["id_ref"]))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarProductos():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto")
        return cursor.fetchall()

    @staticmethod
    def consultarProducto(id_producto):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto WHERE id_producto=?", (id_producto,))
        return cursor.fetchone()

    @staticmethod
    def actualizarProducto(id_producto, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Producto
            SET nombre=?, precio=?, tipo=?, id_ref=?
            WHERE id_producto=?
        """, (
            data["nombre"], data["precio"],
            data["tipo"], data["id_ref"],
            id_producto
        ))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarProductoParcial(id_producto, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []
        
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
            
        valores.append(id_producto)
        
        cursor.execute(
            f"UPDATE Producto SET {', '.join(campos)} WHERE id_producto=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarProducto(id_producto):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Producto WHERE id_producto=?", (id_producto,))
        conn.commit()
        return cursor.rowcount
