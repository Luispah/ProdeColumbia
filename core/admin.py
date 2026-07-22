from django.contrib import admin

from .models import (
    CalendarioReal,
    Categoria,
    Competencia,
    CompetenciaConfig,
    EquipoReal,
    InstanciaCompetencia,
    InstanciaPartido,
    ParticipacionCompetencia,
    Participante,
    ParticipanteTemporada,
    PartidoReal,
    PlantillaCompetencia,
    Pronostico,
    ResumenParticipanteInstancia,
    ResultadoPronostico,
    Temporada,
    Torneo,
)


admin.site.register(Categoria)
admin.site.register(Temporada)
admin.site.register(Torneo)

admin.site.register(PlantillaCompetencia)
admin.site.register(Competencia)
admin.site.register(CompetenciaConfig)
admin.site.register(ParticipanteTemporada)
admin.site.register(ParticipacionCompetencia)
admin.site.register(InstanciaCompetencia)
admin.site.register(InstanciaPartido)

admin.site.register(EquipoReal)
admin.site.register(CalendarioReal)
admin.site.register(PartidoReal)

admin.site.register(Pronostico)
admin.site.register(ResultadoPronostico)
admin.site.register(ResumenParticipanteInstancia)


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