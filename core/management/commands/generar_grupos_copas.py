from django.core.management.base import BaseCommand

from core.models import (
    Competencia,
    GrupoCompetencia,
    ParticipacionCompetencia,
    ParticipacionGrupo,
)


class Command(BaseCommand):

    help = (
        "Genera grupos para competencias con zonas"
    )

    def handle(self, *args, **kwargs):

        competencias = Competencia.objects.filter(
            nombre__icontains="Copa "
        ).exclude(
            nombre__icontains="Argentina"
        ).exclude(
            nombre__icontains="Repechaje"
        ).exclude(
            nombre__icontains="Supercopa"
        )

        total_grupos = 0
        total_participaciones = 0

        for competencia in competencias:

            try:
                config = competencia.competenciaconfig
            except Competencia.DoesNotExist:
                continue
            except Exception:
                continue

            cantidad_zonas = config.cantidad_zonas

            if cantidad_zonas <= 0:
                self.stdout.write(
                    self.style.WARNING(
                        f"{competencia.nombre}: cantidad_zonas <= 0"
                    )
                )
                continue

            ParticipacionGrupo.objects.filter(
                grupo__competencia=competencia
            ).delete()

            GrupoCompetencia.objects.filter(
                competencia=competencia
            ).delete()

            grupos = []

            for i in range(cantidad_zonas):

                letra = chr(65 + i)

                grupo = GrupoCompetencia.objects.create(
                    competencia=competencia,
                    nombre=f"Grupo {letra}",
                    orden=i + 1,
                )

                grupos.append(grupo)
                total_grupos += 1

            participantes = list(
                ParticipacionCompetencia.objects.filter(
                    competencia=competencia
                ).order_by(
                    "participante_temporada__participante__nombre"
                )
            )

            for indice, participacion in enumerate(
                participantes
            ):

                grupo = grupos[
                    indice % cantidad_zonas
                ]

                ParticipacionGrupo.objects.create(
                    grupo=grupo,
                    participante_temporada=
                    participacion.participante_temporada,
                )

                total_participaciones += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f"{competencia.nombre}: "
                    f"{cantidad_zonas} grupos generados"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Grupos creados: {total_grupos}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Participaciones creadas: "
                f"{total_participaciones}"
            )
        )