from django.urls import path
from . import views

urlpatterns = [
    # INDEX
    path("", views.index, name="index"),

    # USUARIOS
    path("usuarios/", views.usuarios_list, name="usuarios_list"),
    path("usuarios/crear/", views.usuarios_create, name="usuarios_create"),
    path("usuarios/editar/<int:id_usuario>/", views.usuarios_update, name="usuarios_update"),
    path("usuarios/eliminar/<int:id_usuario>/", views.usuarios_delete, name="usuarios_delete"),

    # DISCOS MP3
    path("discos/", views.discos_list, name="discos_list"),
    path("discos/crear/", views.discos_create, name="discos_create"),
    path("discos/editar/<int:id_disco>/", views.discos_update, name="discos_update"),
    path("discos/eliminar/<int:id_disco>/", views.discos_delete, name="discos_delete"),

    # CANCIONES
    path("canciones/", views.canciones_list, name="canciones_list"),
    path("canciones/crear/", views.canciones_create, name="canciones_create"),
    path("canciones/editar/<int:id_cancion>/", views.canciones_update, name="canciones_update"),
    path("canciones/eliminar/<int:id_cancion>/", views.canciones_delete, name="canciones_delete"),
    
    # VINILOS
    path("vinilos/", views.vinilos_list, name="vinilos_list"),
    path("vinilos/crear/", views.vinilos_create, name="vinilos_create"),
    path("vinilos/editar/<int:id_vinilo>/", views.vinilos_update, name="vinilos_update"),
    path("vinilos/eliminar/<int:id_vinilo>/", views.vinilos_delete, name="vinilos_delete"),
    
    # RECOPILACIONES
    path("recopilaciones/", views.recopilaciones_list, name="recopilaciones_list"),
    path("recopilaciones/crear/", views.recopilaciones_create, name="recopilaciones_create"),
    path("recopilaciones/editar/<int:id_recopilacion>/", views.recopilaciones_update, name="recopilaciones_update"),
    path("recopilaciones/eliminar/<int:id_recopilacion>/", views.recopilaciones_delete, name="recopilaciones_delete"),
    
    # PRODUCTOS
    path("productos/", views.productos_list, name="productos_list"),
    path("productos/crear/", views.productos_create, name="productos_create"),
    path("productos/editar/<int:id_producto>/", views.productos_update, name="productos_update"),
    path("productos/eliminar/<int:id_producto>/", views.productos_delete, name="productos_delete"),

    # PEDIDOS
    path("pedidos/", views.pedidos_list, name="pedidos_list"),
    path("pedidos/crear/", views.pedidos_create, name="pedidos_create"),
    path("pedidos/editar/<int:id_pedido>/", views.pedidos_update, name="pedidos_update"),
    path("pedidos/eliminar/<int:id_pedido>/", views.pedidos_delete, name="pedidos_delete"),

    # CANCION-VINILO
    path("cancion-vinilo/", views.cancion_vinilo_list, name="cancion_vinilo_list"),
    path("cancion-vinilo/crear/", views.cancion_vinilo_create, name="cancion_vinilo_create"),
    path("cancion-vinilo/editar/<int:id>/", views.cancion_vinilo_update, name="cancion_vinilo_update"),
    path("cancion-vinilo/eliminar/<int:id>/", views.cancion_vinilo_delete, name="cancion_vinilo_delete"),

    # VALORACIONES
    path("valoraciones/", views.valoraciones_list, name="valoraciones_list"),
    path("valoraciones/crear/", views.valoraciones_create, name="valoraciones_create"),
    path("valoraciones/editar/<int:id_valoracion>/", views.valoraciones_update, name="valoraciones_update"),
    path("valoraciones/eliminar/<int:id_valoracion>/", views.valoraciones_delete, name="valoraciones_delete"),

    # CANCION – RECOPILACION
    path("cancion-recopilacion/", views.cancion_recopilacion_list, name="cancion_recopilacion_list"),
    path("cancion-recopilacion/crear/", views.cancion_recopilacion_create, name="cancion_recopilacion_create"),
    path("cancion-recopilacion/editar/<int:id>/", views.cancion_recopilacion_update, name="cancion_recopilacion_update"),
    path("cancion-recopilacion/eliminar/<int:id>/", views.cancion_recopilacion_delete, name="cancion_recopilacion_delete"),

]