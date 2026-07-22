# MODELO DATOS

## Estado Actual

### Implementado

#### Personas

- Participante
- Categoria
- Temporada
- ParticipanteTemporada

---

#### Competiciones

- PlantillaCompetencia
- Competencia
- CompetenciaConfig
- ParticipacionCompetencia
- InstanciaCompetencia

---

#### Fútbol Real

- EquipoReal
- CalendarioReal
- PartidoReal
- InstanciaPartido

---

#### Pronósticos

- Pronostico
- ResultadoPronostico
- ResumenParticipanteInstancia

---

## Pendiente

### Competición

- Enfrentamiento

---

### Equipos Temporales

- EquipoTemporal
- MiembroEquipoTemporal

---

### Históricos

- RankingTemporada
- ReglaClasificacion
- ResultadoCompetencia

---

## Flujo Principal

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

---

## Flujo Fútbol Real

EquipoReal

↓

PartidoReal

↓

InstanciaPartido

↓

Pronostico

---

## Flujo Competitivo

Competencia

↓

InstanciaCompetencia

↓

InstanciaPartido

↓

ResumenParticipanteInstancia

↓

Enfrentamiento

↓

RankingTemporada

---

## Modelos Validados

### ParticipanteTemporada

Validado.

Permite:

- ascensos
- descensos
- reincorporaciones
- históricos

---

### InstanciaCompetencia

Validada.

Soporta:

- fechas
- rondas
- playoffs
- finales

---

### InstanciaPartido

Validada.

Permite:

- reutilizar partidos reales
- marcar penales
- excluir partidos
- subconjuntos de partidos

---

### Pronostico

Validado.

Actualmente soporta:

- Local
- Empate
- Visitante

Diseñado para permitir futuras extensiones.

---

### ResultadoPronostico

Validado mediante pruebas reales.

Permite:

- calcular aciertos
- calcular puntos
- obtener resultado real derivado

---

### ResumenParticipanteInstancia

Validado mediante pruebas reales.

Permite almacenar:

- partidos evaluados
- AF
- AV
- puntos

Es la base para:

- enfrentamientos
- tablas
- clasificaciones
- desempates

---

## Observaciones

DA no pertenece al resumen individual.

DA pertenece al enfrentamiento entre dos participantes.

Será calculado dentro de la entidad Enfrentamiento.