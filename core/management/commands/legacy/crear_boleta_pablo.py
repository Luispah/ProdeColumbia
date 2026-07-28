from django.core.management.base import BaseCommand

from core.models import (
    Participante,
    ParticipanteTemporada,
    Pronostico,
    InstanciaPartido,
    Temporada,
)


class Command(BaseCommand):

    help = "Crea una boleta de prueba para Pablo"

    def handle(self, *args, **kwargs):

        participante = Participante.objects.get(
            nombre="Pablo Camporini"
        )

        temporada = Temporada.objects.get(
            anio=2026
        )

        participante_temporada = (
            ParticipanteTemporada.objects.get(
                participante=participante,
                temporada=temporada,
            )
        )

        instancias = (
            InstanciaPartido.objects.filter(
                instancia__nombre="Fecha 1",
                instancia__competencia__nombre="Liga Profesional Clausura 2026",
            ).order_by("orden")
        )

        creados = 0

        for instancia_partido in instancias:

            _, creado = Pronostico.objects.get_or_create(
                participante_temporada=participante_temporada,
                instancia_partido=instancia_partido,
                defaults={
                    "resultado": "L",
                }
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Pronosticos creados: {creados}"
            )
        )
