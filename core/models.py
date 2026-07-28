from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    orden = models.IntegerField(
        default=0
    )

    activa = models.BooleanField(
        default=True
    )

    color = models.CharField(
        max_length=20,
        default="#FFFFFF"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["orden"]


class Temporada(models.Model):

    anio = models.IntegerField(
        unique=True
    )

    activa = models.BooleanField(
        default=False
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.anio)

    class Meta:
        ordering = ["-anio"]


class Torneo(models.Model):

    TIPOS = [
        ("APERTURA", "Apertura"),
        ("CLAUSURA", "Clausura"),
        ("COPA_ARG", "Copa Argentina"),
        ("SUPERCOPA", "Supercopa"),
    ]

    nombre = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre


class PlantillaCompetencia(models.Model):

    TIPOS = [
        ("LIGA", "Liga"),
        ("COPA", "Copa"),
        ("SUPERCOPA", "Supercopa"),
        ("ESPECIAL", "Especial"),
    ]

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    descripcion = models.TextField(
        blank=True,
        default=""
    )

    tipo_general = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    activa = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre


class Competencia(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    plantilla = models.ForeignKey(
        PlantillaCompetencia,
        on_delete=models.PROTECT
    )

    activa = models.BooleanField(
        default=True
    )

    fecha_inicio = models.DateField(
        null=True,
        blank=True
    )

    fecha_fin = models.DateField(
        null=True,
        blank=True
    )

    descripcion = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self):
        return self.nombre


class Participante(models.Model):

    CATEGORIAS = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
    ]

    id_externo = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIAS
    )

    activo = models.BooleanField(
        default=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    club_hincha = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    club_simpatizante = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    administrador = models.BooleanField(
        default=False
    )

    fecha_alta = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre


class ParticipanteTemporada(models.Model):

    participante = models.ForeignKey(
        Participante,
        on_delete=models.PROTECT
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    activo = models.BooleanField(
        default=True
    )

    fecha_ingreso = models.DateField(
        null=True,
        blank=True
    )

    fecha_baja = models.DateField(
        null=True,
        blank=True
    )

    es_nuevo = models.BooleanField(
        default=False
    )

    observaciones = models.TextField(
        blank=True,
        default=""
    )

    class Meta:
        unique_together = (
            "participante",
            "temporada",
        )

    def __str__(self):
        return (
            f"{self.participante} - {self.temporada}"
        )


class CompetenciaConfig(models.Model):

    competencia = models.OneToOneField(
        Competencia,
        on_delete=models.CASCADE
    )

    cantidad_participantes = models.IntegerField(default=0)
    cantidad_zonas = models.IntegerField(default=0)
    clasificados = models.IntegerField(default=0)

    cantidad_partidos_boleta = models.IntegerField(default=15)

    frecuencia_dias = models.IntegerField(default=7)

    maximo_locales = models.IntegerField(default=11)

    cantidad_ascensos = models.IntegerField(default=0)
    cantidad_descensos = models.IntegerField(default=0)

    tiene_playoff = models.BooleanField(default=False)
    tiene_penales = models.BooleanField(default=False)

    permite_equipos = models.BooleanField(default=False)

    usa_tabla = models.BooleanField(default=True)

    usa_af = models.BooleanField(default=True)
    usa_av = models.BooleanField(default=True)
    usa_da = models.BooleanField(default=True)

    def __str__(self):
        return (
            f"Configuración - {self.competencia.nombre}"
        )


class ParticipacionCompetencia(models.Model):

    ESTADOS = [
        ("INSCRIPTO", "Inscripto"),
        ("ACTIVO", "Activo"),
        ("ELIMINADO", "Eliminado"),
        ("CLASIFICADO", "Clasificado"),
        ("CAMPEON", "Campeón"),
        ("SUBCAMPEON", "Subcampeón"),
    ]

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.PROTECT
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="INSCRIPTO"
    )

    resultado_final = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    posicion_final = models.IntegerField(
        null=True,
        blank=True
    )

    clasificado_desde = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    def __str__(self):
        return (
            f"{self.participante_temporada} - {self.competencia}"
        )


class InstanciaCompetencia(models.Model):

    TIPOS = [
        ("FECHA", "Fecha"),
        ("RONDA", "Ronda"),
        ("PLAYOFF", "Playoff"),
        ("FINAL", "Final"),
        ("ESPECIAL", "Especial"),
    ]

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.PROTECT
    )

    nombre = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    orden = models.IntegerField(
        default=0
    )

    fecha_inicio = models.DateField(
        null=True,
        blank=True
    )

    fecha_fin = models.DateField(
        null=True,
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return (
            f"{self.competencia} - {self.nombre}"
        )


class EquipoReal(models.Model):

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Equipo Real"
        verbose_name_plural = "Equipos Reales"


class CalendarioReal(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    fecha_inicio = models.DateField(
        null=True,
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Calendario Real"
        verbose_name_plural = "Calendarios Reales"


class PartidoReal(models.Model):

    ESTADOS = [
        ("PROGRAMADO", "Programado"),
        ("JUGADO", "Jugado"),
        ("SUSPENDIDO", "Suspendido"),
        ("ANULADO", "Anulado"),
    ]

    calendario = models.ForeignKey(
        CalendarioReal,
        on_delete=models.PROTECT
    )

    equipo_local = models.ForeignKey(
        EquipoReal,
        on_delete=models.PROTECT,
        related_name="partidos_local"
    )

    equipo_visitante = models.ForeignKey(
        EquipoReal,
        on_delete=models.PROTECT,
        related_name="partidos_visitante"
    )

    fecha_hora = models.DateTimeField(
        null=True,
        blank=True
    )

    goles_local = models.IntegerField(
        null=True,
        blank=True
    )

    goles_visitante = models.IntegerField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="PROGRAMADO"
    )

    def __str__(self):
        return (
            f"{self.equipo_local} vs {self.equipo_visitante}"
        )

    class Meta:
        verbose_name = "Partido Real"
        verbose_name_plural = "Partidos Reales"


class InstanciaPartido(models.Model):

    instancia = models.ForeignKey(
        InstanciaCompetencia,
        on_delete=models.PROTECT
    )

    partido = models.ForeignKey(
        PartidoReal,
        on_delete=models.PROTECT
    )

    puntua = models.BooleanField(
        default=True
    )

    es_penal = models.BooleanField(
        default=False
    )

    orden = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = "Instancia Partido"
        verbose_name_plural = "Instancias Partido"
        unique_together = (
            "instancia",
            "partido",
        )

    def __str__(self):
        return (
            f"{self.instancia} - {self.partido}"
        )


class Pronostico(models.Model):

    RESULTADOS = [
        ("L", "Local"),
        ("E", "Empate"),
        ("V", "Visitante"),
    ]

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    instancia_partido = models.ForeignKey(
        InstanciaPartido,
        on_delete=models.PROTECT
    )

    resultado = models.CharField(
        max_length=1,
        choices=RESULTADOS
    )

    fecha_carga = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Pronóstico"
        verbose_name_plural = "Pronósticos"
        unique_together = (
            "participante_temporada",
            "instancia_partido",
        )

    def __str__(self):
        return (
            f"{self.participante_temporada} - "
            f"{self.instancia_partido}"
        )


class ResultadoPronostico(models.Model):

    pronostico = models.OneToOneField(
        Pronostico,
        on_delete=models.CASCADE
    )

    resultado_real = models.CharField(
        max_length=1
    )

    acierto = models.BooleanField(
        default=False
    )

    puntos = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = "Resultado Pronóstico"
        verbose_name_plural = "Resultados Pronóstico"

    def __str__(self):
        return (
            f"{self.pronostico}"
        )


class ResumenParticipanteInstancia(models.Model):

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    instancia = models.ForeignKey(
        InstanciaCompetencia,
        on_delete=models.PROTECT
    )

    partidos_evaluados = models.IntegerField(
        default=0
    )

    af = models.IntegerField(
        default=0
    )

    av = models.IntegerField(
        default=0
    )

    puntos = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = "Resumen Participante Instancia"
        verbose_name_plural = "Resumenes Participante Instancia"
        unique_together = (
            "participante_temporada",
            "instancia",
        )

    def __str__(self):
        return (
            f"{self.participante_temporada} - "
            f"{self.instancia}"
        )


class Enfrentamiento(models.Model):

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("FINALIZADO", "Finalizado"),
    ]

    instancia = models.ForeignKey(
        InstanciaCompetencia,
        on_delete=models.PROTECT
    )

    participante_local = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT,
        related_name="enfrentamientos_local"
    )

    participante_visitante = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT,
        related_name="enfrentamientos_visitante"
    )

    af_local = models.IntegerField(
        default=0
    )

    af_visitante = models.IntegerField(
        default=0
    )

    av_local = models.IntegerField(
        default=0
    )

    av_visitante = models.IntegerField(
        default=0
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="PENDIENTE"
    )

    RESULTADOS = [
        ("LOCAL", "Local"),
        ("VISITANTE", "Visitante"),
        ("EMPATE", "Empate"),
    ]

    resultado = models.CharField(
        max_length=20,
        choices=RESULTADOS,
        blank=True,
        default=""
    )

    puntos_local = models.IntegerField(
        default=0
    )

    puntos_visitante = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = "Enfrentamiento"
        verbose_name_plural = "Enfrentamientos"
        unique_together = (
            "instancia",
            "participante_local",
            "participante_visitante",
        )

    def __str__(self):
        return (
            f"{self.participante_local} vs "
            f"{self.participante_visitante}"
        )


