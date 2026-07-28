\# REGLAS\_NEGOCIO



Fecha:

2026-07-27



\---



\# Principio General



ProdeColumbia no es únicamente un sistema de pronósticos.



Es un sistema de administración competitiva.



Debe modelar:



\- participantes

\- temporadas

\- categorías

\- competiciones

\- pronósticos

\- resultados

\- enfrentamientos

\- clasificaciones

\- ascensos

\- descensos

\- históricos



\---



\# Participantes



Los participantes nunca se eliminan físicamente del sistema.



Pueden:



\- retirarse

\- reincorporarse

\- cambiar de categoría

\- permanecer inactivos durante varias temporadas



La información histórica debe conservarse permanentemente.



\---



\# Categorías



Las categorías son configurables.



No deben existir categorías hardcodeadas en el dominio.



Ejemplos actuales:



\- A

\- B

\- C



La arquitectura debe permitir agregar o eliminar categorías futuras.



\---



\# Temporadas



Las temporadas son independientes entre sí.



Cada participante genera una participación específica por temporada mediante:



```text

ParticipanteTemporada

```



La categoría pertenece a la temporada y no al participante.



\---



\# ParticipanteTemporada



Es la entidad oficial para representar la situación deportiva de una persona en una temporada específica.



Permite modelar:



\- ascensos

\- descensos

\- nuevos participantes

\- reincorporaciones

\- históricos



\---



\# Competiciones



Toda competencia debe crearse desde:



```text

PlantillaCompetencia

```



y configurarse mediante:



```text

CompetenciaConfig

```



\---



\# CompetenciaConfig



CompetenciaConfig es la fuente oficial de configuración del sistema.



Toda regla configurable debe derivarse de esta entidad antes de crear nuevas estructuras o hardcodear lógica.



Ejemplos:



\- cantidad\_participantes

\- cantidad\_zonas

\- clasificados

\- cantidad\_ascensos

\- cantidad\_descensos

\- tiene\_playoff

\- tiene\_penales



\---



\# Regla Arquitectónica



Antes de crear:



\- un nuevo modelo

\- un nuevo campo

\- una nueva lógica específica



debe verificarse si el requerimiento puede resolverse mediante CompetenciaConfig.



\---



\# Persistencia de Cálculos



Los cálculos importantes deben almacenarse.



No deben recalcularse constantemente.



Ejemplos:



\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada

\- ResultadoTemporada

\- MovimientoCategoria



\---



\# Pronósticos



Actualmente los participantes pronostican:



\- Local

\- Empate

\- Visitante



El diseño debe permanecer preparado para futuras extensiones:



\- resultado exacto

\- modalidades especiales

\- reglas alternativas



\---



\# Resultados Reales



Los resultados oficiales se almacenan mediante:



\- goles\_local

\- goles\_visitante



A partir de dichos valores el sistema puede derivar:



\- Local

\- Empate

\- Visitante



cuando sea necesario.



\---



\# AF y AV



AF y AV se calculan a partir de:



```text

ResultadoPronostico

```



Se almacenan en:



```text

ResumenParticipanteInstancia

```



AF y AV forman parte de la información persistida.



No deben calcularse dinámicamente en cada consulta.



\---



\# DA



DA no pertenece al participante.



DA no pertenece al resumen individual.



DA pertenece a la comparación entre participantes.



Por lo tanto su lugar natural es:



```text

Enfrentamiento

```



\---



\# Enfrentamiento



Es la entidad competitiva principal del dominio.



Toda competencia termina expresándose mediante enfrentamientos entre participantes.



Debe permitir determinar:



\- ganador

\- perdedor

\- empate

\- puntos

\- comparaciones deportivas



\---



\# Tablas



Existen tres niveles de acumulación:



\## TablaInstancia



Acumula resultados de una instancia.



\---



\## TablaCompetencia



Acumula resultados de una competencia.



\---



\## TablaTemporada



Acumula resultados de toda la temporada.



Es la fuente principal para:



\- clasificación a copas

\- ascensos

\- descensos



\---



\# ResultadoTemporada



Representa la consecuencia deportiva final de una temporada.



