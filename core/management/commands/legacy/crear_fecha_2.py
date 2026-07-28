from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    InstanciaCompetencia,
)


class Command(BaseCommand):

    help = "Crea la Fecha 2 de la Liga Profesional Clausura 2026"

    def handle(self, *args, **kwargs):

        competencia = Competencia.objects.get(
            nombre="Liga Profesional Clausura 2026"
        )

        instancia, creada = (
            InstanciaCompetencia.objects.get_or_create(
                competencia=competencia,
                nombre="Fecha 2",
                defaults={
                    "tipo": "FECHA",
                    "orden": 2,
                }
            )
        )

        if creada:

            self.stdout.write(
                self.style.SUCCESS(
                    "Fecha 2 creada correctamente"
                )
            )

        else:

            self.stdout.write(
                self.style.WARNING(
                    "Fecha 2 ya existe"
                )
            )