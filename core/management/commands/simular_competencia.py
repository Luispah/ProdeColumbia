from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = (
        "Ejecuta el flujo completo de simulacion"
    )

    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.SUCCESS(
                "1. Generando enfrentamientos..."
            )
        )

        call_command(
            "generar_enfrentamientos"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "2. Generando pronosticos..."
            )
        )

        call_command(
            "generar_pronosticos"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "3. Generando resultados..."
            )
        )

        call_command(
            "generar_resultados"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "4. Generando resumenes..."
            )
        )

        call_command(
            "generar_resumenes"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "5. Actualizando enfrentamientos..."
            )
        )

        call_command(
            "actualizar_enfrentamientos_desde_resumenes"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "6. Resolviendo enfrentamientos..."
            )
        )

        call_command(
            "resolver_enfrentamientos"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "7. Generando tablas por instancia..."
            )
        )

        call_command(
            "generar_tablas_instancia"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "8. Generando tabla competencia..."
            )
        )

        call_command(
            "generar_tabla_competencia"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "9. Generando tabla temporada..."
            )
        )

        call_command(
            "generar_tabla_temporada"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Simulacion finalizada"
            )
        )