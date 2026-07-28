\# VISION\_LARGO\_PLAZO



Fecha:

2026-07-27



\---



\# Propósito



ProdeColumbia no busca simplemente digitalizar una planilla Excel.



El objetivo final es construir una plataforma integral para administrar competiciones de Prode de distintos formatos, con reglas configurables y mínima dependencia de código específico para cada torneo.



\---



\# Visión General



El sistema debe evolucionar desde:



```text

Competiciones programadas manualmente

```



hacia:



```text

Competiciones configuradas

y generadas automáticamente

```



La configuración debe convertirse progresivamente en el principal mecanismo de definición de comportamiento.



\---



\# Objetivo Final



Permitir que un administrador pueda crear una competición nueva mediante una interfaz gráfica y que el sistema sugiera automáticamente todas sus configuraciones principales.



Flujo esperado:



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



Sin necesidad de escribir código.



\---



\# Motor Configurable



La visión de largo plazo es que las competiciones no dependan de comandos específicos.



Deben depender de:



```text

PlantillaCompetencia

\+

CompetenciaConfig

```



\---



\# Plantillas



Las plantillas representan formatos reutilizables.



Ejemplos:



```text

Liga Profesional

```



```text

Copa Internacional

```



```text

Copa Eliminatoria

```



```text

Supercopa

```



Una plantilla debe servir como punto de partida para generar nuevas competiciones.



\---



\# CompetenciaConfig



CompetenciaConfig debe convertirse progresivamente en la principal fuente de comportamiento del sistema.



La intención es que cada vez más reglas surjan de configuración y no de código.



Ejemplos:



\- cantidad de participantes

\- cantidad de zonas

\- clasificados

\- ascensos

\- descensos

\- playoffs

\- penales

\- criterios de desempate



\---



\# Filosofía Principal



La regla general será:



```text

Configurar antes que programar.

```



Antes de crear:



\- nuevos modelos

\- nuevos campos

\- nuevos comandos específicos



debe verificarse si el problema puede resolverse mediante configuración.



\---



\# Familias de Competiciones



El análisis de los reglamentos permitió identificar cuatro grandes familias.



\---



\## Liga



Ejemplo:



```text

Liga Profesional Clausura

```



Formato típico:



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



\- posiciones

\- clasificación por tabla

\- ascensos

\- descensos

\- tabla anual



\---



\## Copa con Grupos



Ejemplos:



```text

Copa Libertadores

Copa Sudamericana

```



Formato típico:



```text

Grupos

↓

Clasificación

↓

Playoffs

```



Características:



\- grupos

\- ranking de clasificados

\- cruces de eliminación



\---



\## Copa Eliminatoria



Ejemplos:



```text

Copa Argentina

Copa Repechaje

```



Formato típico:



```text

Sorteo

↓

Ronda eliminatoria

↓

Sorteo

↓

Ronda eliminatoria

```



Características:



\- eliminación directa

\- sorteos sucesivos

\- penales de desempate



\---



\## Supercopa



Formato especial.



Características:



```text

Equipos temporales

↓

Doble eliminación

↓

Zona Ganadores

↓

Zona Perdedores

```



No puede modelarse como una copa tradicional.



\---



\# Equipos Temporales



La Supercopa justifica la existencia futura de:



```text

EquipoTemporal

```



y



```text

MiembroEquipoTemporal

```



Objetivo:



Agrupar temporalmente participantes para una competición específica.



Ejemplo:



```text

Equipo



Participante A

Participante B

Participante C

```



Los equipos no son permanentes.



Pueden cambiar en cada fecha.



\---



\# Generación Automática



La visión de largo plazo consiste en que el sistema pueda generar automáticamente:



\- grupos

\- clasificaciones

\- llaves

\- instancias

\- ascensos

\- descensos

\- temporadas futuras



a partir de configuración.



\---



\# Generación de Instancias



En el futuro las instancias no deberían crearse manualmente.



El sistema debería poder sugerir automáticamente:



```text

Fecha 1

Fecha 2

...

```



o



```text

Gru​pos

↓

Octavos

↓

Cuartos

↓

Semifinal

↓

Final

```



según el formato configurado.



\---



\# Generación de Llaves



Las llaves deberán soportar múltiples modalidades.



Ejemplos:



```text

Sorteo

```



```text

Seeding

```



```text

Ranking por grupos

```



```text

Doble eliminación

```



La arquitectura debe permanecer abierta para estas variantes.



\---



\# Integración con APIs



La visión futura contempla integración automática con proveedores de datos deportivos.



Objetivos:



\- obtener fixtures

\- obtener resultados

\- actualizar estados de partidos



sin intervención manual.



\---



\## Flujo Esperado



```text

API

↓

EquipoReal

↓

CalendarioReal

↓

PartidoReal

↓

InstanciaPartido

```



\---



\# Independencia de Proveedor



El sistema no debe depender de una única API.



Debe ser posible:



\- cambiar proveedor

\- combinar proveedores

\- seguir operando manualmente



si una API deja de funcionar.



\---



\# Frontend Futuro



El frontend deberá operar sobre un backend ya consolidado.



\---



\## Portal Administrador



Objetivos:



\- crear temporadas

\- crear competiciones

\- configurar reglas

\- administrar resultados

\- administrar participantes



\---



\## Portal Participante



Objetivos:



\- cargar pronósticos

\- consultar resultados

\- visualizar tablas

\- consultar históricos

\- consultar estadísticas



\---



\# Automatización de Temporadas



Objetivo futuro:



Generar automáticamente una nueva temporada utilizando la información obtenida de la temporada anterior.



El sistema deberá poder sugerir:



\- ascensos

\- descensos

\- clasificaciones

\- participantes activos



permitiendo correcciones manuales antes de confirmar.



\---



\# Históricos



La plataforma deberá evolucionar para ofrecer:



\- Hall of Fame

\- campeones

\- subcampeones

\- récords

\- rivalidades

\- estadísticas históricas



\---



\# Objetivo de Arquitectura



El objetivo no es programar:



```text

Liga Profesional 2026

```



ni



```text

Libertadores 2026

```



de forma aislada.



El objetivo es construir un motor capaz de crear:



```text

Liga Profesional

Libertadores

Sudamericana

Repechaje

Copa Argentina

Supercopa

```



y futuras competiciones mediante configuración.



\---



\# Situación Actual



Modelo:

90%



Backend Funcional:

90%



Backend Configurable:

60%



Frontend:

0%



\---



\# Prioridad Vigente



La prioridad actual del proyecto es:



```text

Transformar un backend funcional

en un backend configurable.

```



La eliminación progresiva de hardcodeos y la consolidación de CompetenciaConfig son los pasos necesarios para alcanzar esa visión.

