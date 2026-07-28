from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    LlaveCompetencia,
)


class Command(BaseCommand):

    help = (
        "Genera la siguiente ronda de playoffs"
    )

    ETAPAS = {
        "OCTAVOS": "CUARTOS",
        "CUARTOS": "SEMIFINAL",
        "SEMIFINAL": "FINAL",
    }

    def handle(self, *args, **kwargs):

        creadas = 0

        competencias = Competencia.objects.filter(
            nombre__icontains="Copa "
        )

        for competencia in competencias:

            for etapa_actual, etapa_siguiente in self.ETAPAS.items():

                llaves = list(
                    LlaveCompetencia.objects.filter(
                        competencia=competencia,
                        etapa=etapa_actual,
                        resuelta=True,
                    ).order_by("orden")
                )

                ya_existen = LlaveCompetencia.objects.filter(
                    competencia=competencia,
                    etapa=etapa_siguiente,
                ).exists()

                if ya_existen:
                    continue

                if len(llaves) < 2:
                    continue

                orden = 1

                for i in range(0, len(llaves), 2):

                    if i + 1 >= len(llaves):
                        break

                    LlaveCompetencia.objects.create(
                        competencia=competencia,
                        etapa=etapa_siguiente,
                        orden=orden,
                        participante_1=llaves[i].ganador,
                        participante_2=llaves[i + 1].ganador,
                    )

                    orden += 1
                    creadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Nuevas llaves: {creadas}"
            )
        )