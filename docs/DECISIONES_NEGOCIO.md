# DECISIONES_NEGOCIO

Fecha:
2026-07-27

---

# Propósito

Este documento registra las decisiones funcionales y de negocio que definen el comportamiento general del sistema.

Su objetivo es evitar rediscutir conceptos ya definidos durante futuras etapas de desarrollo.

---

# Principio General

ProdeColumbia no está diseñado para administrar exclusivamente las competiciones actualmente existentes.

El objetivo es construir un motor capaz de crear, configurar y administrar futuras competiciones mediante configuración.

Ejemplos:

- Ligas
- Copas
- Supercopas
- Torneos especiales

sin necesidad de modificar código.

---

# Temporada

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

Todas las competiciones pertenecen a una temporada.

---

# Relación Temporada - Competiciones

Las competiciones son hijas de una temporada.

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

No existe obligación de mantener siempre las mismas competiciones.

Cada temporada puede contener:

- una liga
- dos ligas
- múltiples copas
- competiciones especiales

según las decisiones de la organización.

---

# Competiciones

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

Una competición representa una edición concreta.

Las reglas generales viven en la plantilla.

La configuración específica vive en la competición.

---

# Plantillas

Las plantillas representan formatos reutilizables.

Objetivos:

- reutilización
- creación rápida
- consistencia
- automatización

Las plantillas son editables.

Las nuevas competiciones heredan la configuración vigente de la plantilla seleccionada.

---

# Persistencia de Plantillas

Cuando una competición se crea a partir de una plantilla:

```text
Plantilla
↓
Configuración sugerida
↓
Administrador revisa
↓
Competencia creada
```

La plantilla debe poder evolucionar con el paso del tiempo.

El objetivo es evitar recrear configuraciones manualmente todos los años.

---

# Configuración

La intención principal del proyecto es:

```text
Configurar antes que programar.
```

Toda regla configurable deberá resolverse mediante configuración antes de incorporarse al código.

---

# Rol del Administrador

La filosofía del proyecto es:

```text
Automatización con supervisión humana.
```

El sistema debe:

- sugerir configuraciones
- sugerir participantes
- sugerir ascensos
- sugerir descensos
- sugerir clasificaciones

El administrador conserva siempre la posibilidad de modificar cualquier dato antes de confirmar.

---

# Categorías

Las categorías son dinámicas.

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

---

# Jerarquía de Categorías

Las categorías siempre son jerárquicas.

Ejemplo:

```text
A > B > C > D
```

La categoría superior representa un nivel competitivo superior.

Esta regla forma parte permanente del negocio.

---

# Categorías y Competiciones

Las competiciones podrán indicar qué categorías participan.

Ejemplos:

```text
Liga Apertura
↓
Categoría A
```

```text
Liga Apertura
↓
Categoría B
```

```text
Libertadores
↓
A + B + C
```

El sistema debe poblar automáticamente los participantes según las categorías configuradas.

---

# Ascensos y Descensos

Los ascensos y descensos se determinan utilizando las ligas de una temporada.

No dependen de:

- Libertadores
- Sudamericana
- Repechaje
- Copa Argentina
- Supercopa

Las copas no generan ascensos ni descensos.

---

# Tabla Anual

La Tabla Anual es la fuente principal para:

- ascensos
- descensos
- clasificación a copas

La Tabla Anual surge de las ligas de la temporada.

---

# Generación de Nueva Temporada

Al crear una nueva temporada el sistema deberá:

```text
Buscar última temporada válida
↓
Calcular movimientos
↓
Sugerir participantes
↓
Permitir correcciones
↓
Crear temporada
```

El proceso debe ser automático pero revisable.

---

# Participantes Nuevos

Los participantes nuevos podrán incorporarse mediante reglas definidas por el reglamento vigente.

La lógica no debe estar hardcodeada.

---

# Clasificación a Copas

Las clasificaciones a copas son reglas deportivas.

No deben depender de valores fijos programados.

Deben poder modificarse cuando cambie el reglamento.

---

# Familias de Competiciones

Actualmente se reconocen cuatro familias principales.

---

## Liga

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

---

## Copa con Grupos

Formato:

```text
Grupos
↓
Clasificación
↓
Playoffs
```

Ejemplos:

- Libertadores
- Sudamericana

---

## Copa Eliminatoria

Formato:

```text
Sorteo
↓
Eliminación Directa
```

Ejemplos:

- Repechaje
- Copa Argentina

---

## Supercopa

Formato:

```text
Equipos temporales
↓
Doble eliminación
```

---

# Equipos Temporales

La Supercopa justifica la futura implementación de:

```text
EquipoTemporal
MiembroEquipoTemporal
```

Los equipos existen únicamente para una instancia determinada.

Los integrantes pueden cambiar entre fechas.

---

# Sorteos

Los sorteos forman parte del negocio.

El sistema deberá permitir:

```text
Sorteo automático
```

y también:

```text
Intervención manual
```

cuando la organización lo considere necesario.

---

# Instancias

Las instancias deberán generarse automáticamente a partir de la configuración de una competencia.

Ejemplos:

```text
Fecha 1
Fecha 2
Fecha 3
```

```text
Grupo A
Grupo B
Grupo C
```

```text
Octavos
Cuartos
Semifinal
Final
```

---

# Integración API

La visión futura contempla integración con APIs deportivas.

Objetivos:

- fixture automático
- resultados automáticos
- cambios de programación
- suspendidos

La aplicación deberá continuar funcionando aunque una API no esté disponible.

---

# Objetivo Final

El objetivo no es programar:

- Liga Apertura
- Liga Clausura
- Libertadores
- Sudamericana

de forma individual.

El objetivo es construir un motor capaz de crear futuras competiciones mediante configuración.

Modelo deseado:

```text
Temporada
↓
Plantilla
↓
Configuración
↓
Generación Automática
↓
Competencia Operativa
```

minimizando la necesidad de nuevos desarrollos específicos.

---

# Principio Rector

Toda decisión futura debe responder a la siguiente pregunta:

```text
¿Esto puede resolverse mediante configuración?
```

Si la respuesta es sí:

```text
Configurar antes que programar.
```