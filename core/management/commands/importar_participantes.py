from pathlib import Path

import pandas as pd

from django.core.management.base import BaseCommand

from core.models import Participante


class Command(BaseCommand):

    help = "Importa participantes desde Excel"

    def handle(self, *args, **kwargs):

        archivo = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "01_Participantes_Actuales.xlsx"
        )

        self.stdout.write(f"Leyendo: {archivo}")

        df = pd.read_excel(archivo)

        contador = 0

        for indice, fila in df.iterrows():

            nombre = str(fila["Nombre"]).strip()
            categoria = str(fila["Categoria"]).strip()

            email = ""

            if "Email (opc)" in df.columns:
                valor = fila["Email (opc)"]

                if pd.notna(valor):
                    email = str(valor).strip()

            observaciones = ""

            if "Observaciones" in df.columns:
                valor = fila["Observaciones"]

                if pd.notna(valor):
                    observaciones = str(valor)

            participante, creado = Participante.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "id_externo": f"P{indice + 1:04}",
                    "categoria": categoria,
                    "activo": True,
                    "email": email,
                    "administrador": (
                        "administrador" in observaciones.lower()
                    ),
                },
            )

            if creado:
                contador += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Participantes importados: {contador}"
            )
        )