class TablaInstancia(models.Model):

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    instancia = models.ForeignKey(
        InstanciaCompetencia,
        on_delete=models.PROTECT
    )

    pj = models.IntegerField(
        default=0
    )

    pg = models.IntegerField(
        default=0
    )

    pe = models.IntegerField(
        default=0
    )

    pp = models.IntegerField(
        default=0
    )

    puntos = models.IntegerField(
        default=0
    )

    af = models.IntegerField(
        default=0
    )

    av = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = "Tabla Instancia"
        verbose_name_plural = "Tabla Instancias"
        unique_together = (
            "participante_temporada",
            "instancia",
        )

    def __str__(self):
        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.instancia}"
        )


class TablaCompetencia(models.Model):

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.PROTECT
    )

    pj = models.IntegerField(
        default=0
    )

    pg = models.IntegerField(
        default=0
    )

    pe = models.IntegerField(
        default=0
    )

    pp = models.IntegerField(
        default=0
    )

    puntos = models.IntegerField(
        default=0
    )

    af = models.IntegerField(
        default=0
    )

    av = models.IntegerField(
        default=0
    )

    class Meta:

        verbose_name = "Tabla Competencia"
        verbose_name_plural = "Tablas Competencia"

        unique_together = (
            "participante_temporada",
            "competencia",
        )

    def __str__(self):

        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.competencia}"
        )


