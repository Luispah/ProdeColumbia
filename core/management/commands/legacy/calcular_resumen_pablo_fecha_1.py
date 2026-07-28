from django.core.management.base import BaseCommand

from core.models import (
    Participante,
    ParticipanteTemporada,
    ResultadoPronostico,
    Temporada,
)


class Command(BaseCommand):

    help = "Calcula resumen de Pablo para Fecha 1"

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

        resultados = ResultadoPronostico.objects.filter(
            pronostico__participante_temporada=participante_temporada,
            pronostico__instancia_partido__instancia__nombre="Fecha 1",
            pronostico__instancia_partido__instancia__competencia__nombre="Liga Profesional Clausura 2026",
        )

        af = 0
        av = 0

        for resultado in resultados:

            if resultado.acierto:

                af += 1

                if resultado.resultado_real == "V":
                    av += 1

        self.stdout.write("")
        self.stdout.write("RESUMEN FECHA 1")
        self.stdout.write("--------------------")
        self.stdout.write(
            f"Participante: {participante.nombre}"
        )
        self.stdout.write(
            f"Resultados evaluados: {resultados.count()}"
        )
        self.stdout.write(
            f"AF: {af}"
        )
        self.stdout.write(
            f"AV: {av}"
        )
        self.stdout.write("")