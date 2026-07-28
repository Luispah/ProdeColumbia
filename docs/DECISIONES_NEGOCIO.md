\# DECISIONES\_NEGOCIO



Fecha:

2026-07-27



\---



\# Propósito



Este documento registra las decisiones funcionales y de negocio que definen el comportamiento general del sistema.



Su objetivo es evitar rediscutir conceptos ya definidos durante futuras etapas de desarrollo.



\---



\# Principio General



ProdeColumbia no está diseñado para administrar exclusivamente las competiciones actuales.



El objetivo es construir un motor capaz de generar y administrar futuras competiciones mediante configuración.



Ejemplos:



\- Ligas

\- Copas

\- Supercopas

\- Torneos especiales



sin necesidad de modificar código.



\---



\# Temporada



La entidad principal del negocio es:



```text

Temporada

```



Una temporada representa un año competitivo completo.



Ejemplos:



```text

2026

2027

2028

```



\---



\# Relación Temporada - Competiciones



Las competiciones pertenecen a una temporada.



Ejemplo:



```text

Temporada 2026

│

├── Liga Apertura

├── Liga Clausura

├── Libertadores

├── Sudamericana

├── Repechaje

├── Copa Argentina

└── Supercopa

```



No existe obligación de mantener siempre la misma cantidad de competiciones.



\---



\# Competiciones



Las competiciones son instancias creadas a partir de plantillas.



Ejemplo:



```text

Plantilla

↓

Liga Profesional

↓

Competencia

↓

Liga Apertura 2026

```



\---



\# Plantillas



Las plantillas representan formatos reutilizables.



Objetivos:



\- reutilización

\- creación rápida

\- consistencia



Una plantilla puede modificarse en el tiempo.



Las nuevas competiciones deben heredar la configuración más reciente de su plantilla.



\---



\# Configuración



La intención del proyecto es:



```text

Configurar antes que programar.

```



Las reglas deben definirse mediante configuración siempre que sea posible.



\---



\# Categorías



Las categorías son completamente dinámicas.



Ejemplos válidos:



```text

A

B

C

```



```text

A

B

C

D

```



```text

A

B

C

D

E

```



El sistema no debe asumir una cantidad fija de categorías.



\---



\# Jerarquía de Categorías



Las categorías son jerárquicas.



Ejemplo:



```text

A > B > C > D

```



La categoría superior siempre representa un nivel competitivo superior.



\---



\# Ascensos y Descensos



Los ascensos y descensos se determinan utilizando las ligas de la temporada.



No dependen de las copas.



No dependen de competiciones internacionales.



\---



\# Generación de Nueva Temporada



Al crear una nueva temporada el sistema deberá:



```text

Buscar última temporada válida

↓

Calcular movimientos

↓

Sugerir participantes

↓

Permitir corrección manual

↓

Crear temporada

```



\---



\# Participantes Nuevos



Los nuevos participantes podrán incorporarse mediante los mecanismos definidos por el reglamento vigente.



La lógica no debe estar hardcodeada.



\---



\# Clasificación a Copas



Las clasificaciones a copas son reglas deportivas.



No deben depender de valores hardcodeados.



Deben poder modificarse si cambia el reglamento.



\---



\# Familias de Competiciones



Actualmente se reconocen cuatro familias principales.



\---



\## Liga



Formato:



```text

Zonas

↓

Tabla

↓

Clasificación

↓

Playoffs

```



\---



\## Copa con Grupos



Formato:



```text

Grupos

↓

Clasificación

↓

Playoffs

```



Ejemplos:



\- Libertadores

\- Sudamericana



\---



\## Copa Eliminatoria



Formato:



```text

Sorteo

↓

Eliminación Directa

```



Ejemplos:



\- Repechaje

\- Copa Argentina



\---



\## Supercopa



Formato:



```text

Equipos temporales

↓

Doble eliminación

```



\---



\# Equipos Temporales



La Supercopa justifica la futura implementación de:



```text

EquipoTemporal

MiembroEquipoTemporal

```



Los equipos son temporales y pueden cambiar entre fechas.



\---



\# Sorteos



Los sorteos forman parte del negocio.



El sistema deberá poder generar sorteos de forma automática.



La intervención manual debe seguir siendo posible.



\---



\# Instancias



Las instancias deberán poder generarse automáticamente a partir de la configuración de la competencia.



Ejemplos:



```text

Fecha 1

Fecha 2

Fecha 3

```



o



```text

Grupo A

Grupo B

Grupo C

```



o



```text

Octavos

Cuartos

Semifinal

Final

```



\---



\# Integración API



La visión futura contempla integración con APIs deportivas.



Objetivos:



\- fixture automático

\- resultados automáticos

\- cambios de programación

\- suspendidos



La aplicación debe continuar funcionando aunque no exista API disponible.



\---



\# Rol del Administrador



El sistema debe sugerir configuraciones.



El administrador debe conservar la capacidad de modificar cualquier dato antes de confirmar.



Principio:



```text

Automatización con supervisión humana.

```



\---



\# Objetivo Final



El objetivo no es programar competiciones específicas.



El objetivo es construir un motor capaz de crear futuras competiciones mediante configuración, reutilizando plantillas y minimizando la necesidad de cambios de código.

