from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    TablaCompetencia,
    TablaInstancia,
)


class Command(BaseCommand):

    help = (
        "Genera tabla acumulada de la competencia"
    )

    def handle(self, *args, **kwargs):

        competencia = Competencia.objects.get(
            nombre="Liga Profesional Clausura 2026"
        )

        TablaCompetencia.objects.filter(
            competencia=competencia
        ).delete()

        participantes = {}

        tablas = TablaInstancia.objects.filter(
            instancia__competencia=competencia
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

            TablaCompetencia.objects.create(
                participante_temporada=datos["participante"],
                competencia=competencia,
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