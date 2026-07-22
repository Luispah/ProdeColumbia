from django.core.management.base import BaseCommand

from core.models import PartidoReal


class Command(BaseCommand):

    help = "Carga resultados ficticios para la Fecha 1"

    def handle(self, *args, **kwargs):

        resultados = {
            "Deportivo Riestra vs Boca": (0, 2),
            "Estudiantes vs Independiente": (1, 1),
            "Newell's vs Talleres": (2, 0),
            "Vélez vs Instituto": (1, 0),
            "Platense vs Unión": (0, 0),
        }

        actualizados = 0

        for partido in PartidoReal.objects.all():

            clave = (
                f"{partido.equipo_local} "
                f"vs "
                f"{partido.equipo_visitante}"
            )

            if clave in resultados:

                goles_local, goles_visitante = resultados[clave]

                partido.goles_local = goles_local
                partido.goles_visitante = goles_visitante
                partido.estado = "JUGADO"
                partido.save()

                actualizados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Partidos actualizados: {actualizados}"
            )
        )