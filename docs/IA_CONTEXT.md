\# IA\_CONTEXT



\## Proyecto



ProdeColumbia.



Aplicación web para administrar integralmente el Prode Columbia, actualmente gestionado mediante Excel.



No es un simple sistema de pronósticos deportivos.



Modela:



\- Liga Profesional Apertura

\- Liga Profesional Clausura

\- Copa Argentina

\- Copa Libertadores

\- Copa Sudamericana

\- Copa Repechaje

\- Supercopa

\- Futuras competiciones



\---



\## Objetivo



Reemplazar progresivamente la operatoria manual basada en Excel por una plataforma web centralizada.



El objetivo NO es únicamente registrar pronósticos.



También debe gestionar:



\- participantes

\- categorías

\- temporadas

\- ascensos

\- descensos

\- clasificaciones

\- enfrentamientos

\- históricos

\- estadísticas

\- rankings



\---



\## Tecnología



Backend



\- Python

\- Django



Base de datos



\- SQLite en desarrollo

\- PostgreSQL en producción (previsto)



Versionado



\- Git

\- GitHub



Repositorio



\- ProdeColumbia



\---



\## Estado actual



Implementado:



\- Django operativo

\- Admin operativo

\- Participantes

\- Categorías

\- Temporadas

\- Importador Excel



Datos existentes:



\- 90 participantes reales

\- Categorías A/B/C

\- Temporada 2026



\---



\## Principios arquitectónicos



Separar completamente:



Fútbol Real



de



Prode



\---



Fútbol Real:



CalendarioReal



PartidoReal



\---



Prode:



Pronostico



AF



AV



Enfrentamiento



Tabla



Playoff



\---



\## Entidad central



La entidad principal del negocio es:



ENFRENTAMIENTO



No Partido.



No Pronóstico.



Todo desemboca finalmente en un enfrentamiento.



\---



\## Dominio V1 Congelado



\### Núcleo



Participante



Categoria



Temporada



ParticipanteTemporada



\### Competiciones



PlantillaCompetencia



Competencia



CompetenciaConfig



ParticipacionCompetencia



InstanciaCompetencia



\### Fútbol Real



CalendarioReal



PartidoReal



InstanciaPartido



\### Pronósticos



Pronostico



ResultadoPronostico



ResumenParticipanteInstancia



\### Núcleo del Prode



Enfrentamiento



\### Históricos



RankingTemporada



ReglaClasificacion



ResultadoCompetencia



\### Equipos Temporales



EquipoTemporal



MiembroEquipoTemporal



\### Futuro



Sorteo (V2)



\---



\## Decisiones congeladas



\- La categoría vive en ParticipanteTemporada.

\- Los participantes nunca se eliminan.

\- AF, AV y DA se persisten.

\- Los históricos se persisten.

\- Las competencias se crean a partir de PlantillaCompetencia.

\- Cada competencia posee configuración propia.

\- InstanciaCompetencia reemplaza conceptualmente a "Fecha".

\- Los partidos reales son independientes de las competencias.

\- Una competencia puede utilizar todos o algunos de los partidos disponibles.

\- La Supercopa utiliza equipos temporales.

