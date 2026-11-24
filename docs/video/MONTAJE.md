# Video demo de FleetGuard — montaje

Qué archivo va en cada escena y qué tramo se usa. Sirve para editar en CapCut sin volver a mirar todas las tomas.
Todas las tomas se grabaron entre el 2026-11-23 y el 2026-11-24, y Claude las revisó cuadro a cuadro. El guion está
en [`GUION.md`](GUION.md) y la guía de edición (pistas, estilo, música) en [`GRABACION.md`](GRABACION.md).

**Los tiempos de cada toma son aproximados (±0,5 s)**, salvo los cortes marcados como **exactos**, que se midieron cuadro
a cuadro.

## Archivos

La voz está en `C:\Users\Equipo\Downloads\`. Las tomas de pantalla están en
`C:\Users\Equipo\Videos\Grabaciones de pantalla\`, con el nombre que les pone Windows: "Grabación de pantalla
<fecha> <hora>.mp4". Conviene copiarlas a una carpeta del proyecto con el nombre corto de la primera columna.

| Nombre corto | Archivo original | Dura | Tamaño | Escenas |
|---|---|---|---|---|
| `voz.mp4` | `Borrador de FleetGuard #2.mp4` (Downloads) | 4:51 | solo audio | todas |
| `chofer-2a5.mp4` | `2026-11-23 232458` | 2:00 | 376×822 | 2, 3, 4, 5 |
| `admin-6a8.mp4` | `2026-11-23 235029` | 1:28 | 1920×906 | 6, 7, 8 (y 13) |
| `admin-notificaciones.mp4` | `2026-11-23 235514` | 0:20 | 1920×906 | 6 |
| `admin-foto.mp4` | `2026-11-24 000024` | 0:06 | 1920×904 | 7 |
| `tecnico-9a11.mp4` | `2026-11-24 001352` | 1:11 | 372×816 | 9, 10, 11 |
| `chofer-12a.mp4` | `2026-11-24 001507` | 0:16 | 374×818 | 12 |
| `chofer-12b.mp4` | `2026-11-24 002155` | 0:24 | 374×818 | 12 |
| `admin-13.mp4` | `2026-11-24 002738` | 1:54 | 1920×908 | 13 |
| `admin-comparar.mp4` | `2026-11-24 003424` | 0:14 | 1920×906 | 13 |
| `admin-pdf.mp4` | `2026-11-24 003546` | 0:17 | 1920×908 | 13 |

**Se descarta:** `2026-11-23 235559` (la primera toma de la foto: el cursor quedaba arriba de la foto).

## La voz

`voz.mp4` es la toma final y se usa entera. Dónde empieza cada escena (±1 o 2 s, medido sobre las pausas):

| Escena | Empieza | Dura |
|---|---|---|
| 0 · Apertura | 0:00 | 20 s |
| 1 · El ciclo | 0:20 | 19 s |
| 2 · Elegir el vehículo | 0:39 | 23 s |
| 3 · El checklist | 1:02 | 12 s |
| 4 · Reportar el defecto | 1:14 | 17 s |
| 5 · Enviar y bloqueo | 1:31 | 24 s |
| 6 · Aviso y resumen | 1:55 | 34 s |
| 7 · El defecto | 2:29 | 14 s |
| 8 · Planificar | 2:42 | 14 s |
| 9 · Mis órdenes | 2:57 | 16 s |
| 10 · Trabajar y comentar | 3:12 | 11 s |
| 11 · Cerrar la orden | 3:23 | 12 s |
| 12 · Vuelve a salir | 3:35 | 23 s |
| 13 · Todo lo demás | 3:58 | 47 s |
| 14 · Cierre | 4:46 | 6 s |

Entre escenas de distinto rol van 2 o 3 segundos de música sola, con el cartel del rol: antes de la 2, de la 6, de la
9 y de la 12. Hay que abrir ese hueco en la pista de voz.

## Gráficos

Están en [`graficos/png/`](graficos/png/), todos en PNG de 1920×1080 con los colores y las tipografías de la app. Los
genera [`graficos/generar.py`](graficos/generar.py), que guarda también los SVG en `graficos/svg/`. Para cambiar un
texto, se edita el script y se corre `py generar.py` desde esa carpeta, en unos 10 segundos.

