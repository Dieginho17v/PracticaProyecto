from django.shortcuts import render, redirect, get_object_or_404
from .api_config import api_get, api_post, api_put, api_delete
from .models import Usuario, DiscoMP3, Cancion, Vinilo, Recopilacion, Producto, Pedido, CancionVinilo, Valoracion, CancionRecopilacion

# -------------------------
# INDEX
# -------------------------
def index(request):
    return render(request, "index.html")

# -------------------------
# USUARIOS
# -------------------------
def usuarios_list(request):
    usuarios = api_get("/usuarios")  # Devuelve lista desde API Flask
    return render(request, "usuarios/usuarios_list.html", {"usuarios": usuarios})

def usuarios_create(request):
    if request.method == "POST":
        data = {
            "nombre": request.POST["nombre"],
            "email": request.POST["email"],
            "contrasena": request.POST["contrasena"]
        }
        api_post("/usuarios", data)
        return redirect("usuarios_list")
    return render(request, "usuarios/usuarios_form.html")

def usuarios_update(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)

    if request.method == "POST":
        usuario.nombre = request.POST["nombre"]
        usuario.email = request.POST["email"]
        usuario.save()
        return redirect("usuarios_list")
    return render(request, "usuarios/usuarios_form.html", {"usuario": usuario})

def usuarios_delete(request, id_usuario):
    api_delete(f"/usuarios/{id_usuario}")
    return redirect("usuarios_list")

# -------------------------
# DISCOS MP3
# -------------------------
def discos_list(request):
    discos = DiscoMP3.objects.all()
    return render(request, "discos/discos_list.html", {"discos": discos})

def discos_create(request):
    if request.method == "POST":
        DiscoMP3.objects.create(
            nombre=request.POST["nombre"],
            genero=request.POST["genero"],
        )
        return redirect("discos_list")
    return render(request, "discos/discos_form.html")

def discos_update(request, id_disco):
    disco = get_object_or_404(DiscoMP3, id_disco=id_disco)

    if request.method == "POST":
        disco.nombre = request.POST["nombre"]
        disco.genero = request.POST["genero"]
        disco.save()
        return redirect("discos_list")
    return render(request, "discos/discos_form.html", {"disco": disco})

def discos_delete(request, id_disco):
    disco = get_object_or_404(DiscoMP3, id_disco=id_disco)
    disco.delete()
    return redirect("discos_list")

# -------------------------
# CANCIONES
# -------------------------
def canciones_list(request):
    canciones = Cancion.objects.select_related("id_disco").all()
    return render(request, "canciones/canciones_list.html", {"canciones": canciones})

def canciones_create(request):
    discos = DiscoMP3.objects.all()

    if request.method == "POST":
        Cancion.objects.create(
            nombre=request.POST["nombre"],
            duracion=request.POST["duracion"],
            tamaño_mb=request.POST["tamaño_mb"],
            calidad_kbps=request.POST["calidad_kbps"],
            audio_blob=None,  # por ahora sin archivos
            id_disco_id=request.POST["id_disco"]
        )
        return redirect("canciones_list")
    return render(request, "canciones/canciones_form.html", {"discos": discos})

def canciones_update(request, id_cancion):
    cancion = get_object_or_404(Cancion, id_cancion=id_cancion)
    discos = DiscoMP3.objects.all()

    if request.method == "POST":
        cancion.nombre = request.POST["nombre"]
        cancion.duracion = request.POST["duracion"]
        cancion.tamaño_mb = request.POST["tamaño_mb"]
        cancion.calidad_kbps = request.POST["calidad_kbps"]
        cancion.id_disco_id = request.POST["id_disco"]
        cancion.save()
        return redirect("canciones_list")
    return render(
        request,
        "canciones/canciones_form.html",
        {"cancion": cancion, "discos": discos}
    )

def canciones_delete(request, id_cancion):
    cancion = get_object_or_404(Cancion, id_cancion=id_cancion)
    cancion.delete()
    return redirect("canciones_list")

# -------------------------
# VINILOS
# -------------------------
def vinilos_list(request):
    vinilos = Vinilo.objects.all()
    return render(request, "vinilos/vinilos_list.html", {"vinilos": vinilos})

def vinilos_create(request):
    if request.method == "POST":
        Vinilo.objects.create(
            nombre=request.POST["nombre"],
            rpm=request.POST["rpm"],
            imagen_caratula=request.POST["imagen_caratula"],
        )
        return redirect("vinilos_list")
    return render(request, "vinilos/vinilos_form.html")

