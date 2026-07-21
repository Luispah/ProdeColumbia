\# MODELO DOMINIO V1



\## Personas



Participante



Representa una persona.



Nunca se elimina.



\---



Categoria



Representa una división.



Ejemplos:



A

B

C



\---



Temporada



Representa un ciclo anual.



Ejemplos:



2026

2027

2028



\---



ParticipanteTemporada



Representa la participación de una persona dentro de una temporada determinada.



Resuelve:



\- ascensos

\- descensos

\- participantes nuevos

\- participantes que regresan

\- histórico



\---



\## Competiciones



PlantillaCompetencia



Modelo base para generar nuevas competiciones.



Ejemplos:



\- Liga Profesional

\- Copa Repechaje

\- Copa Argentina

\- Supercopa



\---



Competencia



Instancia concreta de una competición.



Ejemplos:



\- Clausura 2026

\- Copa Repechaje 2026



\---



CompetenciaConfig



Configura reglas de negocio sin modificar código.



\---



ParticipacionCompetencia



Representa la participación de un jugador en una competición.



\---



InstanciaCompetencia



Representa cualquier etapa.



Ejemplos:



Fecha 1



Fecha 2



32avos



Octavos



Final



\---



\## Fútbol Real



CalendarioReal



Agrupa fechas reales del fútbol argentino.



\---



PartidoReal



Representa un partido real.



Ejemplo:



River vs Boca



\---



InstanciaPartido



Relaciona una competencia con partidos específicos.



Permite:



\- excluir partidos

\- marcar penales

\- utilizar subconjuntos de partidos



\---



\## Pronósticos



Pronostico



ResultadoPronostico



ResumenParticipanteInstancia



\---



\## Entidad Central



Enfrentamiento



Representa un duelo entre competidores.



Todo el modelo converge finalmente en esta entidad.



\---



\## Históricos



RankingTemporada



Tabla anual y acumulados.



\---



ReglaClasificacion



Determina accesos a copas y otras competiciones.



\---



ResultadoCompetencia



Almacena resultados definitivos.



\---



\## Equipos Temporales



EquipoTemporal



MiembroEquipoTemporal



Utilizados principalmente por Supercopa.

