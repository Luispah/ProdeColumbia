from django.core.management.base import BaseCommand

from core.models import (
    Pronostico,
    ResultadoPronostico,
)


class Command(BaseCommand):

    help = "Genera resultados de pronósticos"

    def obtener_resultado_real(self, partido):

        if partido.goles_local > partido.goles_visitante:
            return "L"

        if partido.goles_local < partido.goles_visitante:
            return "V"

        return "E"

    def handle(self, *args, **kwargs):

        creados = 0

        pronosticos = Pronostico.objects.filter(
            instancia_partido__partido__estado="JUGADO"
        )

        for pronostico in pronosticos:

            partido = pronostico.instancia_partido.partido

            resultado_real = self.obtener_resultado_real(
                partido
            )

            acierto = (
                pronostico.resultado == resultado_real
            )

            puntos = 1 if acierto else 0

            _, creado = (
                ResultadoPronostico.objects.update_or_create(
                    pronostico=pronostico,
                    defaults={
                        "resultado_real": resultado_real,
                        "acierto": acierto,
                        "puntos": puntos,
                    }
                )
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Resultados generados: {creados}"
            )
        )