def vinilos_update(request, id_vinilo):
    vinilo = get_object_or_404(Vinilo, id_vinilo=id_vinilo)

    if request.method == "POST":
        vinilo.nombre = request.POST["nombre"]
        vinilo.rpm = request.POST["rpm"]
        vinilo.imagen_caratula = request.POST["imagen_caratula"]
        vinilo.save()
        return redirect("vinilos_list")
    return render(request, "vinilos/vinilos_form.html", {"vinilo": vinilo})

def vinilos_delete(request, id_vinilo):
    vinilo = get_object_or_404(Vinilo, id_vinilo=id_vinilo)
    vinilo.delete()
    return redirect("vinilos_list")

# -------------------------
# RECOPILACIONES
# -------------------------
def recopilaciones_list(request):
    recopilaciones = Recopilacion.objects.all()
    return render(request, "recopilaciones/recopilaciones_list.html", {
        "recopilaciones": recopilaciones
    })


def recopilaciones_create(request):
    if request.method == "POST":
        Recopilacion.objects.create(
            nombre=request.POST["nombre"],
            descripcion=request.POST["descripcion"],
            imagen_caratula=request.POST["imagen_caratula"],
        )
        return redirect("recopilaciones_list")
    return render(request, "recopilaciones/recopilaciones_form.html")

def recopilaciones_update(request, id_recopilacion):
    recopilacion = get_object_or_404(Recopilacion, id_recopilacion=id_recopilacion)

    if request.method == "POST":
        recopilacion.nombre = request.POST["nombre"]
        recopilacion.descripcion = request.POST["descripcion"]
        recopilacion.imagen_caratula = request.POST["imagen_caratula"]
        recopilacion.save()
        return redirect("recopilaciones_list")
    return render(request, "recopilaciones/recopilaciones_form.html", {
        "recopilacion": recopilacion
    })

def recopilaciones_delete(request, id_recopilacion):
    recopilacion = get_object_or_404(Recopilacion, id_recopilacion=id_recopilacion)
    recopilacion.delete()
    return redirect("recopilaciones_list")

