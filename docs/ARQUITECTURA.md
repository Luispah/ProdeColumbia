# ARQUITECTURA

Fecha:
2026-07-27

---

# Principio Arquitectónico Principal

Separar completamente:

Fútbol Real

de

Prode

Esta decisión es una de las bases del proyecto.

Permite:

- reutilizar partidos reales en múltiples competiciones
- soportar distintos formatos deportivos
- incorporar nuevas reglas sin alterar datos reales
- integrar múltiples fuentes externas
- desacoplar la lógica competitiva de los datos deportivos

---

# Arquitectura General

El sistema se divide en cinco capas principales:

```text
Fútbol Real
↓
Pronósticos
↓
Resultados
↓
Competición
↓
Histórico Deportivo
```

---

# Capa 1 - Fútbol Real

Representa hechos objetivos.

No depende de participantes.

No depende de categorías.

No depende de competiciones.

---

## EquipoReal

Fuente oficial de equipos.

Ejemplos:

- River Plate
- Boca Juniors
- Estudiantes
- Gimnasia

Responsabilidades:

- nombre oficial
- identificación única
- futura incorporación de escudos

---

## CalendarioReal

Agrupa partidos reales.

Ejemplos:

```text
Liga Profesional Clausura 2026
Fecha 1
```

```text
Liga Profesional Clausura 2026
Fecha 2
```

---

## PartidoReal

Representa un partido real.

Almacena:

- local
- visitante
- fecha
- hora
- goles local
- goles visitante
- estado

La fuente oficial de resultado son los goles.

El sistema deriva automáticamente:

```text
Local
Empate
Visitante
```

cuando es necesario.

---

# Capa 2 - Pronósticos

Representa la participación de los jugadores.

---

## Pronostico

Almacena la predicción realizada por un participante.

Actualmente:

```text
L
E
V
```

Diseñado para soportar en el futuro:

- resultado exacto
- reglas especiales
- variantes por competencia

---

## ResultadoPronostico

Representa la evaluación de un pronóstico.

Almacena:

- resultado real
- acierto
- puntos

Se considera persistencia de cálculo.

No debe recalcularse constantemente.

---

## ResumenParticipanteInstancia

Consolida el rendimiento de un participante dentro de una instancia.

Almacena:

- partidos evaluados
- AF
- AV
- puntos

Es la base para:

- enfrentamientos
- tablas
- clasificaciones
- desempates

---

# Capa 3 - Competición

Representa la lógica competitiva.

---

## Enfrentamiento

Entidad central del negocio.

Representa:

```text
Participante A
vs
Participante B
```

Toda la lógica competitiva converge aquí.

Permite determinar:

- ganador
- perdedor
- empate
- puntos
- diferencias deportivas

---

## TablaInstancia

Representa una tabla para una instancia específica.

Ejemplos:

```text
Fecha 1
```

```text
Fecha 2
```

---

## TablaCompetencia

Representa una tabla acumulada dentro de una competencia.

Ejemplo:

```text
Liga Profesional Clausura 2026
```

---

## TablaTemporada

Representa la tabla anual consolidada.

Es la principal fuente para:

- clasificación a copas
- ascensos
- descensos
- rankings anuales

---

# Capa 4 - Resultados Deportivos

Representa las consecuencias deportivas de una temporada.

---

## ResultadoTemporada

Almacena el resultado deportivo final.

Ejemplos:

- Libertadores
- Sudamericana
- Ascenso
- Descenso
- Repechaje

---

## MovimientoCategoria

Representa el movimiento entre categorías.

Posibles resultados:

- Ascenso
- Descenso
- Mantiene

---

# Arquitectura de Competiciones

Toda competencia se define mediante:

```text
PlantillaCompetencia
+
Competencia
+
CompetenciaConfig
```

---

## PlantillaCompetencia

Define un tipo reutilizable.

Ejemplos:

- Liga
- Copa
- Supercopa

---

## Competencia

Representa una edición concreta.

Ejemplos:

- Liga Profesional Clausura 2026
- Copa Libertadores 2026

---

## CompetenciaConfig

