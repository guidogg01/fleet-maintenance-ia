# Video demo de FleetGuard — grabación y edición

Cómo se prepara, se graba y se edita el video de [`GUION.md`](GUION.md). El estado de avance va en `docs/STATE.md`,
como siempre, con `/cierre`. Qué toma y qué tramo va en cada escena está en [`MONTAJE.md`](MONTAJE.md).

## Orden de trabajo

1. **Guion cerrado.** La voz se lee en voz alta y se cronometra, y los tiempos se ajustan.
2. **Datos.** Se arma `seed-video.sql` con la tabla "Elenco y datos" del guion.
3. **Ensayo.** Se recorre la historia completa en la app, sin grabar, para encontrar lo que falla o se ve feo.
4. **Voz primero.** Guido graba la locución entera, escena por escena. Ella marca el ritmo.
5. **Imagen después.** Se graban las pantallas siguiendo la voz, cada escena con margen al principio y al final.
6. **Edición en CapCut.** Voz, imagen, carteles, etiquetas, zooms y música.
7. **Revisión.** Se exporta un corte y se revisa contra el guion (duración, balance de voz y música, legibilidad).
   Se repite hasta que quede.

## Preparación del día de grabación

- [ ] `develop` actualizado en los dos repos, y el backend reiniciado.
- [ ] Con el backend apagado, `seed-demo.sql` y después `seed-video.sql` (los dos en `../TIP - Backend/docs/db/`).
      Las fotos de demo copiadas a `uploads/photos`. El último `select` de `seed-video.sql` tiene que decir
      "listo para grabar".
- [ ] `demo-fuga-aceite.jpg` y `demo-ot-taller.jpg` copiadas a una carpeta a mano, para elegirlas desde el
      celular simulado.
- [ ] Chrome con un **perfil limpio**: sin extensiones visibles, sin barra de marcadores, sin otras pestañas.
- [ ] Pantalla a **1920×1080** y zoom de Chrome entre 110 y 125 % para el admin. Probar cuál se lee mejor en
      el video.
- [ ] Para el chofer y el técnico, el **modo dispositivo** de las DevTools (por ejemplo, iPhone 12 Pro). Se graba
      solo el recuadro del celular y en la edición se pone dentro del dibujo de un celular.
- [ ] Correr los seeds **el mismo día de la grabación, después de las 8:15**. A las 8:00, 8:05, 8:10 y 8:15 el
      backend revisa vencimientos, documentos, defectos sin atender y turnos, y manda avisos que ensucian las
      campanitas.
- [ ] En el Chrome que graba, **permitir las notificaciones** de `localhost:5173`. Si no, la campanita muestra un
      cartel de notificaciones bloqueadas.
- [ ] En "Planificar" (escena 8), dejar la fecha que propone (mañana a las 09:00) o elegir otra **en el futuro**.
      Con una hora que ya pasó, la app rechaza la fecha.
- [ ] Notificaciones de Windows en "No molestar". Que no aparezca ningún aviso del sistema en la toma.
- [ ] El aviso de contraseñas filtradas de Chrome no tiene que salir al loguearse (ver los Callejones de
      `STATE.md`).
- [ ] Las fotos del defecto y del cierre, a mano en una carpeta.
- [ ] El dictado probado en ese Chrome, con el micrófono que se va a usar.
- [ ] Una sesión abierta por rol, en pestañas separadas, para no grabar ningún login.

## Captura de pantalla

- **OBS Studio** (gratis) es lo más cómodo: graba una ventana o una región fija a 30 fps sin marca de agua. No está
  instalado todavía.
- **Alternativa sin instalar nada:** la Barra de juegos de Windows (Win + Alt + R) graba la ventana activa.
- Cursor visible y movimientos lentos: los zooms después necesitan tiempo para acompañar.
- Un archivo por escena, nombrado con el número de escena y la toma: `04-defecto-toma2.mp4`.

## Locución

- Un lugar sin eco, cerca del micrófono, con el mismo micrófono para todo.
- Una pista por escena, con 1 segundo de silencio antes y después.
- En CapCut: reducción de ruido sobre la voz, y la voz normalizada al mismo volumen en todas las escenas.

## Edición en CapCut

Pistas, de arriba hacia abajo:

1. **Etiquetas y palabras clave:** la del rol fija en una esquina, y las palabras clave de cada escena.
2. **Carteles:** el ciclo de los tres roles y el cartel de cada rol.
3. **Pantallas grabadas,** con los zooms hechos con fotogramas clave de escala y posición.
4. **Voz.**
5. **Música:** libre de derechos (alcanza con la biblioteca de CapCut), unos 10 dB por debajo de la voz.

