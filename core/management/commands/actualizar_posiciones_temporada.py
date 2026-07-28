from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    TablaTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Actualiza posiciones de la tabla temporada"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            activa=True
        )

        total_actualizados = 0

        for categoria in Categoria.objects.all():

            tablas = (
                TablaTemporada.objects.filter(
                    temporada=temporada,
                    participante_temporada__categoria=categoria,
                )
                .order_by(
                    "-puntos",
                    "-af",
                    "-av",
                )
            )

            posicion = 1

            for tabla in tablas:

                tabla.posicion = posicion
                tabla.save()

                posicion += 1
                total_actualizados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Posiciones actualizadas: "
                f"{total_actualizados}"
            )
        )