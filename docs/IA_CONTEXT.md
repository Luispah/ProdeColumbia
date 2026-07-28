\# IA\_CONTEXT



\## Proyecto



ProdeColumbia.



Aplicación web para administrar integralmente el Prode Columbia.



El sistema reemplaza progresivamente la operatoria histórica basada en Excel.



NO es únicamente un sistema de pronósticos deportivos.



El objetivo es modelar completamente la estructura competitiva del Prode.



Incluye actualmente:



\- Liga Profesional

\- Copa Libertadores

\- Copa Sudamericana

\- Copa Argentina

\- Copa Repechaje

\- Supercopa



y deberá ser capaz de soportar futuras competiciones sin necesidad de modificar código.



\---



\## Objetivo Principal



Centralizar toda la operatoria del Prode Columbia en una única plataforma.



El sistema debe administrar:



\- participantes

\- categorías

\- temporadas

\- competencias

\- pronósticos

\- resultados

\- enfrentamientos

\- tablas

\- clasificaciones

\- ascensos

\- descensos

\- históricos

\- estadísticas



\---



\## Visión Estratégica



El objetivo del proyecto NO es implementar únicamente las competiciones actuales.



El objetivo es construir un motor capaz de generar futuras ligas y copas mediante configuración.



Ejemplos:



\- nuevas ligas

\- nuevas copas

\- nuevas supercopas

\- torneos especiales

\- formatos todavía no definidos



La aplicación debe evolucionar hacia:



```text

Plantilla

↓

Configuración

↓

Generación automática

↓

Competencia operativa

```



con supervisión administrativa.



\---



\## Entidad Principal de Negocio



La entidad principal del ecosistema es:



```text

Temporada

```



Una temporada representa un año competitivo completo.



Ejemplos:



```text

2026

2027

2028

```



Todas las competiciones pertenecen a una temporada.



\---



\## Relación Temporada - Competiciones



Ejemplo:



```text

Temporada 2026

│

├── Liga Apertura

├── Liga Clausura

├── Libertadores

├── Sudamericana

├── Repechaje

├── Copa Argentina

└── Supercopa

```



No existe obligación de mantener siempre la misma cantidad ni el mismo tipo de competiciones.



Cada temporada puede contener:



\- una o varias ligas

\- una o varias copas

\- competiciones especiales



según las decisiones de la organización.



\---



\## Tecnología



\### Backend



\- Python

\- Django



\### Base de Datos



\- SQLite (desarrollo)

\- PostgreSQL (objetivo producción)



\### Versionado



\- Git

\- GitHub



\---



\## Estado Actual Real



El proyecto ya superó ampliamente la fase inicial de pronósticos.



Actualmente existe:



\### Personas



\- Participante

\- Categoria

\- Temporada

\- ParticipanteTemporada



\### Competencias



\- PlantillaCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia



\### Fútbol Real



\- EquipoReal

\- CalendarioReal

\- PartidoReal

\- InstanciaPartido



\### Pronósticos



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



\### Competición



\- Enfrentamiento



\### Tablas



\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada



\### Resultados Deportivos



\- ResultadoTemporada

\- MovimientoCategoria



\### Copas



\- GrupoCompetencia

\- ParticipacionGrupo

\- TablaGrupo

\- ClasificacionGrupo

\- LlaveCompetencia



\---



\## Flujo Principal Actual



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



\---



\## Flujo de Copas



```text

Competencia

↓

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



\---



\## Entidad Central del Negocio



La entidad central continúa siendo:



\### ENFRENTAMIENTO



Los partidos reales representan hechos objetivos.



Los enfrentamientos representan la competencia entre participantes.



Toda la lógica deportiva termina convergiendo en un enfrentamiento.



\---



\## Familias de Competiciones



Actualmente se identifican cuatro grandes familias.



\### Liga



```text

Zonas

↓

Tabla

↓

Clasificación

↓

Playoffs

```



\### Copa con Grupos



```text

Grupos

↓

Clasificación

↓

Playoffs

```



Ejemplos:



\- Libertadores

\- Sudamericana



\### Copa Eliminatoria



```text

Sorteo

↓

Eliminación Directa

```



Ejemplos:



\- Copa Argentina

\- Repechaje



\### Supercopa



```text

Equipos temporales

↓

Doble eliminación

↓

Zona Ganadores

↓

Zona Perdedores

```



\---



\## Principios Arquitectónicos



\### Separación estricta



Fútbol Real:



\- EquipoReal

\- CalendarioReal

\- PartidoReal



Representa eventos objetivos.



\---



Prode:



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- Enfrentamiento

\- Tablas

\- Clasificaciones

\- Resultados



Representa la lógica competitiva.



\---



\### Persistencia por etapas



Los cálculos importantes se almacenan.



No se recalculan constantemente.



Ejemplos:



\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada

\- ResultadoTemporada

\- MovimientoCategoria



\---



\### Configuración centralizada



La entidad estratégica del sistema es:



```text

