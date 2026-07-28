\# IA\_CONTEXT



\## Proyecto



ProdeColumbia.



Aplicación web para administrar integralmente el Prode Columbia.



El sistema reemplaza progresivamente la operatoria histórica basada en Excel.



NO es únicamente un sistema de pronósticos deportivos.



El objetivo es modelar completamente la estructura competitiva del Prode.



Incluye:



\- Liga Profesional

\- Copa Libertadores

\- Copa Sudamericana

\- Copa Argentina

\- Copa Repechaje

\- Supercopa

\- futuras competiciones



\---



\## Objetivo Principal



Centralizar toda la operatoria del Prode Columbia en una única plataforma.



El sistema debe administrar:



\- participantes

\- categorías

\- temporadas

\- competencias

\- pronósticos

\- resultados

\- enfrentamientos

\- tablas

\- clasificaciones

\- ascensos

\- descensos

\- históricos

\- estadísticas



\---



\## Tecnología



\### Backend



\- Python

\- Django



\### Base de Datos



\- SQLite (desarrollo)

\- PostgreSQL (objetivo producción)



\### Versionado



\- Git

\- GitHub



\---



\## Estado Actual Real



El proyecto ya superó ampliamente la fase inicial de pronósticos.



Actualmente existe:



\### Personas



\- Participante

\- Categoria

\- Temporada

\- ParticipanteTemporada



\### Competencias



\- PlantillaCompetencia

\- Competencia

\- CompetenciaConfig

\- ParticipacionCompetencia

\- InstanciaCompetencia



\### Fútbol Real



\- EquipoReal

\- CalendarioReal

\- PartidoReal

\- InstanciaPartido



\### Pronósticos



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia



\### Competición



\- Enfrentamiento



\### Tablas



\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada



\### Resultados Deportivos



\- ResultadoTemporada

\- MovimientoCategoria



\### Copas



\- GrupoCompetencia

\- ParticipacionGrupo

\- TablaGrupo

\- ClasificacionGrupo

\- LlaveCompetencia



\---



\## Flujo Principal Actual



Participante



↓



ParticipanteTemporada



↓



Pronostico



↓



ResultadoPronostico



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



\## Flujo de Copas



Competencia



↓



ParticipacionCompetencia



↓



GrupoCompetencia



↓



ParticipacionGrupo



↓



TablaGrupo



↓



ClasificacionGrupo



↓



LlaveCompetencia



↓



Campeón



\---



\## Entidad Central del Negocio



La entidad central continúa siendo:



\### ENFRENTAMIENTO



Los partidos reales representan hechos objetivos.



Los enfrentamientos representan la competencia entre participantes.



Toda la lógica deportiva termina convergiendo en un enfrentamiento.



\---



\## Principios Arquitectónicos



\### Separación estricta



Fútbol Real:



\- EquipoReal

\- CalendarioReal

\- PartidoReal



Representa eventos objetivos.



\---



Prode:



\- Pronostico

\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- Enfrentamiento

\- Tablas

\- Clasificaciones

\- Resultados



Representa la lógica competitiva.



\---



\### Persistencia por etapas



Los cálculos importantes se almacenan.



No se recalculan constantemente.



Ejemplos:



\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada

\- ResultadoTemporada

\- MovimientoCategoria



\---



\### Configuración centralizada



La entidad estratégica del sistema es:



CompetenciaConfig



Debe convertirse progresivamente en la fuente principal de configuración de las competencias.



\---



\## Hallazgo Arquitectónico Importante



Julio 2026



Después de una auditoría completa del proyecto se concluyó:



\### El modelo está más avanzado que los procesos



La mayoría de los modelos actuales son reutilizables y suficientemente flexibles.



La principal deuda técnica NO está en los modelos.



La principal deuda técnica está en los comandos de procesamiento.



\---



\## Problema identificado



Muchos procesos siguen utilizando valores hardcodeados.



Ejemplos:



\- cantidad de grupos

\- cantidad de clasificados

\- cantidad de ascensos

\- cantidad de descensos

\- clasificación a copas

\- estructura de instancias

\- rondas de playoffs



\---



\## Dirección Actual del Proyecto



La siguiente fase del backend no consiste en crear nuevos modelos.



La prioridad es:



\### Transformar el backend funcional en backend configurable.



Esto implica reemplazar reglas fijas por lectura desde:



CompetenciaConfig



\---



\## Campos estratégicos de CompetenciaConfig



Actualmente existen:



\- cantidad\_participantes

\- cantidad\_zonas

\- clasificados

\- cantidad\_ascensos

\- cantidad\_descensos

\- tiene\_playoff

\- tiene\_penales

\- usa\_tabla

\- usa\_af

\- usa\_av

\- usa\_da



Muchos procesos todavía no los utilizan.



La próxima etapa consiste en conectar la configuración con los procesos.



\---



\## Próximas Prioridades



\### Prioridad 1



Eliminar hardcodeos.



Archivos candidatos:



\- generar\_grupos\_copas.py

\- calcular\_clasificaciones\_grupo.py

\- calcular\_movimientos\_categoria.py



\---



\### Prioridad 2



Refactorizar generación de instancias.



Archivo principal:



\- generar\_instancias\_2026.py



\---



\### Prioridad 3



Motor de playoffs configurable.



Objetivo:



Generar rondas automáticamente según la configuración de la competencia.



\---



\## Frontend



Todavía no es prioridad inmediata.



Antes de iniciar frontend se desea:



\- reducir hardcodeos

\- consolidar CompetenciaConfig

\- estabilizar procesos



\---



\## Estado del Proyecto



Modelo de Dominio:

90%



Backend Funcional:

90%



Backend Configurable:

60%



Frontend:

0%



\---



\## Regla de Trabajo Vigente



Antes de implementar una funcionalidad importante:



1\. Revisar si ya existe soporte en el modelo actual.

2\. Revisar si CompetenciaConfig ya contempla el caso.

3\. Revisar repositorios de referencia utilizados por el proyecto.

4\. Evitar agregar nuevos modelos cuando el problema pueda resolverse mediante configuración.



La prioridad actual es mejorar configurabilidad y reducir deuda técnica, no aumentar cantidad de código.

