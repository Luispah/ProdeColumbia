from django.core.management.base import BaseCommand

from core.models import Enfrentamiento


class Command(BaseCommand):

    help = (
        "Resuelve enfrentamientos de todas las instancias"
    )

    def handle(self, *args, **kwargs):

        procesados = 0

        enfrentamientos = Enfrentamiento.objects.all()

        for enfrentamiento in enfrentamientos:

            if enfrentamiento.af_local > enfrentamiento.af_visitante:

                enfrentamiento.resultado = "LOCAL"
                enfrentamiento.puntos_local = 3
                enfrentamiento.puntos_visitante = 0

            elif enfrentamiento.af_local < enfrentamiento.af_visitante:

                enfrentamiento.resultado = "VISITANTE"
                enfrentamiento.puntos_local = 0
                enfrentamiento.puntos_visitante = 3

            else:

                enfrentamiento.resultado = "EMPATE"
                enfrentamiento.puntos_local = 1
                enfrentamiento.puntos_visitante = 1

            enfrentamiento.estado = "FINALIZADO"

            enfrentamiento.save()

            procesados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Enfrentamientos procesados: {procesados}"
            )
        )