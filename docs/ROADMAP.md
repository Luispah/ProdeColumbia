\# ROADMAP



\## DOMINIO V1



Estado:



✅ CONGELADO



✅ VALIDADO CONTRA LOS REGLAMENTOS VIGENTES



Incluye:



\- Participantes

\- Temporadas

\- Competiciones

\- Fútbol Real

\- Pronósticos

\- Resultados

\- Resúmenes



\---



\## FASE 1 DJANGO



Estado:



✅ COMPLETADA



Implementado:



\- ParticipanteTemporada

\- PlantillaCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia



\---



\## FASE 2 DJANGO



Estado:



✅ COMPLETADA



Implementado:



\- EquipoReal

\- CalendarioReal

\- PartidoReal

\- InstanciaPartido



Validado mediante:



\- Equipos reales cargados

\- Calendario Fecha 1

\- Partidos reales cargados



\---



\## FASE 3 DJANGO



Estado:



✅ COMPLETADA



Implementado:



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



Validado mediante:



\- Pronósticos reales

\- Resultados reales

\- AF

\- AV

\- Puntos



\---



\## FASE 4 DJANGO



Estado:



🔄 EN CURSO



Próximo objetivo:



\- Enfrentamiento



Posteriormente:



\- EquipoTemporal

\- MiembroEquipoTemporal



Objetivo:



Representar duelos directos entre participantes y soportar competiciones por equipos.



\---



\## FASE 5 DJANGO



Estado:



⏳ PENDIENTE



Implementar:



\- RankingTemporada

\- ReglaClasificacion

\- ResultadoCompetencia



Objetivo:



\- tablas anuales

\- ascensos

\- descensos

\- clasificación a copas

\- históricos



\---



\## FUNCIONALIDAD PENDIENTE (ALTA PRIORIDAD)



\### Bloqueo de Boletas



Implementar cierre automático.



Objetivo inicial:



\- 1 hora antes del primer partido válido.



\---



\### Visibilidad de Boletas



Antes del cierre:



\- sólo el propietario visualiza la boleta



Después del cierre:



\- todos los participantes pueden visualizar todas las boletas



\---



\### Partidos Decisivos



Identificar partidos donde dos participantes tienen pronósticos diferentes.



Mostrar visualmente dichos partidos.



\---



\### Carga Administrativa



Permitir:



\- creación de boletas por terceros

\- modificación de boletas por terceros



\---



\### Auditoría



Registrar:



\- propietario de la boleta

\- usuario que efectuó la carga

\- fecha de creación

\- fecha de modificación



\---



\### Zona Horaria Argentina



Configurar:



America/Argentina/Buenos\_Aires



\---



\### Escudos



Soporte para:



\- escudos oficiales

\- almacenamiento local



\---



\## INTEGRACIONES FUTURAS



\### Importación Automática



\- Fixture

\- Resultados

\- Horarios



Origen previsto:



\- APIs de fútbol



\---



\### Actualización Automática



\- resultados de partidos

\- estados de encuentros

\- horarios



\---



\## FRONTEND



Estado:



⏳ PENDIENTE



\### Administrador



\- gestión de temporadas

\- competiciones

\- fixture

\- resultados

\- participantes



\### Participante



\- carga de boletas

\- visualización de resultados

\- historial

\- estadísticas



\---



\## ESTADÍSTICAS E HISTÓRICOS



\### Hall of Fame



\- campeones

\- subcampeones

\- récords



\### Rivalidades



\- historial entre participantes



\### Estadísticas Avanzadas



\- AF históricos

\- AV históricos

\- efectividad

\- rendimiento por competencia

\- rendimiento por temporada



\---



\## ESTADO ACTUAL DEL PROYECTO



El sistema ya permite:



Participante



↓



Pronostico



↓



PartidoReal



↓



ResultadoPronostico



↓



ResumenParticipanteInstancia



con datos persistidos y validados en base de datos.



Próximo desarrollo principal:



Enfrentamiento.

