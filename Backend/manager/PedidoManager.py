# manager/PedidoManager.py

from dao.PedidoDAO import PedidoDAO
from dao.ProductoDAO import ProductoDAO
from dao.ValoracionDAO import ValoracionDAO

class PedidoManager:

    # -------------------------
    #          PEDIDOS
    # -------------------------
    @staticmethod
    def crearPedido(data):
        return PedidoDAO.insertarPedido(data)

    @staticmethod
    def obtenerPedidos():
        return PedidoDAO.consultarPedidos()

    @staticmethod
    def obtenerPedido(id_pedido):
        return PedidoDAO.consultarPedido(id_pedido)

    @staticmethod
    def actualizarPedido(id_pedido, data):
        return PedidoDAO.actualizarPedido(id_pedido, data)

    @staticmethod
    def actualizarPedidoParcial(id_pedido, data):
        return PedidoDAO.actualizarPedidoParcial(id_pedido, data)

    @staticmethod
    def eliminarPedido(id_pedido):
        return PedidoDAO.eliminarPedido(id_pedido)

    # -------------------------
    #         PRODUCTOS
    # -------------------------
    @staticmethod
    def crearProducto(data):
        return ProductoDAO.insertarProducto(data)

    @staticmethod
    def obtenerProductos():
        return ProductoDAO.consultarProductos()

    @staticmethod
    def obtenerProducto(id_producto):
        return ProductoDAO.consultarProducto(id_producto)

    @staticmethod
    def actualizarProducto(id_producto, data):
        return ProductoDAO.actualizarProducto(id_producto, data)

    @staticmethod
    def actualizarProductoParcial(id_producto, data):
        return ProductoDAO.actualizarProductoParcial(id_producto, data)

    @staticmethod
    def eliminarProducto(id_producto):
        return ProductoDAO.eliminarProducto(id_producto)

    # -------------------------
    #        VALORACIONES
    # -------------------------
    @staticmethod
    def crearValoracion(data):
        return ValoracionDAO.insertarValoracion(data)

    @staticmethod
    def obtenerValoraciones():
        return ValoracionDAO.consultarValoraciones()

    @staticmethod
    def obtenerValoracion(id_valoracion):
        return ValoracionDAO.consultarValoracion(id_valoracion)

    @staticmethod
    def actualizarValoracion(id_valoracion, data):
        return ValoracionDAO.actualizarValoracion(id_valoracion, data)

    @staticmethod
    def actualizarValoracionParcial(id_valoracion, data):
        return ValoracionDAO.actualizarValoracionParcial(id_valoracion, data)

    @staticmethod
    def eliminarValoracion(id_valoracion):
        return ValoracionDAO.eliminarValoracion(id_valoracion)
