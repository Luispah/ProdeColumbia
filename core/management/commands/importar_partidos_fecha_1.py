
from django.core.management.base import BaseCommand

from core.models import (
    CalendarioReal,
    EquipoReal,
    PartidoReal,
)


class Command(BaseCommand):

    help = "Importa los partidos de la Fecha 1"

    def handle(self, *args, **kwargs):

        calendario = CalendarioReal.objects.get(
            nombre="Liga Profesional Clausura 2026 - Fecha 1"
        )

        partidos = [
            ("Deportivo Riestra", "Boca"),
            ("Estudiantes", "Independiente"),
            ("Newell's", "Talleres"),
            ("Vélez", "Instituto"),
            ("Platense", "Unión"),
            ("Lanús", "San Lorenzo"),
            ("Gimnasia (Mza)", "Central Córdoba"),
            ("River", "Barracas Central"),
            ("Racing", "Gimnasia"),
            ("Belgrano", "Rosario Central"),
            ("Estudiantes (RC)", "Tigre"),
            ("Sarmiento", "Argentinos"),
            ("Huracán", "Banfield"),
            ("Atlético Tucumán", "Independiente Rivadavia"),
            ("Defensa y Justicia", "Aldosivi"),
        ]

        creados = 0

        for local, visitante in partidos:

            equipo_local = EquipoReal.objects.get(
                nombre=local
            )

            equipo_visitante = EquipoReal.objects.get(
                nombre=visitante
            )

            _, creado = PartidoReal.objects.get_or_create(
                calendario=calendario,
                equipo_local=equipo_local,
                equipo_visitante=equipo_visitante,
            )

            if creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Partidos creados: {creados}"
            )
        )
