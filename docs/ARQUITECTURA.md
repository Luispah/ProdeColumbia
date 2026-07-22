\# ARQUITECTURA



\## Principio Principal



Separar completamente:



Fútbol Real



de



Prode



Esta decisión permite:



\- reutilizar partidos reales en múltiples competiciones

\- soportar distintos formatos de competición

\- incorporar nuevas reglas sin modificar los datos deportivos

\- integrar múltiples fuentes externas de información



\---



\# Capa Fútbol Real



Representa hechos objetivos del mundo real.



\## EquipoReal



Fuente única de verdad para los equipos.



Utiliza nombres oficiales.



Preparado para incorporar:



\- escudos

\- información adicional

\- integraciones externas



\---



\## CalendarioReal



Agrupa partidos reales.



Ejemplo:



```text

Liga Profesional Clausura 2026 - Fecha 1

```



\---



\## PartidoReal



Representa un partido real.



Almacena:



\- local

\- visitante

\- fecha

\- hora

\- goles local

\- goles visitante

\- estado



El resultado oficial siempre se almacena mediante goles.



A partir de esos valores el sistema deriva:



```text

L

E

V

```



cuando es necesario.



\---



\# Capa Prode



Representa la participación de los jugadores.



\## Pronostico



Almacena la predicción realizada por un participante.



Actualmente:



```text

L

E

V

```



\---



\## ResultadoPronostico



Representa la evaluación de un pronóstico.



Almacena:



\- resultado real

\- acierto

\- puntos



\---



\## ResumenParticipanteInstancia



Representa el acumulado de una instancia.



Almacena:



\- partidos evaluados

\- AF

\- AV

\- puntos



\---



\## Enfrentamiento



Entidad central del negocio.



Responsable de representar:



```text

Participante A

vs

Participante B

```



y resolver:



\- ganador

\- perdedor

\- empate

\- DA

\- desempates



\---



\## RankingTemporada



Representa tablas acumuladas.



Responsable de:



\- ascensos

\- descensos

\- clasificación a copas

\- rankings históricos



\---



\## ResultadoCompetencia



Representa resultados definitivos de una competición.



Ejemplos:



\- Campeón

\- Subcampeón

\- Ascendido

\- Descendido

\- Clasificado



\---



\# Arquitectura de Competiciones



Las competiciones no deben depender de código.



Toda competición debe generarse mediante:



```text

PlantillaCompetencia

\+

CompetenciaConfig

```



Lo que permite crear nuevas competiciones sin programar.



\---



\# Arquitectura de Instancias



InstanciaCompetencia reemplaza el concepto tradicional de fecha.



Puede representar:



\- Fecha

\- Ronda

\- Playoff

\- Final

\- Etapa especial



\---



\## InstanciaPartido



Es la capa de unión entre:



```text

InstanciaCompetencia

```



y



```text

PartidoReal

```



Permite:



\- reutilizar partidos

\- excluir partidos

\- marcar penales

\- utilizar subconjuntos de encuentros

\- soportar múltiples competiciones simultáneamente



\---



\# Flujo Principal



```text

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

```



\---



\# Integraciones



\## V1



Importación mediante Excel.



Fuentes manuales.



\---



\## V2



Integración con APIs deportivas.



Posibles fuentes:



\- API-Football

\- TheSportsDB



\---



\# Regla de Integración



Nunca depender de una única fuente externa.



El sistema debe poder:



\- cambiar de API

\- combinar múltiples APIs

\- continuar funcionando mediante importaciones manuales



\---



\# Frontend Futuro



La implementación actual utiliza Django Admin como interfaz operativa.



El objetivo final incluye:



\## Portal Administrador



\- gestión de temporadas

\- gestión de competiciones

\- gestión de participantes

\- carga de resultados

\- administración de boletas



\## Portal Participante



\- carga de pronósticos

\- consulta de resultados

\- historial personal

\- estadísticas

\- enfrentamientos



\---



\# Requisitos Arquitectónicos Pendientes



\## Bloqueo de Boletas



Las boletas deberán cerrarse automáticamente.



Objetivo inicial:



\- una hora antes del primer partido válido



\---



\## Visibilidad de Boletas



Antes del cierre:



\- privadas



Después del cierre:



\- públicas para todos los participantes



\---



\## Auditoría



Registrar:



\- propietario de la boleta

\- usuario que la cargó

\- fecha de modificación



\---



\## Partidos Decisivos



Identificar enfrentamientos donde los participantes realizaron pronósticos diferentes.



Estos partidos deberán destacarse visualmente.



\---



\## Escudos



Los equipos deberán soportar almacenamiento local de escudos oficiales.



\---



\## Zona Horaria



El sistema deberá utilizar:



```text

America/Argentina/Buenos\_Aires

```



como configuración principal.