| Archivo | Escena | Uso |
|---|---|---|
| `logo.png` | 0 | El logo completo sobre el fondo de la app |
| `logo-capa-camion.png` y `logo-capa-texto.png` | 0 | Las dos partes del logo, con fondo transparente y ya ubicadas. Se apilan sobre un fondo `#F3F4F0` y se animan por separado: primero el camión y después el nombre |
| `ciclo-0-base.png` | 1 | Los tres roles, ninguno resaltado. Abre la escena |
| `ciclo-1-chofer`, `ciclo-2-admin` y `ciclo-3-tecnico` | 1 | Fundido a cada uno cuando la voz nombra ese rol |
| `ciclo-4-completo.png` | 1 | Todo resaltado, con "…de punta a punta" |
| `cartel-1-chofer.png` | antes de la 2 | Cartel CHOFER |
| `cartel-2-admin.png` | antes de la 6 | Cartel ADMINISTRADOR |
| `cartel-3-tecnico.png` | antes de la 9 | Cartel TÉCNICO |
| `cartel-4-vuelta.png` | antes de la 12 | CHOFER otra vez, con la flecha del técnico al chofer en verde |
| `cartel-5-ademas.png` | antes de la 13 | "Y además…" |
| `cierre.png` | 14 | Logo, "Muchas gracias", los nombres del equipo y "Trabajo de Inserción Profesional · 2026" |
| `celular.png` | 2 a 5, 9 a 12 | El fondo de la app con el dibujo del celular y la pantalla transparente. Va **arriba** de la toma |
| `etiqueta-chofer`, `etiqueta-admin` y `etiqueta-tecnico` | cada rol | La etiqueta fija, arriba a la izquierda, durante todas las escenas de ese rol |
| `clave-1-defecto-bloqueante` | 4 | Palabra clave en rojo, a la derecha del celular |
| `clave-2-vehiculo-bloqueado` | 5 | También en rojo, a la derecha del celular |
| `clave-3-orden-asignada` | 8 | En azul. Queda a la derecha, sobre la pantalla del admin |
| `clave-4-defecto-resuelto` | 11 | En verde |

Todos ocupan el cuadro entero (1920×1080) con fondo transparente y ya están ubicados: se ponen en su pista sin mover
ni escalar. Así CapCut no los agranda solos, como hace con una imagen chica.

**Cómo va el celular:** la toma abajo, escalada al **88 %** y centrada, y `celular.png` arriba. Con 88 % la toma
llena el hueco de la pantalla y lo que sobra queda tapado por el borde. Sirve para las tres tomas del celular, que
tienen casi la misma proporción. Un zoom sobre la toma queda adentro de la pantalla. Para acercarse con el celular
entero, hay que agrupar las dos pistas y hacer el zoom sobre el grupo. Se probó con cuadros reales de
`chofer-2a5` y `admin-13`.

**Las tomas del admin** (1920×906) entran a lo ancho y dejan unas franjas de 87 px arriba y abajo. Conviene poner el
fondo del proyecto en `#F3F4F0` para que esas franjas sean del color de la app.

El logo es **provisorio**: usa el camión del favicon de la app, con un tilde verde. El definitivo queda para charlarlo
con Tomás.

## Escenas 0 y 1 — apertura y ciclo

No hay tomas de pantalla: son el logo y el ciclo de los tres roles (ver Gráficos).

## Escenas 2 a 5 — chofer: `chofer-2a5.mp4`

Celular, con la etiqueta `CHOFER · Carlos · celular`.

| Tramo | Qué se ve | Escena | Uso |
|---|---|---|---|
| 0:00 – 0:09 | Lista de la flota | 2 | Abrir con este plano |
| 0:09 – 0:16 | Búsqueda "AF638" y toque en el Volvo | 2 | Zoom al buscador |
| 0:16 – 0:38 | Pre-viaje: checklist por secciones | 3 | Acelerar el scroll. Zoom a "Marcá solo lo que tenga un defecto" |
| 0:39 – 0:58 | "Fugas visibles…", "Bloqueante" y el título | 4 | Palabra clave **"Defecto bloqueante"** |
| 0:59 – 1:10 | Dictado de la descripción (botón rojo "Detener") | 4 | Zoom al texto que aparece |
| 1:10 – 1:15 | Foto adjunta | 4 | La miniatura es chica: zoom de 2× como máximo |
| 1:15 – 1:31 | Resto del checklist y remolque | 3 o 4 | Acelerar o cortar |
| 1:32 – 1:41 | Resumen: anillo rojo "17/18" y casilla "Declaro…" | 5 | Vale la pena mostrarlo |
| 1:41 – 1:49 | "Inspección enviada" con el recuadro rojo | 5 | Palabra clave **"Vehículo bloqueado"** |
| **1:49 (corte)** | | | **El clic derecho está en 1:51,7 – 1:52,6 (exacto): no usar nada después de 1:49** |

