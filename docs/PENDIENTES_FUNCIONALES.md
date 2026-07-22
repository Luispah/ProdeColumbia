\# PENDIENTES FUNCIONALES



Este documento registra funcionalidades aprobadas conceptualmente pero aún no implementadas.



\---



\# Alta Prioridad



\## Bloqueo Automático de Boletas



Estado:



PENDIENTE



Descripción:



La carga y modificación de boletas deberá bloquearse automáticamente antes del inicio de los partidos.



Objetivo inicial:



\- 1 hora antes del primer partido válido de la instancia.



Ejemplo:



Primer partido: 20:00



Cierre: 19:00



\---



\## Visibilidad de Boletas



Estado:



PENDIENTE



Antes del cierre:



\- cada participante sólo puede visualizar su propia boleta



Después del cierre:



\- todos los participantes pueden visualizar todas las boletas



\---



\## Carga Administrativa



Estado:



PENDIENTE



Los administradores deberán poder:



\- crear boletas

\- modificar boletas

\- cargar pronósticos para terceros



Objetivo:



Permitir la participación de usuarios que no utilicen habitualmente la plataforma.



\---



\## Auditoría de Boletas



Estado:



PENDIENTE



Registrar:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de creación

\- fecha de modificación



Objetivo:



Garantizar trazabilidad completa.



\---



\# Prioridad Media



\## Partidos Decisivos



Estado:



PENDIENTE



El sistema deberá detectar automáticamente los partidos donde dos participantes realizaron pronósticos diferentes.



Ejemplo:



Pablo: Local



Alejandro: Visitante



↓



Partido decisivo.



Objetivo:



Destacar visualmente los partidos que realmente pueden modificar el resultado de un enfrentamiento.



\---



\## Escudos de Equipos



Estado:



PENDIENTE



Los equipos deberán soportar:



\- escudo oficial

\- almacenamiento local



Objetivo:



Utilización en frontend y reportes.



\---



\## Zona Horaria Argentina



Estado:



PENDIENTE



Configurar:



America/Argentina/Buenos\_Aires



Objetivo:



Eliminar diferencias entre horario del servidor y horario mostrado al usuario.



\---



\# Prioridad Baja



\## Pronósticos por Resultado Exacto



Estado:



PENDIENTE



Actualmente:



\- Local

\- Empate

\- Visitante



A futuro algunas competiciones podrían utilizar:



\- resultado exacto



Ejemplo:



River 2 - 1 Boca



El dominio deberá soportarlo sin rediseños importantes.



\---



\## Sorteos



Estado:



PENDIENTE



Posible incorporación futura.



Aplicable principalmente a:



\- Copa Argentina

\- Libertadores

\- Sudamericana

\- Supercopa



\---



\# Observaciones



La existencia de un pendiente en este documento no implica que deba implementarse inmediatamente.



Este documento funciona como memoria funcional del proyecto para evitar perder acuerdos tomados durante el análisis y desarrollo.

