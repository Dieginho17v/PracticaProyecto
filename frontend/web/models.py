from django.db import models

# Modelo que representa a un usuario del sistema
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=100)  # Nombre del usuario
    email = models.EmailField()  # Correo electrónico del usuario
    contrasena = models.CharField(max_length=200)  # Contraseña almacenada

    class Meta:
        db_table = 'Usuario'  # Nombre de la tabla en la base de datos

# Modelo para representar un disco MP3
class DiscoMP3(models.Model):
    id_disco = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=200)  # Nombre del disco
    genero = models.CharField(max_length=100)  # Género musical
    imagen_portada = models.BinaryField(null=True, blank=True)  # Imagen en binario

    class Meta:
        db_table = 'DiscoMP3'

    def __str__(self):
        return self.nombre  # Representación del objeto

# Modelo para representar una canción
class Cancion(models.Model):
    id_cancion = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=200)  # Nombre de la canción
    duracion = models.CharField(max_length=10)  # Duración en formato texto
    tamaño_mb = models.IntegerField()  # Tamaño en MB
    calidad_kbps = models.IntegerField()  # Calidad de audio en kbps
    audio_blob = models.BinaryField()  # Archivo de audio en binario
    id_disco = models.ForeignKey(DiscoMP3, on_delete=models.CASCADE, db_column="id_disco")  # Relación con DiscoMP3

    class Meta:
        db_table = 'Cancion'

    def __str__(self):
        return self.nombre

# Modelo para representar un vinilo
class Vinilo(models.Model):
    id_vinilo = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=255)  # Nombre del vinilo
    rpm = models.IntegerField()  # Revoluciones por minuto
    imagen_caratula = models.TextField(null=True, blank=True)  # Imagen en base64 u otro texto

    class Meta:
        db_table = "Vinilo"

# Modelo para representar una recopilación de canciones
class Recopilacion(models.Model):
    id_recopilacion = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=255)  # Nombre de la recopilación
    descripcion = models.TextField()  # Descripción
    imagen_caratula = models.TextField(null=True, blank=True)  # Imagen de portada

    class Meta:
        db_table = "Recopilacion"

# Modelo general de Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=255)  # Nombre del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    tipo = models.CharField(max_length=100)  # Tipo de producto (MP3, Vinilo, etc.)
    id_ref = models.IntegerField()  # ID referencial al objeto real

    class Meta:
        db_table = "Producto"

    def __str__(self):
        return self.nombre

# Modelo para representar un pedido realizado por un usuario
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)  # ID autoincremental
    fecha = models.DateField()  # Fecha del pedido
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total del pedido
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')  # Relación con Usuario

    class Meta:
        db_table = "Pedido"

    def __str__(self):
        return f"Pedido #{self.id_pedido}"

# Relación muchos a muchos entre Cancion y Vinilo
class CancionVinilo(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, db_column='id_cancion')  # Canción asociada
    id_vinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE, db_column='id_vinilo')  # Vinilo asociado

    class Meta:
        db_table = "CancionVinilo"

    def __str__(self):
        return f"{self.id_cancion.nombre} → {self.id_vinilo.nombre}"

# Modelo de valoraciones para productos
class Valoracion(models.Model):
    id_valoracion = models.AutoField(primary_key=True)  # ID autoincremental
    puntuacion = models.IntegerField()  # Puntuación numérica
    comentario = models.TextField(null=True, blank=True)  # Comentario opcional
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column="id_producto")  # Producto valorado
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="id_usuario")  # Usuario que valora

    class Meta:
        db_table = "Valoracion"

# Relación muchos a muchos entre Cancion y Recopilacion
class CancionRecopilacion(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, db_column="id_cancion")  # Canción
    id_recopilacion = models.ForeignKey(Recopilacion, on_delete=models.CASCADE, db_column="id_recopilacion")  # Recopilación

    class Meta:
        db_table = "CancionRecopilacion"