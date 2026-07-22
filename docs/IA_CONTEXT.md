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

\- futuras competiciones



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



\### Backend



\- Python

\- Django



\### Base de Datos



\- SQLite en desarrollo

\- PostgreSQL en producción (previsto)



\### Versionado



\- Git

\- GitHub



\### Repositorio



\- ProdeColumbia



\---



\## Estado Actual



Implementado:



\### Base



\- Django operativo

\- Admin operativo

\- Importador Excel

\- Participantes

\- Categorías

\- Temporadas



\### Competiciones



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



\---



\## Datos Existentes



\### Participantes



\- 90 participantes reales



\### Categorías



\- A

\- B

\- C



\### Temporada



\- 2026



\### Competencias



\- Liga Profesional Clausura 2026

\- Copa Repechaje 2026

\- Copa Argentina 2026

\- Supercopa 2026



\### Equipos Reales



\- 32 equipos cargados



\### Calendario



\- Fecha 1 cargada



\### Partidos



\- 15 partidos reales cargados



\### Pronósticos



\- Primer flujo completo validado



\### Resultados



\- ResultadoPronostico validado



\### Resúmenes



\- ResumenParticipanteInstancia validado



\---



\## Principios Arquitectónicos



Separar completamente:



\### Fútbol Real



de



\### Prode



\---



\### Fútbol Real



\- EquipoReal

\- CalendarioReal

\- PartidoReal



Representa hechos objetivos.



\---



\### Prode



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- Enfrentamiento

\- RankingTemporada

\- ResultadoCompetencia



Representa la lógica competitiva.



\---



\## Flujo Principal



Participante



↓



ParticipanteTemporada



↓



Pronostico



↓



InstanciaPartido



↓



PartidoReal



↓



ResultadoPronostico



↓



ResumenParticipanteInstancia



↓



Enfrentamiento



↓



RankingTemporada



↓



ResultadoCompetencia



\---



\## Entidad Central



La entidad principal del negocio es:



\### ENFRENTAMIENTO



No Partido.



No Pronóstico.



No Resultado.



Toda la lógica competitiva converge finalmente en un enfrentamiento entre participantes.



\---



\## Dominio V1



\### Personas



\- Participante

\- Categoria

\- Temporada

\- ParticipanteTemporada



\### Competiciones



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



\### Núcleo Competitivo



\- Enfrentamiento



\### Históricos



\- RankingTemporada

\- ReglaClasificacion

\- ResultadoCompetencia



\### Equipos Temporales



\- EquipoTemporal

\- MiembroEquipoTemporal



\### Futuro



\- Sorteo (V2)



\---



\## Decisiones Congeladas



\### Participantes



\- Los participantes nunca se eliminan.

\- La categoría vive en ParticipanteTemporada.



\### Competiciones



\- Las competiciones se crean desde PlantillaCompetencia.

\- Cada competencia posee CompetenciaConfig propia.

\- InstanciaCompetencia reemplaza conceptualmente a Fecha.



\### Fútbol Real



\- Los partidos reales son independientes de las competiciones.

\- InstanciaPartido relaciona competiciones con partidos reales.

\- Los equipos utilizan nombres oficiales.

\- Los resultados reales se almacenan mediante goles.



\### Pronósticos



\- Actualmente se utiliza L/E/V.

\- El diseño debe permitir soportar resultado exacto en el futuro.

\- ResultadoPronostico almacena resultado real, acierto y puntos.



\### Resúmenes



\- AF y AV se almacenan en ResumenParticipanteInstancia.

\- DA NO pertenece al resumen individual.

\- DA pertenece al enfrentamiento entre participantes.



\### Supercopa



\- Utiliza equipos temporales.



\---



\## Requisitos Funcionales Descubiertos



\### Bloqueo de Boletas



Las boletas deberán bloquearse automáticamente.



Objetivo inicial:



\- una hora antes del primer partido válido de la instancia



\---



\### Visibilidad de Boletas



Antes del cierre:



\- el participante sólo puede ver su propia boleta



Después del cierre:



\- todos los participantes pueden ver todas las boletas



\---



\### Partidos Decisivos



El sistema deberá identificar:



\- partidos donde dos participantes realizaron pronósticos distintos



Estos partidos deberán destacarse visualmente.



\---



\### Carga Administrativa



Los administradores deberán poder:



\- crear boletas

\- modificar boletas

\- cargar boletas para terceros



\---



\### Auditoría



Deberá registrarse:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de creación

\- fecha de modificación



\---



\### Escudos



Los equipos deberán soportar:



\- escudos oficiales

\- almacenamiento local



\---



\### Zona Horaria



Pendiente configurar:



America/Argentina/Buenos\_Aires



\---



\## Próximo Objetivo



Implementar:



\### Enfrentamiento



Luego:



\### RankingTemporada



\### ReglaClasificacion



\### ResultadoCompetencia



El backend continúa siendo la prioridad actual.



El frontend se desarrollará posteriormente sobre una base funcional ya validada.