## Escenas 6 a 8 — admin: `admin-6a8.mp4` y dos clips

Computadora, con la etiqueta `ADMINISTRADOR · computadora`.

| Archivo y tramo | Qué se ve | Escena | Uso |
|---|---|---|---|
| `admin-6a8` 0:00 – 0:05 | Resumen quieto | 6 | Fondo del cartel ADMINISTRADOR, o se corta |
| `admin-6a8` 0:05 – 0:13 | Campanita abierta con "Defecto bloqueante en AF638RB" | 6 | **Zoom solo al aviso**: abajo dice "Recibí estos avisos aunque FleetMaintenance…", que no va |
| `admin-notificaciones` 0:06,8 – 0:19,6 | Pestaña Notificaciones: Campanita, Push y Email | 6 | Con la frase de los canales. Zoom a la primera fila y las columnas |
| `admin-6a8` 0:13 – 0:22 | Resumen: indicadores y calendario | 6 | Zoom a la fila de indicadores |
| `admin-6a8` 0:22 – 0:43 | Scroll por el Resumen | 6 | Acelerar al doble o recortar |
| `admin-6a8` 0:45 – 0:53 | Defectos: "Perdida de Aceite" primero, BLOQUEANTE | 7 | Zoom al renglón |
| `admin-foto` 0:02,1 – 0:05,3 (exacto) | La foto del defecto a pantalla completa | 7 | Con "…y la foto que tomó" |
| `admin-6a8` 0:53,75 – 1:09 (exacto el inicio) | Modal Planificar: fecha, hora, técnico | 8 | Recortar las esperas |
| `admin-6a8` 1:10 – 1:15 | Renglón "OT asignada · javier.romero" | 8 | Palabra clave **"Orden de trabajo asignada"** |
| `admin-6a8` 1:15 – 1:22 | Calendario con el turno del martes 24 | 8 | Zoom al turno |
| `admin-6a8` 1:22,75 – 1:26,25 (exacto) | Detalle del turno: "Defecto reportado", "Asignada · javier.romero" | 8 | Cierre de la escena |

## Escenas 9 a 11 — técnico: `tecnico-9a11.mp4`

Celular, con la etiqueta `TÉCNICO · Javier · celular`.

| Tramo | Qué se ve | Escena | Uso |
|---|---|---|---|
| 0:00 – 0:03 | "Mis órdenes" (dos órdenes: AF638RB y AD556HX) | 9 | Corto |
| 0:03 – 0:09 | Campanita: "Te asignaron una orden de trabajo" | 9 | Zoom al aviso, sin el cartel de "FleetMaintenance" de abajo |
| 0:10 – 0:19 | La orden: "Defecto reportado", descripción y foto | 9 | |
| 0:19,75 – 0:22 (exacto) | La foto a pantalla completa | 9 | |
| 0:25 – 0:27 | "Empezar trabajo" | 10 | |
| 0:31 – 0:43 | El comentario, publicado con la etiqueta "Técnico" | 10 | Zoom al comentario publicado |
| 0:45 – 0:56 | "Qué se hizo", dictado (botón rojo "Detener") | 11 | |
| 0:56 – 1:01 | Foto del trabajo adjunta | 11 | |
| 1:02 – 1:08 | "Finalizar" y "Orden finalizada" | 11 | Palabra clave **"Defecto resuelto"** |
| **1:08 (corte)** | | | Después toca "Volver a mis órdenes": no se usa |

## Escena 12 — chofer: `chofer-12a.mp4` y `chofer-12b.mp4`

Celular, con la etiqueta `CHOFER · Carlos · celular`.

| Archivo y tramo | Qué se ve | Uso |
|---|---|---|
| `chofer-12a` 0:00 – 0:03 | Lista de la flota | Corto |
| `chofer-12a` 0:03 – 0:08,6 (exacto) | Campanita: "Tu vehículo vuelve a estar disponible… «Perdida de Aceite»" | Zoom al aviso |
| `chofer-12a` 0:08,6 – 0:16 | Búsqueda y pre-viaje abierto | Acelerar |
| `chofer-12b` 0:00 – 0:08 | Pre-viaje sin defectos (scroll) | Acelerado, sin voz encima |
| `chofer-12b` 0:09 – 0:12 | Anillo verde "18/18 — Sin defectos reportados" | Contrasta con el rojo de la escena 5 |
| `chofer-12b` 0:12 – 0:14 | "Inspección enviada… Buen viaje" | Corto |
| `chofer-12b` 0:14 – 0:24 | "Mi viaje" con "Reportar un problema" | Con la frase del reporte en viaje. **Zoom al botón rojo** (el cursor quedó cerca de "Cerrar viaje") |

