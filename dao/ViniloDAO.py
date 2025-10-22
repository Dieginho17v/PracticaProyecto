from Datos import get_conn

class ViniloDAO:
    @staticmethod
    def insertarVinilo(data):
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO vinilo(nombre, artista, ano_salida, precio, inventario, id_proveedor) VALUES (?,?,?,?,?,?)",
                (data["nombre"], data.get("artista"), data.get("ano_salida"), data.get("precio"),
                 data.get("inventario"), data.get("id_proveedor"))
            )
            conn.commit()
            return cur.lastrowid

    @staticmethod
    def consultarVinilos(nombre=None):
        with get_conn() as conn:
            if nombre:
                filas = conn.execute("SELECT * FROM vinilo WHERE nombre LIKE ?", (f"%{nombre}%",)).fetchall()
            else:
                filas = conn.execute("SELECT * FROM vinilo").fetchall()
            return [dict(f) for f in filas]
