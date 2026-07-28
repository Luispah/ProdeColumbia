from django.contrib import admin

from .models import (
    CalendarioReal,
    Categoria,
    Competencia,
    CompetenciaConfig,
    Enfrentamiento,
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
    ResultadoTemporada,
    TablaCompetencia,
    TablaInstancia,
    TablaTemporada,
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

admin.site.register(Enfrentamiento)


@admin.register(TablaInstancia)
class TablaInstanciaAdmin(admin.ModelAdmin):

    list_display = (
        "participante_temporada",
        "instancia",
        "puntos",
        "pj",
        "pg",
        "pe",
        "pp",
        "af",
        "av",
    )

    ordering = (
        "-puntos",
        "-af",
        "-av",
    )

    list_filter = (
        "instancia",
    )

    search_fields = (
        "participante_temporada__participante__nombre",
    )


@admin.register(TablaCompetencia)
class TablaCompetenciaAdmin(admin.ModelAdmin):

    list_display = (
        "participante_temporada",
        "competencia",
        "puntos",
        "pj",
        "pg",
        "pe",
        "pp",
        "af",
        "av",
    )

    ordering = (
        "-puntos",
        "-af",
        "-av",
    )

    list_filter = (
        "competencia",
    )

    search_fields = (
        "participante_temporada__participante__nombre",
    )


@admin.register(TablaTemporada)
class TablaTemporadaAdmin(admin.ModelAdmin):

    list_display = (
        "posicion",
        "participante_temporada",
        "temporada",
        "puntos",
        "pj",
        "pg",
        "pe",
        "pp",
        "af",
        "av",
    )

    ordering = (
        "posicion",
    )

    list_filter = (
        "temporada",
    )

    search_fields = (
        "participante_temporada__participante__nombre",
    )


@admin.register(ResultadoTemporada)
class ResultadoTemporadaAdmin(admin.ModelAdmin):

    list_display = (
        "participante_temporada",
        "temporada",
        "resultado",
    )

    ordering = (
        "resultado",
    )

    list_filter = (
        "temporada",
        "resultado",
    )

    search_fields = (
        "participante_temporada__participante__nombre",
    )


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