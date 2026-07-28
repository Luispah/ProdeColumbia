from django.core.management.base import BaseCommand

from core.models import (
    ClasificacionGrupo,
    GrupoCompetencia,
    TablaGrupo,
)


class Command(BaseCommand):

    help = (
        "Calcula clasificaciones de grupos"
    )

    def handle(self, *args, **kwargs):

        ClasificacionGrupo.objects.all().delete()

        grupos = GrupoCompetencia.objects.all()

        creados = 0

        for grupo in grupos:

            tablas = (
                TablaGrupo.objects.filter(
                    grupo=grupo
                )
                .order_by(
                    "posicion"
                )
            )

            for tabla in tablas:

                resultado = "ELIMINADO"

                if tabla.posicion <= 2:

                    resultado = "CLASIFICADO"

                ClasificacionGrupo.objects.create(
                    grupo=grupo,
                    participante_temporada=
                    tabla.participante_temporada,
                    posicion=tabla.posicion,
                    resultado=resultado,
                )

                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Clasificaciones generadas: "
                f"{creados}"
            )
        )