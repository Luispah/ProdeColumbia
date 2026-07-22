\# DECISIONES TECNICAS



\## 2026-07-18



Se adopta Django como framework principal.



\---



\## 2026-07-18



Se adopta GitHub como repositorio oficial del proyecto.



\---



\## 2026-07-18



Se adopta SQLite para desarrollo local.



\---



\## 2026-07-18



Las categorías no serán hardcodeadas.



Se administrarán mediante datos de negocio.



\---



\## 2026-07-20



La categoría deja de pertenecer a Participante.



La categoría pasa a vivir en ParticipanteTemporada.



\---



\## 2026-07-20



Se adopta PlantillaCompetencia como mecanismo base para generar competiciones.



\---



\## 2026-07-20



Se adopta CompetenciaConfig para parametrizar reglas de negocio sin modificar código.



\---



\## 2026-07-20



InstanciaCompetencia reemplaza el concepto tradicional de Fecha.



El objetivo es soportar:



\- fechas

\- rondas

\- playoffs

\- finales

\- fases especiales



mediante una única entidad.



\---



\## 2026-07-20



Los partidos reales son independientes de las competiciones.



Un mismo partido puede ser reutilizado por múltiples competiciones.



\---



\## 2026-07-20



Se adopta InstanciaPartido como entidad puente entre:



InstanciaCompetencia



y



PartidoReal



Motivos:



\- reutilización de partidos

\- exclusiones

\- penales

\- subconjuntos de partidos

\- flexibilidad futura



\---



\## 2026-07-20



Enfrentamiento se define como la entidad competitiva principal del sistema.



\---



\## 2026-07-20



Se incorpora RankingTemporada.



\---



\## 2026-07-20



Se incorpora ReglaClasificacion.



\---



\## 2026-07-20



La Supercopa utilizará equipos temporales.



No utilizará participantes individuales directamente.



\---



\## 2026-07-21



Se adopta EquipoReal como entidad propia.



Motivos:



\- nombres oficiales

\- importación desde APIs

\- escudos

\- históricos

\- eliminación de duplicación de textos



\---



\## 2026-07-21



Se utilizarán nombres oficiales de equipos como única fuente de verdad.



No se implementarán alias internos como estrategia principal.



Las boletas futuras deberán utilizar la misma nomenclatura que el sistema.



\---



\## 2026-07-21



Los resultados reales se almacenan mediante:



\- goles\_local

\- goles\_visitante



El sistema deriva automáticamente:



\- Local

\- Empate

\- Visitante



a partir de dichos valores.



\---



\## 2026-07-21



Los pronósticos se almacenan inicialmente como:



\- L

\- E

\- V



El diseño deberá permitir soportar en el futuro:



\- resultado exacto

\- modalidades especiales

\- reglas particulares por competición



sin rediseñar el dominio.



\---



\## 2026-07-21



ResultadoPronostico almacena:



\- resultado real

\- acierto

\- puntos



No almacena AF ni AV.



\---



\## 2026-07-21



AF y AV se calculan a partir de ResultadoPronostico.



Luego se persisten en ResumenParticipanteInstancia.



\---



\## 2026-07-21



DA no pertenece al resumen individual.



DA pertenece al enfrentamiento entre dos participantes.



Por lo tanto no se almacena en ResumenParticipanteInstancia.



\---



\## 2026-07-21



Se valida la persistencia de:



\- partidos evaluados

\- AF

\- AV

\- puntos



mediante ResumenParticipanteInstancia.



\---



\## 2026-07-21



Se adopta la estrategia:



Backend primero.



Orden de implementación:



\- Dominio

\- Persistencia

\- Lógica de negocio

\- Automatizaciones

\- Frontend



El Django Admin será utilizado como interfaz operativa durante el desarrollo.



\---



\## 2026-07-21



Se decide soportar carga administrativa de boletas.



Un administrador podrá cargar pronósticos para terceros.



Se implementará auditoría para registrar:



\- propietario de la boleta

\- usuario que realizó la carga

\- fechas de modificación



\---



\## 2026-07-21



Se define como requisito futuro el bloqueo automático de boletas.



Objetivo inicial:



1 hora antes del primer partido válido de la instancia.



\---



\## 2026-07-21



Se define como requisito futuro que las boletas sean:



Antes del cierre:



\- privadas



Después del cierre:



\- públicas para todos los participantes



\---



\## 2026-07-21



Los escudos de equipos deberán almacenarse localmente.



Se evitará depender permanentemente de APIs externas para su visualización.

