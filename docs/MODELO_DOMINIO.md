\# MODELO DOMINIO V1



\---



\# Visión General



El dominio modela un sistema de Prode capaz de:



\- administrar temporadas

\- administrar participantes

\- administrar competiciones

\- administrar pronósticos

\- calcular resultados

\- generar tablas y clasificaciones

\- soportar múltiples formatos de competición



El modelo separa explícitamente:



\- personas

\- competiciones

\- fútbol real

\- pronósticos

\- resultados

\- históricos



\---



\# Personas



\## Participante



Representa una persona.



Características:



\- nunca se elimina

\- mantiene identidad histórica

\- puede participar en múltiples temporadas



Ejemplos:



\- Pablo Camporini

\- Alejandro Caramia



\---



\## Categoria



Representa una división.



Ejemplos:



\- A

\- B

\- C



Responsabilidades:



\- ascensos

\- descensos

\- organización de participantes



\---



\## Temporada



Representa un ciclo anual.



Ejemplos:



\- 2026

\- 2027

\- 2028



\---



\## ParticipanteTemporada



Representa la participación de un participante dentro de una temporada específica.



Resuelve:



\- ascensos

\- descensos

\- nuevos participantes

\- participantes reincorporados

\- histórico por temporada



Ejemplo:



```text

Pablo Camporini

↓

Temporada 2026

↓

Categoría A

