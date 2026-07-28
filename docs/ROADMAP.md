\# ROADMAP



Fecha de actualización:

2026-07-27



\---



\# Estado General



Proyecto:

ProdeColumbia



Estado actual:



✅ Modelo de dominio consolidado



✅ Backend funcional



🔄 Backend configurable en construcción



⏳ Frontend pendiente



\---



\# Fase 1 - Base



Estado:

✅ COMPLETADA



Implementado:



\- Participante

\- Categoria

\- Temporada

\- ParticipanteTemporada



Resultado:



Base de personas y temporadas validada.



\---



\# Fase 2 - Competiciones



Estado:

✅ COMPLETADA



Implementado:



\- PlantillaCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia



Resultado:



Motor básico de competiciones implementado.



\---



\# Fase 3 - Fútbol Real



Estado:

✅ COMPLETADA



Implementado:



\- EquipoReal

\- CalendarioReal

\- PartidoReal

\- InstanciaPartido



Resultado:



Separación completa entre fútbol real y lógica del Prode.



\---



\# Fase 4 - Pronósticos



Estado:

✅ COMPLETADA



Implementado:



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



Resultado:



Flujo completo validado con datos reales.



\---



\# Fase 5 - Competición



Estado:

✅ COMPLETADA



Implementado:



\- Enfrentamiento

\- Resolver enfrentamientos

\- TablaInstancia



Resultado:



Motor competitivo operativo.



\---



\# Fase 6 - Tablas



Estado:

✅ COMPLETADA



Implementado:



\- TablaCompetencia

\- TablaTemporada

\- Actualización de posiciones



Resultado:



Sistema de rankings y acumulados operativo.



\---



\# Fase 7 - Resultados Deportivos



Estado:

✅ COMPLETADA



Implementado:



\- ResultadoTemporada

\- MovimientoCategoria



Resultado:



Sistema de:



\- clasificación a copas

\- ascensos

\- descensos



funcionando.



\---



\# Fase 8 - Copas



Estado:

✅ IMPLEMENTADA (V1)



Implementado:



\- GrupoCompetencia

\- ParticipacionGrupo

\- TablaGrupo

\- ClasificacionGrupo

\- LlaveCompetencia



Resultado:



Flujo:



Participación



↓



Grupos



↓



Clasificaciones



↓



Playoffs



↓



Campeón



validado.



\---



\# Fase 9 - Refactor Configuración



Estado:

🔄 ACTUAL



Objetivo:



Eliminar hardcodeos y utilizar CompetenciaConfig como fuente de verdad.



\---



\## Prioridad 1



Refactorizar:



\### generar\_grupos\_copas.py



Actualmente:



\- 4 grupos fijos



Objetivo:



Utilizar:



\- cantidad\_zonas



\---



\### calcular\_clasificaciones\_grupo.py



Actualmente:



\- clasifican 2



Objetivo:



Utilizar:



\- clasificados



\---



\### calcular\_movimientos\_categoria.py



Actualmente:



\- 3 ascensos

\- 3 descensos



Objetivo:



Utilizar:



\- cantidad\_ascensos

\- cantidad\_descensos



\---



\# Fase 10 - Instancias Dinámicas



Estado:

⏳ PENDIENTE



Objetivo:



Eliminar estructuras de competencia hardcodeadas.



Archivo principal:



\- generar\_instancias\_2026.py



Situación actual:



Cada competencia define manualmente:



\- fechas

\- rondas

\- playoffs



Objetivo futuro:



Generarlas mediante configuración.



\---



\# Fase 11 - Playoffs Dinámicos



Estado:

⏳ PENDIENTE



Objetivo:



Generar automáticamente:



\- llaves

\- rondas

\- finales



a partir de:



\- cantidad\_participantes

\- clasificados

\- configuración de competencia



Ejemplos soportados:



\- Supercopa

\- Repechaje

\- Libertadores

\- Sudamericana

\- Copa Argentina



sin cambiar código.



\---



\# Fase 12 - Automatización de Temporadas



Estado:

⏳ PENDIENTE



Objetivos:



\- generación automática de nueva temporada

\- aplicación automática de ascensos

\- aplicación automática de descensos

\- migración de participantes



\---



\# Fase 13 - Equipos Temporales



Estado:

⏳ PENDIENTE



Implementar:



\- EquipoTemporal

\- MiembroEquipoTemporal



Necesario para:



\- Supercopa

\- competiciones por equipos



\---



\# Funcionalidades Pendientes



\## Bloqueo de Boletas



Prioridad:

Alta



Objetivo:



Bloquear edición automáticamente antes del inicio de la instancia.



\---



\## Visibilidad de Boletas



Antes del cierre:



\- cada participante sólo ve su boleta



Después del cierre:



\- todos ven todas las boletas



\---



\## Auditoría



Registrar:



\- propietario

\- usuario cargador

\- fecha creación

\- fecha modificación



\---



\## Partidos Decisivos



Detectar automáticamente partidos donde dos participantes difieren en sus pronósticos.



\---



\## Zona Horaria Argentina



Configurar:



America/Argentina/Buenos\_Aires



\---



\## Escudos



Soporte para:



\- escudos oficiales

\- almacenamiento local



\---



\# Frontend



Estado:

⏳ PENDIENTE



Se iniciará después de consolidar:



\- CompetenciaConfig

\- Instancias dinámicas

\- Playoffs dinámicos



\---



\## Portal Administrador



\- temporadas

\- competencias

\- participantes

\- resultados

\- configuraciones



\---



\## Portal Participante



\- carga de boletas

\- resultados

\- tablas

\- estadísticas

\- históricos



\---



\# Estadísticas e Históricos



Estado:

⏳ PENDIENTE



Implementar:



\## Hall of Fame



\- campeones

\- subcampeones

\- récords



\## Rivalidades



\- historial entre participantes



\## Métricas



\- AF histórico

\- AV histórico

\- efectividad

\- rendimiento por competencia

\- rendimiento por temporada



\---



\# Estado Actual Estimado



Modelo de Dominio:

90%



Backend Funcional:

90%



Backend Configurable:

60%



Frontend:

0%



\---



\# Objetivo Inmediato



Eliminar hardcodeos.



Prioridad absoluta:



Convertir CompetenciaConfig en la fuente única de configuración del sistema.