class TablaTemporada(models.Model):

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    posicion = models.IntegerField(
        default=0
    )

    pj = models.IntegerField(
        default=0
    )

    pg = models.IntegerField(
        default=0
    )

    pe = models.IntegerField(
        default=0
    )

    pp = models.IntegerField(
        default=0
    )

    puntos = models.IntegerField(
        default=0
    )

    af = models.IntegerField(
        default=0
    )

    av = models.IntegerField(
        default=0
    )

    class Meta:

        verbose_name = "Tabla Temporada"
        verbose_name_plural = "Tablas Temporada"

        unique_together = (
            "participante_temporada",
            "temporada",
        )

    def __str__(self):

        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.temporada}"
        )


class ResultadoTemporada(models.Model):

    RESULTADOS = [
        ("NINGUNO", "Ninguno"),
        ("LIBERTADORES", "Libertadores"),
        ("SUDAMERICANA", "Sudamericana"),
        ("ASCENSO", "Ascenso"),
        ("DESCENSO", "Descenso"),
        ("REPECHAJE", "Repechaje"),
    ]

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    resultado = models.CharField(
        max_length=20,
        choices=RESULTADOS,
        default="NINGUNO"
    )

    class Meta:

        verbose_name = "Resultado Temporada"
        verbose_name_plural = "Resultados Temporada"

        unique_together = (
            "participante_temporada",
            "temporada",
        )

    def __str__(self):

        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.resultado}"
        )

