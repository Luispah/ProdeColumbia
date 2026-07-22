from django.core.management.base import BaseCommand

from core.models import EquipoReal


class Command(BaseCommand):

    help = "Genera los equipos reales de Primera Division"

    def handle(self, *args, **kwargs):

        equipos = [
            "Aldosivi",
            "Argentinos",
            "Atlético Tucumán",
            "Banfield",
            "Barracas Central",
            "Belgrano",
            "Boca",
            "Central Córdoba",
            "Defensa y Justicia",
            "Deportivo Riestra",
            "Estudiantes",
            "Gimnasia",
            "Godoy Cruz",
            "Huracán",
            "Independiente",
            "Independiente Rivadavia",
            "Instituto",
            "Lanús",
            "Newell's",
            "Platense",
            "Racing",
            "River",
            "Rosario Central",
            "San Lorenzo",
            "San Martín SJ",
            "Sarmiento",
            "Talleres",
            "Tigre",
            "Unión",
            "Vélez",
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