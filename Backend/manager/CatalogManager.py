# manager/CatalogManager.py

from dao.CancionDAO import CancionDAO
from dao.DiscoMP3DAO import DiscoMP3DAO
from dao.ViniloDAO import ViniloDAO

class CatalogManager:

    # -------------------------
    #        CANCIONES
    # -------------------------
    @staticmethod
    def crearCancion(data, audio=None):
        return CancionDAO.insertarCancion(data, audio)

    @staticmethod
    def obtenerCanciones():
        return CancionDAO.consultarCanciones()

    @staticmethod
    def obtenerCancion(id_cancion):
        return CancionDAO.consultarCancion(id_cancion)

    @staticmethod
    def obtenerAudioCancion(id_cancion):
        return CancionDAO.obtenerAudio(id_cancion)

    @staticmethod
    def actualizarCancion(id_cancion, data, audio=None):
        return CancionDAO.actualizarCancion(id_cancion, data, audio)

    @staticmethod
    def actualizarCancionParcial(id_cancion, data, audio=None):
        return CancionDAO.actualizarCancionParcial(id_cancion, data, audio)

    @staticmethod
    def eliminarCancion(id_cancion):
        return CancionDAO.eliminarCancion(id_cancion)

    # -------------------------
    #        DISCOS MP3
    # -------------------------
    @staticmethod
    def crearDisco(data, portada=None):
        return DiscoMP3DAO.insertarDisco(data, portada)

    @staticmethod
    def obtenerDiscos():
        return DiscoMP3DAO.consultarDiscos()

    @staticmethod
    def obtenerDisco(id_disco):
        return DiscoMP3DAO.consultarDisco(id_disco)

    @staticmethod
    def obtenerPortada(id_disco):
        return DiscoMP3DAO.obtenerPortada(id_disco)

    @staticmethod
    def actualizarDisco(id_disco, data, portada=None):
        return DiscoMP3DAO.actualizarDisco(id_disco, data, portada)

    @staticmethod
    def actualizarDiscoParcial(id_disco, data, portada=None):
        return DiscoMP3DAO.actualizarDiscoParcial(id_disco, data, portada)

    @staticmethod
    def eliminarDisco(id_disco):
        return DiscoMP3DAO.eliminarDisco(id_disco)

    # -------------------------
    #          VINILOS
    # -------------------------
    @staticmethod
    def crearVinilo(data, caratula=None):
        return ViniloDAO.insertarVinilo(data, caratula)

    @staticmethod
    def obtenerVinilos():
        return ViniloDAO.consultarVinilos()

    @staticmethod
    def obtenerVinilo(id_vinilo):
        return ViniloDAO.consultarVinilo(id_vinilo)

    @staticmethod
    def obtenerCaratulaVinilo(id_vinilo):
        return ViniloDAO.obtenerCaratula(id_vinilo)

    @staticmethod
    def actualizarVinilo(id_vinilo, data, caratula=None):
        return ViniloDAO.actualizarVinilo(id_vinilo, data, caratula)

    @staticmethod
    def actualizarViniloParcial(id_vinilo, data, caratula=None):
        return ViniloDAO.actualizarViniloParcial(id_vinilo, data, caratula)

    @staticmethod
    def eliminarVinilo(id_vinilo):
        return ViniloDAO.eliminarVinilo(id_vinilo)
