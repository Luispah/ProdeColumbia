from django.core.management.base import BaseCommand

from core.models import (
    Enfrentamiento,
    TablaInstancia,
)


class Command(BaseCommand):

    help = (
        "Genera tablas de todas las instancias"
    )

    def handle(self, *args, **kwargs):

        TablaInstancia.objects.all().delete()

        creados = 0

        for enfrentamiento in Enfrentamiento.objects.all():

            TablaInstancia.objects.create(
                participante_temporada=
                enfrentamiento.participante_local,

                instancia=
                enfrentamiento.instancia,

                pj=1,

                pg=1 if enfrentamiento.resultado == "LOCAL" else 0,

                pe=1 if enfrentamiento.resultado == "EMPATE" else 0,

                pp=1 if enfrentamiento.resultado == "VISITANTE" else 0,

                puntos=enfrentamiento.puntos_local,

                af=enfrentamiento.af_local,

                av=enfrentamiento.av_local,
            )

            creados += 1

            TablaInstancia.objects.create(
                participante_temporada=
                enfrentamiento.participante_visitante,

                instancia=
                enfrentamiento.instancia,

                pj=1,

                pg=1 if enfrentamiento.resultado == "VISITANTE" else 0,

                pe=1 if enfrentamiento.resultado == "EMPATE" else 0,

                pp=1 if enfrentamiento.resultado == "LOCAL" else 0,

                puntos=enfrentamiento.puntos_visitante,

                af=enfrentamiento.af_visitante,

                av=enfrentamiento.av_visitante,
            )

            creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Registros creados: {creados}"
            )
        )