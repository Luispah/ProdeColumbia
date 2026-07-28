from django.core.management.base import BaseCommand

from core.models import (
    Enfrentamiento,
    InstanciaCompetencia,
    Participante,
    ParticipanteTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = "Genera un enfrentamiento de prueba"

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            anio=2026
        )

        instancia = InstanciaCompetencia.objects.get(
            competencia__nombre="Liga Profesional Clausura 2026",
            nombre="Fecha 1"
        )

        local = ParticipanteTemporada.objects.get(
            participante__nombre="Pablo Camporini",
            temporada=temporada,
        )

        visitante = ParticipanteTemporada.objects.exclude(
            participante__nombre="Pablo Camporini"
        ).filter(
            temporada=temporada
        ).order_by("participante__nombre").first()

        enfrentamiento, creado = (
            Enfrentamiento.objects.get_or_create(
                instancia=instancia,
                participante_local=local,
                participante_visitante=visitante,
            )
        )

        mensaje = (
            "Enfrentamiento creado"
            if creado
            else
            "Enfrentamiento ya existente"
        )

        self.stdout.write(
            self.style.SUCCESS(mensaje)
        )

        self.stdout.write(
            f"Local: {local}"
        )

        self.stdout.write(
            f"Visitante: {visitante}"
        )