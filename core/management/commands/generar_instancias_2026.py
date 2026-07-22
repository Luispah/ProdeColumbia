from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    InstanciaCompetencia,
)


class Command(BaseCommand):

    help = "Genera instancias iniciales de las competencias 2026"

    def handle(self, *args, **kwargs):

        total = 0

        definiciones = {
            "Liga Profesional Clausura 2026": [
                ("Fecha 1", "FECHA"),
                ("Fecha 2", "FECHA"),
                ("Fecha 3", "FECHA"),
                ("Fecha 4", "FECHA"),
                ("Fecha 5", "FECHA"),
                ("Fecha 6", "FECHA"),
                ("Fecha 7", "FECHA"),
                ("Fecha 8", "FECHA"),
                ("Fecha 9", "FECHA"),
                ("Fecha 10", "FECHA"),
                ("Fecha 11", "FECHA"),
                ("Fecha 12", "FECHA"),
                ("Fecha 13", "FECHA"),
                ("Fecha 14", "FECHA"),
                ("Fecha 15", "FECHA"),
                ("Fecha 16", "FECHA"),
                ("Octavos de Final", "PLAYOFF"),
                ("Cuartos de Final", "PLAYOFF"),
                ("Semifinal", "PLAYOFF"),
                ("Final", "FINAL"),
            ],
            "Copa Repechaje 2026": [
                ("32avos de Final", "RONDA"),
                ("16avos de Final", "RONDA"),
                ("Octavos de Final", "RONDA"),
                ("Cuartos de Final", "RONDA"),
                ("Semifinal", "RONDA"),
                ("Final", "FINAL"),
            ],
            "Copa Argentina 2026": [
                ("Primera Fase", "RONDA"),
                ("32avos de Final", "RONDA"),
                ("16avos de Final", "RONDA"),
                ("Octavos de Final", "RONDA"),
                ("Cuartos de Final", "RONDA"),
                ("Semifinal", "RONDA"),
                ("Final", "FINAL"),
            ],
            "Supercopa 2026": [
                ("Fase Inicial", "ESPECIAL"),
                ("Ronda Ganadores", "ESPECIAL"),
                ("Ronda Perdedores", "ESPECIAL"),
                ("Semifinal", "PLAYOFF"),
                ("Final", "FINAL"),
            ],
        }

        for nombre_competencia, instancias in definiciones.items():

            competencia = Competencia.objects.get(
                nombre=nombre_competencia
            )

            orden = 10

            for nombre, tipo in instancias:

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