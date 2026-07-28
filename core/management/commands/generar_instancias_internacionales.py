from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    InstanciaCompetencia,
)


class Command(BaseCommand):

    help = (
        "Genera instancias para copas internacionales"
    )

    def handle(self, *args, **kwargs):

        total = 0

        competencias = Competencia.objects.filter(
            nombre__in=[
                "Copa Libertadores 2026",
                "Copa Sudamericana 2026",
            ]
        )

        for competencia in competencias:

            orden = 10

            for grupo in [
                "Grupo A",
                "Grupo B",
                "Grupo C",
                "Grupo D",
                "Grupo E",
                "Grupo F",
            ]:

                _, creada = (
                    InstanciaCompetencia.objects.get_or_create(
                        competencia=competencia,
                        nombre=grupo,
                        defaults={
                            "tipo": "RONDA",
                            "orden": orden,
                        }
                    )
                )

                if creada:
                    total += 1

                orden += 10

            for nombre, tipo in [
                ("Octavos", "PLAYOFF"),
                ("Cuartos", "PLAYOFF"),
                ("Semifinal", "PLAYOFF"),
                ("Final", "FINAL"),
            ]:

                _, creada = (
                    InstanciaCompetencia.objects.get_or_create(
                        competencia=competencia,
                        nombre=nombre,
                        defaults={
                            "tipo": tipo,
                            "orden": orden,
                        }
                    )
                )

                if creada:
                    total += 1

                orden += 10

        self.stdout.write(
            self.style.SUCCESS(
                f"Instancias creadas: {total}"
            )
        )