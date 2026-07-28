from django.core.management.base import BaseCommand

from core.models import (
    TablaCompetencia,
    TablaTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Genera tabla acumulada de la temporada"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            activa=True
        )

        TablaTemporada.objects.filter(
            temporada=temporada
        ).delete()

        participantes = {}

        tablas = TablaCompetencia.objects.filter(
            competencia__temporada=temporada,
            competencia__plantilla__tipo_general="LIGA",
        )

        for tabla in tablas:

            participante = tabla.participante_temporada

            if participante.id not in participantes:

                participantes[participante.id] = {
                    "participante": participante,
                    "pj": 0,
                    "pg": 0,
                    "pe": 0,
                    "pp": 0,
                    "puntos": 0,
                    "af": 0,
                    "av": 0,
                }

            participantes[participante.id]["pj"] += tabla.pj
            participantes[participante.id]["pg"] += tabla.pg
            participantes[participante.id]["pe"] += tabla.pe
            participantes[participante.id]["pp"] += tabla.pp
            participantes[participante.id]["puntos"] += tabla.puntos
            participantes[participante.id]["af"] += tabla.af
            participantes[participante.id]["av"] += tabla.av

        creados = 0

        for datos in participantes.values():

            TablaTemporada.objects.create(
                participante_temporada=
                datos["participante"],

                temporada=temporada,

                pj=datos["pj"],
                pg=datos["pg"],
                pe=datos["pe"],
                pp=datos["pp"],

                puntos=datos["puntos"],

                af=datos["af"],
                av=datos["av"],
            )

            creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Registros creados: {creados}"
            )
        )