## Escena 13 — todo lo demás: varios archivos

Computadora. Montaje rápido, en el orden de la voz:

| Orden | Archivo y tramo | Qué se ve | Frase de la voz |
|---|---|---|---|
| 1 | `admin-13` 0:02 – 0:12 | Planes de Mantenimiento | "…gestiona el mantenimiento preventivo" |
| 2 | `admin-13` 0:13 – 0:20,3 (exacto) | "Nuevo plan" con el selector por km o por tiempo | "Planes por kilómetros o por tiempo" |
| 3 | `admin-13` 0:46 – 0:55 | Ficha del Volvo: Resumen con el código QR | "Cada vehículo tiene su ficha…" y "…su propio QR" |
| 4 | `admin-13` 0:55 – 0:58 | Pestaña Historial | "…con su historial" |
| 5 | `admin-13` 1:00 – 1:02 | Pestaña Documentación con los vencimientos | "…la documentación y sus vencimientos" |
| 6 | `admin-13` 1:10 – 1:22 | Pestaña Neumáticos con la vista de arriba | "…el estado de los neumáticos" |
| 7 | `admin-13` 1:02 – 1:09 | Pestaña Combustible con el gráfico de consumo | "…detecta consumos de combustible fuera de lo normal" |
| 8 | `admin-6a8` 0:29 – 0:35 | Tarjeta "Disponibilidad de la flota" (fuera de servicio 2,2 días) | "…cuánto tiempo pasó cada vehículo fuera de servicio" |
| 9 | `admin-13` 1:25 – 1:34 | Gastos: total, dona por origen y barras por mes | "El administrador controla los gastos…" |
| 10 | `admin-comparar` 0:02,4 – 0:08,3 (exacto) | Comparar vehículos ordenado por costo por km, con "Para revisar" | "…compara el costo por kilómetro…" |
| 11 | `admin-pdf` 0:02,2 – 0:14,7 (exacto) | "Exportar historial" y la vista previa del PDF | "…exportar el historial completo en PDF" |

Qué **no** usar de `admin-13`:

- 0:24,5 – 0:29: listado de vehículos de un plan;
- 0:31 – 0:46 y 1:22 – 1:25: menú y listado de vehículos;
- 0:59: pestaña Checklist;
- 1:34,5 – 1:38,5: el cuadro "Cargar gasto" que se abre y se cierra;
- **1:47,2 – 1:52,0 (exacto): la burbuja de descarga de Chrome.** Lo más simple es no usar nada después de 1:40. La exportación a CSV no la nombra la voz.

Qué **no** usar de los clips:

- de `admin-comparar`, después de 0:08,3: ahí se ordena por disponibilidad y aparecen filas con "$ 0" y "Sin datos";
- de `admin-pdf`, después de 0:14,7: ahí se abre la ventana "Guardar como" de Windows. En la vista previa, el zoom va a la hoja, del lado izquierdo, para dejar afuera los controles oscuros de Chrome.

## Escena 14 — cierre

Sin tomas de pantalla: `cierre.png` (ver Gráficos).

## Lo que falta antes de editar

- **Música:** instrumental, sin voces y con graves, unos 12 a 15 dB por debajo de la voz.

## Notas para la edición

- **Resolución:** las tomas del celular tienen unos 375 píxeles de ancho. En 1920×1080 se ven bien en plano general y
  con zoom de hasta 2×. Más que eso se pone borroso. Las tomas de la computadora están a resolución completa y
  aguantan cualquier zoom.
- **Cuánto hay que recortar:** casi todas las tomas duran más que su voz. Por ejemplo, la de las escenas 2 a 5 dura
  1:49 útiles para 1:16 de voz, y la de la 13, 1:54 para 47 segundos. Lo que se recorta son esperas, scrolls y
  menús.
- **Lo que se dejó como está, decidido con Guido:**
  - el título "Perdida de Aceite", sin tilde y con mayúscula;
  - el "Hace 1 día" en el aviso del técnico;
  - el comentario del filtro de aire;
  - "dashboard" y "modal" en la voz;
  - el cierre del técnico sin kilómetros y con "mantenimiento".
- **Palabras clave en pantalla:** "Defecto bloqueante" (escena 4), "Vehículo bloqueado" (5), "Orden de trabajo
  asignada" (8) y "Defecto resuelto" (11).
