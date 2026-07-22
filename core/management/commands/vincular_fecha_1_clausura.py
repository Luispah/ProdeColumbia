from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    InstanciaCompetencia,
    InstanciaPartido,
    PartidoReal,
)


class Command(BaseCommand):

    help = "Vincula los partidos reales a la Fecha 1 del Clausura"

    def handle(self, *args, **kwargs):

        competencia = Competencia.objects.get(
            nombre="Liga Profesional Clausura 2026"
        )

        instancia = InstanciaCompetencia.objects.get(
            competencia=competencia,
            nombre="Fecha 1"
        )

        partidos = PartidoReal.objects.filter(
            calendario__nombre="Liga Profesional Clausura 2026 - Fecha 1"
        ).order_by("id")

        creados = 0
        orden = 1

        for partido in partidos:

            _, creado = InstanciaPartido.objects.get_or_create(
                instancia=instancia,
                partido=partido,
                defaults={
                    "puntua": True,
                    "es_penal": False,
                    "orden": orden,
                }
            )

            if creado:
                creados += 1

            orden += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"InstanciasPartido creadas: {creados}"
            )
        )