from Datos import get_conn

class CancionRecopilacionDAO:
    @staticmethod
    def asociarCancion(id_recopilacion, id_cancion):
        with get_conn() as conn:
            conn.execute("INSERT INTO cancion_recopilacion(id_recopilacion,id_cancion) VALUES (?,?)",
                         (id_recopilacion, id_cancion))
            conn.commit()
