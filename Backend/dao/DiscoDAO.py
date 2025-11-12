from Datos import get_conn

class DiscoDAO:

    @staticmethod
    def insertarDisco(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO disco (nombre, genero, imagen_portada)
                VALUES (?, ?, ?)
            """, (
                data.get("nombre"),
                data.get("genero"),
                data.get("imagen_portada")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarDiscos(nombre=None):
        with get_conn() as conn:
            if nombre:
                cursor = conn.execute("SELECT * FROM disco WHERE nombre LIKE ?", (f"%{nombre}%",))
            else:
                cursor = conn.execute("SELECT * FROM disco")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarDisco(id_disco):
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM disco WHERE id_disco=?", (id_disco,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarDisco(id_disco, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE disco
                SET nombre=?, genero=?, imagen_portada=?
                WHERE id_disco=?
            """, (
                data.get("nombre"),
                data.get("genero"),
                data.get("imagen_portada"),
                id_disco
            ))
            conn.commit()

    @staticmethod
    def actualizarDiscoParcial(id_disco, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_disco)
        with get_conn() as conn:
            conn.execute(f"UPDATE disco SET {', '.join(campos)} WHERE id_disco=?", valores)
            conn.commit()

    @staticmethod
    def eliminarDisco(id_disco):
        with get_conn() as conn:
            conn.execute("DELETE FROM disco WHERE id_disco=?", (id_disco,))
            conn.commit()
