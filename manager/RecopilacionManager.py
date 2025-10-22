from dao.RecopilacionDAO import RecopilacionDAO
from dao.CancionRecopilacionDAO import CancionRecopilacionDAO

class RecopilacionManager:
    def crearRecopilacion(self, data):
        return RecopilacionDAO.insertarRecopilacion(data)

    def asociarCanciones(self, id_recopilacion, canciones):
        for c in canciones:
            CancionRecopilacionDAO.asociarCancion(id_recopilacion, c)
