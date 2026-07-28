# PLAN_REFACTOR_2026

Fecha:
2026-07-27

---

# Objetivo

Este documento resume las conclusiones obtenidas durante la auditoría integral realizada sobre:

- documentación
- modelos
- comandos
- Django Admin
- flujo competitivo
- estructura de competiciones
- reglamentos oficiales

Su objetivo es evitar futuras discusiones ya resueltas y servir como guía oficial para el desarrollo posterior.

---

# Conclusión Principal

La auditoría permitió identificar una diferencia importante entre:

```text
Problema percibido
```

y

```text
Problema real
```

Inicialmente se consideró que la principal deuda técnica se encontraba en:

```text
LlaveCompetencia
```

Sin embargo, luego de revisar:

- modelos
- comandos
- documentación
- reglamentos oficiales

se concluyó que:

```text
La principal deuda técnica NO está en los modelos.
```

La principal deuda técnica se encuentra en los procesos implementados mediante comandos.

---

# Estado Actual del Proyecto

## Modelo

Estado:

✅ Estable

✅ Funcional

✅ Extensible

Actualmente se consideran consolidados:

- Participante
- ParticipanteTemporada
- Categoria
- Temporada
- Competencia
- CompetenciaConfig
- InstanciaCompetencia
- InstanciaPartido
- Pronostico
- ResultadoPronostico
- ResumenParticipanteInstancia
- Enfrentamiento
- TablaInstancia
- TablaCompetencia
- TablaTemporada
- ResultadoTemporada
- MovimientoCategoria
- GrupoCompetencia
- ParticipacionGrupo
- TablaGrupo
- ClasificacionGrupo
- LlaveCompetencia

---

## Backend

Estado:

✅ Funcional

Actualmente el sistema puede ejecutar:

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

Y además:

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

# Hallazgo Principal

## El modelo está más avanzado que los comandos

Durante el crecimiento del proyecto se agregó soporte para:

- grupos
- clasificaciones
- playoffs
- ascensos
- descensos
- clasificaciones a copas

Sin embargo muchos procesos continúan utilizando valores fijos.

Por lo tanto:

```text
La configurabilidad existe en el modelo.

Pero todavía no existe completamente en los procesos.
```

---

# Hallazgos Obtenidos del Análisis de Reglamentos

Se analizaron los reglamentos oficiales de:

- Liga Profesional Clausura
- Copa Libertadores
- Copa Sudamericana
- Copa Repechaje
- Copa Argentina
- Supercopa

La conclusión principal es que la arquitectura actual es más correcta de lo que inicialmente parecía.

Los reglamentos validan muchas de las decisiones tomadas en el dominio.

---

# Familias de Competiciones Identificadas

El análisis permitió identificar cuatro grandes familias de competiciones.

---

## Tipo 1 - Liga

Ejemplo:

```text
Liga Profesional Clausura
```

Formato:

```text
Zonas
↓
Tabla
↓
Clasificación
↓
Playoffs
```

Características:

- posiciones
- clasificación deportiva
- ascensos
- descensos
- clasificación a copas

---

## Tipo 2 - Copa con Grupos

Ejemplos:

```text
Copa Libertadores
Copa Sudamericana
```

Formato:

```text
Grupos
↓
Clasificación
↓
Playoffs
```

Características:

- grupos
- clasificación por posiciones
- ranking posterior de clasificados
- cruces eliminatorios

---

## Tipo 3 - Copa Eliminatoria

Ejemplos:

```text
Copa Argentina
Copa Repechaje
```

Formato:

```text
Sorteo
↓
Eliminación directa
↓
Sorteo
↓
Eliminación directa
```

Características:

- no hay grupos
- no hay tabla
- sorteos sucesivos
- desempates por penales

---

## Tipo 4 - Supercopa

Formato:

```text
Equipos temporales
↓
Doble eliminación
↓
Zona Ganadores
↓
Zona Perdedores
```

