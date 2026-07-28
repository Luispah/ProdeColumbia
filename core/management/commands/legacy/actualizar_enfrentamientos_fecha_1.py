from django.core.management.base import BaseCommand

from core.models import (
    Enfrentamiento,
    ResumenParticipanteInstancia,
)


class Command(BaseCommand):

    help = "Actualiza AF y AV de los enfrentamientos"

    def handle(self, *args, **kwargs):

        actualizados = 0

        for enfrentamiento in Enfrentamiento.objects.all():

            resumen_local = (
                ResumenParticipanteInstancia.objects.filter(
                    participante_temporada=
                    enfrentamiento.participante_local,
                    instancia=enfrentamiento.instancia,
                ).first()
            )

            resumen_visitante = (
                ResumenParticipanteInstancia.objects.filter(
                    participante_temporada=
                    enfrentamiento.participante_visitante,
                    instancia=enfrentamiento.instancia,
                ).first()
            )

            if resumen_local:

                enfrentamiento.af_local = (
                    resumen_local.af
                )

                enfrentamiento.av_local = (
                    resumen_local.av
                )

            if resumen_visitante:

                enfrentamiento.af_visitante = (
                    resumen_visitante.af
                )

                enfrentamiento.av_visitante = (
                    resumen_visitante.av
                )

            enfrentamiento.save()

            actualizados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Enfrentamientos actualizados: "
                f"{actualizados}"
            )
        )