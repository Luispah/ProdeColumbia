\# PROJECT SNAPSHOT



Fecha:

2026-07-27



\---



\# Proyecto



ProdeColumbia



Sistema integral para administrar el Prode Columbia.



No es solamente un sistema de pronósticos.



Modela:



\- Participantes

\- Temporadas

\- Categorías

\- Competiciones

\- Pronósticos

\- Resultados

\- Enfrentamientos

\- Tablas

\- Clasificaciones

\- Ascensos

\- Descensos

\- Copas internacionales

\- Históricos



\---



\# Estado General



Estado global:



✅ Backend funcional



✅ Modelo de dominio consolidado



✅ Flujo competitivo implementado



⚠️ Configuración parcialmente utilizada



⏳ Frontend pendiente



\---



\# Estado Actual del Backend



Actualmente el sistema puede ejecutar:



Participante



↓



ParticipanteTemporada



↓



Pronóstico



↓



ResultadoPronóstico



↓



ResumenParticipanteInstancia



↓



Enfrentamiento



↓



TablaInstancia



↓



TablaCompetencia



↓



TablaTemporada



↓



ResultadoTemporada



↓



MovimientoCategoria



\---



\# Competiciones Implementadas



Actualmente existen modelos para:



\- Liga Profesional Clausura

\- Copa Libertadores

\- Copa Sudamericana

\- Copa Repechaje

\- Copa Argentina

\- Supercopa



La arquitectura permite nuevas competiciones futuras.



\---



\# Modelos Implementados



\## Personas



\- Participante

\- Categoria

\- Temporada

\- ParticipanteTemporada



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



\## Pronósticos



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



\## Núcleo Competitivo



\- Enfrentamiento



\## Tablas



\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada



\## Resultados Deportivos



\- ResultadoTemporada

\- MovimientoCategoria



\## Copas



\- GrupoCompetencia

\- ParticipacionGrupo

\- TablaGrupo

\- ClasificacionGrupo

\- LlaveCompetencia



\---



\# Funcionalidades Implementadas



\## Pronósticos



✅ Generación



✅ Evaluación



✅ Cálculo de aciertos



✅ Cálculo de puntos



\---



\## Enfrentamientos



✅ Generación



✅ Resolución



✅ Victoria



✅ Derrota



✅ Empate



\---



\## Tablas



✅ Tabla por instancia



✅ Tabla por competencia



✅ Tabla anual



✅ Posiciones



\---



\## Temporadas



✅ Clasificación a copas



✅ Ascensos



✅ Descensos



✅ Movimientos de categoría



\---



\## Copas



✅ Grupos



✅ Clasificaciones



✅ Playoffs



✅ Generación de llaves



⚠️ Versión inicial



\---



\# Datos Actuales



\## Participantes



\- \~90 participantes reales



\## Categorías



\- A

\- B

\- C



\## Temporada



\- 2026



\## Equipos Reales



\- 32 equipos



\## Partidos



\- Fecha 1 cargada



\## Pronósticos



\- Flujo validado



\---



\# Arquitectura



Separación estricta entre:



\## Fútbol Real



\- EquipoReal

\- CalendarioReal

\- PartidoReal



Representa hechos objetivos.



\## Prode



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- Enfrentamiento

\- Tablas

\- Clasificaciones



Representa la lógica competitiva.



\---



\# Hallazgos de la Auditoría Julio 2026



Luego de revisar modelos, documentación y comandos se concluyó:



\## El modelo está más avanzado que los procesos



La mayoría de los modelos son reutilizables y suficientemente flexibles.



La principal deuda técnica NO se encuentra actualmente en los modelos.



\---



\## CompetenciaConfig es la pieza central



Ya existen configuraciones para:



\- cantidad\_participantes

\- cantidad\_zonas

\- clasificados

\- cantidad\_ascensos

\- cantidad\_descensos

\- tiene\_playoff

\- tiene\_penales



Sin embargo muchos procesos todavía utilizan valores hardcodeados.



\---



\## Deuda Técnica Principal



Los comandos aún contienen reglas fijas para:



\- cantidad de grupos

\- cantidad de clasificados

\- cantidad de ascensos

\- cantidad de descensos

\- clasificación a copas

\- estructura de playoffs

\- generación de instancias



La próxima etapa consiste en reemplazar dichos valores por lectura desde CompetenciaConfig.



\---



\# Próxima Etapa



\## Prioridad 1



Refactor CompetenciaConfig



Objetivo:



Eliminar hardcodeos de los procesos.



Archivos prioritarios:



\- generar\_grupos\_copas.py

\- calcular\_clasificaciones\_grupo.py

\- calcular\_movimientos\_categoria.py



\---



\## Prioridad 2



Refactor generación de instancias



Archivo:



\- generar\_instancias\_2026.py



Objetivo:



Reducir dependencia de estructuras fijas por competencia.



\---



\## Prioridad 3



Motor de playoffs configurable



Objetivo:



Generar rondas dinámicamente según configuración de la competencia.



\---



\# Frontend



Todavía NO es prioridad inmediata.



La prioridad actual continúa siendo:



Backend configurable.



Una vez completada la eliminación de hardcodeos se evaluará iniciar:



\- Portal Administrador

\- Portal Participante

\- Carga de boletas

\- Tablas

\- Resultados

\- Estadísticas



\---



\# Estado del Proyecto



Modelo de Dominio:

90%



Backend Funcional:

90%



Backend Configurable:

60%



Frontend:

0%



El proyecto ya superó la etapa de prueba conceptual y actualmente se encuentra en proceso de transformación hacia un motor configurable de competiciones.

