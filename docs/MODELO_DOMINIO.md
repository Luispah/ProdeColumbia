# MODELO_DOMINIO

Fecha:
2026-07-27

---

# Visión General

ProdeColumbia modela un ecosistema competitivo completo.

No modela únicamente pronósticos.

Modela:

- participantes
- temporadas
- categorías
- competiciones
- fútbol real
- pronósticos
- enfrentamientos
- tablas
- clasificaciones
- ascensos
- descensos
- copas
- playoffs
- históricos

---

# Principio Fundamental

El proyecto separa estrictamente:

## Fútbol Real

Representa eventos objetivos.

Ejemplos:

- EquipoReal
- CalendarioReal
- PartidoReal

---

## Competencia Prode

Representa la lógica competitiva.

Ejemplos:

- Pronostico
- ResultadoPronostico
- ResumenParticipanteInstancia
- Enfrentamiento
- Tablas
- Clasificaciones

---

# Personas

## Participante

Representa una persona.

Características:

- nunca se elimina
- mantiene histórico completo
- puede participar en múltiples temporadas

---

## Categoria

Representa una división competitiva.

Ejemplos:

- A
- B
- C

Responsabilidades:

- ascensos
- descensos
- organización deportiva

---

## Temporada

Representa un ciclo anual.

Ejemplos:

- 2026
- 2027
- 2028

---

## ParticipanteTemporada

Representa la participación de un participante en una temporada específica.

Permite modelar:

- ascensos
- descensos
- reincorporaciones
- nuevos jugadores
- histórico anual

Ejemplo:

```text
Participante
↓
Temporada
↓
Categoría