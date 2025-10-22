from dao.CancionDAO import CancionDAO
from dao.DiscoDAO import DiscoDAO
from dao.ViniloDAO import ViniloDAO

class CatalogManager:
    def buscarCancion(self, nombre=None):
        return CancionDAO.consultarCanciones(nombre)

    def buscarDisco(self, nombre=None):
        return DiscoDAO.consultarDiscos(nombre)

    def buscarVinilo(self, nombre=None):
        return ViniloDAO.consultarVinilos(nombre)
