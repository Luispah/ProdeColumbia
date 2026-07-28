from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    ParticipacionCompetencia,
    ResultadoTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Genera clasificaciones para competencias"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        libertadores = Competencia.objects.filter(
            nombre__icontains="Libertadores"
        ).first()

        sudamericana = Competencia.objects.filter(
            nombre__icontains="Sudamericana"
        ).first()

        creados = 0

        resultados = ResultadoTemporada.objects.filter(
            temporada=temporada
        )

        for resultado in resultados:

            competencia = None

            if resultado.resultado == "LIBERTADORES":
                competencia = libertadores

            elif resultado.resultado == "SUDAMERICANA":
                competencia = sudamericana

            if competencia is None:
                continue

            ParticipacionCompetencia.objects.get_or_create(
                participante_temporada=
                resultado.participante_temporada,

                competencia=competencia,

                defaults={
                    "estado": "INSCRIPTO"
                }
            )

            creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Clasificaciones generadas: "
                f"{creados}"
            )
        )