Ejemplos:



\- Libertadores

\- Sudamericana

\- Ascenso

\- Descenso

\- Repechaje



\---



\# MovimientoCategoria



Representa el movimiento deportivo entre categorías.



Posibles valores:



\- Ascenso

\- Descenso

\- Mantiene



\---



\# Copas



Las copas pueden utilizar:



\- fase de grupos

\- clasificación

\- eliminación directa



o cualquier combinación de ellas.



No debe asumirse que todas las copas poseen la misma estructura.



\---



\# Grupos



Los grupos representan una fase clasificatoria.



Deben poder configurarse mediante:



```text

CompetenciaConfig.cantidad\_zonas

```



No deben depender de cantidades hardcodeadas.



\---



\# Clasificaciones



La cantidad de clasificados debe obtenerse desde:



```text

CompetenciaConfig.clasificados

```



No debe depender de posiciones fijas programadas en código.



\---



\# Playoffs



Los playoffs representan fases eliminatorias.



La dirección actual del proyecto es evolucionar hacia un sistema totalmente configurable.



El objetivo futuro es soportar:



\- Supercopa

\- Repechaje

\- Libertadores

\- Sudamericana

\- Copa Argentina



sin modificar código para cada competencia.



\---



\# Ascensos y Descensos



La cantidad de ascensos y descensos debe obtenerse desde configuración.



No debe depender de valores fijos definidos en comandos.



\---



\# Fútbol Real



Todas las competiciones utilizan partidos reales.



Una competencia puede:



\- utilizar todos los partidos

\- utilizar algunos partidos

\- excluir partidos suspendidos

\- utilizar partidos especiales

\- definir instancias con penales



\---



\# Equipos Reales



Los equipos deben utilizar nombres oficiales.



No deben utilizarse alias como fuente principal.



Las boletas deben utilizar exactamente los nombres definidos en la base de datos.



\---



\# Supercopa



La Supercopa utilizará equipos temporales.



No necesariamente participantes individuales.



Por este motivo permanecen pendientes:



\- EquipoTemporal

\- MiembroEquipoTemporal



\---



\# Históricos



Los resultados finales deben conservarse.



El proyecto deberá permitir construir:



\- Hall of Fame

\- campeones históricos

\- rivalidades

\- récords

\- estadísticas acumuladas



\---



\# Bloqueo de Boletas



Las boletas sólo podrán modificarse antes de la hora de cierre.



Objetivo inicial:



```text

1 hora antes del primer partido válido

de la instancia

```



\---



\# Visibilidad de Boletas



Antes del cierre:



\- cada participante sólo puede ver su propia boleta



Después del cierre:



\- todos los participantes pueden visualizar todas las boletas



\---



\# Partidos Decisivos



El sistema deberá identificar automáticamente partidos donde dos participantes realizaron pronósticos distintos.



Estos partidos son los únicos que pueden producir diferencias deportivas entre ambos participantes.



\---



\# Carga Administrativa



Los administradores deben poder:



\- crear boletas

\- modificar boletas

\- cargar boletas para terceros



\---



\# Auditoría



Toda carga deberá permitir registrar:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de creación

\- fecha de modificación



El objetivo es garantizar trazabilidad completa.



\---



\# Escudos



Los equipos deberán soportar:



\- escudos oficiales

\- almacenamiento local



Prioridad:



evitar dependencia permanente de APIs externas.



\---



\# Zona Horaria



La aplicación deberá operar utilizando:



```text

America/Argentina/Buenos\_Aires

```



como zona horaria oficial.



\---



\# Hallazgo de Auditoría Julio 2026



Luego de analizar modelos, comandos y documentación se concluyó:



\## El modelo es más maduro que los procesos



La principal deuda técnica actual NO se encuentra en los modelos.



La principal deuda técnica se encuentra en los comandos que aún utilizan valores hardcodeados.



\---



\# Prioridad Actual



La prioridad inmediata del proyecto es:



```text

Transformar un backend funcional

en un backend configurable

```



utilizando:



```text

CompetenciaConfig

```



como fuente principal de configuración del sistema.

