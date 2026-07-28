from django.core.management.base import BaseCommand

from core.models import (
    ParticipacionGrupo,
    TablaGrupo,
)


class Command(BaseCommand):

    help = (
        "Genera tablas de todos los grupos"
    )

    def handle(self, *args, **kwargs):

        TablaGrupo.objects.all().delete()

        grupos = {}

        participaciones = (
            ParticipacionGrupo.objects.select_related(
                "grupo",
                "participante_temporada",
            )
        )

        for participacion in participaciones:

            grupo = participacion.grupo

            if grupo.id not in grupos:

                grupos[grupo.id] = []

            grupos[grupo.id].append(participacion)

        creados = 0

        for grupo_id, participantes in grupos.items():

            posicion = 1

            participantes = sorted(
                participantes,
                key=lambda p:
                p.participante_temporada.participante.nombre
            )

            for participacion in participantes:

                TablaGrupo.objects.create(
                    grupo=participacion.grupo,
                    participante_temporada=
                    participacion.participante_temporada,
                    posicion=posicion,
                    pj=0,
                    pg=0,
                    pe=0,
                    pp=0,
                    puntos=0,
                    af=0,
                    av=0,
                )

                posicion += 1
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Registros creados: {creados}"
            )
        )