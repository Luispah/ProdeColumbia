import random

from django.core.management.base import BaseCommand

from core.models import (
    InstanciaPartido,
    ParticipanteTemporada,
    Pronostico,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Genera pronosticos ficticios para todos "
        "los participantes de la temporada 2026"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        participantes = (
            ParticipanteTemporada.objects.filter(
                temporada=temporada,
                activo=True,
            )
        )

        partidos = (
            InstanciaPartido.objects.filter(
                instancia__competencia__nombre=
                "Liga Profesional Clausura 2026",
                instancia__nombre="Fecha 1",
            ).order_by("orden")
        )

        resultados = [
            "L",
            "E",
            "V",
        ]

        creados = 0

        for participante in participantes:

            for partido in partidos:

                _, creado = (
                    Pronostico.objects.get_or_create(
                        participante_temporada=
                        participante,
                        instancia_partido=partido,
                        defaults={
                            "resultado":
                            random.choice(resultados)
                        }
                    )
                )

                if creado:
                    creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Pronosticos creados: {creados}"
            )
        )