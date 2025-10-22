from dao.UsuarioDAO import UsuarioDAO

class UsuarioManager:
    def registrarUsuario(self, data):
        if not all(k in data for k in ("nombre", "correo", "contrasena", "tipo_usuario")):
            raise ValueError("Faltan datos para registrar usuario")
        if UsuarioDAO.consultarPorCorreo(data["correo"]):
            raise ValueError("El correo ya está registrado")
        return UsuarioDAO.insertarUsuario(data)

    def validarCredenciales(self, correo, contrasena):
        usuario = UsuarioDAO.consultarPorCorreo(correo)
        if usuario and usuario["contrasena"] == contrasena:
            return usuario
        return None

    def actualizarPerfil(self, id_usuario, data):
        UsuarioDAO.actualizarUsuario(id_usuario, data)
