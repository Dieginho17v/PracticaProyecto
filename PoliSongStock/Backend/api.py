# api.py
from flask import Flask, request, jsonify, send_file
from io import BytesIO

from manager.CatalogManager import CatalogManager
from manager.UsuarioManager import UsuarioManager
from manager.PedidoManager import PedidoManager
from manager.RecopilacionManager import RecopilacionManager

app = Flask(__name__)

catalog_mgr = CatalogManager()
usuario_mgr = UsuarioManager()
pedido_mgr = PedidoManager()
recop_mgr = RecopilacionManager()

def detect_image_mime(b: bytes) -> str:
    if not b:
        return "application/octet-stream"
    if b.startswith(b'\xff\xd8'):
        return "image/jpeg"
    if b.startswith(b'\x89PNG'):
        return "image/png"
    return "image/jpeg"

def detect_audio_mime(b: bytes) -> str:
    if not b:
        return "application/octet-stream"
    if b.startswith(b'ID3') or b[0:2] == b'\xff\xfb':
        return "audio/mpeg"
    if b.startswith(b'OggS'):
        return "audio/ogg"
    # fallback
    return "application/octet-stream"

def json_or_400():
    data = None
    try:
        data = request.get_json(force=True)
    except Exception:
        return None
    return data

def respond_error(msg, code=400):
    return jsonify({"error": str(msg)}), code

