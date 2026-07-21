\# PROJECT SNAPSHOT



Fecha del snapshot:



2026-07-18



\---



\## Git



Repositorio:



ProdeColumbia



Primer hito publicado en GitHub.



\---



\## Entorno



Python:

3.14.3



Django:

6.0.7



Git:

instalado



\---



\## Base de datos



SQLite



Archivo:



db.sqlite3



\---



\## Aplicación



core



\---



\## Modelos existentes



Participante



Categoria



Temporada



\---



\## Participantes



Cantidad:



90



Importados desde:



01\_Participantes\_Actuales.xlsx



\---



\## Categorías



A



B



C



\---



\## Temporadas



2026 (activa)



\---



\## Funcionalidades operativas



Admin



Importador de participantes



Gestión de categorías



Gestión de temporadas



\---



\## Riesgos conocidos



La categoría del participante todavía está modelada como texto.



No existe todavía modelo de competencia.



No existe todavía modelo de enfrentamiento.



No existe todavía modelo de pronóstico.



\---



\## Estado de arquitectura



Dominio V1 definido conceptualmente.



No implementado todavía en Django.



Entidades planeadas:



\- ParticipanteTemporada

\- TipoCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia

\- InstanciaPartido

\- CalendarioReal

\- PartidoReal

\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- Enfrentamiento

\- ResultadoCompetencia

\- EquipoTemporal

\- MiembroEquipoTemporal

\- Sorteo



\---



\## Próximo paso aprobado



Transformar el Dominio V1 en modelos Django.

