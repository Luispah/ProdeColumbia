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