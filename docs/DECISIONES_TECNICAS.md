\# DECISIONES TECNICAS



\## 2026-07-18



Se adopta Django como framework principal.



\---



\## 2026-07-18



Se adopta GitHub como repositorio oficial.



\---



\## 2026-07-18



Se adopta SQLite para desarrollo.



\---



\## 2026-07-18



No se hardcodearán categorías.



\---



\## 2026-07-18



No se hardcodeará cantidad de participantes.



\---



\## 2026-07-18



La entidad principal del negocio pasa a ser:



Enfrentamiento.



No Partido.



\---



\## 2026-07-18



Se decide diseñar primero el dominio completo antes de continuar agregando modelos.



\## 2026-07-20



La categoría pasa conceptualmente a ParticipanteTemporada.



\---



\## 2026-07-20



Se adopta CompetenciaConfig para parametrizar torneos.



\---



\## 2026-07-20



Se adopta InstanciaCompetencia como reemplazo conceptual de "Fecha".



Permite representar:



\- Fechas

\- Rondas

\- Octavos

\- Finales



con una misma entidad.



\---



\## 2026-07-20



Se adopta InstanciaPartido para vincular partidos reales con una competencia específica.



\---



\## 2026-07-20



Se adopta EquipoTemporal para soportar Supercopa.



\---



\## 2026-07-20



AF, AV y DA serán persistidos.

