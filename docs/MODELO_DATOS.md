# MODELO_DATOS

Fecha:
2026-07-27

---

# Estado General

El modelo de datos principal se considera:

✅ Implementado

✅ Validado funcionalmente

🔄 En proceso de aumento de configurabilidad

---

# Entidades Implementadas

## Personas

### Participante

Representa una persona dentro del sistema.

---

### Categoria

Representa una división deportiva.

Ejemplos:

- A
- B
- C

---

### Temporada

Representa un ciclo anual.

Ejemplos:

- 2026
- 2027
- 2028

---

### ParticipanteTemporada

Representa la participación de una persona en una temporada determinada.

Permite modelar:

- ascensos
- descensos
- reincorporaciones
- nuevos participantes
- histórico anual

---

# Competiciones

### PlantillaCompetencia

Define un tipo de competencia reutilizable.

---

### Competencia

Representa una edición concreta de una competencia.

Ejemplos:

- Liga Profesional Clausura 2026
- Copa Libertadores 2026
- Copa Sudamericana 2026

---

### CompetenciaConfig

Entidad estratégica del sistema.

Almacena la configuración de comportamiento de una competencia.

Campos relevantes:

- cantidad_participantes
- cantidad_zonas
- clasificados
- cantidad_ascensos
- cantidad_descensos
- tiene_playoff
- tiene_penales
- usa_tabla
- usa_af
- usa_av
- usa_da

---

### ParticipacionCompetencia

Representa la inscripción de un participante dentro de una competencia.

Permite registrar:

- inscripto
- activo
- eliminado
- clasificado
- campeón
- subcampeón

---

### InstanciaCompetencia

Representa una unidad competitiva.

Ejemplos:

- Fecha 1
- Fecha 2
- Octavos
- Cuartos
- Semifinal
- Final

Tipos actualmente soportados:

- FECHA
- RONDA
- PLAYOFF
- FINAL
- ESPECIAL

---

# Fútbol Real

### EquipoReal

Representa un equipo oficial.

---

### CalendarioReal

Agrupa partidos reales.

---

### PartidoReal

Representa un partido de fútbol real.

Almacena:

- equipos
- fecha
- goles
- estado

---

### InstanciaPartido

Relaciona:

InstanciaCompetencia

↓

PartidoReal

Permite:

- reutilizar partidos
- excluir partidos
- marcar penales
- definir subconjuntos

---

# Pronósticos

### Pronostico

Representa una predicción realizada por un participante.

Actualmente soporta:

- Local
- Empate
- Visitante

---

### ResultadoPronostico

Representa un pronóstico evaluado.

Almacena:

- resultado real
- acierto
- puntos

---

### ResumenParticipanteInstancia

Consolida el rendimiento de un participante dentro de una instancia.

Almacena:

- partidos evaluados
- AF
- AV
- puntos

---

# Núcleo Competitivo

### Enfrentamiento

Entidad central del dominio.

Representa:

```text
Participante A
vs
Participante B
```

Almacena:

- AF local
- AF visitante
- AV local
- AV visitante
- ganador
- empate
- puntos

---

# Tablas

### TablaInstancia

Representa la tabla correspondiente a una instancia.

---

### TablaCompetencia

Representa la tabla acumulada de una competencia.

---

### TablaTemporada

Representa la tabla anual consolidada.

Es la fuente principal para:

- ascensos
- descensos
- clasificación a copas

---

# Resultados Deportivos

### ResultadoTemporada

Representa el resultado deportivo final de una temporada.

Valores actuales:

- NINGUNO
- LIBERTADORES
- SUDAMERICANA
- ASCENSO
- DESCENSO
- REPECHAJE

---

### MovimientoCategoria

Representa el movimiento entre categorías.

Valores:

- ASCENSO
- DESCENSO
- MANTIENE

---

# Copas

### GrupoCompetencia

Representa un grupo dentro de una copa.

Ejemplos:

- Grupo A
- Grupo B
- Grupo C
- Grupo D

---

### ParticipacionGrupo

Relaciona participantes con grupos.

---

### TablaGrupo

Representa posiciones dentro de un grupo.

Almacena:

- posición
- PJ
- PG
- PE
- PP
- puntos
- AF
- AV

---

### ClasificacionGrupo

Representa el resultado final de la fase de grupos.

Valores:

- CLASIFICADO
- ELIMINADO

---

### LlaveCompetencia

Representa un cruce eliminatorio.

Almacena:

- competencia
- orden
- participante_1
- participante_2
- ganador
- resuelta

Actualmente soporta los playoffs implementados en la versión actual.

---

# Flujo Principal

```text
Participante
↓
ParticipanteTemporada
↓
Pronostico
↓
ResultadoPronostico
↓
ResumenParticipanteInstancia
↓
Enfrentamiento
↓
TablaInstancia
↓
TablaCompetencia
↓
TablaTemporada
↓
ResultadoTemporada
↓
MovimientoCategoria
```

---

# Flujo Copas

```text
ParticipacionCompetencia
↓
GrupoCompetencia
↓
ParticipacionGrupo
↓
TablaGrupo
↓
ClasificacionGrupo
↓
LlaveCompetencia
↓
Campeón
```

---

# Modelos Validados

## ParticipanteTemporada

Validado.

Permite:

- ascensos
- descensos
- históricos
- reincorporaciones

---

## InstanciaCompetencia

Validada.

Soporta:

- fechas
- rondas
- playoffs
- finales
- etapas especiales

---

## InstanciaPartido

Validada.

Permite:

- reutilización de partidos
- penales
- exclusiones
- subconjuntos de partidos

---

## Pronostico

Validado.

Actualmente soporta:

- Local
- Empate
- Visitante

Preparado para futuras extensiones.

---

## ResultadoPronostico

Validado mediante pruebas reales.

Permite:

- calcular aciertos
- calcular puntos
- derivar resultados oficiales

---

## ResumenParticipanteInstancia

Validado mediante pruebas reales.

Base para:

- enfrentamientos
- tablas
- clasificaciones
- desempates

---

## Enfrentamiento

Validado.

Permite:

- determinar ganador
- determinar empate
- asignar puntos

---

## Tablas

Validadas:

- TablaInstancia
- TablaCompetencia
- TablaTemporada

---

## Copas

Validadas en versión actual:

- grupos
- clasificaciones
- playoffs
- llaves

---

# Hallazgos de Auditoría

Julio 2026

Luego de revisar modelos y procesos se concluyó:

## El modelo de datos está más avanzado que los comandos

La mayoría de las estructuras necesarias ya existen.

No se identifican refactors urgentes del modelo.

---

## La principal deuda está en los procesos

Muchos comandos todavía utilizan valores hardcodeados.

Ejemplos:

- cantidad de grupos
- clasificados
- ascensos
- descensos
- rondas
- instancias

---

## CompetenciaConfig debe convertirse en la fuente de verdad

La próxima etapa consiste en reemplazar configuraciones fijas por lectura de:

CompetenciaConfig

---

# Entidades Futuras

Pendientes de implementación.

## Equipos Temporales

- EquipoTemporal
- MiembroEquipoTemporal

Necesarios para:

- Supercopa
- formatos por equipos

---

## Históricos

Posibles entidades futuras:

- HallOfFame
- Rivalidad
- RecordHistorico

No existen todavía en el modelo actual.

---

# Estado del Modelo

Modelo de Dominio:
90%

Modelo de Datos:
90%

Backend Funcional:
90%

Backend Configurable:
60%

El modelo actual se considera suficientemente estable para continuar la evolución mediante refactor de procesos y no mediante incorporación masiva de nuevas entidades.