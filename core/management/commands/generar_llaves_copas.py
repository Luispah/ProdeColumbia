from django.core.management.base import BaseCommand

from core.models import (
    ClasificacionGrupo,
    Competencia,
    LlaveCompetencia,
)


class Command(BaseCommand):

    help = (
        "Genera llaves de octavos para las copas"
    )

    def handle(self, *args, **kwargs):

        LlaveCompetencia.objects.all().delete()

        competencias = Competencia.objects.filter(
            nombre__icontains="Copa "
        ).exclude(
            nombre__icontains="Argentina"
        ).exclude(
            nombre__icontains="Repechaje"
        ).exclude(
            nombre__icontains="Supercopa"
        )

        creadas = 0

        for competencia in competencias:

            clasificados = list(
                ClasificacionGrupo.objects.filter(
                    grupo__competencia=competencia,
                    resultado="CLASIFICADO",
                ).order_by(
                    "grupo__orden",
                    "posicion",
                )
            )

            for i in range(
                0,
                len(clasificados),
                2
            ):

                if i + 1 >= len(clasificados):
                    break

                LlaveCompetencia.objects.create(
                    competencia=competencia,
                    etapa="OCTAVOS",
                    orden=(i // 2) + 1,
                    participante_1=
                    clasificados[i]
                    .participante_temporada,
                    participante_2=
                    clasificados[i + 1]
                    .participante_temporada,
                )

                creadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Llaves creadas: {creadas}"
            )
        )