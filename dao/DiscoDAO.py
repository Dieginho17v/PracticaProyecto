from Datos import get_conn

class DiscoDAO:
    @staticmethod
    def insertarDisco(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO disco(nombre, genero, imagen_portada) VALUES (?,?,?)",
                (data["nombre"], data.get("genero"), data.get("imagen_portada"))
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarDiscos(nombre=None):
        with get_conn() as conn:
            if nombre:
                filas = conn.execute("SELECT * FROM disco WHERE nombre LIKE ?", (f"%{nombre}%",)).fetchall()
            else:
                filas = conn.execute("SELECT * FROM disco").fetchall()
            return [dict(f) for f in filas]