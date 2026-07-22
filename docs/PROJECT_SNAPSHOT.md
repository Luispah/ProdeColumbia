\# PROJECT SNAPSHOT



Fecha:



2026-07-21



\---



\# Estado General



Proyecto:



ProdeColumbia



Repositorio GitHub operativo.



Dominio V1 implementado parcialmente y validado mediante pruebas reales.



Arquitectura principal consolidada.



\---



\# Entorno



Python 3.14



Django 6



SQLite



Git



GitHub



\---



\# Estado Actual



La aplicación ya puede ejecutar el flujo completo:



Participante



↓



ParticipanteTemporada



↓



Pronóstico



↓



InstanciaPartido



↓



PartidoReal



↓



ResultadoPronostico



↓



ResumenParticipanteInstancia



\---



\# Modelos Implementados



\## Base



\- Participante

\- Categoria

\- Temporada



\## Competiciones



\- PlantillaCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia



\## Fútbol Real



\- EquipoReal

\- CalendarioReal

\- PartidoReal

\- InstanciaPartido



\## Juego



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



\---



\# Datos Existentes



\## Participantes



90



\## Categorías



\- A

\- B

\- C



\## Temporada Activa



2026



\## Plantillas



\- Liga Profesional

\- Copa Repechaje

\- Copa Argentina

\- Supercopa



\## Competencias



\- Liga Profesional Clausura 2026

\- Copa Repechaje 2026

\- Copa Argentina 2026

\- Supercopa 2026



\## ParticipantesTemporada



90 registros generados



\## InstanciasCompetencia



38 registros generados



\## Equipos Reales



32 registros



Incluye:



\- Estudiantes

\- Estudiantes (RC)

\- Gimnasia

\- Gimnasia (Mza)



\## Calendarios Reales



\- Liga Profesional Clausura 2026 - Fecha 1



\## Partidos Reales



15 partidos cargados para Fecha 1



\## Pronósticos



15 pronósticos de prueba



Participante:



\- Pablo Camporini



\## Resultados de Pronóstico



Generados correctamente para los partidos evaluados.



\## Resúmenes



Generado correctamente:



\- Pablo Camporini

\- Fecha 1

\- AF = 2

\- AV = 0

\- Puntos = 2



\---



\# Validaciones Realizadas



\## Equipos



Se decidió utilizar nombres oficiales como fuente única.



No se utilizarán alias internos.



Las boletas futuras deberán utilizar los mismos nombres almacenados en el sistema.



\## Resultados Reales



Los partidos almacenan:



\- goles\_local

\- goles\_visitante



El sistema deriva automáticamente:



\- L

\- E

\- V



a partir de dichos resultados.



\## Pronósticos



Actualmente:



\- L

\- E

\- V



Diseño preparado para soportar futuras modalidades:



\- resultado exacto

\- variantes especiales por competencia



\## AF / AV



Validados mediante pruebas reales.



Resultado esperado obtenido:



AF = 2



AV = 0



\---



\# Estado Arquitectónico



Dominio V1 vigente.



No se detectaron cambios estructurales necesarios luego de analizar:



\- Liga Profesional Clausura

\- Copa Repechaje

\- Copa Argentina

\- Copa Libertadores

\- Copa Sudamericana

\- Supercopa



La arquitectura sigue considerándose válida.



\---



\# Próxima Fase



\## Implementación



Enfrentamiento



Objetivo:



Representar partidos entre participantes y calcular:



\- ganador

\- perdedor

\- empate

\- diferencias de AF

\- diferencias de AV

\- reglas de desempate



\---



\# Fases Pendientes



\## Fase Competitiva



\- Enfrentamiento



\## Fase Ranking



\- RankingTemporada

\- ResultadoCompetencia

\- ReglaClasificacion



\## Fase Deportiva



\- Ascensos

\- Descensos

\- Clasificaciones



\## Fase Frontend



\- Portal Administrador

\- Portal Participante

\- Boletas online

\- Visualización de tablas

\- Historiales



\## Fase Integraciones



\- API de fútbol

\- Importación automática de fixtures

\- Actualización automática de resultados



\---



\# Requisitos Funcionales Descubiertos



\## Bloqueo de Boletas



La edición deberá bloquearse automáticamente antes del inicio de los partidos.



Objetivo inicial:



1 hora antes del primer partido válido de la instancia.



\## Visibilidad de Boletas



Antes del cierre:



\- cada participante sólo ve su propia boleta



Después del cierre:



\- todos los participantes pueden visualizar todas las boletas



\## Partidos Decisivos



El sistema deberá identificar y resaltar:



\- partidos donde dos participantes realizaron pronósticos diferentes



\## Carga Administrativa



Los administradores deberán poder:



\- crear boletas

\- modificar boletas

\- cargar boletas para terceros



\## Auditoría



Registrar:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de modificación



\## Escudos



Los equipos deberán soportar escudos oficiales.



Preferencia:



\- almacenamiento local

\- no depender permanentemente de una API externa



\## Zona Horaria



Pendiente configurar:



America/Argentina/Buenos\_Aires



para evitar diferencias entre horario del servidor y horario visible para usuarios.



\---



\# Estado del Proyecto



El proyecto dejó la etapa de diseño conceptual.



La aplicación ya permite cargar y evaluar una fecha completa de Prode utilizando datos reales y modelos persistidos en base de datos.

