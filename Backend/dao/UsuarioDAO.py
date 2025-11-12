from Datos import get_conn

class UsuarioDAO:
    @staticmethod
    def insertarUsuario(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO usuario(nombre, correo, contrasena, tipo_usuario) VALUES (?,?,?,?)",
                (data["nombre"], data["correo"], data["contrasena"], data["tipo_usuario"])
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarPorCorreo(correo):
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM usuario WHERE correo = ?", (correo,)).fetchone()
            return dict(row) if row else None

    @staticmethod
    def consultarUsuario(id_usuario):
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM usuario WHERE id_usuario = ?", (id_usuario,)).fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarUsuario(id_usuario, data):
        with get_conn() as conn:
            conn.execute(
                "UPDATE usuario SET nombre=?, correo=?, contrasena=?, tipo_usuario=? WHERE id_usuario = ?",
                (data["nombre"], data["correo"], data["contrasena"], data["tipo_usuario"], id_usuario)
            )
            conn.commit()

    @staticmethod
    def eliminarUsuario(id_usuario):
        with get_conn() as conn:
            conn.execute("DELETE FROM usuario WHERE id_usuario = ?", (id_usuario,))
            conn.commit()