from django.contrib import admin

from .models import (
    Participante,
    Categoria,
    Temporada,
    Torneo
)

admin.site.register(Categoria)
admin.site.register(Temporada)
admin.site.register(Torneo)
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
