from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    Enfrentamiento,
    InstanciaCompetencia,
    ParticipanteTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Genera enfrentamientos para todas las "
        "instancias de tipo FECHA"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        instancias = InstanciaCompetencia.objects.filter(
            competencia__nombre="Liga Profesional Clausura 2026",
            tipo="FECHA",
        ).order_by("orden")

        total_creados = 0

        for instancia in instancias:

            Enfrentamiento.objects.filter(
                instancia=instancia
            ).delete()

            for categoria_nombre in ["A", "B", "C"]:

                categoria = Categoria.objects.get(
                    nombre=categoria_nombre
                )

                participantes = list(
                    ParticipanteTemporada.objects.filter(
                        temporada=temporada,
                        categoria=categoria,
                        activo=True,
                    ).order_by(
                        "participante__nombre"
                    )
                )

                for i in range(
                    0,
                    len(participantes),
                    2
                ):

                    if i + 1 >= len(participantes):
                        break

                    Enfrentamiento.objects.create(
                        instancia=instancia,
                        participante_local=
                        participantes[i],
                        participante_visitante=
                        participantes[i + 1],
                    )

                    total_creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Enfrentamientos creados: "
                f"{total_creados}"
            )
        )