\# ARQUITECTURA



\## Principio principal



Separar:



Fútbol Real



de



Prode



\---



\## Fútbol Real



CalendarioReal



PartidoReal



\---



\## Prode



Pronostico



ResultadoPronostico



ResumenParticipanteInstancia



Enfrentamiento



RankingTemporada



ResultadoCompetencia



\---



\## Diseño modular



Las competiciones no deben depender de código.



Toda nueva competición debe generarse a partir de:



PlantillaCompetencia



\+



CompetenciaConfig



\---



\## Integraciones



V1



Importación Excel



\---



V2



API-Football



\---



V2



TheSportsDB



\---



Nunca depender de una única fuente externa.

