from django.core.management.base import BaseCommand

from core.models import (
    Participante,
    ParticipanteTemporada,
    ResumenParticipanteInstancia,
    ResultadoPronostico,
    Temporada,
    InstanciaCompetencia,
)


class Command(BaseCommand):

    help = "Genera resumenes de la Fecha 1"

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

        instancia = InstanciaCompetencia.objects.get(
            competencia__nombre="Liga Profesional Clausura 2026",
            nombre="Fecha 1"
        )

        resultados = ResultadoPronostico.objects.filter(
            pronostico__participante_temporada=participante_temporada,
            pronostico__instancia_partido__instancia=instancia,
        )

        partidos_evaluados = resultados.count()

        af = 0
        av = 0

        for resultado in resultados:

            if resultado.acierto:

                af += 1

                if resultado.resultado_real == "V":
                    av += 1

        puntos = af

        resumen, _ = (
            ResumenParticipanteInstancia.objects.update_or_create(
                participante_temporada=participante_temporada,
                instancia=instancia,
                defaults={
                    "partidos_evaluados": partidos_evaluados,
                    "af": af,
                    "av": av,
                    "puntos": puntos,
                }
            )
        )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Resumen generado correctamente"
            )
        )

        self.stdout.write(
            f"Partidos evaluados: {resumen.partidos_evaluados}"
        )

        self.stdout.write(
            f"AF: {resumen.af}"
        )

        self.stdout.write(
            f"AV: {resumen.av}"
        )

        self.stdout.write(
            f"Puntos: {resumen.puntos}"
        )

        self.stdout.write("")