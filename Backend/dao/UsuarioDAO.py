# dao/UsuarioDAO.py
from Datos import obtener_conexion

class UsuarioDAO:

    @staticmethod
    def insertarUsuario(data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Usuario(nombre, email, contrasena)
            VALUES (?, ?, ?)
        """, (data["nombre"], data["email"], data["contrasena"]))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def consultarUsuarios():
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuario")
        return cursor.fetchall()

    @staticmethod
    def consultarUsuario(id_usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuario WHERE id_usuario = ?", (id_usuario,))
        return cursor.fetchone()

    @staticmethod
    def actualizarUsuario(id_usuario, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Usuario SET nombre=?, email=?, contrasena=?
            WHERE id_usuario=?
        """, (data["nombre"], data["email"], data["contrasena"], id_usuario))
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def actualizarUsuarioParcial(id_usuario, data):
        conn = obtener_conexion()
        cursor = conn.cursor()
        campos = []
        valores = []

        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)

        valores.append(id_usuario)
        cursor.execute(
            f"UPDATE Usuario SET {', '.join(campos)} WHERE id_usuario=?",
            valores
        )
        conn.commit()
        return cursor.rowcount

    @staticmethod
    def eliminarUsuario(id_usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuario WHERE id_usuario=?", (id_usuario,))
        conn.commit()
        return cursor.rowcount
