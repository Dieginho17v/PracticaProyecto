from Datos import get_conn

class CancionViniloDAO:
    @staticmethod
    def asociarCancionVinilo(id_vinilo, id_cancion, duracion=None):
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO cancion_vinilo(id_vinilo,id_cancion,duracion_segundos_vinilo) VALUES (?,?,?)",
                (id_vinilo, id_cancion, duracion)
            )
            conn.commit()
