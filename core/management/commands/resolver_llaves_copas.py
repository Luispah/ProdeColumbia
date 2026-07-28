import random

from django.core.management.base import BaseCommand

from core.models import LlaveCompetencia


class Command(BaseCommand):

    help = (
        "Resuelve todas las llaves pendientes"
    )

    def handle(self, *args, **kwargs):

        llaves = LlaveCompetencia.objects.filter(
            resuelta=False
        )

        procesadas = 0

        for llave in llaves:

            ganador = random.choice([
                llave.participante_1,
                llave.participante_2,
            ])

            llave.ganador = ganador
            llave.resuelta = True
            llave.save()

            procesadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Llaves resueltas: {procesadas}"
            )
        )