Es la pieza estratégica del sistema.

Debe convertirse en la fuente única de configuración.

Actualmente contiene:

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

# Hallazgo Arquitectónico

Julio 2026

Luego de una auditoría completa se concluyó:

## El modelo está más avanzado que los procesos

Los modelos actuales son suficientemente flexibles para la mayoría de los escenarios previstos.

La principal deuda técnica actual NO se encuentra en los modelos.

La principal deuda técnica se encuentra en los comandos de procesamiento.

---

## Situación Actual

Existe soporte en CompetenciaConfig para:

- cantidad de grupos
- cantidad de clasificados
- ascensos
- descensos
- playoffs

Sin embargo muchos procesos todavía utilizan valores hardcodeados.

---

## Dirección Arquitectónica

La evolución del sistema consiste en mover progresivamente la lógica de los comandos hacia CompetenciaConfig.

Objetivo:

```text
Modificar configuración
↓
Cambiar comportamiento
↓
Sin modificar código
```

---

# Arquitectura de Copas

Actualmente el flujo es:

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

## GrupoCompetencia

Representa un grupo de una copa.

Ejemplos:

```text
Grupo A
Grupo B
Grupo C
Grupo D
```

---

## ParticipacionGrupo

Relaciona participantes con grupos.

---

## TablaGrupo

Representa la posición dentro de un grupo.

---

## ClasificacionGrupo

Representa el resultado final de la fase de grupos.

Posibles resultados:

- Clasificado
- Eliminado

---

## LlaveCompetencia

Representa un cruce eliminatorio.

Almacena:

- competencia
- orden
- participantes
- ganador
- estado

Actualmente soporta:

- playoffs
- semifinales
- finales

---

# Arquitectura de Instancias

InstanciaCompetencia reemplaza el concepto clásico de fecha.

Puede representar:

- Fecha
- Ronda
- Playoff
- Final
- Etapa especial

---

## InstanciaPartido

Es la unión entre:

```text
InstanciaCompetencia
```

y

```text
PartidoReal
```

Permite:

- reutilizar partidos
- excluir partidos
- marcar penales
- definir subconjuntos
- reutilizar calendarios

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

# Próxima Evolución Arquitectónica

## Fase 1

Eliminar hardcodeos.

Prioridades:

- grupos dinámicos
- clasificados dinámicos
- ascensos dinámicos
- descensos dinámicos

---

## Fase 2

Instancias dinámicas.

Objetivo:

Generar instancias desde configuración.

---

## Fase 3

Playoffs dinámicos.

Objetivo:

Generar rondas automáticamente según:

- participantes
- clasificados
- configuración de competencia

---

# Integraciones Futuras

## Importación de Datos

Posibles fuentes:

- Excel
- CSV
- APIs deportivas

---

## Regla de Integración

Nunca depender de una única fuente.

El sistema debe poder:

- cambiar de API
- combinar múltiples APIs
- operar manualmente

---

# Frontend Futuro

Estado actual:

Django Admin

---

## Portal Administrador

- temporadas
- participantes
- competencias
- resultados
- configuraciones

---

## Portal Participante

- carga de pronósticos
- tablas
- resultados
- históricos
- estadísticas

---

# Requisitos Arquitectónicos Pendientes

## Bloqueo de Boletas

Cierre automático previo al inicio de los partidos.

---

## Visibilidad de Boletas

Antes del cierre:

- privadas

Después del cierre:

- visibles para todos

---

## Auditoría

Registrar:

- propietario
- usuario cargador
- fecha creación
- fecha modificación

---

## Partidos Decisivos

Identificar partidos donde dos participantes realizaron pronósticos distintos.

---

## Escudos

Soporte para:

- almacenamiento local
- imágenes oficiales

---

## Zona Horaria

Configuración objetivo:

```text
America/Argentina/Buenos_Aires
```

---

# Estado Arquitectónico

Modelo de Dominio:
90%

Backend Funcional:
90%

Backend Configurable:
60%

Frontend:
0%

La prioridad actual es consolidar la configurabilidad del sistema utilizando CompetenciaConfig como fuente central de comportamiento.