# manager/RecopilacionManager.py

from dao.RecopilacionDAO import RecopilacionDAO
from dao.CancionRecopilacionDAO import CancionRecopilacionDAO

class RecopilacionManager:

    # -------------------------
    #     RECOPILACIONES
    # -------------------------
    @staticmethod
    def crearRecopilacion(data, imagen=None):
        return RecopilacionDAO.insertarRecopilacion(data, imagen)

    @staticmethod
    def obtenerRecopilaciones():
        return RecopilacionDAO.consultarRecopilaciones()

    @staticmethod
    def obtenerRecopilacion(id_recopilacion):
        return RecopilacionDAO.consultarRecopilacion(id_recopilacion)

    @staticmethod
    def obtenerCaratula(id_recopilacion):
        return RecopilacionDAO.obtenerCaratula(id_recopilacion)

    @staticmethod
    def actualizarRecopilacion(id_recopilacion, data, imagen=None):
        return RecopilacionDAO.actualizarRecopilacion(id_recopilacion, data, imagen)

    @staticmethod
    def actualizarRecopilacionParcial(id_recopilacion, data, imagen=None):
        return RecopilacionDAO.actualizarRecopilacionParcial(id_recopilacion, data, imagen)

    @staticmethod
    def eliminarRecopilacion(id_recopilacion):
        return RecopilacionDAO.eliminarRecopilacion(id_recopilacion)

    # -------------------------
    #      CANCIONES–RECO
    # -------------------------
    @staticmethod
    def agregarCancionARecopilacion(id_cancion, id_recopilacion):
        return CancionRecopilacionDAO.agregarCancionARecopilacion(id_cancion, id_recopilacion)

    @staticmethod
    def obtenerCancionesDeRecopilacion(id_recopilacion):
        return CancionRecopilacionDAO.obtenerCancionesDeRecopilacion(id_recopilacion)

    @staticmethod
    def eliminarCancionDeRecopilacion(id_cancion, id_recopilacion):
        return CancionRecopilacionDAO.eliminarCancionDeRecopilacion(id_cancion, id_recopilacion)
