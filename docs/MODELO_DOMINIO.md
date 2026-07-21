\# MODELO DOMINIO V1



\## Personas



Participante



Categoria



ParticipanteTemporada



Temporada



\---



\## Competencias



TipoCompetencia



Competencia



CompetenciaConfig



ParticipacionCompetencia



InstanciaCompetencia



\---



\## Fútbol Real



CalendarioReal



PartidoReal



\---



\## Relación Competencia ↔ Partidos



InstanciaPartido



Permite:



\- habilitar/deshabilitar partidos

\- marcar penales

\- utilizar subconjuntos de partidos



\---



\## Pronósticos



Pronostico



ResultadoPronostico



ResumenParticipanteInstancia



\---



\## Núcleo



Enfrentamiento



La entidad principal del negocio.



Todo desemboca finalmente en un enfrentamiento.



\---



\## Históricos



ResultadoCompetencia



\---



\## Equipos temporales



EquipoTemporal



MiembroEquipoTemporal



Utilizados principalmente por Supercopa.



\---



\## Sorteos



Sorteo



Persistencia de sorteos realizados por la organización.



\---



\## Principios



Separar:



Fútbol Real



de



Prode



\---



No hardcodear:



\- categorías

\- participantes

\- formatos de competencia

\- cantidad de partidos

\- cantidad de zonas



\---



Toda competencia debe poder configurarse desde la interfaz administrativa.



