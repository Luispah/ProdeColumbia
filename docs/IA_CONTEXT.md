\# IA\_CONTEXT



\## Proyecto



ProdeColumbia.



Aplicación web para administrar el Prode interno que actualmente se gestiona mediante Excel.



El objetivo es reemplazar gradualmente la operatoria manual por una plataforma web.



\---



\## Tecnología



Backend:

\- Python

\- Django 6



Base de datos:

\- SQLite (desarrollo)

\- PostgreSQL (previsto para producción)



Control de versiones:

\- Git

\- GitHub



Repositorio:

\- ProdeColumbia



\---



\## Estado actual



Implementado:



\- Django funcionando

\- Admin funcionando

\- Participante

\- Categoria

\- Temporada

\- Importador de participantes



Datos cargados:



\- 90 participantes reales

\- Categorías A/B/C

\- Temporada 2026



\---



\## Conceptos del negocio



La entidad principal NO es Partido.



La entidad principal es Enfrentamiento.



Flujo:



Partido Real

↓

Pronóstico

↓

AF / AV

↓

Enfrentamiento

↓

Tabla

↓

Playoffs



\---



\## Principios de diseño



No hardcodear:



\- categorías

\- cantidad de categorías

\- cantidad de participantes

\- cantidad de temporadas



Diseñar para soportar:



\- Liga

\- Copa Argentina

\- Supercopa

\- futuras competencias



\---



\## Situación actual



Categoria ya existe como tabla.



Participante todavía almacena categoria como texto.



La migración a ForeignKey fue intentada y falló.



Debe rediseñarse correctamente.



\---



\## Próximo paso



Diseñar el modelo de dominio completo antes de agregar más modelos.



\## Modelo Dominio V1 (congelado)



Participante



Categoria



Temporada



ParticipanteTemporada



TipoCompetencia



Competencia



CompetenciaConfig



ParticipacionCompetencia



InstanciaCompetencia



InstanciaPartido



CalendarioReal



PartidoReal



Pronostico



ResultadoPronostico



ResumenParticipanteInstancia



Enfrentamiento



ResultadoCompetencia



EquipoTemporal



MiembroEquipoTemporal



Sorteo



\---



\## Decisiones confirmadas



\- La categoría pertenece a ParticipanteTemporada.

\- Se guardan históricos.

\- Se guardan AF, AV y DA.

\- La Supercopa utilizará equipos temporales.

\- Las competencias se basan en partidos reales.

\- Los partidos reales pueden reutilizarse entre múltiples competencias.

\- Cada competencia puede decidir qué partidos puntúan.

