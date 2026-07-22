\# REGLAS NEGOCIO



\## Participantes



Los participantes nunca se eliminan.



Pueden:



\- retirarse

\- volver años después

\- cambiar de categoría



\---



\## Categorías



Configurables.



No hardcodeadas.



\---



\## Temporadas



Las temporadas son independientes.



Cada participante posee una participación por temporada.



\---



\## Creación de Temporadas



El sistema deberá generar propuestas automáticas.



Incluyendo:



\- ascensos

\- descensos

\- participantes activos



La propuesta podrá modificarse manualmente.



\---



\## Competiciones



Se crean desde PlantillaCompetencia.



Toda configuración debe poder modificarse desde interfaz gráfica.



\---



\## AF / AV



Se calculan a partir de ResultadoPronostico.



Se almacenan en ResumenParticipanteInstancia.



No deben recalcularse permanentemente.



\---



\## DA



No pertenece al participante.



No pertenece al resumen individual.



DA pertenece al enfrentamiento entre dos participantes y se calcula comparando sus resultados.



\---



\## Históricos



Los resultados finales de todas las competiciones se almacenarán.



\---



\## Partidos Reales



Todas las competiciones utilizan partidos reales.



Una competición puede:



\- utilizar todos los partidos

\- utilizar algunos

\- excluir partidos suspendidos

\- definir partidos de penales



Los resultados reales se almacenan mediante:



\- goles\_local

\- goles\_visitante



A partir de dichos valores el sistema deriva:



\- Local

\- Empate

\- Visitante



cuando sea necesario.



\---



\## Equipos Reales



Los equipos se almacenan utilizando nombres oficiales.



No se utilizarán alias internos como fuente principal.



Las boletas deberán utilizar los mismos nombres definidos en el sistema.



\---



\## Pronósticos



Actualmente los participantes pronostican:



\- Local

\- Empate

\- Visitante



El modelo deberá permanecer preparado para soportar futuras modalidades:



\- resultado exacto

\- competiciones especiales

\- reglas alternativas



\---



\## Cierre de Boletas



Las boletas podrán modificarse únicamente hasta la hora de cierre.



Objetivo inicial:



1 hora antes del inicio del primer partido válido de la instancia.



Ejemplo:



Primer partido = 20:00



Cierre de carga = 19:00



\---



\## Bloqueo de Edición



Una vez alcanzada la hora de cierre:



\- no podrán modificarse pronósticos

\- no podrán agregarse pronósticos nuevos

\- la instancia quedará bloqueada



\---



\## Visibilidad de Boletas



Antes del cierre:



\- cada participante sólo puede visualizar su propia boleta



Después del cierre:



\- todos los participantes podrán visualizar todas las boletas



\---



\## Partidos Decisivos



El sistema deberá identificar los partidos donde dos participantes realizaron pronósticos diferentes.



Estos partidos deberán destacarse visualmente porque son los únicos que pueden generar diferencias directas entre ambos participantes.



\---



\## Carga Administrativa



Los administradores deberán poder:



\- crear boletas

\- modificar boletas

\- cargar pronósticos para terceros



Pensado especialmente para participantes que no utilicen habitualmente sistemas informáticos.



\---



\## Auditoría



Toda carga de pronósticos deberá permitir registrar:



\- propietario de la boleta

\- usuario que realizó la carga

\- fecha de creación

\- fecha de modificación



El objetivo es garantizar trazabilidad total.



\---



\## Supercopa



Utiliza equipos temporales.



No utiliza participantes individuales directamente.



\---



\## Ranking Temporada



Es la fuente oficial para:



\- ascensos

\- descensos

\- clasificación a copas

\- rankings históricos



\---



\## Escudos



Los equipos deberán soportar escudos oficiales.



Preferencia:



\- almacenamiento local

\- independencia de APIs externas



\---



\## Zona Horaria



La aplicación deberá operar utilizando horario argentino.



Configuración pendiente:



America/Argentina/Buenos\_Aires

