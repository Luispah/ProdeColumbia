from django.core.management.base import BaseCommand

from core.models import EquipoReal


class Command(BaseCommand):

    help = "Agrega equipos faltantes"

    def handle(self, *args, **kwargs):

        equipos = [
            "Estudiantes (RC)",
            "Gimnasia (Mza)",
        ]

        creados = 0

        for nombre in equipos:

            _, creado = EquipoReal.objects.get_or_create(
                nombre=nombre
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Equipos creados: {creados}"
            )
        )