CompetenciaConfig

```



Debe convertirse progresivamente en la fuente principal de configuración de las competiciones.



\---



\## Filosofía del Proyecto



Principio rector:



```text

Configurar antes que programar.

```



Antes de:



\- crear modelos nuevos

\- agregar campos

\- crear lógica específica



debe verificarse si el problema puede resolverse mediante configuración.



\---



\## Automatización con Supervisión Humana



La aplicación debe proponer.



El administrador debe decidir.



Ejemplos:



\- participantes sugeridos

\- ascensos sugeridos

\- descensos sugeridos

\- clasificaciones sugeridas

\- configuraciones sugeridas



La decisión final siempre pertenece al administrador.



\---



\## Generación de Nueva Temporada



Visión futura:



```text

Crear nueva temporada

↓

Buscar última temporada válida

↓

Calcular movimientos

↓

Sugerir participantes

↓

Permitir correcciones

↓

Generar temporada

```



sin reconstruir manualmente toda la estructura.



\---



\## Categorías



Las categorías son dinámicas.



Ejemplos válidos:



```text

A

B

C

```



```text

A

B

C

D

```



```text

A

B

C

D

E

```



El sistema no debe asumir una cantidad fija de categorías.



\---



\## Jerarquía de Categorías



Las categorías siempre son jerárquicas.



Ejemplo:



```text

A > B > C > D

```



La categoría superior representa un nivel competitivo superior.



\---



\## Hallazgo Arquitectónico Importante



Julio 2026.



Después de una auditoría completa del proyecto y del análisis de reglamentos oficiales se concluyó:



\### El modelo está más avanzado que los procesos



La mayoría de los modelos actuales son reutilizables y suficientemente flexibles.



La principal deuda técnica NO está en los modelos.



La principal deuda técnica está en los comandos de procesamiento.



\---



\## Problemas Identificados



Muchos procesos siguen utilizando valores hardcodeados.



Ejemplos:



\- cantidad de grupos

\- cantidad de clasificados

\- cantidad de ascensos

\- cantidad de descensos

\- clasificación a copas

\- estructura de instancias

\- rondas de playoffs



\---



\## Dirección Actual del Proyecto



La siguiente fase del backend no consiste en crear nuevos modelos.



La prioridad es:



\### Transformar el backend funcional en backend configurable.



Esto implica reemplazar reglas fijas por lectura desde configuraciones.



\---



\## Campos Estratégicos de CompetenciaConfig



Actualmente existen:



\- cantidad\_participantes

\- cantidad\_zonas

\- clasificados

\- cantidad\_ascensos

\- cantidad\_descensos

\- tiene\_playoff

\- tiene\_penales

\- permite\_equipos

\- usa\_tabla

\- usa\_af

\- usa\_av

\- usa\_da



Muchos procesos todavía no los utilizan correctamente.



\---



\## Objetivo de Largo Plazo



La creación futura de una competencia debería funcionar así:



```text

Seleccionar plantilla

↓

Generar configuración sugerida

↓

Modificar parámetros

↓

Crear competencia

↓

Generar estructura automáticamente

```



Incluyendo:



\- participantes

\- grupos

\- instancias

\- clasificaciones

\- llaves

\- tablas



\---



\## Integración API



La arquitectura futura contempla integración con APIs deportivas.



Objetivos:



\- fixture automático

\- resultados automáticos

\- cambios de programación

\- partidos suspendidos



La aplicación debe seguir funcionando aunque no exista una API disponible.



\---



\## Frontend



Todavía no es prioridad inmediata.



Antes de iniciar frontend se desea:



\- reducir hardcodeos

\- consolidar CompetenciaConfig

\- estabilizar procesos

\- consolidar generación automática



\---



\## Estado del Proyecto



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



\---



\## Regla de Trabajo Vigente



Antes de implementar una funcionalidad importante:



1\. Revisar si ya existe soporte en el modelo actual.

2\. Revisar si CompetenciaConfig ya contempla el caso.

3\. Revisar PLAN\_REFACTOR\_2026.md.

4\. Revisar VISION\_LARGO\_PLAZO.md.

5\. Revisar DECISIONES\_NEGOCIO.md.

6\. Evitar agregar modelos cuando el problema pueda resolverse mediante configuración.



La prioridad actual es mejorar configurabilidad y reducir deuda técnica, no aumentar cantidad de código.

