# Video demo de FleetGuard — guion

**Versión:** v0 (2026-11-16). Primer borrador: la voz todavía no se leyó en voz alta ni se cronometró.

## Qué es este video

- Demostración grabada de **unos 5 minutos** (entre 4:50 y 5:20; ni 3 ni 7).
- Para la presentación de la facultad. **No se publica en YouTube.** Se proyecta con parlante propio.
- **Solo la app, nada técnico:** ni backend, ni código, ni arquitectura. Las palabras de interfaz que usa un
  programador ("dashboard", "modal") sí van: buena parte del público son programadores.
- Referencia de estilo: el video de miTVU del cuatrimestre pasado
  (https://www.youtube.com/watch?v=oGvUdvQByfo). Tiene logo al principio y al final, carteles por rol, zooms a las
  partes de la pantalla y música de fondo todo el tiempo.

## Reglas del guion

- **Una sola historia de punta a punta.** Un defecto real recorre los tres roles: el chofer lo reporta, el admin lo
  planifica, el técnico lo resuelve y el chofer vuelve a salir. Esa es la diferencia con el video de referencia, que
  mostraba tres recorridos sueltos. Después de la historia viene un repaso rápido del resto de la app.
- **Siempre se sabe dónde estamos:**
  - un mapa del ciclo en cada cambio de rol;
  - la etiqueta fija del rol en una esquina, todo el tiempo: `CHOFER · Carlos · celular`;
  - las pantallas del chofer y del técnico, dentro del dibujo de un celular.
- **Tono neutro, en "ustedes"**, como el video de referencia: "el chofer selecciona su unidad", "desde el panel
  podemos ver…". Sin voseo.
- **Sin subtítulos.** Solo palabras clave en pantalla, de 5 a 8 en todo el video (ver la columna Edición).
- **Ritmo de la voz:** unas 2,1 palabras por segundo, como el video de referencia. Una pausa de 2 a 4 segundos con
  música sola en cada cambio de
  rol.
- **Mezcla:** la música suena todo el tiempo, unos 10 dB por debajo de la voz. Cuando la voz se calla, la música no
  sube más de 4 o 5 dB.

## Elenco y datos

Lo que se ve en pantalla sale de `seed-demo.sql` más `seed-video.sql`, los dos en `../TIP - Backend/docs/db/`. El
segundo se corre justo después del primero y deja la app en el punto de partida exacto de la escena 2. Correr los
dos de nuevo es **volver a empezar una toma**. Las fechas de `seed-demo.sql` son relativas al día en que se corre,
así que siempre se ven actuales.

| Qué | Valor | Notas |
|---|---|---|
| Chofer | Carlos Gómez (`carlos.gomez`) | `seed-video.sql` le saca el viaje abierto que tiene en el Scania AE215KT (pasa a Diego Sosa) |
| Técnico | Javier Romero (`javier.romero`) | `seed-video.sql` le pasa sus dos OTs abiertas a Nicolás Benítez, así "Mis órdenes" muestra solo la de la historia |
| Admin | `admin` | Sus avisos anteriores quedan leídos: el del video es el único sin leer |
| Vehículo de la historia | **Volvo FH 460, AF638RB** | El de Carlos. Disponible, sin defectos abiertos ni turnos. Tiene un semirremolque enganchado, así que el pre-viaje suma el checklist del remolque. Para la escena 13 tiene el aviso de consumo alto, un mantenimiento por vencer y el seguro por vencer en 10 días |
| Km del pre-viaje | Unos 150 km más que el del vehículo | El Volvo arranca en 297.800 km. Por ejemplo, 297.950 |
| Defecto en vivo | Ítem "Fugas visibles debajo del vehículo", **bloqueante**. Título: "Pérdida de aceite" | Foto: `demo-fuga-aceite.jpg`. Se cambió de "pérdida de aire en frenos" porque el Constellation AE487GD ya tiene ese defecto abierto en los datos de demo, y en la lista se verían dos casi iguales |
| Foto del cierre del técnico | `demo-ot-taller.jpg` | O una propia |
| Resumen del admin | El de `seed-demo.sql` | Hay vehículos al día, por vencer y vencidos, 5 defectos abiertos y 2 vehículos en viaje |
| Calendario semanal | 6 turnos en la semana | Los de `seed-demo.sql` |

## Escenas

Los tiempos son de referencia y se ajustan cuando esté grabada la voz. Los textos entre comillas son los que se ven
en la app.

### 0 · Apertura — 0:00 a 0:18

- **Pantalla:** logo de FleetGuard animado sobre el fondo de la app (`#F3F4F0`).
- **Voz** (35 palabras):
  > Hola. En una empresa de transporte, cada camión parado significa pérdidas, y muchas fallas se descubren cuando
  > ya es tarde. Por eso creamos FleetGuard, un sistema de mantenimiento preventivo e inspecciones para flotas de
  > vehículos.
- **Edición:** logo provisorio hasta que se defina el final con Tomás. La música arranca con el logo.

### 1 · El ciclo — 0:18 a 0:41

- **Pantalla:** diagrama animado del ciclo de tres roles: chofer → administrador → técnico → chofer.
- **Voz** (48 palabras):
  > FleetGuard conecta a tres roles: el chofer, que inspecciona su vehículo antes y después de cada viaje; el
  > administrador, que ve el estado de toda la flota y organiza el trabajo; y el técnico, que realiza las
  > reparaciones. Vamos a seguir un caso real, de punta a punta.
- **Edición:** cada rol se ilumina cuando se lo nombra. El mismo diagrama vuelve en cada cambio de rol, con el rol
  activo resaltado.

### 2 · Chofer: elegir el vehículo — 0:41 a 1:01

- **Cartel:** CHOFER (1,5 s, con el ciclo y el chofer resaltado).
- **Pantalla:** chofer en el celular, con la lista de vehículos ("Elegí un vehículo para iniciar la inspección").
- **Acción:** escribe la patente en "Buscar por patente" y toca "Pre-viaje".
- **Voz** (40 palabras):
  > Empezamos con Carlos, uno de los choferes de la empresa. Desde su celular ve los vehículos de la flota; busca su unidad por
  > patente, o escanea el código QR pegado en la cabina, y comienza la inspección previa al viaje.
- **Edición:** etiqueta fija `CHOFER · Carlos · celular`. Zoom al buscador. No hace falta mostrar el escaneo del QR
  (ver la escena 13).

### 3 · Chofer: el checklist — 1:01 a 1:16

- **Pantalla:** checklist del pre-viaje, con "Inspección visual (exterior)", "Inspección interior (cabina)" y
  "Estado del vehículo".
- **Acción:** scroll lento por las secciones.
- **Voz** (27 palabras):
  > El checklist está organizado por secciones: exterior, cabina y estado del vehículo. Carlos solo marca lo que
  > tiene un problema; todo lo demás se da por revisado.
- **Edición:** zoom a la indicación "Marcá solo lo que tenga un defecto."

### 4 · Chofer: reportar el defecto — 1:16 a 1:38

- **Pantalla:** el ítem "Fugas visibles debajo del vehículo" abierto, con el panel del defecto.
- **Acción:** marca el ítem, escribe el título "Pérdida de aceite", elige "Bloqueante", saca la foto y dicta la
  descripción con el micrófono.
- **Voz** (35 palabras):
  > Al revisar debajo del camión, Carlos encuentra una pérdida de aceite. Marca el ítem e indica la gravedad: en este
  > caso, es bloqueante. Después saca una foto y dicta la descripción, sin necesidad de escribir.
- **Edición:**
  - palabra clave **"Defecto bloqueante"** cuando elige la gravedad;
  - zoom a la foto y al texto que aparece mientras dicta;
  - el momento de elegir el archivo de la foto se corta.

### 5 · Chofer: enviar y bloqueo — 1:38 a 2:02

- **Pantalla:** "Enviar inspección", y después la confirmación: "Mantenimiento fue notificado — vehículo no apto para
  circular."
- **Voz** (45 palabras):
  > Al enviar la inspección, la aplicación le indica que no salga con el camión, y mantenimiento recibe el aviso al
  > instante. Desde ese momento, el vehículo queda bloqueado. Y si no hay señal, la inspección se guarda y se envía
  > sola al volver la conexión.
- **Edición:** zoom al cartel de confirmación. Palabra clave **"Vehículo bloqueado"**.
- **Pausa:** 2 a 3 s de música sola.

### 6 · Admin: el aviso y el resumen — 2:02 a 2:35

- **Cartel:** ADMINISTRADOR (ciclo con el admin resaltado).
- **Pantalla:** panel del admin en la computadora, pestaña Resumen.
- **Acción:** abre la campanita y ve el aviso "Defecto bloqueante en <patente>", con el texto "<defecto>. Reportado
  en el pre-viaje por Carlos Gómez. El vehículo no puede salir hasta resolverlo." Después recorre los indicadores
  ("Vehículos al día", "Por vencer", "Vencidos", "Defectos abiertos") y la disponibilidad de la flota. En el medio,
  un corte de 3 segundos a la pestaña Notificaciones, con los canales de cada aviso.
- **Voz** (63 palabras):
  > Del otro lado, el administrador recibe el aviso con el detalle del problema, quién lo reportó y en qué
  > vehículo. Cada aviso puede llegar a la campanita, como notificación del navegador o por correo, según lo que se
  > configure. En el resumen ve el estado de toda la flota de un vistazo: vehículos al día, mantenimientos por vencer y
  > vencidos, y defectos abiertos.
- **Edición:** etiqueta fija `ADMINISTRADOR · computadora`. Zoom a la campanita, después a los canales de
  Notificaciones y por último a la fila de indicadores.

### 7 · Admin: el defecto — 2:35 a 2:46

- **Pantalla:** la pantalla de Defectos ("Reportados en inspecciones, para priorizar mantenimiento"), con el de
  Carlos primero. Cada renglón muestra la descripción, la patente, la fecha, "Ver foto", la gravedad y el botón
  "Planificar".
- **Acción:** toca "Ver foto" y se abre la foto a pantalla completa.
- **Voz** (23 palabras):
  > En la lista de defectos, el de Carlos aparece primero, marcado como bloqueante, con la descripción que dictó y la
  > foto que sacó.
- **Edición:** zoom a la etiqueta de gravedad y después a la foto abierta.

### 8 · Admin: planificar y asignar — 2:46 a 3:06

- **Pantalla:** el modal "Planificar" del defecto (día, hora y responsable). Al confirmar, el renglón del defecto
  muestra "OT asignada · javier.romero". Corte al Resumen, con el turno nuevo en el calendario semanal.
- **Acción:** elige día y hora, asigna a Javier Romero y confirma.
- **Voz** (34 palabras):
  > Desde ahí lo planifica: elige el día y el horario, y se lo asigna a Javier, uno de los técnicos. Se genera la
  > orden de trabajo y el turno aparece en el calendario semanal.
- **Edición:**
  - palabra clave **"Orden de trabajo asignada"** sobre el renglón "OT asignada · javier.romero";
  - zoom al turno nuevo en el calendario. Si el corte al Resumen alarga mucho la escena, se puede quitar.
- **Pausa:** 2 a 3 s de música sola.

### 9 · Técnico: Mis órdenes — 3:06 a 3:22

- **Cartel:** TÉCNICO (ciclo con el técnico resaltado).
- **Pantalla:** técnico en el celular. La campanita muestra el aviso "Orden de trabajo asignada", que abre la orden
  directamente. La orden muestra "Qué hay que hacer", "Defecto reportado" y la foto. "Mis órdenes" se ve de pasada.
- **Voz** (32 palabras):
  > Javier, por su parte, recibe el aviso en su celular y abre la orden. Ahí tiene todo lo que necesita: qué hay
  > que hacer, el defecto reportado y la foto del chofer.
- **Edición:** etiqueta fija `TÉCNICO · Javier · celular`.

### 10 · Técnico: trabajar y comentar — 3:22 a 3:34

- **Pantalla:** "Empezar trabajo", y después la sección Comentarios.
- **Acción:** empieza el trabajo y deja un comentario dictado, por ejemplo "Cambio la válvula, en una hora queda
  listo".
- **Voz** (22 palabras):
  > Empieza el trabajo y, si necesita avisar o consultar algo, deja un comentario en la orden, que le llega
  > directamente al administrador.
- **Edición:** zoom al comentario recién enviado.

### 11 · Técnico: cerrar la orden — 3:34 a 3:48

- **Pantalla:** "Cierre del trabajo": descripción, kilómetros y "Fotos del trabajo". Después, "Finalizar".
- **Voz** (25 palabras):
  > Al terminar, registra qué se hizo, los kilómetros del vehículo y una foto del trabajo, y finaliza la orden. Con
  > eso, el defecto queda resuelto.
- **Edición:** palabra clave **"Defecto resuelto"** sobre "El defecto quedó resuelto.".
- **Pausa:** 2 s de música sola.

### 12 · Chofer: vuelve a salir — 3:48 a 4:17

- **Cartel:** el ciclo completo, con la vuelta al chofer resaltada.
- **Pantalla:** chofer en el celular. La campanita muestra "Tu vehículo vuelve a estar disponible", con el texto
  "<patente> ya puede salir. Se resolvió con la orden de trabajo «<título>»." El vehículo vuelve a figurar
  disponible en la lista. Después Carlos hace un pre-viaje sin defectos (se ve de pasada, acelerado) y queda en
  "Mi viaje", donde aparece "Reportar un problema".
- **Voz** (50 palabras):
  > Carlos recibe el aviso de que su vehículo vuelve a estar disponible, con la orden de trabajo que lo resolvió, y
  > ya puede volver a salir. Y si durante el viaje surge un problema, lo reporta desde el celular, sin esperar a la
  > próxima inspección. Así se cierra el ciclo.
- **Edición:** etiqueta fija `CHOFER · Carlos · celular`. Zoom al aviso y después al botón "Reportar un problema".
  El pre-viaje sin defectos va acelerado, sin voz encima.

### 13 · Admin: todo lo demás — 4:17 a 4:59

Montaje rápido, de 5 a 7 segundos por pantalla, en la computadora del admin.

- **Cartel:** "Y además…" o ADMINISTRADOR.
- **Pantallas, en orden:**
  1. Planes de Mantenimiento y "Próximos vencimientos".
  2. Detalle del vehículo, pestañas Historial y Documentación (vencimientos).
  3. Pestaña Neumáticos, con la vista de arriba del vehículo.
  4. Tarjeta del QR del vehículo. Cubre lo que no se mostró en la escena 2.
  5. Pestaña Combustible del Volvo, con el aviso de consumo alto.
  6. Disponibilidad de la flota en el Resumen, con el tiempo fuera de servicio.
  7. Gastos: el gráfico por origen.
  8. Comparar vehículos por costo por km.
  9. Exportar el historial a PDF.
- **Voz** (87 palabras):
  > Además de las reparaciones, FleetGuard gestiona el mantenimiento preventivo: planes por kilómetros o por tiempo,
  > que avisan antes de vencer. Cada vehículo tiene su ficha, con su historial, la documentación y sus
  > vencimientos, el estado de los neumáticos y su propio código QR. La aplicación también detecta consumos de
  > combustible fuera de lo normal y muestra cuánto tiempo pasó cada vehículo fuera de servicio. El administrador
  > controla los gastos de la flota, compara el costo por kilómetro entre vehículos y puede exportar el historial
  > completo en PDF.
- **Edición:** un zoom distinto por pantalla. Transiciones cortas al ritmo de la música.
- **Tentativo:** si con el primer corte sobra tiempo, se pueden sumar los defectos recurrentes. Si falta, lo primero
  que sale es la comparación de vehículos.

### 14 · Cierre — 4:59 a 5:07

- **Pantalla:** el logo otra vez, con "Muchas gracias" y los nombres del equipo.
- **Voz** (11 palabras):
  > FleetGuard: menos vehículos parados, más control de la flota. Muchas gracias.
- **Edición:** la música termina con el logo.

## Cuentas

- **Voz total:** 577 palabras. Leídas a **2,1 palabras por segundo**, más carteles, pausas y acciones sin voz, dan
  unos **5:07**. Los tiempos de cada escena están calculados así: palabras divididas por 2,1, más los segundos de
  carteles, pausas y acciones.
- **El ritmo importa más que el texto:** el borrador 1 se leyó a 2,45 palabras por segundo. A ese ritmo, estas
  mismas 577 palabras darían unos 4:35.
- **Si sobra o falta tiempo en el primer corte:**
  - si sobra, se pueden sumar los defectos recurrentes (escena 13) o "¿Salís igual?" cuando el vehículo tiene turno
    de taller ese día (escena 2);
  - si falta, lo primero que sale es la comparación de vehículos (escena 13).
- **Lo que no se muestra:** el login de cada rol, el ABM de usuarios, las plantillas de checklist, la importación de
  vehículos, los formularios de combustible del admin, pausar una OT y la actividad de usuarios.

## Cronometraje

**Borrador 1 de la voz (2026-11-18).** Guido leyó las 15 escenas de corrido, con el texto de la v0.2. Lo midió
Claude sobre el audio: las escenas se separaron por las pausas, así que los cortes son aproximados (±1 s).

| Escena | Duración | Palabras | Palabras por segundo |
|---|---|---|---|
| 0 · Apertura | 8,5 s | 16 | 1,9 |
| 1 · El ciclo | 19,2 s | 50 | 2,6 |
| 2 · Elegir el vehículo | 14,9 s | 36 | 2,4 |
| 3 · El checklist | 8,6 s | 28 | 3,3 |
| 4 · Reportar el defecto | 13,9 s | 34 | 2,4 |
| 5 · Enviar y bloqueo | 19,4 s | 45 | 2,3 |
| 6 · Aviso y resumen | 18,1 s | 44 | 2,4 |
| 7 · El defecto | 9,6 s | 24 | 2,5 |
| 8 · Planificar | 12,1 s | 33 | 2,7 |
| 9 · Mis órdenes | 13,6 s | 32 | 2,4 |
| 10 · Trabajar y comentar | 10,3 s | 24 | 2,3 |
| 11 · Cerrar la orden | 11,2 s | 25 | 2,2 |
| 12 · Vuelve a salir | 14,3 s | 27 | 1,9 |
| 13 · Todo lo demás | 30,4 s | 78 | 2,6 |
| 14 · Cierre | 5,2 s | 11 | 2,1 |
| **Total** | **3:29** | **~510** | **2,45** |

Lo que dice:

- **Falta más de un minuto.** Con 3:29 de voz, más unos 15 a 20 s de carteles y pausas con música, el video da
  alrededor de 3:50. El objetivo es 5:00.
- **El ritmo es más rápido que el de la referencia:** 2,45 palabras por segundo contra unas 2,05 del video de miTVU.
  Leer más despacio, sin cambiar el texto, ya suma unos 40 segundos.
- **El volumen sube unos 3,5 dB desde la escena 6.** De la 0 a la 5 la voz está en unos -18 dB y de la 6 en adelante
  en unos -14,5 dB. En la edición se empareja, pero en la grabación final conviene mantener siempre la misma
  distancia al micrófono.
- **El ambiente es silencioso:** el piso de ruido está en unos -50 dB, y el pico más alto en -6,5 dB, sin saturar.

**Tono (2026-11-18).** Claude siguió la altura de la voz cuadro a cuadro en el borrador y en el video de miTVU. En
el de miTVU la medición es más gruesa, porque la música de fondo tapa parte de la voz.

| | Borrador 1 | miTVU |
|---|---|---|
| Altura típica | 180 Hz | 125 Hz |
| Variación dentro de las frases (desvío) | 3,7 semitonos | 2,9 semitonos |
| Rango habitual (del 10 % al 90 %) | 10 semitonos | 7,7 semitonos |
| Cambio de altura de principio a fin | **baja unos 8 semitonos** (249 Hz en la apertura, 156 Hz en el cierre) | casi nada (entre 123 y 132 Hz todo el video) |

- **No suena monótono:** la voz varía más que la de la referencia.
- **Arranca muy arriba y termina abajo.** La apertura está casi una octava por encima del cierre, y la voz va bajando
  de a poco durante todo el borrador. Es lo típico de leer de corrido: se arranca con mucha energía y se va
  apagando. Para la grabación final conviene arrancar más tranquilo y sostener la misma energía hasta el "Muchas
  gracias". Grabar por escena, con pausas, ayuda.

**Transcripción (2026-11-18).** Guido pasó la transcripción automática del borrador. Además de los cambios de la
v0.3:

- La transcripción escribió "Freeward" y "Fleetward" en lugar de FleetGuard. Puede ser solo un error del
  reconocedor, pero conviene marcar bien la "g" de "guard" y acordar con Tomás cómo se pronuncia.
- Le faltan palabras cortas en algunos lugares ("se lo asigna Javier", "la lista defectos"). Puede ser el
  reconocedor o que se comieron al leer rápido. Leyendo más despacio se resuelve.

**Borrador 2 de la voz (2026-11-23).** Con la v0.4 y el micrófono bueno. Guido lo propone como **toma
candidata para el video final**: si hay que corregir algo, se regraba solo esa parte. Dura **4:51**. Los cortes
entre escenas se calcularon alineando las oraciones del guion con las pausas, así que tienen ±1 o 2 s de error.

| Escena | Desde | Duración | Palabras por segundo |
|---|---|---|---|
| 0 · Apertura | 0:00 | 20 s | 1,7 |
| 1 · El ciclo | 0:20 | 19 s | 2,1 |
| 2 · Elegir el vehículo | 0:39 | 23 s | 1,8 |
| 3 · El checklist | 1:02 | 12 s | 2,2 |
| 4 · Reportar el defecto | 1:14 | 17 s | 2,1 |
| 5 · Enviar y bloqueo | 1:31 | 24 s | 1,9 |
| 6 · Aviso y resumen | 1:55 | 34 s | 1,9 |
| 7 · El defecto | 2:29 | 14 s | 1,7 |
| 8 · Planificar | 2:42 | 14 s | 2,4 |
| 9 · Mis órdenes | 2:57 | 16 s | 2,1 |
| 10 · Trabajar y comentar | 3:12 | 11 s | 2,0 |
| 11 · Cerrar la orden | 3:23 | 12 s | 2,1 |
| 12 · Vuelve a salir | 3:35 | 23 s | 2,1 |
| 13 · Todo lo demás | 3:58 | 47 s | 1,8 |
| 14 · Cierre | 4:46 | 6 s | 1,8 |

- **El tiempo da.** 4:51 de voz, más el logo, los carteles y las pausas con música entre roles (unos 15 a 20 s),
  da unos **5:05 a 5:10**.
- **Ritmo:** 2,0 palabras por segundo en total, prácticamente el de la referencia (2,05).
- **Los "espacios vacíos" son normales.** Entre oraciones hay pausas de 1 segundo, unos 81 s de silencio en total.
  El video de miTVU tiene casi lo mismo: unos 70 a 80 s de pausas en 5:18, con un promedio de 1,4 s cada una. Con
  la música de fondo y la pantalla moviéndose, no se van a sentir como huecos. Si en la edición falta lugar, las
  más largas se pueden acortar a medio segundo.
- **Volumen parejo:** de -19 dB al principio a -21,5 dB al final, una diferencia que no se nota. Se corrigió el
  salto de 3,5 dB del borrador 1.
- **Muy buen ruido de fondo:** el piso está en unos -62 dB, contra -50 dB del borrador 1. El micrófono nuevo se nota.
  No satura (el pico más alto está en -7,5 dB).
- **Tono parejo de punta a punta:** la altura típica va de 155 a 176 Hz en todas las escenas, sin la caída de casi
  una octava del borrador 1. La variación (3,5 semitonos) sigue por encima de la de la referencia (2,9), así que no
  suena plano. Las escenas 11 y 12 son las más planas (2,6 y 2,9), pero siguen al nivel de la referencia.

**Transcripción del borrador 2 (2026-11-23).** El borrador 2 es la toma de voz del video, así que lo que vale es lo
que dice la grabación, no el texto de las escenas de arriba (v0.4). Diferencias con el guion:

- Guido cambió la apertura ("Hola, sean bienvenidos a FleetGuard…", sin la frase del problema) y sumó una frase al
  cierre: "Esto es FleetGuard, una aplicación que ayuda a las empresas del transporte a gestionar sus flotas de
  manera sencilla y práctica." Queda así.
- **No hay frases para regrabar.** Claude propuso regrabar tres y Guido decidió dejarlas como están:
  - **escena 6**, "dashboard", y **escena 8**, "modal": el público son en buena parte programadores, así que esas
    palabras se entienden. En la escena 8, el primer "planificar" nombra el botón y el segundo, la acción;
  - **escena 11**: la frase está completa ("…y una foto del trabajo y dejando el defecto reportado por Carlos como
    resuelto"). Claude la había marcado como cortada por error.
- **Opcionales**, solo si en algún momento se regraba algo:
  - escenas 5 y 12: "con dicho camión" suena a texto escrito. Mejor "que no salga con el camión" y "ya puede
    volver a salir";
  - escena 13: "Además del reporte de defectos, la gestión de órdenes de trabajo y el arreglo técnico de los
    mismos" → "Además del reporte de defectos y las órdenes de trabajo, FleetGuard gestiona el mantenimiento
    preventivo".
- **Para escuchar**, porque puede ser error del reconocedor o de la lectura: "inspecciónpección" (escena 2, cerca
  de 0:55), "gradad" en lugar de "gravedad" (escena 4, cerca de 1:20) y "fruta" en lugar de "flota" (escena 6). La
  transcripción vuelve a escribir "Fleetward" y "fetward": conviene escuchar una vez cómo suena FleetGuard.

## Ensayo (2026-11-23)

Claude recorrió la historia completa en el navegador de la sesión, con los dos seeds recién corridos: el celular a
375×812 y la computadora a 1536×864 (1920×1080 con el zoom al 125 %). **Toda la historia funciona de punta a
punta.** Lo que hay que saber para grabar, escena por escena:

- **Escena 2:** al tocar la tarjeta del vehículo se abre directo el pre-viaje. No hay un botón "Pre-viaje" aparte.
  El encabezado muestra el usuario (`carlos.gomez`) y la hora real, así que en el video se va a ver la hora en que
  se grabó.
- **Escena 3:** las secciones son "Inspección visual (exterior)", "Inspección interior (cabina)" y "Remolque" (con
  su propio checklist, porque el Volvo lleva el semirremolque AD440TP). No hay una sección "Estado del vehículo":
  cuando la voz la nombra, en pantalla se ve el remolque. No hace falta cambiar nada. Arriba dice "18 controles en
  OK", y después de marcar el defecto, "1 de 18 con defecto".
- **Escena 4:** al marcar el ítem se abre el panel con Gravedad, Título, Descripción, "Dictar" y Foto, y entra casi
  entero en la pantalla del celular. Al elegir "Bloqueante", la foto pasa a "(obligatoria)" pero la descripción
  sigue diciendo "(opcional)", aunque también es obligatoria. Es un detalle menor: conviene no hacerle zoom. La
  miniatura de la foto es chica, así que necesita zoom.
- **Escena 5:** antes de enviar aparece el **Resumen** con un anillo rojo ("17/18 OK"), el defecto marcado como
  BLOQUEANTE y la casilla "Declaro que la información es correcta". Se ve muy bien: vale la pena mostrarlo. Después
  sale "Inspección enviada", con el recuadro rojo "Mantenimiento fue notificado — vehículo no apto para circular."
- **Escena 6:** el aviso del admin dice "Defecto bloqueante en AF638RB — Pérdida de aceite. Reportado en el
  pre-viaje por carlos.gomez. El vehículo no puede salir hasta resolverlo." El Resumen muestra 15 vehículos al día,
  3 por vencer, 2 vencidos y 6 defectos abiertos, y la tarjeta "Defectos abiertos recientes" ya tiene arriba el de
  Carlos. La pestaña Notificaciones muestra las columnas Campanita, Push (navegador) y Email: sirve para el corte.
  - En el ensayo, arriba del aviso del defecto apareció un "Mantenimiento por vencer" del Volvo, disparado por el km
    del pre-viaje. También aparecieron avisos viejos de pruebas anteriores. **`seed-video.sql` ya los evita.**
  - Si Chrome tiene bloqueadas las notificaciones de `localhost:5173`, la campanita muestra abajo un cartel
    ("Bloqueaste las notificaciones de FleetMaintenance…"). Hay que permitirlas antes de grabar.
- **Escena 7:** en la pantalla de Defectos el contenido ocupa solo el centro, así que en 1920×1080 necesita zoom.
  "Ver foto" abre la foto grande.
- **Escena 8:** el modal "Planificar" propone mañana a las 09:00, y eso sirve tal cual. La voz dice "se puede
  elegir un horario y día": la transcripción había entendido "hoy día". Si se cambia la fecha, tiene que quedar
  **en el futuro**. Si no, la app responde "Datos inválidos para programar el mantenimiento". El técnico aparece como `javier.romero`. Al confirmar, el
  renglón muestra "OT asignada · javier.romero" y el botón pasa a "Replanificar".
- **Escena 9:** el aviso dice "Te asignaron una orden de trabajo — Pérdida de aceite (AF638RB), planificada para el
  <día> a las <hora>." **Tocarlo no abre la orden:** así está hecho, porque solo los avisos de comentarios la abren.
  Se graba así: se toca el aviso, se cierra el panel y se toca la orden en "Mis órdenes", que tiene solo esa. La
  orden muestra "Defecto reportado" (BLOQUEANTE, descripción, "Reportado por carlos.gomez" y la foto grande). No
  tiene una sección "Qué hay que hacer" aparte: el título y el defecto cumplen ese papel.
- **Escena 10:** "Empezar trabajo" y el comentario funcionan. El comentario aparece con la etiqueta "Técnico" y la
  hora.
- **Escena 11:** el cierre pide "Qué se hizo" (con "Dictar") y "Fotos del trabajo". **No pide kilómetros**: la app
  los pide solo en los mantenimientos de un plan. Y al finalizar dice "Orden finalizada — El mantenimiento quedó
  registrado como hecho", no "El defecto quedó resuelto", porque toda orden que nace de "Planificar" cuenta como
  mantenimiento programado. La voz nombra los kilómetros y el defecto resuelto. **Queda así** (decidido con
  Guido): la voz no tiene que repetir lo que dice la pantalla, y suena más natural.
- **Escena 12:** el aviso del chofer dice "Tu vehículo vuelve a estar disponible — AF638RB ya puede salir. Se resolvió
  con la orden de trabajo «Pérdida de aceite»." **El título de la orden se lee bien.** El pre-viaje sin defectos
  termina en un anillo verde ("18/18 OK, sin defectos reportados. Todo en orden.") y en "Mi viaje", con "En viaje",
  "Con el remolque AD440TP" y los botones "Cerrar viaje", "Cargar combustible" y "Reportar un problema".
- **Escena 13:** Neumáticos (vista de arriba del tractor) y Combustible (gráfico de consumo por mes) cargan bien.

**Para la grabación real:** la foto del defecto y la del trabajo se eligen con el selector de archivos. En el
ensayo se cargaron por código, porque el navegador de la sesión no tiene selector. El dictado lo probó Guido en su
Chrome el 2026-11-16 y anda (escenas 4 y 10).
Ya verificados en el código el 2026-11-16: el renglón del defecto en el admin (escena 7), el aviso del bloqueante al
admin (escena 6), el aviso de OT asignada al técnico (escena 9), el renglón "OT asignada · técnico" (escena 8) y el
aviso al chofer cuando el vehículo vuelve a estar disponible (escena 12). Para un defecto bloqueante, el chofer recibe
"Tu vehículo vuelve a estar disponible" y no "Defecto resuelto": la app no le manda los dos.

## Cambios

- **v0 (2026-11-16):** primer borrador, a partir de la propuesta charlada con Guido en la sesión.
- **v0.1 (2026-11-16):** escenas 6 a 9 y 12 ajustadas a los textos reales de los avisos y de la lista de defectos.
- **v0.4 (2026-11-18):** para llegar a 5 minutos, más texto y lectura más lenta (decidido con Guido). Se sumaron
  unas 70 palabras:
  - escena 0: el problema que resuelve la app;
  - escena 6: los canales de los avisos, con un corte a Notificaciones;
  - escena 12: reportar un problema durante el viaje, con un pre-viaje sin defectos acelerado;
  - escena 13: el consumo de combustible fuera de lo normal y el tiempo fuera de servicio.

  Los tiempos de todas las escenas se recalcularon a 2,1 palabras por segundo.
- **v0.3 (2026-11-18):** voz retocada con lo que mostró la transcripción del borrador 1:
  - se reescribieron las frases donde Guido se trabó: el "qué se rompió… que el vehículo no puede salir" de la escena 6
    (ahora sin la seguidilla de "que"), "Comienza" (ahora "Empieza") y el "vehículo" repetido de la escena 5;
  - entraron las improvisaciones que sonaron naturales: "uno de los choferes", "en este caso, es bloqueante",
    "Javier, por su parte", "Con eso, el defecto queda resuelto" y "ya puede volver a salir";
  - quedaron afuera "de la misma" (escena 1) y "con dicho vehículo" (escena 12), que suenan forzados.
- **v0.2 (2026-11-16):** datos definidos con `seed-video.sql`. El vehículo es el Volvo AF638RB, y el defecto en vivo
  pasa a ser una pérdida de aceite (escena 4).
