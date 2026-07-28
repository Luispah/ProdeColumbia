\# DECISIONES\_TECNICAS



Fecha de actualización:

2026-07-27



\---



\# 2026-07-18



Se adopta Django como framework principal del proyecto.



Motivos:



\- madurez

\- ORM integrado

\- Django Admin

\- velocidad de desarrollo



\---



\# 2026-07-18



Se adopta GitHub como repositorio oficial.



Todo desarrollo deberá versionarse mediante Git.



\---



\# 2026-07-18



Se adopta SQLite para desarrollo local.



Objetivo futuro:



\- PostgreSQL en producción



\---



\# 2026-07-18



Las categorías no serán hardcodeadas.



Se administrarán mediante datos de negocio.



Motivo:



Permitir futuras modificaciones sin cambios de código.



\---



\# 2026-07-20



La categoría deja de pertenecer a Participante.



La categoría pasa a vivir en ParticipanteTemporada.



Motivo:



La categoría es una condición deportiva anual y no una característica permanente de una persona.



\---



\# 2026-07-20



Se adopta PlantillaCompetencia como mecanismo principal para crear competiciones.



Motivo:



Separar:



\- definición

\- configuración

\- ejecución



\---



\# 2026-07-20



Se adopta CompetenciaConfig como entidad estratégica de configuración.



Objetivo:



Permitir que las reglas deportivas se definan mediante datos y no mediante código.



Ejemplos:



\- participantes

\- grupos

\- clasificados

\- playoffs

\- ascensos

\- descensos



\---



\# 2026-07-20



InstanciaCompetencia reemplaza el concepto tradicional de Fecha.



Puede representar:



\- Fecha

\- Ronda

\- Playoff

\- Final

\- Etapa especial



Motivo:



Utilizar una única abstracción para distintos formatos competitivos.



\---



\# 2026-07-20



Los partidos reales son independientes de las competiciones.



Motivo:



Un mismo partido real puede ser reutilizado por múltiples competiciones.



\---



\# 2026-07-20



Se adopta InstanciaPartido como entidad puente entre:



```text

InstanciaCompetencia

```



y



```text

PartidoReal

```



Motivos:



\- reutilización de partidos

\- exclusiones

\- penales

\- subconjuntos

\- flexibilidad futura



\---



\# 2026-07-20



Enfrentamiento se define como la entidad competitiva principal del sistema.



Motivo:



Toda la lógica deportiva termina resolviéndose mediante enfrentamientos entre participantes.



\---



\# 2026-07-21



Se adopta EquipoReal como entidad propia.



Motivos:



\- nombres oficiales

\- escudos

\- integraciones

\- históricos

\- eliminación de duplicaciones



\---



\# 2026-07-21



Los equipos utilizarán nombres oficiales como única fuente de verdad.



No se utilizarán alias internos como estrategia principal.



\---



\# 2026-07-21



Los resultados oficiales se almacenan mediante:



\- goles\_local

\- goles\_visitante



El sistema deriva:



\- Local

\- Empate

\- Visitante



cuando sea necesario.



\---



\# 2026-07-21



Los pronósticos se almacenan inicialmente como:



\- L

\- E

\- V



El modelo deberá soportar en el futuro:



\- resultado exacto

\- modalidades especiales

\- reglas particulares



sin rediseñar el dominio.



\---



\# 2026-07-21



ResultadoPronostico almacena:



\- resultado real

\- acierto

\- puntos



No almacena AF ni AV.



\---



\# 2026-07-21



AF y AV se calculan a partir de ResultadoPronostico.



Posteriormente se persisten en:



```text

ResumenParticipanteInstancia

```



Motivo:



Evitar recálculos permanentes.



\---



\# 2026-07-21



DA no pertenece al resumen individual.



DA pertenece a un enfrentamiento entre participantes.



Por lo tanto:



No se almacena en ResumenParticipanteInstancia.



\---



\# 2026-07-21



Se adopta persistencia de cálculos.



Los resultados importantes deben almacenarse.



Ejemplos:



\- ResultadoPronostico

\- ResumenParticipanteInstancia

\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada

\- ResultadoTemporada

\- MovimientoCategoria



\---



\# 2026-07-21



Se adopta estrategia:



```text

Backend primero

```



Orden oficial:



```text

Dominio

↓

Persistencia

↓

Lógica de negocio

↓

Automatizaciones

↓

Frontend

```



Django Admin será utilizado como interfaz operativa durante el desarrollo.