Características:

- equipos temporales
- doble eliminación
- sorteos permanentes
- competencia colectiva

---

# Fuente Oficial de Configuración

Se ratifica la siguiente decisión:

## CompetenciaConfig

es la fuente oficial de configuración del sistema.

Antes de:

- crear un nuevo modelo
- agregar un nuevo campo
- desarrollar lógica específica

debe verificarse si el problema puede resolverse utilizando:

```text
CompetenciaConfig
```

---

# Decisiones Validadas por los Reglamentos

## cantidad_zonas sigue siendo correcta

Se comprobó que existen competiciones con grupos y competiciones sin grupos.

Ejemplos:

```text
Libertadores
↓
6 grupos

Sudamericana
↓
6 grupos

Repechaje
↓
0 grupos

Copa Argentina
↓
0 grupos
```

Por lo tanto:

```text
cantidad_zonas = 0
```

es una configuración perfectamente válida.

---

## tiene_playoff sigue siendo correcta

Existen torneos:

```text
con grupos y playoffs
```

y otros:

```text
playoff puro
```

La configuración actual continúa teniendo sentido.

---

## tiene_penales sigue siendo correcta

Los reglamentos de:

- Copa Argentina
- Copa Repechaje

incluyen sistemas de definición por penales.

Por lo tanto:

```text
tiene_penales
```

está plenamente justificado.

---

## EquipoTemporal continúa siendo necesario

La Supercopa requiere equipos formados dinámicamente por:

```text
1 participante A
1 participante B
1 participante C
```

Por lo tanto siguen siendo válidos como desarrollo futuro:

- EquipoTemporal
- MiembroEquipoTemporal

---

# Deuda Técnica Detectada

Durante la auditoría se identificaron los siguientes hardcodeos.

---

## Grupos de Copas

Actualmente:

```text
4 grupos fijos
```

Situación deseada:

```text
cantidad_zonas
```

obtenida desde:

```text
CompetenciaConfig
```

---

## Clasificación de Grupos

Actualmente:

```text
clasifican 2
```

Situación deseada:

obtener la clasificación desde configuración.

IMPORTANTE:

Los reglamentos revelan casos más complejos:

```text
2 clasificados por grupo
+
mejores terceros
```

Por lo tanto esta parte requerirá una evolución futura.

---

## Ascensos y Descensos

Actualmente:

```text
3 ascensos
3 descensos
```

Situación deseada:

```text
cantidad_ascensos
cantidad_descensos
```

configurables.

---

## Clasificación a Copas

Actualmente:

clasificaciones fijas.

Situación deseada:

clasificaciones obtenidas desde configuración.

---

## Instancias de Competencia

Actualmente:

```text
Fecha 1
Fecha 2
...
Octavos
Cuartos
Semifinal
Final
```

se generan mediante definiciones específicas.

Situación deseada:

generación basada en configuración.

---

## Playoffs

Actualmente:

```text
OCTAVOS
CUARTOS
SEMIFINAL
FINAL
```

se generan mediante reglas fijas.

Situación deseada:

generación automática basada en:

- participantes
- clasificados
- formato
- configuración

---

# Riesgos Detectados para CompetenciaConfig V2

Actualmente CompetenciaConfig sigue siendo suficiente para la fase actual.

Sin embargo los reglamentos muestran futuras necesidades.

Posibles configuraciones futuras:

- clasificados_por_grupo
- mejores_terceros
- usa_sorteos
- tipo_armado_llaves
- doble_eliminacion

IMPORTANTE:

Estas mejoras NO forman parte de la refactor actual.

Primero deben eliminarse los hardcodeos existentes.

---

# Qué NO Hacer

## No refactorizar modelos

No modificar todavía:

- Competencia
- CompetenciaConfig
- InstanciaCompetencia
- LlaveCompetencia

Motivo:

La deuda principal no se encuentra allí.

---

