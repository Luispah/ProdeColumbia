from django.core.management.base import BaseCommand

from core.models import (
    InstanciaCompetencia,
    ParticipanteTemporada,
    ResumenParticipanteInstancia,
    ResultadoPronostico,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Genera resumenes de Fecha 1 "
        "para todos los participantes"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        instancia = InstanciaCompetencia.objects.get(
            competencia__nombre=
            "Liga Profesional Clausura 2026",
            nombre="Fecha 1",
        )

        participantes = (
            ParticipanteTemporada.objects.filter(
                temporada=temporada,
                activo=True,
            )
        )

        generados = 0

        for participante in participantes:

            resultados = (
                ResultadoPronostico.objects.filter(
                    pronostico__participante_temporada=
                    participante,
                    pronostico__instancia_partido__instancia=
                    instancia,
                )
            )

            partidos_evaluados = resultados.count()

            af = 0
            av = 0

            for resultado in resultados:

                if resultado.acierto:

                    af += 1

                    if resultado.resultado_real == "V":
                        av += 1

            resumen, _ = (
                ResumenParticipanteInstancia.objects.update_or_create(
                    participante_temporada=participante,
                    instancia=instancia,
                    defaults={
                        "partidos_evaluados":
                        partidos_evaluados,
                        "af":
                        af,
                        "av":
                        av,
                        "puntos":
                        af,
                    }
                )
            )

            generados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Resumenes generados: {generados}"
            )
        )