@app.route("/usuarios", methods=["GET"])
def usuarios_get_all():
    try:
        datos = usuario_mgr.obtenerUsuarios()
        # sqlite returns rows; ensure serializable -> convert to list of dicts if necessary
        return jsonify([dict(row) if hasattr(row, "keys") else row for row in datos]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/usuarios/<int:id_usuario>", methods=["GET"])
def usuarios_get_by_id(id_usuario):
    try:
        u = usuario_mgr.obtenerUsuario(id_usuario)
        if not u:
            return respond_error("Usuario no encontrado", 404)
        return jsonify(dict(u) if hasattr(u, "keys") else u), 200
    except Exception as e:
        return respond_error(e)

@app.route("/usuarios", methods=["POST"])
def usuarios_post():
    data = json_or_400()
    if data is None:
        return respond_error("JSON inválido")
    try:
        nuevo = usuario_mgr.crearUsuario(data)
        return jsonify({"id_usuario": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/usuarios/<int:id_usuario>", methods=["PUT"])
def usuarios_put(id_usuario):
    data = json_or_400()
    if data is None:
        return respond_error("JSON inválido")
    try:
        usuario_mgr.actualizarUsuario(id_usuario, data)
        return jsonify({"mensaje": "Usuario actualizado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/usuarios/<int:id_usuario>", methods=["PATCH"])
def usuarios_patch(id_usuario):
    data = json_or_400()
    if data is None:
        return respond_error("JSON inválido")
    try:
        usuario_mgr.actualizarUsuarioParcial(id_usuario, data)
        return jsonify({"mensaje": "Usuario actualizado parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def usuarios_delete(id_usuario):
    try:
        usuario_mgr.eliminarUsuario(id_usuario)
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/discos", methods=["GET"])
def discos_get_all():
    try:
        discos = catalog_mgr.obtenerDiscos()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in discos]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/discos/<int:id_disco>", methods=["GET"])
def discos_get_by_id(id_disco):
    try:
        d = catalog_mgr.obtenerDisco(id_disco)
        if not d:
            return respond_error("Disco no encontrado", 404)
        return jsonify(dict(d) if hasattr(d, "keys") else d), 200
    except Exception as e:
        return respond_error(e)

@app.route("/discos/<int:id_disco>/imagen", methods=["GET"])
def discos_get_imagen(id_disco):
    try:
        blob = catalog_mgr.obtenerPortada(id_disco)
        if not blob:
            return respond_error("Imagen no encontrada", 404)
        mimetype = detect_image_mime(blob)
        return send_file(BytesIO(blob), mimetype=mimetype)
    except Exception as e:
        return respond_error(e)

@app.route("/discos", methods=["POST"])
def discos_post():
    try:
        data = request.form.to_dict()
        imagen = request.files.get("imagen")
        portada = imagen.read() if imagen else None
        nuevo = catalog_mgr.crearDisco(data, portada)
        return jsonify({"id_disco": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/discos/<int:id_disco>", methods=["PUT"])
def discos_put(id_disco):
    try:
        data = request.form.to_dict()
        imagen = request.files.get("imagen")
        portada = imagen.read() if imagen else None
        catalog_mgr.actualizarDisco(id_disco, data, portada)
        return jsonify({"mensaje": "Disco actualizado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/discos/<int:id_disco>", methods=["PATCH"])
def discos_patch(id_disco):
    try:
        data = request.form.to_dict()
        imagen = request.files.get("imagen")
        portada = imagen.read() if imagen else None
        catalog_mgr.actualizarDiscoParcial(id_disco, data, portada)
        return jsonify({"mensaje": "Disco actualizado parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/discos/<int:id_disco>", methods=["DELETE"])
def discos_delete(id_disco):
    try:
        catalog_mgr.eliminarDisco(id_disco)
        return jsonify({"mensaje": "Disco eliminado"}), 200
    except Exception as e:
        return respond_error(e)

# -------------------------
# CANCIONES (audio_blob)
# -------------------------
@app.route("/canciones", methods=["GET"])
def canciones_get_all():
    try:
        canciones = catalog_mgr.obtenerCanciones()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in canciones]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/canciones/<int:id_cancion>", methods=["GET"])
def canciones_get_by_id(id_cancion):
    try:
        c = catalog_mgr.obtenerCancion(id_cancion)
        if not c:
            return respond_error("Canción no encontrada", 404)
        return jsonify(dict(c) if hasattr(c, "keys") else c), 200
    except Exception as e:
        return respond_error(e)

@app.route("/canciones/<int:id_cancion>/audio", methods=["GET"])
def canciones_get_audio(id_cancion):
    try:
        blob = catalog_mgr.obtenerAudioCancion(id_cancion)
        if not blob:
            return respond_error("Audio no encontrado", 404)
        mimetype = detect_audio_mime(blob)
        return send_file(BytesIO(blob), mimetype=mimetype)
    except Exception as e:
        return respond_error(e)

@app.route("/canciones", methods=["POST"])
def canciones_post():
    try:
        data = request.form.to_dict()
        audio_file = request.files.get("audio")
        audio_blob = audio_file.read() if audio_file else None
        nuevo = catalog_mgr.crearCancion(data, audio_blob)
        return jsonify({"id_cancion": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/canciones/<int:id_cancion>", methods=["PUT"])
def canciones_put(id_cancion):
    try:
        data = request.form.to_dict()
        audio_file = request.files.get("audio")
        audio_blob = audio_file.read() if audio_file else None
        catalog_mgr.actualizarCancion(id_cancion, data, audio_blob)
        return jsonify({"mensaje": "Canción actualizada"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/canciones/<int:id_cancion>", methods=["PATCH"])
def canciones_patch(id_cancion):
    try:
        data = request.form.to_dict()
        audio_file = request.files.get("audio")
        audio_blob = audio_file.read() if audio_file else None
        catalog_mgr.actualizarCancionParcial(id_cancion, data, audio_blob)
        return jsonify({"mensaje": "Canción actualizada parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/canciones/<int:id_cancion>", methods=["DELETE"])
def canciones_delete(id_cancion):
    try:
        catalog_mgr.eliminarCancion(id_cancion)
        return jsonify({"mensaje": "Canción eliminada"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos", methods=["GET"])
def vinilos_get_all():
    try:
        vinilos = catalog_mgr.obtenerVinilos()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in vinilos]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos/<int:id_vinilo>", methods=["GET"])
def vinilos_get_by_id(id_vinilo):
    try:
        v = catalog_mgr.obtenerVinilo(id_vinilo)
        if not v:
            return respond_error("Vinilo no encontrado", 404)
        return jsonify(dict(v) if hasattr(v, "keys") else v), 200
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos/<int:id_vinilo>/caratula", methods=["GET"])
def vinilos_get_caratula(id_vinilo):
    try:
        blob = catalog_mgr.obtenerCaratulaVinilo(id_vinilo)
        if not blob:
            return respond_error("Carátula no encontrada", 404)
        mimetype = detect_image_mime(blob)
        return send_file(BytesIO(blob), mimetype=mimetype)
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos", methods=["POST"])
def vinilos_post():
    try:
        data = request.form.to_dict()
        caratula_file = request.files.get("caratula")
        caratula = caratula_file.read() if caratula_file else None
        nuevo = catalog_mgr.crearVinilo(data, caratula)
        return jsonify({"id_vinilo": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos/<int:id_vinilo>", methods=["PUT"])
def vinilos_put(id_vinilo):
    try:
        data = request.form.to_dict()
        caratula_file = request.files.get("caratula")
        caratula = caratula_file.read() if caratula_file else None
        catalog_mgr.actualizarVinilo(id_vinilo, data, caratula)
        return jsonify({"mensaje": "Vinilo actualizado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos/<int:id_vinilo>", methods=["PATCH"])
def vinilos_patch(id_vinilo):
    try:
        data = request.form.to_dict()
        caratula_file = request.files.get("caratula")
        caratula = caratula_file.read() if caratula_file else None
        catalog_mgr.actualizarViniloParcial(id_vinilo, data, caratula)
        return jsonify({"mensaje": "Vinilo actualizado parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/vinilos/<int:id_vinilo>", methods=["DELETE"])
def vinilos_delete(id_vinilo):
    try:
        catalog_mgr.eliminarVinilo(id_vinilo)
        return jsonify({"mensaje": "Vinilo eliminado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones", methods=["GET"])
def recop_get_all():
    try:
        recos = recop_mgr.obtenerRecopilaciones()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in recos]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>", methods=["GET"])
def recop_get_by_id(id_reco):
    try:
        r = recop_mgr.obtenerRecopilacion(id_reco)
        if not r:
            return respond_error("Recopilacion no encontrada", 404)
        return jsonify(dict(r) if hasattr(r, "keys") else r), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>/caratula", methods=["GET"])
def recop_get_caratula(id_reco):
    try:
        blob = recop_mgr.obtenerCaratula(id_reco)
        if not blob:
            return respond_error("Carátula no encontrada", 404)
        mimetype = detect_image_mime(blob)
        return send_file(BytesIO(blob), mimetype=mimetype)
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones", methods=["POST"])
def recop_post():
    try:
        data = request.form.to_dict()
        imagen_file = request.files.get("imagen")
        imagen = imagen_file.read() if imagen_file else None
        nuevo = recop_mgr.crearRecopilacion(data, imagen)
        return jsonify({"id_recopilacion": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>", methods=["PUT"])
def recop_put(id_reco):
    try:
        data = request.form.to_dict()
        imagen_file = request.files.get("imagen")
        imagen = imagen_file.read() if imagen_file else None
        recop_mgr.actualizarRecopilacion(id_reco, data, imagen)
        return jsonify({"mensaje": "Recopilación actualizada"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>", methods=["PATCH"])
def recop_patch(id_reco):
    try:
        data = request.form.to_dict()
        imagen_file = request.files.get("imagen")
        imagen = imagen_file.read() if imagen_file else None
        recop_mgr.actualizarRecopilacionParcial(id_reco, data, imagen)
        return jsonify({"mensaje": "Recopilación actualizada parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>", methods=["DELETE"])
def recop_delete(id_reco):
    try:
        recop_mgr.eliminarRecopilacion(id_reco)
        return jsonify({"mensaje": "Recopilación eliminada"}), 200
    except Exception as e:
        return respond_error(e)

# Canciones de una recopilacion
@app.route("/recopilaciones/<int:id_reco>/canciones", methods=["GET"])
def recop_canciones_get(id_reco):
    try:
        canciones = recop_mgr.obtenerCancionesDeRecopilacion(id_reco)
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in canciones]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>/canciones", methods=["POST"])
def recop_canciones_post(id_reco):
    try:
        # Accept JSON: {"id_cancion": X} or form-data
        data = request.get_json(silent=True) or request.form.to_dict()
        id_cancion = data.get("id_cancion") or data.get("idCancion") or data.get("id")
        if not id_cancion:
            return respond_error("Falta id_cancion en el body")
        recop_mgr.agregarCancionARecopilacion(int(id_cancion), id_reco)
        return jsonify({"mensaje": "Canción asociada"}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/recopilaciones/<int:id_reco>/canciones/<int:id_cancion>", methods=["DELETE"])
def recop_canciones_delete(id_reco, id_cancion):
    try:
        recop_mgr.eliminarCancionDeRecopilacion(id_cancion, id_reco)
        return jsonify({"mensaje": "Canción eliminada de la recopilación"}), 200
    except Exception as e:
        return respond_error(e)

# PEDIDOS
@app.route("/pedidos", methods=["GET"])
def pedidos_get_all():
    try:
        pedidos = pedido_mgr.obtenerPedidos()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in pedidos]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/pedidos/<int:id_pedido>", methods=["GET"])
def pedidos_get_by_id(id_pedido):
    try:
        p = pedido_mgr.obtenerPedido(id_pedido)
        if not p:
            return respond_error("Pedido no encontrado", 404)
        return jsonify(dict(p) if hasattr(p, "keys") else p), 200
    except Exception as e:
        return respond_error(e)

@app.route("/pedidos", methods=["POST"])
def pedidos_post():
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        nuevo = pedido_mgr.crearPedido(data)
        return jsonify({"id_pedido": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/pedidos/<int:id_pedido>", methods=["PUT"])
def pedidos_put(id_pedido):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarPedido(id_pedido, data)
        return jsonify({"mensaje": "Pedido actualizado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/pedidos/<int:id_pedido>", methods=["PATCH"])
def pedidos_patch(id_pedido):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarPedidoParcial(id_pedido, data)
        return jsonify({"mensaje": "Pedido actualizado parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/pedidos/<int:id_pedido>", methods=["DELETE"])
def pedidos_delete(id_pedido):
    try:
        pedido_mgr.eliminarPedido(id_pedido)
        return jsonify({"mensaje": "Pedido eliminado"}), 200
    except Exception as e:
        return respond_error(e)

# PRODUCTOS
@app.route("/productos", methods=["GET"])
def productos_get_all():
    try:
        prods = pedido_mgr.obtenerProductos()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in prods]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/productos/<int:id_producto>", methods=["GET"])
def productos_get_by_id(id_producto):
    try:
        p = pedido_mgr.obtenerProducto(id_producto)
        if not p:
            return respond_error("Producto no encontrado", 404)
        return jsonify(dict(p) if hasattr(p, "keys") else p), 200
    except Exception as e:
        return respond_error(e)

@app.route("/productos", methods=["POST"])
def productos_post():
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        nuevo = pedido_mgr.crearProducto(data)
        return jsonify({"id_producto": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/productos/<int:id_producto>", methods=["PUT"])
def productos_put(id_producto):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarProducto(id_producto, data)
        return jsonify({"mensaje": "Producto actualizado"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/productos/<int:id_producto>", methods=["PATCH"])
def productos_patch(id_producto):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarProductoParcial(id_producto, data)
        return jsonify({"mensaje": "Producto actualizado parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/productos/<int:id_producto>", methods=["DELETE"])
def productos_delete(id_producto):
    try:
        pedido_mgr.eliminarProducto(id_producto)
        return jsonify({"mensaje": "Producto eliminado"}), 200
    except Exception as e:
        return respond_error(e)

# VALORACIONES
@app.route("/valoraciones", methods=["GET"])
def valoraciones_get_all():
    try:
        vals = pedido_mgr.obtenerValoraciones()
        return jsonify([dict(r) if hasattr(r, "keys") else r for r in vals]), 200
    except Exception as e:
        return respond_error(e)

@app.route("/valoraciones/<int:id_valoracion>", methods=["GET"])
def valoraciones_get_by_id(id_valoracion):
    try:
        v = pedido_mgr.obtenerValoracion(id_valoracion)
        if not v:
            return respond_error("Valoración no encontrada", 404)
        return jsonify(dict(v) if hasattr(v, "keys") else v), 200
    except Exception as e:
        return respond_error(e)

@app.route("/valoraciones", methods=["POST"])
def valoraciones_post():
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        nuevo = pedido_mgr.crearValoracion(data)
        return jsonify({"id_valoracion": nuevo}), 201
    except Exception as e:
        return respond_error(e)

@app.route("/valoraciones/<int:id_valoracion>", methods=["PUT"])
def valoraciones_put(id_valoracion):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarValoracion(id_valoracion, data)
        return jsonify({"mensaje": "Valoración actualizada"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/valoraciones/<int:id_valoracion>", methods=["PATCH"])
def valoraciones_patch(id_valoracion):
    try:
        data = json_or_400()
        if data is None:
            return respond_error("JSON inválido")
        pedido_mgr.actualizarValoracionParcial(id_valoracion, data)
        return jsonify({"mensaje": "Valoración actualizada parcialmente"}), 200
    except Exception as e:
        return respond_error(e)

@app.route("/valoraciones/<int:id_valoracion>", methods=["DELETE"])
def valoraciones_delete(id_valoracion):
    try:
        pedido_mgr.eliminarValoracion(id_valoracion)
        return jsonify({"mensaje": "Valoración eliminada"}), 200
    except Exception as e:
        return respond_error(e)

if __name__ == "__main__":
    app.run(debug=True)