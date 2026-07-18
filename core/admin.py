from django.contrib import admin
from .models import Participante


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):

    list_display = (
        "id_externo",
        "nombre",
        "categoria",
        "activo",
        "administrador",
    )

    list_filter = (
        "categoria",
        "activo",
    )

    search_fields = (
        "nombre",
        "email",
    )