\---



\# 2026-07-21



Se habilitará carga administrativa de boletas.



Los administradores podrán:



\- crear pronósticos

\- modificar pronósticos

\- cargar por terceros



\---



\# 2026-07-21



Se define auditoría obligatoria para futuras cargas.



Deberá registrarse:



\- propietario

\- usuario cargador

\- fecha creación

\- fecha modificación



\---



\# 2026-07-21



Se define bloqueo automático de boletas.



Objetivo inicial:



```text

1 hora antes del primer partido válido

de la instancia

```



\---



\# 2026-07-21



Se define visibilidad diferida de boletas.



Antes del cierre:



\- privadas



Después del cierre:



\- públicas para todos los participantes



\---



\# 2026-07-21



Los escudos deberán almacenarse localmente.



Motivo:



Reducir dependencia de APIs externas.



\---



\# 2026-07-25



Se incorpora el modelo completo de tablas deportivas.



Implementaciones:



\- TablaInstancia

\- TablaCompetencia

\- TablaTemporada



Decisión:



Mantener tablas persistidas en base de datos.



Motivo:



Simplificar consultas futuras y frontend.



\---



\# 2026-07-25



Se incorpora ResultadoTemporada.



Motivo:



Separar consecuencias deportivas finales de las tablas.



Ejemplos:



\- Libertadores

\- Sudamericana

\- Ascenso

\- Descenso

\- Repechaje



\---



\# 2026-07-25



Se incorpora MovimientoCategoria.



Motivo:



Representar explícitamente:



\- ascensos

\- descensos

\- permanencias



sin recalcularlos continuamente.



\---



\# 2026-07-26



Se incorpora soporte para copas.



Implementaciones:



\- GrupoCompetencia

\- ParticipacionGrupo

\- TablaGrupo

\- ClasificacionGrupo

\- LlaveCompetencia



Motivo:



Separar fases de grupos y eliminación directa.



\---



\# 2026-07-27



Auditoría integral del proyecto.



Se revisaron:



\- documentación

\- modelos

\- comandos

\- flujo competitivo



\---



\# 2026-07-27



Conclusión de auditoría:



\## El modelo está más avanzado que los procesos.



No se identifican refactors urgentes sobre:



\- Competencia

\- CompetenciaConfig

\- Enfrentamiento

\- Tablas

\- Copas



La principal deuda técnica actual se encuentra en los comandos.



\---



\# 2026-07-27



Se decide NO realizar una refactor inmediata de modelos.



Especialmente:



```text

NO modificar todavía:



\- CompetenciaConfig

\- InstanciaCompetencia

\- LlaveCompetencia

```



Motivo:



El problema principal no está en la estructura de datos.



Está en la utilización de configuraciones.



\---



\# 2026-07-27



Se redefine la prioridad técnica del proyecto.



Antes:



```text

Refactor modelos

```



Ahora:



```text

Refactor procesos

```



\---



\# 2026-07-27



CompetenciaConfig se define formalmente como:



\## Fuente única de configuración.



Toda nueva funcionalidad deberá verificar primero si puede resolverse mediante configuración.



Antes de:



\- crear modelos

\- agregar campos

\- agregar lógica específica



\---



\# 2026-07-27



Se identifica como deuda técnica principal la existencia de hardcodeos en comandos.



Ejemplos:



\- cantidad de grupos

\- clasificados

\- ascensos

\- descensos

\- instancias

\- rondas



\---



\# 2026-07-27



Se establece el siguiente orden oficial de refactor.



\## Prioridad 1



Eliminar hardcodeos de:



\- generar\_grupos\_copas.py

\- calcular\_clasificaciones\_grupo.py

\- calcular\_movimientos\_categoria.py



\---



\## Prioridad 2



Refactorizar:



\- generar\_instancias\_2026.py



\---



\## Prioridad 3



Implementar playoffs dinámicos.



\---



\# 2026-07-27



Se posterga el inicio del frontend.



Motivo:



Primero consolidar:



\- CompetenciaConfig

\- generación dinámica de instancias

\- playoffs dinámicos



\---



\# Estado Actual



Modelo de Dominio:

90%



Backend Funcional:

90%



Backend Configurable:

60%



Frontend:

0%



\---



\# Decisión Vigente



La prioridad del proyecto ya no es agregar más modelos.



La prioridad es transformar un backend funcional en un backend completamente configurable mediante CompetenciaConfig.

