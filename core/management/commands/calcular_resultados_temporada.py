from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    ResultadoTemporada,
    TablaTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Calcula clasificaciones de temporada"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            activa=True
        )

        ResultadoTemporada.objects.filter(
            temporada=temporada
        ).delete()

        reglas = {
            "A": {
                "libertadores": 10,
                "sudamericana": 20,
                "descenso_desde": 27,
            },
            "B": {
                "libertadores": 8,
                "sudamericana": 16,
                "descenso_desde": 27,
            },
            "C": {
                "libertadores": 6,
                "sudamericana": 12,
                "descenso_desde": None,
            },
        }

        total = 0

        categorias = Categoria.objects.all()

        for categoria in categorias:

            if categoria.nombre not in reglas:
                continue

            regla = reglas[categoria.nombre]

            tablas = (
                TablaTemporada.objects.filter(
                    temporada=temporada,
                    participante_temporada__categoria=categoria,
                )
                .order_by("posicion")
            )

            for tabla in tablas:

                resultado = "NINGUNO"

                if tabla.posicion <= regla["libertadores"]:

                    resultado = "LIBERTADORES"

                elif tabla.posicion <= regla["sudamericana"]:

                    resultado = "SUDAMERICANA"

                elif (
                    regla["descenso_desde"] is not None
                    and tabla.posicion >= regla["descenso_desde"]
                ):

                    resultado = "DESCENSO"

                ResultadoTemporada.objects.create(
                    participante_temporada=
                    tabla.participante_temporada,

                    temporada=temporada,

                    resultado=resultado,
                )

                total += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Resultados generados: {total}"
            )
        )