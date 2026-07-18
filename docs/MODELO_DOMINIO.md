\# MODELO DOMINIO



\## Entidades confirmadas



Participante



Categoria



Temporada



\---



\## Entidades aprobadas conceptualmente



ParticipanteTemporada



Competencia



ParticipacionCompetencia



FechaReal



PartidoReal



Pronostico



ResultadoPronostico



FechaProde



Enfrentamiento



TablaCompetencia



Playoff



\---



\## Filosofía



Separar:



Futbol Real



de



Prode



\---



\### Futbol Real



FechaReal



PartidoReal



ResultadoReal



\---



\### Prode



Pronostico



AF



AV



Enfrentamiento



Tabla



Playoff



\---



\## Relación principal



Participante

↓

Pronostico

↓

AF

↓

Enfrentamiento

↓

Tabla



\---



\## IMPORTANTE



No todos los participantes juegan todas las competencias.



No todos los participantes permanecen activos durante toda una competencia.



Por ese motivo debe existir:



ParticipacionCompetencia.



\---



\## IMPORTANTE



La categoría puede cambiar entre temporadas.



Por ese motivo debe existir:



ParticipanteTemporada.

