from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    Enfrentamiento,
    InstanciaCompetencia,
    ParticipanteTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = "Genera enfrentamientos ficticios para Fecha 1"

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        instancia = InstanciaCompetencia.objects.get(
            competencia__nombre="Liga Profesional Clausura 2026",
            nombre="Fecha 1"
        )

        Enfrentamiento.objects.filter(
            instancia=instancia
        ).delete()

        creados = 0

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

                local = participantes[i]
                visitante = participantes[i + 1]

                Enfrentamiento.objects.create(
                    instancia=instancia,
                    participante_local=local,
                    participante_visitante=visitante,
                )

                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Enfrentamientos creados: {creados}"
            )
        )