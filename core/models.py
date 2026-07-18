from django.db import models


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