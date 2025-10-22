from flask import Flask, request, jsonify
from Datos import ensure_schema, get_conn
from manager.UsuarioManager import UsuarioManager
from manager.CatalogManager import CatalogManager
from manager.PedidoManager import PedidoManager
from manager.RecopilacionManager import RecopilacionManager
from dao import UsuarioDAO, CancionDAO, DiscoDAO, ViniloDAO, RecopilacionDAO, CancionRecopilacionDAO, CancionViniloDAO, PedidoDAO, DetallePedidoDAO, ValoracionDAO
from dao.CancionDAO import CancionDAO

app = Flask(__name__)

# Crear estructura de base de datos si no existe
ensure_schema()

# Instancias de managers
usuario_mgr = UsuarioManager()
catalogo_mgr = CatalogManager()
pedido_mgr = PedidoManager()
recopilacion_mgr = RecopilacionManager()


# =========================================================
#                     FUNCIONES AUXILIARES
# =========================================================
def actualizar_parcial(tabla, id_columna, id_valor, data):
    """
    Función genérica para PATCH parcial de cualquier tabla.
    """
    columnas = ", ".join([f"{col}=?" for col in data.keys()])
    valores = list(data.values()) + [id_valor]
    query = f"UPDATE {tabla} SET {columnas} WHERE {id_columna}=?"
    with get_conn() as conn:
        conn.execute(query, valores)
        conn.commit()
    return {"mensaje": f"{tabla} actualizada parcialmente"}


def eliminar_registro(tabla, id_columna, id_valor):
    """
    Función genérica para DELETE de cualquier tabla.
    """
    with get_conn() as conn:
        conn.execute(f"DELETE FROM {tabla} WHERE {id_columna}=?", (id_valor,))
        conn.commit()
    return {"mensaje": f"{tabla} eliminada correctamente"}


# =========================================================
#                     ENDPOINTS USUARIOS
# =========================================================
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = UsuarioDAO.consultarUsuarios() if hasattr(UsuarioDAO, "consultarUsuarios") else []
    return jsonify(usuarios), 200

@app.route("/usuarios/<int:id_usuario>", methods=["GET"])
def get_usuario_por_id(id_usuario):
    usuario = UsuarioDAO.consultarUsuario(id_usuario)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/usuarios", methods=["POST"])
def post_usuario():
    data = request.get_json()
    try:
        id_usuario = usuario_mgr.registrarUsuario(data)
        return jsonify({"id_usuario": id_usuario}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/usuarios/<int:id_usuario>", methods=["PUT"])
def put_usuario(id_usuario):
    data = request.get_json()
    try:
        usuario_mgr.actualizarPerfil(id_usuario, data)
        return jsonify({"mensaje": "Usuario actualizado completamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/usuarios/<int:id_usuario>", methods=["PATCH"])
def patch_usuario(id_usuario):
    data = request.get_json()
    return jsonify(actualizar_parcial("usuario", "id_usuario", id_usuario, data)), 200

@app.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def delete_usuario(id_usuario):
    return jsonify(eliminar_registro("usuario", "id_usuario", id_usuario)), 200

@app.route("/usuarios/login", methods=["POST"])
def login_usuario():
    data = request.get_json()
    usuario = usuario_mgr.validarCredenciales(data.get("correo"), data.get("contrasena"))
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Credenciales inválidas"}), 401


# =========================================================
#                     ENDPOINTS CANCIONES
# =========================================================
@app.route("/canciones", methods=["GET"])
def get_canciones():
    nombre = request.args.get("nombre")
    canciones = catalogo_mgr.buscarCancion(nombre)
    return jsonify(canciones), 200

@app.route("/canciones/<int:id_cancion>", methods=["GET"])
def get_cancion_por_id(id_cancion):
    cancion = CancionDAO.consultarCancion(id_cancion) if hasattr(CancionDAO, "consultarCancion") else None
    if cancion:
        return jsonify(cancion), 200
    return jsonify({"error": "Canción no encontrada"}), 404

@app.route("/canciones", methods=["POST"])
def post_cancion():
    data = request.get_json()
    try:
        id_cancion = CancionDAO.insertarCancion(data)
        return jsonify({"id_cancion": id_cancion}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/canciones/<int:id_cancion>", methods=["PUT"])
def put_cancion(id_cancion):
    data = request.get_json()
    try:
        CancionDAO.actualizarCancion(id_cancion, data)
        return jsonify({"mensaje": "Canción actualizada completamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/canciones/<int:id_cancion>", methods=["PATCH"])
def patch_cancion(id_cancion):
    data = request.get_json()
    return jsonify(actualizar_parcial("cancion", "id_cancion", id_cancion, data)), 200

@app.route("/canciones/<int:id_cancion>", methods=["DELETE"])
def delete_cancion(id_cancion):
    return jsonify(eliminar_registro("cancion", "id_cancion", id_cancion)), 200


# =========================================================
#                     ENDPOINTS DISCOS
# =========================================================
@app.route("/discos", methods=["GET"])
def get_discos():
    from dao.DiscoDAO import DiscoDAO
    discos = DiscoDAO.consultarDiscos()
    return jsonify(discos), 200

@app.route("/discos/<int:id_disco>", methods=["GET"])
def get_disco_por_id(id_disco):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM disco WHERE id_disco=?", (id_disco,)).fetchone()
        if row:
            return jsonify(dict(row)), 200
        return jsonify({"error": "Disco no encontrado"}), 404

@app.route("/discos", methods=["POST"])
def post_disco():
    data = request.get_json()
    from dao.DiscoDAO import DiscoDAO
    id_disco = DiscoDAO.insertarDisco(data)
    return jsonify({"id_disco": id_disco}), 201

@app.route("/discos/<int:id_disco>", methods=["PUT"])
def put_disco(id_disco):
    data = request.get_json()
    actualizar_parcial("disco", "id_disco", id_disco, data)
    return jsonify({"mensaje": "Disco actualizado"}), 200

@app.route("/discos/<int:id_disco>", methods=["PATCH"])
def patch_disco(id_disco):
    data = request.get_json()
    return jsonify(actualizar_parcial("disco", "id_disco", id_disco, data)), 200

@app.route("/discos/<int:id_disco>", methods=["DELETE"])
def delete_disco(id_disco):
    return jsonify(eliminar_registro("disco", "id_disco", id_disco)), 200


# =========================================================
#                     ENDPOINTS VINILOS
# =========================================================
@app.route("/vinilos", methods=["GET"])
def get_vinilos():
    from dao.ViniloDAO import ViniloDAO
    vinilos = ViniloDAO.consultarVinilos()
    return jsonify(vinilos), 200

@app.route("/vinilos/<int:id_vinilo>", methods=["GET"])
def get_vinilo_por_id(id_vinilo):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM vinilo WHERE id_vinilo=?", (id_vinilo,)).fetchone()
        if row:
            return jsonify(dict(row)), 200
        return jsonify({"error": "Vinilo no encontrado"}), 404

@app.route("/vinilos", methods=["POST"])
def post_vinilo():
    data = request.get_json()
    from dao.ViniloDAO import ViniloDAO
    id_vinilo = ViniloDAO.insertarVinilo(data)
    return jsonify({"id_vinilo": id_vinilo}), 201

@app.route("/vinilos/<int:id_vinilo>", methods=["PUT"])
def put_vinilo(id_vinilo):
    data = request.get_json()
    actualizar_parcial("vinilo", "id_vinilo", id_vinilo, data)
    return jsonify({"mensaje": "Vinilo actualizado"}), 200

@app.route("/vinilos/<int:id_vinilo>", methods=["PATCH"])
def patch_vinilo(id_vinilo):
    data = request.get_json()
    return jsonify(actualizar_parcial("vinilo", "id_vinilo", id_vinilo, data)), 200

@app.route("/vinilos/<int:id_vinilo>", methods=["DELETE"])
def delete_vinilo(id_vinilo):
    return jsonify(eliminar_registro("vinilo", "id_vinilo", id_vinilo)), 200


# =========================================================
#         ENDPOINTS PARA RECOPILACIONES Y RELACIONES
# =========================================================
@app.route("/recopilaciones", methods=["GET"])
def get_recopilaciones():
    recopilaciones = RecopilacionDAO.consultarRecopilaciones()
    return jsonify(recopilaciones), 200

@app.route("/recopilaciones/<int:id_recopilacion>", methods=["GET"])
def get_recopilacion_por_id(id_recopilacion):
    recopilacion = RecopilacionDAO.obtenerPorId(id_recopilacion)
    if recopilacion:
        return jsonify(recopilacion), 200
    return jsonify({"error": "Recopilación no encontrada"}), 404

@app.route("/recopilaciones", methods=["POST"])
def post_recopilacion():
    data = request.get_json()
    id_recopilacion = recopilacion_mgr.crearRecopilacion(data)
    return jsonify({"id_recopilacion": id_recopilacion}), 201

@app.route("/recopilaciones/<int:id_recopilacion>", methods=["PUT"])
def put_recopilacion(id_recopilacion):
    data = request.get_json()
    actualizar_parcial("recopilacion", "id_recopilacion", id_recopilacion, data)
    return jsonify({"mensaje": "Recopilación actualizada"}), 200

@app.route("/recopilaciones/<int:id_recopilacion>", methods=["PATCH"])
def patch_recopilacion(id_recopilacion):
    data = request.get_json()
    return jsonify(actualizar_parcial("recopilacion", "id_recopilacion", id_recopilacion, data)), 200

@app.route("/recopilaciones/<int:id_recopilacion>", methods=["DELETE"])
def delete_recopilacion(id_recopilacion):
    return jsonify(eliminar_registro("recopilacion", "id_recopilacion", id_recopilacion)), 200

@app.route("/recopilaciones/<int:id_recopilacion>/canciones", methods=["POST"])
def post_recopilacion_canciones(id_recopilacion):
    data = request.get_json()
    canciones = data.get("canciones", [])
    recopilacion_mgr.asociarCanciones(id_recopilacion, canciones)
    return jsonify({"mensaje": "Canciones asociadas"}), 200


# =========================================================
#                     ENDPOINTS PEDIDOS
# =========================================================
@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    pedidos = PedidoDAO.consultarPedidos()
    return jsonify(pedidos), 200

@app.route("/pedidos/<int:id_pedido>", methods=["GET"])
def get_pedido_por_id(id_pedido):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM pedido WHERE id_pedido=?", (id_pedido,)).fetchone()
        if row:
            return jsonify(dict(row)), 200
        return jsonify({"error": "Pedido no encontrado"}), 404

@app.route("/pedidos", methods=["POST"])
def post_pedido():
    data = request.get_json()
    pedido = data.get("pedido")
    detalles = data.get("detalles", [])
    id_pedido = pedido_mgr.crearPedido(pedido, detalles)
    return jsonify({"id_pedido": id_pedido}), 201

@app.route("/pedidos/<int:id_pedido>", methods=["PUT"])
def put_pedido(id_pedido):
    data = request.get_json()
    pedido_mgr.cambiarEstado(id_pedido, data.get("estado"))
    return jsonify({"mensaje": "Estado actualizado"}), 200

@app.route("/pedidos/<int:id_pedido>", methods=["PATCH"])
def patch_pedido(id_pedido):
    data = request.get_json()
    return jsonify(actualizar_parcial("pedido", "id_pedido", id_pedido, data)), 200

@app.route("/pedidos/<int:id_pedido>", methods=["DELETE"])
def delete_pedido(id_pedido):
    return jsonify(eliminar_registro("pedido", "id_pedido", id_pedido)), 200

@app.route("/pedidos/<int:id_pedido>/valoracion", methods=["POST"])
def post_valoracion(id_pedido):
    data = request.get_json()
    data["pedido_id_pedido"] = id_pedido
    id_val = pedido_mgr.agregarValoracion(data)
    return jsonify({"id_valoracion": id_val}), 201

@app.route("/pedidos/reporte", methods=["GET"])
def get_reporte():
    reporte = pedido_mgr.generarReporte()
    return jsonify(reporte), 200


# =========================================================
#                    VALORACIONES
# =========================================================
@app.route("/valoraciones", methods=["GET"])
def get_valoraciones():
    valoraciones = ValoracionDAO.consultarValoraciones()
    return jsonify(valoraciones), 200

@app.route("/valoraciones/<int:id_valoracion>", methods=["GET"])
def get_valoracion_por_id(id_valoracion):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM valoracion WHERE id_valoracion=?", (id_valoracion,)).fetchone()
        if row:
            return jsonify(dict(row)), 200
        return jsonify({"error": "Valoración no encontrada"}), 404

@app.route("/valoraciones/<int:id_valoracion>", methods=["PATCH"])
def patch_valoracion(id_valoracion):
    data = request.get_json()
    return jsonify(actualizar_parcial("valoracion", "id_valoracion", id_valoracion, data)), 200

@app.route("/valoraciones/<int:id_valoracion>", methods=["DELETE"])
def delete_valoracion(id_valoracion):
    return jsonify(eliminar_registro("valoracion", "id_valoracion", id_valoracion)), 200


# =========================================================
#                   INICIO DEL SERVIDOR
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)
