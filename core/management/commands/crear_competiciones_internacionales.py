from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    CompetenciaConfig,
    PlantillaCompetencia,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Crea Libertadores y Sudamericana"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        plantilla_copa = (
            PlantillaCompetencia.objects.filter(
                tipo_general="COPA"
            ).first()
        )

        if plantilla_copa is None:

            self.stdout.write(
                self.style.ERROR(
                    "No existe una plantilla tipo COPA"
                )
            )

            return

        competencias = [
            "Copa Libertadores 2026",
            "Copa Sudamericana 2026",
        ]

        creadas = 0

        for nombre in competencias:

            competencia, creada = (
                Competencia.objects.get_or_create(
                    nombre=nombre,
                    defaults={
                        "temporada": temporada,
                        "plantilla": plantilla_copa,
                        "activa": True,
                    }
                )
            )

            CompetenciaConfig.objects.get_or_create(
                competencia=competencia,
                defaults={
                    "cantidad_participantes": 16,
                    "cantidad_zonas": 4,
                    "clasificados": 8,
                    "cantidad_partidos_boleta": 15,
                    "usa_tabla": True,
                    "usa_af": True,
                    "usa_av": True,
                    "usa_da": True,
                }
            )

            if creada:
                creadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Competencias creadas: {creadas}"
            )
        )