**Estilo:**
- Los colores de la app: verde `#27804F`, petróleo `#15616D`, rojo `#C8373F` para lo bloqueante, y el fondo
  `#F3F4F0`.
- Las tipografías de la app: Space Grotesk para títulos e Inter para el texto.
- Zooms suaves de 0,4 a 0,6 s, con aceleración al entrar y al salir. Nunca más de un zoom a la vez.

### Ayuda de Claude con CapCut

- **No hay un conector (MCP) de CapCut.** Las herramientas de IA de CapCut (reducción de ruido, quitar fondo y
  demás) las usa Guido desde la app.
- **Computer use** (que Claude maneje la pantalla) no apareció en la sesión del 2026-11-16, aunque Guido lo activó
  durante esa sesión. Hay que probarlo al abrir una sesión nueva: tienen que aparecer herramientas `computer-use`.
  Remote Control es otra cosa: sirve para seguir la sesión desde otro dispositivo.
- **CapCut 9.4 guarda cada proyecto como JSON legible**, en
  `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\<proyecto>\draft_content.json`. Así que Claude puede:
  - leer un proyecto y revisar los tiempos, los zooms y las pistas contra el guion;
  - generar o corregir partes repetitivas, como los zooms de cada escena, las etiquetas o los cortes, escribiendo
    ese archivo.
- **Reglas para tocar un borrador:**
  - CapCut **cerrado** mientras Claude escribe. Si existe el archivo `.locked`, el proyecto está abierto;
  - una **copia** del proyecto antes de cada cambio;
  - probarlo primero en un proyecto chico de prueba, no en el del video.

## Qué tiene el video de referencia

Análisis del archivo de miTVU que pasó Guido (5:18, 1280×720), hecho el 2026-11-23. Se midieron el audio y la imagen
cuadro a cuadro.

**Estructura:**

| Tramo | Desde | Dura | Qué se ve |
|---|---|---|---|
| Logo | 0:00 | 16 s | Logo sobre fondo bordó (el color de su marca) |
| Cartel "1. ESTUDIANTES" | 0:17 | 15 s | Texto bordó sobre fondo blanco, animado |
| Estudiantes | 0:33 | 63 s | La app |
| Cartel "TUTORES" | 1:37 | 8 s | |
| Tutores | 1:45 | 107 s | La app |
| Cartel "ADMINISTRADORES" | 3:33 | 4 s | |
| Administradores | 3:37 | 80 s | La app |
| Logo y "MUCHAS GRACIAS" | 5:01 | 17 s | Fondo bordó |

- **Casi un minuto sin app:** logo, carteles y cierre suman unos 60 s. Nuestro guion usa unos 15 a 20 s, así que
  quedan casi 40 s más para mostrar la app.
- **Ritmo de imagen:** la pantalla cambia (un clic, un zoom, una pantalla nueva) cada 2,6 s en promedio. Nunca queda
  quieta mucho tiempo.
- **Dos tipos de toma que se alternan:**
  - la ventana completa del navegador, **con la barra de pestañas y la dirección visibles**. Nosotros vamos a
    recortarla: se ve más prolijo y la app se lee más grande;
  - acercamientos de 2× a una parte: un calendario, una tarjeta, barras de progreso, un cartel de confirmación.
- **Los carteles de cada rol** son texto simple en el color de la marca, sobre fondo claro. No hay subtítulos.

**Audio:**

- La música suena del primer al último segundo, sin cortes. Hay un solo hueco casi en silencio, de 1 segundo,
  cerca de 1:36, justo antes del cartel "TUTORES".
- **La música está cargada en los graves.** En total suena apenas 3 o 4 dB por debajo de la voz, pero en la banda
  donde está la voz queda unos 10 dB abajo. Por eso se escucha fuerte sin tapar lo que se dice. Para elegir la
  nuestra: instrumental, sin voces, con peso en los graves. En CapCut conviene arrancar con la música unos 12 a 15 dB
  por debajo de la voz y ajustar de oído.
- Las pausas largas de la voz (2 a 6 s) caen en los cambios de rol, alrededor de 1:19, 1:34 y 4:54.

## Revisión de cada corte

- **Duración:** entre 4:50 y 5:20.
- **Voz y música:** la voz unos 10 dB por encima de la música. Claude lo puede medir sobre el archivo exportado,
  igual que se midió el video de referencia.
- **Legibilidad:** que todo texto que importa se lea en un proyector. Ante la duda, zoom.
- **Que se entienda sin conocer la app:** que alguien que nunca la vio, como Tomás o un compañero, diga en una frase
  qué hace cada rol.

## Registro de tomas

| Fecha | Escena | Toma | Archivo | Sirve | Notas |
|---|---|---|---|---|---|
| | | | | | |
