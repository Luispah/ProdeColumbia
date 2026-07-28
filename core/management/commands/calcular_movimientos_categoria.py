from django.core.management.base import BaseCommand

from core.models import (
    Categoria,
    MovimientoCategoria,
    ParticipanteTemporada,
    TablaTemporada,
    Temporada,
)


class Command(BaseCommand):

    help = (
        "Calcula ascensos y descensos"
    )

    def handle(self, *args, **kwargs):

        temporada = Temporada.objects.get(
            activa=True
        )

        categoria_a = Categoria.objects.get(
            nombre="A"
        )

        categoria_b = Categoria.objects.get(
            nombre="B"
        )

        categoria_c = Categoria.objects.get(
            nombre="C"
        )

        MovimientoCategoria.objects.filter(
            temporada=temporada
        ).delete()

        participantes = (
            ParticipanteTemporada.objects.filter(
                temporada=temporada,
                activo=True,
            )
        )

        for participante in participantes:

            MovimientoCategoria.objects.create(
                participante_temporada=participante,
                temporada=temporada,
                movimiento="MANTIENE",
                categoria_origen=participante.categoria,
                categoria_destino=participante.categoria,
            )

        # DESCENSOS A -> B

        tabla_a = (
            TablaTemporada.objects.filter(
                temporada=temporada,
                participante_temporada__categoria=categoria_a,
            )
            .order_by("-posicion")
        )

        for tabla in tabla_a[:4]:

            movimiento = MovimientoCategoria.objects.get(
                participante_temporada=
                tabla.participante_temporada,
                temporada=temporada,
            )

            movimiento.movimiento = "DESCENSO"
            movimiento.categoria_destino = categoria_b
            movimiento.save()

        # ASCENSOS B -> A

        tabla_b = (
            TablaTemporada.objects.filter(
                temporada=temporada,
                participante_temporada__categoria=categoria_b,
            )
            .order_by("posicion")
        )

        for tabla in tabla_b[:4]:

            movimiento = MovimientoCategoria.objects.get(
                participante_temporada=
                tabla.participante_temporada,
                temporada=temporada,
            )

            movimiento.movimiento = "ASCENSO"
            movimiento.categoria_destino = categoria_a
            movimiento.save()

        # DESCENSOS B -> C

        tabla_b_descenso = (
            TablaTemporada.objects.filter(
                temporada=temporada,
                participante_temporada__categoria=categoria_b,
            )
            .order_by("-posicion")
        )

        for tabla in tabla_b_descenso[:4]:

            movimiento = MovimientoCategoria.objects.get(
                participante_temporada=
                tabla.participante_temporada,
                temporada=temporada,
            )

            movimiento.movimiento = "DESCENSO"
            movimiento.categoria_destino = categoria_c
            movimiento.save()

        # ASCENSOS C -> B

        tabla_c = (
            TablaTemporada.objects.filter(
                temporada=temporada,
                participante_temporada__categoria=categoria_c,
            )
            .order_by("posicion")
        )

        for tabla in tabla_c[:4]:

            movimiento = MovimientoCategoria.objects.get(
                participante_temporada=
                tabla.participante_temporada,
                temporada=temporada,
            )

            movimiento.movimiento = "ASCENSO"
            movimiento.categoria_destino = categoria_b
            movimiento.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Movimientos calculados"
            )
        )