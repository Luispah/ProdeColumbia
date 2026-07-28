from django.core.management.base import BaseCommand

from core.models import (
    ClasificacionGrupo,
    Competencia,
    GrupoCompetencia,
    TablaGrupo,
)


class Command(BaseCommand):

    help = (
        "Calcula clasificaciones de grupos"
    )

    def handle(self, *args, **kwargs):

        ClasificacionGrupo.objects.all().delete()

        creados = 0

        competencias = Competencia.objects.filter(
            nombre__icontains="Copa "
        ).exclude(
            nombre__icontains="Argentina"
        ).exclude(
            nombre__icontains="Repechaje"
        ).exclude(
            nombre__icontains="Supercopa"
        )

        for competencia in competencias:

            terceros = []

            grupos = GrupoCompetencia.objects.filter(
                competencia=competencia
            )

            for grupo in grupos:

                tablas = (
                    TablaGrupo.objects.filter(
                        grupo=grupo
                    )
                    .order_by(
                        "posicion"
                    )
                )

                for tabla in tablas:

                    resultado = "ELIMINADO"

                    if tabla.posicion <= 2:

                        resultado = "CLASIFICADO"

                    elif tabla.posicion == 3:

                        resultado = "TERCERO"

                        terceros.append(
                            {
                                "tabla": tabla,
                                "puntos": tabla.puntos,
                                "af": tabla.af,
                                "av": tabla.av,
                            }
                        )

                    ClasificacionGrupo.objects.create(
                        grupo=grupo,
                        participante_temporada=
                        tabla.participante_temporada,
                        posicion=tabla.posicion,
                        resultado=resultado,
                    )

                    creados += 1

            terceros = sorted(
                terceros,
                key=lambda t: (
                    t["puntos"],
                    t["af"],
                    t["av"],
                ),
                reverse=True,
            )

            for tercero in terceros[:4]:

                clasificacion = ClasificacionGrupo.objects.get(
                    grupo=tercero["tabla"].grupo,
                    participante_temporada=
                    tercero["tabla"].participante_temporada,
                )

                clasificacion.resultado = (
                    "MEJOR_TERCERO"
                )

                clasificacion.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Clasificaciones generadas: "
                f"{creados}"
            )
        )