from django.core.management.base import BaseCommand

from core.models import (
    InstanciaCompetencia,
    LlaveCompetencia,
)


class Command(BaseCommand):

    help = (
        "Vincula cada llave con su instancia"
    )

    MAPA = {
        "OCTAVOS": "Octavos",
        "CUARTOS": "Cuartos",
        "SEMIFINAL": "Semifinal",
        "FINAL": "Final",
    }

    def handle(self, *args, **kwargs):

        actualizadas = 0

        for llave in LlaveCompetencia.objects.all():

            nombre_instancia = self.MAPA.get(
                llave.etapa
            )

            if nombre_instancia is None:
                continue

            try:

                instancia = (
                    InstanciaCompetencia.objects.get(
                        competencia=llave.competencia,
                        nombre=nombre_instancia,
                    )
                )

            except InstanciaCompetencia.DoesNotExist:
                continue

            llave.instancia = instancia
            llave.save()

            actualizadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Llaves vinculadas: {actualizadas}"
            )
        )