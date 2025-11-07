from Datos import get_conn

class ViniloDAO:

    @staticmethod
    def insertarVinilo(data):
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO vinilo (nombre, artista, ano_salida, precio, inventario, id_proveedor)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data.get("nombre"),
                data.get("artista"),
                data.get("ano_salida"),
                data.get("precio"),
                data.get("inventario"),
                data.get("id_proveedor")
            ))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def consultarVinilos(nombre=None):
        with get_conn() as conn:
            if nombre:
                cursor = conn.execute("SELECT * FROM vinilo WHERE nombre LIKE ?", (f"%{nombre}%",))
            else:
                cursor = conn.execute("SELECT * FROM vinilo")
            return [dict(row) for row in cursor.fetchall()]

    @staticmethod
    def consultarVinilo(id_vinilo):
        with get_conn() as conn:
            cursor = conn.execute("SELECT * FROM vinilo WHERE id_vinilo=?", (id_vinilo,))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def actualizarVinilo(id_vinilo, data):
        with get_conn() as conn:
            conn.execute("""
                UPDATE vinilo
                SET nombre=?, artista=?, ano_salida=?, precio=?, inventario=?, id_proveedor=?
                WHERE id_vinilo=?
            """, (
                data.get("nombre"),
                data.get("artista"),
                data.get("ano_salida"),
                data.get("precio"),
                data.get("inventario"),
                data.get("id_proveedor"),
                id_vinilo
            ))
            conn.commit()

    @staticmethod
    def actualizarViniloParcial(id_vinilo, data):
        campos, valores = [], []
        for k, v in data.items():
            campos.append(f"{k}=?")
            valores.append(v)
        valores.append(id_vinilo)
        with get_conn() as conn:
            conn.execute(f"UPDATE vinilo SET {', '.join(campos)} WHERE id_vinilo=?", valores)
            conn.commit()

    @staticmethod
    def eliminarVinilo(id_vinilo):
        with get_conn() as conn:
            conn.execute("DELETE FROM vinilo WHERE id_vinilo=?", (id_vinilo,))
            conn.commit()
