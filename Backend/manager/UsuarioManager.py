# manager/UsuarioManager.py

from dao.UsuarioDAO import UsuarioDAO

class UsuarioManager:

    @staticmethod
    def crearUsuario(data):
        return UsuarioDAO.insertarUsuario(data)

    @staticmethod
    def obtenerUsuarios():
        return UsuarioDAO.consultarUsuarios()

    @staticmethod
    def obtenerUsuario(id_usuario):
        return UsuarioDAO.consultarUsuario(id_usuario)

    @staticmethod
    def actualizarUsuario(id_usuario, data):
        return UsuarioDAO.actualizarUsuario(id_usuario, data)

    @staticmethod
    def actualizarUsuarioParcial(id_usuario, data):
        return UsuarioDAO.actualizarUsuarioParcial(id_usuario, data)

    @staticmethod
    def eliminarUsuario(id_usuario):
        return UsuarioDAO.eliminarUsuario(id_usuario)
