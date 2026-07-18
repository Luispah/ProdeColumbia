from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    orden = models.IntegerField(
        default=0
    )

    activa = models.BooleanField(
        default=True
    )

    color = models.CharField(
        max_length=20,
        default="#FFFFFF"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["orden"]

class Temporada(models.Model):

    anio = models.IntegerField(
        unique=True
    )

    activa = models.BooleanField(
        default=False
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.anio)

    class Meta:
        ordering = ["-anio"]

class Torneo(models.Model):

    TIPOS = [
        ("APERTURA", "Apertura"),
        ("CLAUSURA", "Clausura"),
        ("COPA_ARG", "Copa Argentina"),
        ("SUPERCOPA", "Supercopa"),
    ]

    nombre = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

class Participante(models.Model):

    CATEGORIAS = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
    ]

    id_externo = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIAS
    )

    activo = models.BooleanField(
        default=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    club_hincha = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    club_simpatizante = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    administrador = models.BooleanField(
        default=False
    )

    fecha_alta = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre