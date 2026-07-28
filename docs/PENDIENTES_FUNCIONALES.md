\# PENDIENTES\_FUNCIONALES



Fecha de actualización:

2026-07-27



\---



\# PENDIENTES FUNCIONALES



Este documento registra funcionalidades aprobadas conceptualmente pero todavía no implementadas.



No incluye deuda técnica.



No incluye refactors internos.



No incluye mejoras de arquitectura.



Únicamente funcionalidades visibles o comportamientos de negocio pendientes.



\---



\# Prioridad Alta



\## Bloqueo Automático de Boletas



Estado:



⏳ PENDIENTE



Descripción:



La carga y modificación de boletas deberá bloquearse automáticamente antes del inicio de los partidos.



Objetivo inicial:



```text

1 hora antes del primer partido válido

de la instancia

```



Ejemplo:



```text

Primer partido: 20:00



Cierre: 19:00

```



Una vez alcanzado el horario de cierre:



\- no podrán modificarse pronósticos

\- no podrán agregarse pronósticos

\- la boleta quedará bloqueada



\---



\## Visibilidad de Boletas



Estado:



⏳ PENDIENTE



Antes del cierre:



\- cada participante visualiza únicamente su propia boleta



Después del cierre:



\- todos los participantes pueden visualizar todas las boletas



Objetivo:



Garantizar confidencialidad previa al inicio de los partidos.



\---



\## Carga Administrativa



Estado:



⏳ PENDIENTE



Los administradores deberán poder:



\- crear boletas

\- modificar boletas

\- cargar pronósticos por terceros



Objetivo:



Facilitar la participación de usuarios con poca experiencia informática.



\---



\## Auditoría de Boletas



Estado:



⏳ PENDIENTE



Debe registrarse:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de creación

\- fecha de modificación



Objetivo:



Garantizar trazabilidad completa.



\---



\# Prioridad Media



\## Partidos Decisivos



Estado:



⏳ PENDIENTE



El sistema deberá detectar automáticamente partidos donde dos participantes tengan pronósticos diferentes.



Ejemplo:



```text

Participante A

↓

Local



Participante B

↓

Visitante

```



Resultado:



```text

Partido decisivo

```



Objetivo:



Identificar los partidos que realmente pueden producir diferencias deportivas entre dos participantes.



\---



\## Escudos de Equipos



Estado:



⏳ PENDIENTE



Los equipos deberán soportar:



\- escudo oficial

\- almacenamiento local



Objetivo:



Utilización en:



\- frontend

\- tablas

\- reportes

\- estadísticas



\---



\## Zona Horaria Argentina



Estado:



⏳ PENDIENTE



Configurar:



```text

America/Argentina/Buenos\_Aires

```



Objetivo:



Evitar diferencias entre:



\- horario del servidor

\- horario visible al usuario



\---



\## Generación Automática de Temporadas



Estado:



⏳ PENDIENTE



Objetivo:



Permitir generar automáticamente una nueva temporada utilizando los resultados de la temporada anterior.



Deberá contemplar:



\- ascensos

\- descensos

\- participantes activos

\- reincorporaciones



La propuesta generada deberá poder modificarse manualmente antes de confirmarse.



\---



\# Prioridad Media-Baja



\## Equipos Temporales



Estado:



⏳ PENDIENTE



Implementaciones futuras:



\- EquipoTemporal

\- MiembroEquipoTemporal



Objetivo:



Soportar:



\- Supercopa

\- competencias por equipos

\- formatos especiales



\---



\## Hall of Fame



Estado:



⏳ PENDIENTE



Objetivo:



Mantener históricos de:



\- campeones

\- subcampeones

\- récords

\- títulos



\---



\## Rivalidades



Estado:



⏳ PENDIENTE



Objetivo:



Generar historial entre participantes.



Ejemplos:



\- enfrentamientos disputados

\- victorias

\- empates

\- derrotas



\---



\## Estadísticas Históricas



Estado:



⏳ PENDIENTE



Posibles métricas:



\- AF histórico

\- AV histórico

\- efectividad

\- rendimiento por competencia

\- rendimiento por temporada



\---



\# Prioridad Baja



\## Pronósticos por Resultado Exacto



Estado:



⏳ PENDIENTE



Actualmente:



```text

Local

Empate

Visitante

```



A futuro deberá poder soportarse:



```text

Resultado exacto

```



Ejemplo:



```text

River 2 - 1 Boca

```



La implementación no debe requerir rediseñar el dominio existente.



\---



\## Sorteos



Estado:



⏳ PENDIENTE



Posible incorporación futura.



Aplicable principalmente a:



\- Copa Argentina

\- Copa Libertadores

\- Copa Sudamericana

\- Supercopa



Objetivo:



Automatizar cruces cuando el reglamento lo requiera.



\---



\# Fuera de Alcance Inmediato



Las siguientes tareas NO forman parte de la prioridad actual:



\- rediseño completo del frontend

\- aplicaciones móviles

\- APIs públicas

\- integración con redes sociales



\---



\# Situación Actual



El backend principal ya permite:



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



y además:



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



Por lo tanto los pendientes actuales corresponden principalmente a:



\- experiencia de usuario

\- administración

\- históricos

\- automatizaciones

\- frontend



y no al flujo competitivo principal.



\---



\# Observación Importante



Luego de la auditoría de julio de 2026 se concluyó que:



```text

La principal deuda actual del proyecto

NO es funcional.

```



La principal deuda actual es técnica y consiste en reemplazar los hardcodeos existentes por configuraciones basadas en:



```text

CompetenciaConfig

```



Dicha tarea se encuentra documentada en:



\- ROADMAP.md

\- IA\_CONTEXT.md

\- DECISIONES\_TECNICAS.md

