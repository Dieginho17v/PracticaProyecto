from dao.PedidoDAO import PedidoDAO
from dao.DetallePedidoDAO import DetallePedidoDAO
from dao.ValoracionDAO import ValoracionDAO

class PedidoManager:
    def crearPedido(self, pedido, detalles):
        id_pedido = PedidoDAO.insertarPedido(pedido)
        for d in detalles:
            d["id_pedido"] = id_pedido
            DetallePedidoDAO.insertarDetallePedido(d)
        return id_pedido

    def cambiarEstado(self, id_pedido, estado):
        PedidoDAO.actualizarEstado(id_pedido, estado)

    def agregarValoracion(self, data):
        return ValoracionDAO.insertarValoracion(data)

    def generarReporte(self):
        pedidos = PedidoDAO.consultarPedidos()
        valoraciones = ValoracionDAO.consultarValoraciones()
        return {"pedidos": pedidos, "valoraciones": valoraciones}