## No agregar más modelos

Antes de incorporar nuevas entidades se deberá verificar si la necesidad puede resolverse mediante configuración.

---

## No comenzar frontend

Todavía existen reglas y procesos que deben estabilizarse.

---

# Orden Oficial de Refactor

## Fase 1

Eliminar hardcodeos simples.

Archivos:

```text
generar_grupos_copas.py
calcular_clasificaciones_grupo.py
calcular_movimientos_categoria.py
```

Objetivo:

utilizar:

```text
CompetenciaConfig
```

---

## Fase 2

Refactorizar instancias.

Archivo principal:

```text
generar_instancias_2026.py
```

Objetivo:

reducir definiciones específicas por competencia.

---

## Fase 3

Playoffs dinámicos.

Archivos:

```text
generar_llaves_copas.py
generar_siguiente_ronda.py
resolver_llaves_copas.py
```

Objetivo:

generación automática de rondas.

---

## Fase 4

Automatización de temporadas.

Objetivos:

- generación automática de temporada siguiente
- aplicación automática de ascensos
- aplicación automática de descensos
- aplicación automática de clasificaciones

---

## Fase 5

CompetenciaConfig V2

Objetivo:

incorporar configuraciones avanzadas descubiertas durante el análisis de reglamentos.

---

## Fase 6

Equipos Temporales y Supercopa

Objetivo:

implementar correctamente:

- EquipoTemporal
- MiembroEquipoTemporal
- doble eliminación
- zona ganadores
- zona perdedores

---

# Integración API

La visión de largo plazo continúa contemplando integración con APIs deportivas.

Objetivos:

- importar fixtures
- importar resultados
- actualizar estados de partidos

La arquitectura actual:

```text
EquipoReal
CalendarioReal
PartidoReal
```

ya permite esta evolución sin afectar la lógica competitiva.

---

# Estado del Django Admin

Actualmente el Admin permite operar sobre la mayoría de los modelos principales.

Todavía faltan mejoras para:

- MovimientoCategoria
- GrupoCompetencia
- ParticipacionGrupo
- TablaGrupo
- ClasificacionGrupo
- LlaveCompetencia

Esta tarea queda postergada hasta estabilizar la lógica de negocio.

---

# Frontend

Estado:

⏳ Postergado

Condición para iniciar:

- reducción de hardcodeos
- consolidación de CompetenciaConfig
- estabilización de instancias
- estabilización de playoffs

---

# Objetivo Arquitectónico Ratificado

El objetivo NO es implementar exclusivamente:

- Liga Profesional 2026
- Libertadores 2026
- Sudamericana 2026
- Copa Argentina 2026

El objetivo es construir un motor capaz de crear competiciones futuras mediante configuración.

Objetivo final:

```text
PlantillaCompetencia
+
CompetenciaConfig
↓
Generación automática
↓
Competencia operativa
```

sin necesidad de desarrollar lógica específica para cada nuevo torneo.

---

# Métrica Actual del Proyecto

Modelo de Dominio:

```text
90%
```

Backend Funcional:

```text
90%
```

Backend Configurable:

```text
60%
```

Frontend:

```text
0%
```

---

# Decisión Vigente

La prioridad del proyecto ya no es agregar funcionalidad.

La prioridad actual es:

```text
Transformar un backend funcional
en un backend configurable.
```

Toda decisión futura deberá alinearse con este objetivo.

---

# Regla de Trabajo

Antes de implementar cualquier cambio importante:

1. Revisar IA_CONTEXT.md.
2. Revisar PROJECT_SNAPSHOT.md.
3. Revisar DECISIONES_TECNICAS.md.
4. Revisar VISION_LARGO_PLAZO.md.
5. Revisar este documento.
6. Verificar si CompetenciaConfig ya contempla el problema.

Si la respuesta es sí:

```text
Configurar antes que programar.
```

Esta es la directriz oficial vigente del proyecto.