# -------------------------
# PRODUCTOS
# -------------------------
def productos_list(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos_list.html", {"productos": productos})

def productos_create(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST["nombre"],
            precio=request.POST["precio"],
            tipo=request.POST["tipo"],
            id_ref=request.POST["id_ref"]
        )
        return redirect("productos_list")
    return render(request, "productos/productos_form.html")

def productos_update(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)

    if request.method == "POST":
        producto.nombre = request.POST["nombre"]
        producto.precio = request.POST["precio"]
        producto.tipo = request.POST["tipo"]
        producto.id_ref = request.POST["id_ref"]
        producto.save()
        return redirect("productos_list")
    return render(request, "productos/productos_form.html", {"producto": producto})

def productos_delete(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    producto.delete()
    return redirect("productos_list")

# -------------------------
# PEDIDOS
# -------------------------
def pedidos_list(request):
    pedidos = Pedido.objects.select_related("id_usuario").all()
    return render(request, "pedidos/pedidos_list.html", {"pedidos": pedidos})

def pedidos_create(request):
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        Pedido.objects.create(
            fecha=request.POST["fecha"],
            total=request.POST["total"],
            id_usuario_id=request.POST["id_usuario"]
        )
        return redirect("pedidos_list")
    return render(request, "pedidos/pedidos_form.html", {"usuarios": usuarios})

def pedidos_update(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        pedido.fecha = request.POST["fecha"]
        pedido.total = request.POST["total"]
        pedido.id_usuario_id = request.POST["id_usuario"]
        pedido.save()
        return redirect("pedidos_list")
    return render(
        request,
        "pedidos/pedidos_form.html",
        {"pedido": pedido, "usuarios": usuarios}
    )

def pedidos_delete(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    pedido.delete()
    return redirect("pedidos_list")

# -------------------------
# CANCION-VINILO
# -------------------------
def cancion_vinilo_list(request):
    relaciones = CancionVinilo.objects.select_related("id_cancion", "id_vinilo").all()
    return render(request, "cancion_vinilo/cancion_vinilo_list.html", {"relaciones": relaciones})

def cancion_vinilo_create(request):
    canciones = Cancion.objects.all()
    vinilos = Vinilo.objects.all()

    if request.method == "POST":
        CancionVinilo.objects.create(
            id_cancion_id=request.POST["id_cancion"],
            id_vinilo_id=request.POST["id_vinilo"]
        )
        return redirect("cancion_vinilo_list")
    return render(request, "cancion_vinilo/cancion_vinilo_form.html", {"canciones": canciones, "vinilos": vinilos})

def cancion_vinilo_update(request, id):
    relacion = get_object_or_404(CancionVinilo, id=id)
    canciones = Cancion.objects.all()
    vinilos = Vinilo.objects.all()

    if request.method == "POST":
        relacion.id_cancion_id = request.POST["id_cancion"]
        relacion.id_vinilo_id = request.POST["id_vinilo"]
        relacion.save()
        return redirect("cancion_vinilo_list")
    return render(
        request,
        "cancion_vinilo/cancion_vinilo_form.html",
        {"relacion": relacion, "canciones": canciones, "vinilos": vinilos}
    )

def cancion_vinilo_delete(request, id):
    relacion = get_object_or_404(CancionVinilo, id=id)
    relacion.delete()
    return redirect("cancion_vinilo_list")

# -------------------------
# VALORACIONES
# -------------------------
def valoraciones_list(request):
    valoraciones = Valoracion.objects.select_related("id_producto", "id_usuario").all()
    return render(request, "valoraciones/valoraciones_list.html", {"valoraciones": valoraciones})

def valoraciones_create(request):
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        Valoracion.objects.create(
            puntuacion=request.POST["puntuacion"],
            comentario=request.POST["comentario"],
            id_producto_id=request.POST["id_producto"],
            id_usuario_id=request.POST["id_usuario"],
        )
        return redirect("valoraciones_list")
    return render(
        request,
        "valoraciones/valoraciones_form.html",
        {"productos": productos, "usuarios": usuarios}
    )

def valoraciones_update(request, id_valoracion):
    valoracion = get_object_or_404(Valoracion, id_valoracion=id_valoracion)
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        valoracion.puntuacion = request.POST["puntuacion"]
        valoracion.comentario = request.POST["comentario"]
        valoracion.id_producto_id = request.POST["id_producto"]
        valoracion.id_usuario_id = request.POST["id_usuario"]
        valoracion.save()
        return redirect("valoraciones_list")
    return render(
        request,
        "valoraciones/valoraciones_form.html",
        {
            "valoracion": valoracion,
            "productos": productos,
            "usuarios": usuarios
        }
    )

def valoraciones_delete(request, id_valoracion):
    valoracion = get_object_or_404(Valoracion, id_valoracion=id_valoracion)
    valoracion.delete()
    return redirect("valoraciones_list")

# -------------------------
# CANCION – RECOPILACION
# -------------------------
def cancion_recopilacion_list(request):
    relaciones = (
        CancionRecopilacion.objects
        .select_related("id_cancion", "id_recopilacion")
        .all()
    )
    return render(
        request,
        "cancion_recopilacion/cancion_recopilacion_list.html",
        {"relaciones": relaciones}
    )

def cancion_recopilacion_create(request):
    canciones = Cancion.objects.all()
    recopilaciones = Recopilacion.objects.all()

    if request.method == "POST":
        CancionRecopilacion.objects.create(
            id_cancion_id=request.POST["id_cancion"],
            id_recopilacion_id=request.POST["id_recopilacion"],
        )
        return redirect("cancion_recopilacion_list")
    return render(
        request,
        "cancion_recopilacion/cancion_recopilacion_form.html",
        {"canciones": canciones, "recopilaciones": recopilaciones}
    )

def cancion_recopilacion_update(request, id):
    relacion = get_object_or_404(CancionRecopilacion, id=id)
    canciones = Cancion.objects.all()
    recopilaciones = Recopilacion.objects.all()

    if request.method == "POST":
        relacion.id_cancion_id = request.POST["id_cancion"]
        relacion.id_recopilacion_id = request.POST["id_recopilacion"]
        relacion.save()
        return redirect("cancion_recopilacion_list")
    return render(
        request,
        "cancion_recopilacion/cancion_recopilacion_form.html",
        {
            "relacion": relacion,
            "canciones": canciones,
            "recopilaciones": recopilaciones
        }
    )

def cancion_recopilacion_delete(request, id):
    relacion = get_object_or_404(CancionRecopilacion, id=id)
    relacion.delete()
    return redirect("cancion_recopilacion_list")