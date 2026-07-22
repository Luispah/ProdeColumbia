from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    Participante,
    ParticipanteTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = "Genera registros ParticipanteTemporada"

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        creados = 0

        for participante in Participante.objects.all():

            categoria = Categoria.objects.get(
                nombre=participante.categoria
            )

            _, creado = ParticipanteTemporada.objects.get_or_create(
                participante=participante,
                temporada=temporada,
                defaults={
                    "categoria": categoria,
                    "activo": participante.activo,
                    "es_nuevo": False,
                },
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"ParticipantesTemporada creados: {creados}"
            )
        )