class MovimientoCategoria(models.Model):

    MOVIMIENTOS = [
        ("ASCENSO", "Ascenso"),
        ("DESCENSO", "Descenso"),
        ("MANTIENE", "Mantiene"),
    ]

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.PROTECT
    )

    movimiento = models.CharField(
        max_length=20,
        choices=MOVIMIENTOS
    )

    categoria_origen = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="movimientos_origen"
    )

    categoria_destino = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="movimientos_destino"
    )

    class Meta:

        verbose_name = "Movimiento Categoria"
        verbose_name_plural = "Movimientos Categoria"

        unique_together = (
            "participante_temporada",
            "temporada",
        )

    def __str__(self):

        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.movimiento}"
        )


class GrupoCompetencia(models.Model):

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.PROTECT
    )

    nombre = models.CharField(
        max_length=50
    )

    orden = models.IntegerField(
        default=0
    )

    class Meta:

        verbose_name = "Grupo Competencia"
        verbose_name_plural = "Grupos Competencia"

        unique_together = (
            "competencia",
            "nombre",
        )

    def __str__(self):

        return (
            f"{self.competencia}"
            f" - "
            f"{self.nombre}"
        )


class ParticipacionGrupo(models.Model):

    grupo = models.ForeignKey(
        GrupoCompetencia,
        on_delete=models.PROTECT
    )

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    class Meta:

        verbose_name = "Participacion Grupo"
        verbose_name_plural = "Participaciones Grupo"

        unique_together = (
            "grupo",
            "participante_temporada",
        )

    def __str__(self):

        return (
            f"{self.participante_temporada}"
            f" - "
            f"{self.grupo}"
        )


class TablaGrupo(models.Model):

    grupo = models.ForeignKey(
        GrupoCompetencia,
        on_delete=models.PROTECT
    )

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    posicion = models.IntegerField(
        default=0
    )

    pj = models.IntegerField(
        default=0
    )

    pg = models.IntegerField(
        default=0
    )

    pe = models.IntegerField(
        default=0
    )

    pp = models.IntegerField(
        default=0
    )

    puntos = models.IntegerField(
        default=0
    )

    af = models.IntegerField(
        default=0
    )

    av = models.IntegerField(
        default=0
    )

    class Meta:

        verbose_name = "Tabla Grupo"
        verbose_name_plural = "Tablas Grupo"

        unique_together = (
            "grupo",
            "participante_temporada",
        )

    def __str__(self):

        return (
            f"{self.grupo}"
            f" - "
            f"{self.participante_temporada}"
        )


class ClasificacionGrupo(models.Model):

    RESULTADOS = [
        ("CLASIFICADO", "Clasificado"),
        ("MEJOR_TERCERO", "Mejor tercero"),
        ("ELIMINADO", "Eliminado"),
    ]

    grupo = models.ForeignKey(
        GrupoCompetencia,
        on_delete=models.PROTECT
    )

    participante_temporada = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT
    )

    posicion = models.IntegerField(
        default=0
    )

    resultado = models.CharField(
        max_length=20,
        choices=RESULTADOS
    )

    class Meta:

        verbose_name = "Clasificacion Grupo"
        verbose_name_plural = "Clasificaciones Grupo"

        unique_together = (
            "grupo",
            "participante_temporada",
        )

    def __str__(self):

        return (
            f"{self.grupo}"
            f" - "
            f"{self.participante_temporada}"
        )


class LlaveCompetencia(models.Model):

    ETAPAS = [
        ("OCTAVOS", "Octavos"),
        ("CUARTOS", "Cuartos"),
        ("SEMIFINAL", "Semifinal"),
        ("FINAL", "Final"),
    ]

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.PROTECT
    )

    instancia = models.ForeignKey(
        InstanciaCompetencia,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    etapa = models.CharField(
        max_length=20,
        choices=ETAPAS
    )

    orden = models.IntegerField(
        default=0
    )

    participante_1 = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT,
        related_name="llaves_1"
    )

    participante_2 = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT,
        related_name="llaves_2"
    )

    ganador = models.ForeignKey(
        ParticipanteTemporada,
        on_delete=models.PROTECT,
        related_name="llaves_ganadas",
        null=True,
        blank=True,
    )

    resuelta = models.BooleanField(
        default=False
    )

    class Meta:

        verbose_name = "Llave Competencia"
        verbose_name_plural = "Llaves Competencia"

    def __str__(self):

        return (
            f"{self.competencia}"
            f" - "
            f"{self.etapa}"
        )