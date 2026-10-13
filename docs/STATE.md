# Estado — FleetGuard

Última actualización: **2026-10-12**
Se escribe con el ritual de `docs/guias/sesiones.md`, siempre con confirmación
de Guido.

---

## Dónde estamos

El Sprint 5 cerró. Todas las cards de Guido de ese sprint están en `develop`: CAM-93, 84, 88, 92
y 90, que entraron con una release por repo (backend #20, frontend #28). Las de Tomás también:
CAM-52, 85, 86, 87, 89, 91 y 94 (#19, fe#27). Ahora está activo el **Sprint 7 - Entrega 2**
(hasta el 17/10). La base local tiene cargado el seed de demo de Tomás.

## En qué quedé

- **Nuevo flujo de ramas (2026-10-12):**
  - Las cards de Guido se trabajan en `feature/CAM-XX`, salen de una release por sprint y se
    mergean **directo, sin PR**, a esa release.
  - Al final del sprint va **un solo PR** de la release a `develop`.
  - La del Sprint 5 fue `release/guido-sprint-5`, en los dos repos; ya se mergeó y se borró.
- **CAM-93** (frontend): "Desactivar plan" se movió de la lista al modal de "Editar". El botón es
  neutro y se pone rojo al pasar el mouse. Si otro admin ya lo había desactivado
  (`PLAN_INACTIVE`), se trata como hecho.
- **CAM-84** (frontend): los botones "Dictar" y "Adjuntar foto" usan el color principal. Mientras
  escucha, el dictado dice "Detener". Aplica también a "Sacar foto" del técnico.
- **CAM-88** (frontend): el calendario agrupa y pide los turnos por día local
  (`utils/localDate.ts`), así lo programado desde las 21:00 ya no cae al día siguiente.
- **CAM-92** (frontend): filtro por fecha de creación en Órdenes de trabajo. Después se unificó
  con lo de Tomás:
  - OTs usa su `PeriodFilter`, con "Todas las fechas" y el texto "Creadas:".
  - `utils/period.ts` es la única fuente de los períodos.
  - Se corrigió "Últimos 3 meses" los días 29, 30 y 31, también en Gastos y Usuarios.
- **CAM-90** (backend): el km del vehículo avanza solo con las inspecciones, las OTs finalizadas
  y los mantenimientos hechos (`service/OdometerReadings`).
  - Tope de salto: `fleetguard.odometer.max-jump-km: 5000`.
  - Un vehículo dado de baja no cambia su km.
  - Contrato en `CAM-40-fleet-status-contract.md` y `openapi.yaml`.
- **CAM-85 se descartó sin pushear**, porque la hizo Tomás para CAM-87. Hay un respaldo en un
  parche local.
- **Seed de demo cargado** (`docs/db/seed-demo.sql`, de Tomás):
  - 10 camiones, 177 OTs y 46 defectos, con sus fotos copiadas a `uploads/photos`.
  - Usuarios: `admin`, 5 choferes y 2 técnicos (lista y contraseñas en el encabezado del
    archivo).
  - Ya no existe `chofer`, y se borraron los usuarios de prueba viejos.
- **Jira:**
  - Nueva épica **CAM-95 Notificaciones**, con CAM-96 a CAM-103; CAM-19 se movió ahí.
  - Gastos: **CAM-104 a CAM-109**.
  - **CAM-115**: avisar en la app cuando se ignora una lectura de km.
  - Se asignó épica a CAM-84, 91 y 94, y se completaron las descripciones de CAM-93 y CAM-84.
  - CAM-90 se pasó al Sprint 7 y queda en "Finalizada".
- Todo pasó por `revisor`, incluida una revisión final de cada PR completo.

## Qué sigue

- **Poner al día los repos locales:**
  - `git switch develop && git pull` en los dos repos de código.
  - Borrar las ramas locales: `release/guido-sprint-5`, `feature/CAM-84`, `feature/CAM-88`,
    `feature/CAM-90`, `feature/CAM-92`, `feature/CAM-92-periodo-unificado` y `feature/CAM-93`.
- **Levantar el backend de IntelliJ desde `develop`.** El seed ya está cargado.
- **Confirmar que el CI de `develop` del backend quedó en verde** después del merge de #20.
- **Sprint 7:**
  - Crear la release del sprint (definir el nombre; antes fue `release/guido-sprint-5`).
  - Las cards de Guido son CAM-65 (UI del calendario) y CAM-104 a 108 (Gastos).
- **Jira:**
  - Completar la descripción de CAM-92.
  - Dejar en CAM-88 un comentario con lo implementado.
- **Avisar a Tomás:**
  - El arreglo de "Últimos 3 meses" ya toca su `period.ts`.
  - `PeriodFilter` ahora acepta `allLabel` y `label`.
- **Cards para proponer** (salieron de las revisiones):
  - Cerrar la concurrencia del km (`@Version` en `Vehicle`).
  - El encabezado de Planes no entra en un celular.
  - El contraste del rojo del dictado (4,2 contra 4,5).
  - Siguen de antes: las fotos de `FinalizeWorkOrderModal` al cancelar, unificar
    `WORK_ORDER_FINALIZED` con `WORK_ORDER_CLOSED`, y el botón atrás con un modal sin guardar.
- **Siguen vigentes de antes:**
  - CAM-73, CAM-69/70 y CAM-76.
  - Probar con sesión de admin CAM-82 (navegación) y CAM-53.
  - Reactivar el aviso de contraseñas filtradas de Chrome.
  - Probar la cámara en un Android real.
  - El foco de los modales del admin.

## Decisiones abiertas

- **Resuelta: flujo de ramas y PRs.** Una release por sprint, sin PR por card, y un solo PR a
  `develop` que revisa Tomás.
- **Resueltas, de CAM-90 (con Guido):**
  - Tope de 5.000 km: un salto mayor se carga a mano, y los vehículos se dan de alta con su km
    real.
  - La OT se cierra cuando se repara, así que `completedKm` no puede ser menor al km del
    vehículo (CAM-74 sigue igual).
  - Un vehículo de baja no cambia su km.
- **Siguen de antes:**
  - Protección de rama en `develop` con CI obligatorio.
  - CI para el frontend.
  - Unicidad del username con acentos.
  - Resetear la contraseña no invalida los tokens ya emitidos.
  - CAM-33.
  - Épicas CAM-7 y CAM-9.
  - Paginación.
  - `workOrderId` de las completions cargadas a mano.
  - `bugfix/` contra `feature/`.
  - `STATE.md` cuando Tomás mergea sin ritual.
  - `ddl-auto`, versionado de schema, CAM-21 y CAM-66.

## Callejones sin salida

Lo que se probó y no funcionó, con el motivo. Se agrega, no se reemplaza.

- **2026-08-28** — Primero se armó todo para OpenCode (`opencode.json`,
  `.opencode/commands/`, `.opencode/agents/`) en la carpeta padre `TIP`. No servía:
  la herramienta que se usa es Claude Code, que lee `.claude/` y solo `CLAUDE.md`.
  El contenido (`AGENTS.md` y `docs/`) se reusó tal cual —era markdown plano a
  propósito— y solo hubo que rehacer la capa de punteros. Se puede borrar
  `TIP\opencode.json` y `TIP\.opencode\`.
- **2026-08-28** — El error de Rolldown en Windows ("Cannot find native
  binding") no se resolvió solo borrando `node_modules` + `package-lock.json`
  y reinstalando (la solución que sugiere el propio mensaje de error). La causa
  real era el bug npm/cli#4828 combinado con Node por debajo del `engines`
  mínimo (`v20.17.0` vs `^20.19.0` que piden Vite 8 / rolldown). Se resolvió
  instalando el binding a mano (`npm install @rolldown/binding-win32-x64-msvc
  --save-optional`) y actualizando Node a `20.20.2` vía
  `winget upgrade --id OpenJS.NodeJS.20`.
- **2026-08-28** — Un commit (`5f68501`) se hizo estando en HEAD desprendida
  tras un `git checkout origin/<rama>`, lo que lo dejó sin rama que lo sostenga
  (git avisa "leaving N commits behind" en este caso). Se recupera con
  `git branch <rama> <sha>` + checkout + push, sin pérdida de trabajo mientras
  no se corra `git gc` antes de rescatarlo. Confirmado con `git fetch` +
  comparación de SHAs que el push efectivamente llegó a GitHub.
- **2026-08-28** — El mismo problema de detached HEAD que ya estaba anotado
  para el backend (`git checkout origin/<rama>` en vez de la rama local) pasó
  también en el frontend. Se resolvió con
  `git switch -c feature/guido --track origin/feature/guido`, sin perder los
  cambios sin commitear que había en el working tree.
- **2026-08-29** — Un proceso backend levantado por Claude Code en una
  sesión anterior (vía `./gradlew run` en background) quedó ocupando el
  puerto 8080 después de terminar las pruebas, y rompió el "Run" desde
  IntelliJ con un error sin causa aparente (`BUILD FAILED in 644ms`, exit
  value 1, sin stacktrace visible). Se diagnostica con
  `netstat -ano | grep 8080` (compara el PID contra el que arranca
  IntelliJ) y se soluciona matando el proceso viejo. Vale la pena recordar
  cerrar los procesos de background al terminar una sesión de prueba.
- **2026-08-31** — Repetición del problema anterior, con una vuelta de
  rosca: parar la tarea en background de `./gradlew bootRun` (con la
  herramienta de tareas de Claude Code) no libera el puerto 8080, porque
  Gradle forkea la JVM de Spring Boot en un proceso hijo separado que
  sigue vivo. Hace falta matar ese PID específico
  (`netstat -ano | grep 8080` → `taskkill /PID <pid> /F`), no alcanza con
  parar la tarea que lo lanzó.
- **2026-09-01** — Después de matar por PID el proceso de Vite en `:5173`
  (parado explícitamente), volvió a aparecer un proceso nuevo escuchando en
  ese puerto sin que se ejecutara ningún comando que lo iniciara. Sospecha
  sin confirmar: la tarea de background quedó marcada "failed" tras el
  `taskkill` anterior y algo la reintentó. Se resolvió igual que siempre
  (`netstat -ano` → `taskkill /PID <pid> /F`). Si vuelve a pasar, vale la
  pena investigar si hay un auto-retry de tareas fallidas.
- **2026-09-03** — `psql` no estaba en el PATH de esta máquina pese a tener
  Postgres instalado; hubo que usar la ruta completa
  (`C:\Program Files\PostgreSQL\16\bin\psql.exe`). Además, correrlo con
  `PGPASSWORD=""` (vacío, en vez de la contraseña real) lo dejó colgado
  esperando un prompt de contraseña en una shell no interactiva — se
  resolvió matando la tarea y reintentando con la contraseña real de
  `application-local.yml`.
- **2026-09-03** — `gh` CLI no estaba instalado; se instaló con
  `winget install --id GitHub.cli`. Ni Bash ni PowerShell heredan el PATH
  actualizado dentro de la misma sesión — hubo que invocar `gh` por ruta
  completa (`C:\Program Files\GitHub CLI\gh.exe`) el resto de la sesión,
  hasta que se reinicien las terminales.
- **2026-09-03** — Al verificar a mano un fix de seguridad en `AuthService`
  (cerrar un canal de timing), medir con `curl` contra un backend "recién
  reiniciado" dio una diferencia de 81ms vs 4ms — como si el fix no
  funcionara. Resultó que el proceso JVM contra el que se medía había
  quedado corriendo con el código viejo pese a parecer recién iniciado. Se
  resolvió instrumentando con logs de timing directos en el código y
  reiniciando el proceso de cero — ahí sí confirmó que el fix andaba
  (~77-80ms en los dos casos). Ante una medición que no cierra, conviene
  matar y reiniciar el proceso antes de asumir que el código tiene un bug.
- **2026-09-05** — El subagente `revisor` y los comandos `/retomar`/`/cierre`
  dejan de estar disponibles apenas la sesión queda parada en una rama/
  checkout sin `.claude/` — pasó dos veces en la misma sesión, justo después
  de migrar `.claude/` a `fleet-maintenance-ia`. No es un bug: hay que abrir
  la sesión siguiente parada en `TIP - IA` para que vuelvan a cargar.
- **2026-09-05** — Editar la descripción de un ticket de Jira vía
  `editJiraIssue` (contentFormat markdown) reescribe internamente la
  referencia a una imagen embebida (de "archivo" a una envoltura "externa"
  con la misma URL adentro) — no se pudo confirmar si el mock se sigue
  viendo bien porque el navegador de la sesión no tiene login de Jira.
  Revisar a mano antes de asumir que se rompió o que quedó bien.
- **2026-09-11** — `STATE.md` quedó 6 días desactualizado porque Tomás
  mergeó CAM-49 (2026-09-06) y CAM-42/50/51 (2026-09-11) sin pasar por el
  ritual de este repo (es solo de Guido). `/retomar` lo detectó comparando
  el git log inyectado contra el Historial, pero hizo falta reconstruir a
  mano con `gh pr list --state all` (en los dos repos) y una consulta JQL a
  Jira (`project = CAM order by updated DESC`) para saber qué se había
  hecho realmente. Si vuelve a pasar, ese es el procedimiento — no asumir
  que "no pasó nada" solo porque no lo hizo Guido.
- **2026-09-11** — `ddl-auto: update` no retroactiva constraints en bases
  ya creadas. Pasó dos veces: agregar `Vehicle.active` como `NOT NULL` sin
  `columnDefinition` con default rompió el `ALTER` en silencio (Hibernate
  seguía de largo, la columna nunca se creaba) — se resolvió agregando el
  default a nivel columna, mismo patrón que ya usaba `odometerKm`. Sacarle
  `NOT NULL` a `MaintenancePlan.category` en el código tampoco lo sacó de
  una base ya existente — hizo falta `ALTER TABLE ... DROP NOT NULL` a
  mano. Ante un cambio de nullability en una entidad, revisar si la base
  local ya tiene la columna creada con la constraint vieja.
- **2026-09-11** — Un `useEffect` que solo pone `mountedRef.current = false`
  en el cleanup (sin `= true` en el setup) queda permanentemente en
  `false` después del doble mount/unmount que hace React 18 `StrictMode`
  en desarrollo — un timer que chequeaba ese ref antes de actualizar
  estado nunca volvía a dispararse. Mismo patrón que ya se usaba bien en
  otros componentes de la sesión, acá se pasó por alto. Fix: setear
  `true` también en el setup del efecto.
- **2026-09-11** — `lastDoneKm`/`lastDoneDate` de una asignación de
  mantenimiento no son señal confiable de "el mantenimiento se hizo": el
  backend los siembra con el estado del vehículo al momento de *asignar*
  el plan, no solo cuando se registra un completion real. Para saber si
  un plan realmente se hizo alguna vez hace falta consultar
  `GET .../completions` y ver si hay al menos un registro.
- **2026-09-16** — Cancelar una programación de prueba haciendo click en el
  botón de basura del calendario, en el navegador de la sesión, dispara un
  `window.confirm()` nativo que no se pudo confirmar visualmente (el click
  no tuvo efecto observable). Se resolvió cancelando directo por API
  (`PATCH /api/maintenance-schedule/{id}` con `status: cancelled`). Si hace
  falta limpiar datos de prueba generados vía UI y hay un `confirm()` de
  por medio, ir directo por API es más confiable que interactuar con el
  diálogo nativo.
- **2026-09-16** — La sesión del 2026-09-05 registró en su Historial
  "memoria actualizada" sobre no poner atribución de Claude en commits/PRs,
  pero el archivo de memoria correspondiente nunca se creó — el pedido se
  repitió esta sesión (rechazando un intento de commit) sin que hubiera
  quedado guardado la primera vez. Ante una afirmación de "ya quedó
  guardado en memoria" en una sesión anterior, vale la pena confirmar que
  el archivo realmente existe antes de asumirlo.
- **2026-09-16** — Tickets de Jira con título de broma ("Sarasa 1"/"Sarasa
  2", CAM-65/66) no son basura ni error de carga: son placeholders
  pre-estimados a propósito, para poder sumar trabajo no planeado durante
  el sprint sin alterar la velocity (Story Points ya comprometidos). Antes
  de asumir que un ticket así es descartable, confirmar si ya fue
  repurposeado (título/descripción reales) o sigue de comodín.
- **2026-09-16** — El `CHECK` constraint que Hibernate genera para un campo
  `@Enumerated(EnumType.STRING)` tampoco se actualiza solo con
  `ddl-auto: update` en una base local ya creada — mismo problema ya
  documentado para `Vehicle.active`/`MaintenancePlan.category`, pero esta
  vez en `users.role` (`users_role_check`), al agregar el valor `TECNICO`
  al enum. Se resuelve igual: `ALTER TABLE users DROP CONSTRAINT
  users_role_check` + recrearlo con el valor nuevo, a mano, antes de poder
  insertar un usuario con el rol agregado.
- **2026-09-20** — Una rama creada con `git checkout -b <rama> origin/develop`
  queda trackeando `origin/develop`. Hay que pushear con
  `git push -u origin <rama>` para que apunte a su propia rama remota.
- **2026-09-20** — Los puertos 8080 y 5173 ya estaban ocupados por procesos de
  Guido (backend de IntelliJ con código viejo y su Vite), así que el backend con
  los endpoints nuevos no estaba disponible ahí. Para probar sin pisarlos se
  levantó un backend propio con
  `./gradlew bootRun --args='--server.port=8081 --fleetguard.cors.allowed-origins=http://localhost:5174'`
  y un Vite con `VITE_API_BASE_URL=http://localhost:8081 npx vite --port 5174`.
  Al terminar se matan solo esos PIDs, no los de Guido.
- **2026-09-20** — El navegador integrado de la sesión es aparte del de Guido: un
  login hecho en su Chrome no se comparte con él, y Claude no ingresa
  contraseñas en formularios de login aunque se las pasen. La verificación
  visual la tiene que hacer Guido en su navegador, o loguearse él en el panel de
  la sesión.
- **2026-09-20** — Un script de Bash con varios `cat > archivo <<'EOF'` (código
  Java con comillas y acentos) falló entero con `unexpected EOF` y no escribió
  nada. Para archivos de código conviene la herramienta Write, o Read + Edit en
  los existentes. Además, los archivos del frontend son CRLF: al agregar CSS con
  Bash, convertir con `sed 's/$/\r/'`.
- **2026-09-20** — Se propuso crear una US nueva de "órdenes de trabajo desde el
  detalle del vehículo" sin buscar antes en Jira; resultó que **CAM-14** (Tomás,
  En curso) ya cubre el núcleo. Antes de proponer una US nueva, revisar el
  backlog por solapamientos.
- **2026-09-22** — Un `git merge` 100% local (sin push) hacia la rama
  `feature-combined` fue bloqueado por el clasificador de permisos de Auto
  Mode como "modificar recursos compartidos", solo por el nombre de la rama
  de destino. Hace falta confirmación explícita del usuario en el chat antes
  de cada merge de este tipo, aunque no toque el remoto.
- **2026-09-22** — El `localStorage` del panel de preview embebido del Code
  tab se limpió solo varias veces durante la sesión (no coincide siempre con
  un restart de servidor de por medio), obligando a re-loguearse repetidas
  veces. No se encontró la causa; parece un comportamiento del panel entre
  turnos, no algo que dependa de lo que se estaba haciendo.
- **2026-09-22** — Después de un merge de git con archivos a medio resolver,
  el HMR de Vite deja errores 500/404 "stale" en `read_console_messages` que
  no reflejan el estado real una vez terminado el merge — hay que confirmar
  con `read_network_requests` (la respuesta más reciente) en vez de confiar
  en el buffer de consola, que no se limpia solo ni con un `navigate` nuevo.
- **2026-09-22** — Dos PRs independientes (CAM-22 y CAM-14/CAM-15) agregaron,
  sin coordinarse, el mismo query de repositorio (`DefectRepository`,
  defectos por vehículo) con nombres distintos, y dos formas distintas de
  mostrar el historial de un vehículo en la misma pantalla
  (`VehiclesSection.tsx`). Pasó por construirse en paralelo sobre `develop`
  sin que ninguna de las dos ramas viera el trabajo de la otra. Vale la pena,
  antes de arrancar una card que toca una pantalla que otra card también
  toca, revisar si hay algo a medio mergear en `feature-combined` que la
  pise.
- **2026-09-24** — El cartel "Cambia tu contraseña" al loguearse es la detección
  de contraseñas filtradas del Gestor de contraseñas de Chrome, no de FleetGuard.
  No hay forma legítima de apagarlo desde el código (los trucos de disfrazar el
  campo de contraseña rompen gestores y accesibilidad). Se apaga en
  `chrome://settings/security`, pero el interruptor **solo aparece con
  "Protección estándar"**; con "Protección mejorada" está siempre activo y oculto.
  Alternativa sin tocar Chrome: contraseñas de prueba que no estén filtradas.
- **2026-09-24** — `.claude/launch.json` con `cmd /c "cd /d ... && ..."` y comillas
  anidadas falló ("sintaxis de la etiqueta del volumen no son correctos"), y un
  `sed` sobre rutas de Windows se comió las barras invertidas. Lo que anduvo:
  scripts `.cmd` aparte (con `set VAR=` y `call`) y `runtimeExecutable` apuntando
  a ellos.
- **2026-09-24** — Un heredoc de Bash con Python adentro (con `'\n'` en strings) se
  cortó a la mitad ("unexpected EOF"), mismo problema que el 2026-09-20 con Java.
  Escribir el script a un archivo de la carpeta temporal y correrlo.
- **2026-09-24** — Repetición del callejón del 2026-09-20: Guido se logueó en su
  Chrome/`5173` y el panel del navegador de la sesión (`5174`) seguía sin sesión;
  además el panel puede estar **oculto** en la app sin que se note (`tabs_select`
  lo trae al frente). Claude tampoco usa la contraseña de Postgres para correr
  `psql`: el seed lo corrió Guido desde pgAdmin.
- **2026-09-25** — Al verificar los PRs, `feature/CAM-22` (frontend) parecía tener
  3 commits que no estaban en `feature-combined`. Falso positivo: el PR #15 se
  mergeó a `develop` con **squash**, así que los commits originales quedan
  "sueltos" aunque su contenido ya está. Ante una rama que parece incompleta,
  mirar si su PR se mergeó con squash antes de asumir que falta algo.
- **2026-09-24** — Los defectos de prueba cargados el 2026-09-22 en CB299ZA tienen
  `photoUrl` relativo a un archivo que no existe (`/uploads/photos/seed-placeholder-1.jpg`);
  en la vista del técnico se ve "No se pudo cargar la foto del defecto". No es un
  bug: los defectos reales guardan URL absoluta.
- **2026-09-26** — El flujo de Jira del proyecto **no permite pasar una card de
  "Tareas por hacer" a "Finalizada" en un solo paso**: hay que recorrer las
  transiciones en orden, `2` (En refinamiento) → `3` (En curso) → `4` (Pendiente a
  Integrar) → `5` (Finalizada), con un `transitionJiraIssue` por paso. Datos útiles
  para editar Jira por API: los Story Points están en `customfield_10016`, y la
  épica se asigna con `parent: {key}` (al crear, dentro de `additional_fields`;
  al editar, en `fields`).
- **2026-09-26** — No se reescribió por API la descripción de una card con imagen
  embebida (CAM-65), para no repetir el problema del 2026-09-05 (la referencia a la
  imagen se reescribe y no se puede confirmar si sigue viéndose). El refinamiento
  se dejó como comentario y Guido lo pasó a mano a la descripción desde Jira,
  conservando la captura.
- **2026-10-03** — El paquete raíz `org` a secas rompe Spring. `@SpringBootApplication`
  escanea el paquete de la clase de arranque y todos sus subpaquetes, así que
  barría `org.springframework.*` y el contexto no levantaba
  (`ConflictingBeanDefinitionException` con `ProblemDetailsExceptionHandler`). Se
  resolvió con un paquete propio, `org.fleetguard`.
- **2026-10-03** — Repetición del callejón del 2026-09-03. El backend levantado desde
  IntelliJ seguía con el código anterior al cambio de usernames (arrancó 01:49, el
  cambio fue 01:54) y mostraba el mensaje de error viejo. Ante un comportamiento
  que no coincide con el código, revisar a qué hora arrancó el proceso y
  reiniciarlo.
- **2026-10-03** — El lanzador de servidores del Code tab no soporta rutas con
  espacios ("TIP - Backend"). Para el backend sirvió la ruta corta de Windows
  (`TIP-BA~1\gradlew.bat -p TIP-BA~1 bootRun`). Para el frontend la ruta corta no
  sirve, porque Vite la rechaza como fuera de su allow list; anduvo un `.cmd` en
  una carpeta sin espacios que hace `cd /d` a la ruta larga y `npm run dev`.
- **2026-10-03** — `curl` desde Bash en Windows manda la "ñ" en Latin-1 y Jackson
  rechaza el JSON (parecía un 500 del backend). Para probar con acentos, escribir
  el JSON a un archivo con Node y mandarlo con `--data-binary @archivo`.
- **2026-10-03** — `gradlew` estaba commiteado sin permiso de ejecución (100644). En
  el runner Linux de GitHub hubiera fallado con "permission denied". Se corrigió
  con `git update-index --chmod=+x gradlew`.
- **2026-10-03** — En Mockito, re-stubbear con `when(mock.metodo())` un mock que ya
  tira una excepción la dispara durante el propio stubbing; hay que usar
  `doThrow(...).when(mock)`. Y armar un stub adentro del `thenReturn(...)` de otro
  (stubbing anidado) también falla: hay que sacarlo a una variable antes.
- **2026-10-03** — #17 y fe#23 se mergearon antes de que se pushearan a sus ramas las
  correcciones de `revisor`. Los commits quedaron en las ramas, fuera de `develop`, y hubo
  que abrir PRs nuevos (#18, fe#26). Después de mergear un PR, cualquier push a esa rama no
  entra solo. Para confirmar si un commit llegó:
  `git merge-base --is-ancestor <sha> origin/develop`.
- **2026-10-03** — Con un campo `Long`, Jackson convierte `1500.7` en `1500` sin avisar,
  porque `ACCEPT_FLOAT_AS_INT` viene activado. Para rechazar decimales hay que recibir
  `BigDecimal`. Y con `BigDecimal`, no usar `remainder(BigDecimal.ONE)` para detectar
  decimales: con `1e100000`, 8 caracteres que Jackson acepta, traba el hilo unos 7
  segundos. Usar `stripTrailingZeros().scale() > 0` y `longValueExact()`.
- **2026-10-03** — En un `.cmd` del lanzador, `cd /d` a la carpeta del backend no tuvo
  efecto ("gradlew.bat no se reconoce"), ni con CRLF ni con la ruta corta. Anduvo
  `call <ruta corta>\gradlew.bat -p <ruta corta> bootRun`. Para el frontend sí anduvo
  `cd /d "<ruta larga>"` + `npx vite`. Además, la herramienta Write deja los `.cmd` en LF,
  así que hay que pasarlos a CRLF.
- **2026-10-03** — Cambiar de rama en `TIP - Frontend` cambia lo que sirve el Vite de
  Guido, porque corre desde la misma carpeta. Para probar sin pisarle nada, se usó una
  copia aparte en 8081/5174.
- **2026-10-07** — `git log --since` sobre la rama local no mostró los commits de Tomás, porque
  el `develop` local estaba atrás. Para ver qué pasó entre sesiones hay que hacer `git fetch` y
  mirar `origin/develop`.
- **2026-10-08** — Se arrancó CAM-85 sin mirar las ramas de Tomás, y él la estaba haciendo para
  CAM-87. Antes de empezar una card de la que otra depende, revisar
  `git for-each-ref refs/remotes/origin` por ramas que la mencionen.
- **2026-10-12** — Al cerrar el Sprint 5, Jira marcó CAM-90 como Finalizada sin estar hecha. Para
  traer al sprint activo una card de un sprint cerrado: `editJiraIssue` con `customfield_10020` =
  id del sprint (el 7 es `40`). Mantiene el estado y la card queda en los dos sprints.
- **2026-10-12** — `cmd //c mklink /J` desde Git Bash con rutas con espacios dejó un enlace roto.
  Para enlazar `node_modules` en un worktree aparte anduvo PowerShell:
  `New-Item -ItemType Junction`. Para borrarlo sin tocar el `node_modules` real:
  `(Get-Item <link>).Delete()`.
- **2026-10-12** — `seed-demo.sql` **borra todos los datos operativos y todos los usuarios salvo
  `admin`**. Hay que correrlo con el backend apagado y copiar `docs/db/demo-photos/*` a
  `uploads/photos`. Sus fotos apuntan a `localhost:8080`, así que para verlas el backend tiene que
  estar en ese puerto.

## Historial

Una línea por sesión.

- **2026-08-23** — Backend inicial: Gradle + `HttpServer` en `:8080`,
  `DatabaseConnection` contra Postgres `TIP`, `GET /api/health`, README.
- **2026-08-25** — Frontend inicial: scaffold de Vite + React 19 + TS, Oxlint,
  `App.tsx` con chequeo de conexión, README.
- **2026-08-28** — Infraestructura de contexto para IA: `AGENTS.md` por repo,
  `docs/` (PROJECT, STATE, ROADMAP, API, SETUP, guías) y configuración de Claude
  Code versionada en `.claude/`. Se detectó la desalineación `/api/ping` vs
  `/api/health`.
- **2026-08-28** — Corregido `/api/ping` → `/api/health` en `App.tsx` (Hito 0
  #1, sin commitear). Resuelto bug de entorno del frontend en Windows (Node
  desactualizado + npm/cli#4828 con Rolldown). Recuperado y pusheado a
  `origin/feature/guido` el commit de la capa de contexto que había quedado en
  HEAD desprendida — confirmado en GitHub con `git fetch`.
- **2026-08-28** — Cerrado Hito 0 completo (toolchain Java,
  `db.properties.example`, remote sin token — con el hallazgo de que el PAT
  era de Tomás, no de Guido). Completada la card CAM-13 en Jira. Implementado
  `GET /api/defectos` con refactor a arquitectura en capas a pedido explícito
  de Guido. Probado a mano (datos, vacío, caracteres especiales, DB caída) y
  revisado por el subagente `revisor` en dos pasadas. Agregado el request a
  la colección de Postman. Commiteado y pusheado en los dos repos a
  `origin/feature/guido` (backend `617aa8b`, frontend `0eff382`).
- **2026-08-29** — Cerrada CAM-13 de punta a punta: frontend consume
  `GET /api/defectos` con los tres estados, primer paso del sistema de
  diseño "Cuidado preventivo" (paleta + tipografía) aplicado vía variables
  CSS. Encontrado y arreglado un bug de CORS preexistente en el backend que
  bloqueaba todo fetch del frontend. Revisado por el subagente `revisor` sin
  hallazgos bloqueantes. Commiteado y pusheado en los dos repos a
  `origin/feature/guido` (backend `41c2656`, frontend `71cb44c`).
- **2026-08-31** — Confirmado (leyendo el PR de GitHub) que Tomás había
  migrado su parte a Spring Boot con arquitectura en capas (CAM-11) y ya
  mergeó ese trabajo a `develop` en los dos repos. Guido confirmó adoptar
  ese stack como el del equipo, se mergeó `develop` → `feature/guido` en
  backend y frontend (se descartó la arquitectura vieja y el contrato de
  `/api/defectos`, se adoptó `GET /api/defects` de Tomás), y se actualizó
  toda la documentación para reflejar el cambio de stack. Se construyó la
  pantalla de listado de defectos que quedaba pendiente (`DefectsList.tsx`),
  verificada de punta a punta con datos reales. Guido compartió un mock de
  la vista de administrador (dashboard de escritorio, distinta del flujo
  mobile del chofer) como norte de largo plazo — commiteado en
  `docs/design/admin-dashboard-mock.png` y anotado en `ROADMAP.md`. Guido
  probó el backend por su cuenta, corriendo `./gradlew bootRun` con éxito.
  Revisado el backlog de Jira: confirmado que varias historias del
  dashboard admin están fragmentadas y sin refinar (`CAM-37/38/39/40/44`) y
  que Login (`CAM-43`) no tiene descripción — acordado como punto de
  partida de la próxima sesión, junto con una revisión de cobertura de
  tests del backend. Commits en local en los dos repos (backend
  `d7e9dd0`/`4996fd0`/`c13f320`, frontend `d7fa2ee`/`638d31f`) — **sigue
  faltando pushear y abrir el PR a `develop`**.
- **2026-09-03** — Confirmado el commit de estado 2026-09-01 a
  `feature/guido`. Refinado el backlog de Jira para Login: CAM-43 pasó a
  ser "Login — backend" (modelo mínimo de Usuario+Rol, sin invitaciones) y
  CAM-45 "Login — pantalla y sesión en frontend" se creó como card nueva,
  las dos bajo el épico CAM-10; CAM-23 anotada como dependiente sin tocar
  su alcance; JWT elegido como mecanismo de sesión. Implementado y
  verificado de punta a punta el login de backend (JWT+BCrypt, con un canal
  de timing de enumeración de usuarios encontrado y corregido por el
  subagente `revisor`) y de frontend (pantalla de login, sesión en
  `localStorage`, redirect por rol, logout), cada uno probado a mano contra
  el backend/frontend reales y pasado por `revisor`. Resuelto el problema
  de organización de git que señaló Guido: se pusheó `feature/guido` tal
  cual (limpio, solo docs/infraestructura, confirmado con el diff real) y
  se adoptó la convención de una rama por card de Jira, nombrada solo con
  el ID, para todo trabajo nuevo. Se instaló y autenticó GitHub CLI. Se
  abrieron 4 PRs a `develop` (2 por repo) — pendientes de merge, sugerido
  mergear primero los de `feature/guido`.
- **2026-09-05** — Centralizada toda la documentación/contexto de IA en el
  repo nuevo `fleet-maintenance-ia`, reconciliado con una limpieza
  equivalente que Tomás hizo por su cuenta en CAM-43 (`API.md` →
  `openapi.yaml`, que se queda en el backend). Revisado `ROADMAP.md` +
  backlog de Jira, encontrado que CAM-16/17/18/20/46/47/48 ya están hechas
  pese a que Jira dice lo contrario. Implementada, verificada a mano y
  pusheada CAM-37 (widget de defectos recientes en panel admin) en los dos
  repos, con PRs abiertos a `develop`. Actualizada la card de Jira de
  CAM-37 con historia de usuario y criterios de aceptación. Guido pidió no
  volver a poner atribución de Claude en commits/PRs — memoria actualizada.
- **2026-09-05** (continuación, sin `/cierre`) — Guido construyó y mergeó
  CAM-20 (dashboard de admin: KPIs, tabla de estado de flota, próximos
  vencimientos, layout de 2 columnas) en el frontend.
- **2026-09-06** — Tomás implementó y mergeó CAM-49 (ajustes de UI: vista
  de chofer sin pestaña de defectos, vehículos con defecto bloqueante en
  estado "No disponible", vista de admin con menú hamburguesa y pestañas
  Resumen/Vehículos/Planes de Mantenimiento) en el frontend.
- **2026-09-11** — Tomás implementó y mergeó CAM-42/CAM-50/CAM-51
  (calendario de mantenimientos: entidad `ScheduledMaintenance` +
  endpoints en el backend, `WeeklyScheduleCard`/`MonthScheduleModal`/
  `SchedulePickerModal`/`VehicleMaintenanceModal` en el frontend — programar
  por asignación, por defecto o manual; ver detalle desde "Estado de la
  flota"; planificar desde "Defectos abiertos recientes") en los dos repos.
- **2026-09-11** — Sesión de reconciliación: detectado el desfasaje de 6
  días entre `STATE.md` y git/Jira. Reconstruido cruzando `git log`/
  `gh pr list` de los dos repos de código contra Jira (JQL
  `project = CAM order by updated DESC`), sin tocar código. Confirmado que
  CAM-16/17/18 siguen desalineadas en Jira (código ya hecho, Jira dice "por
  hacer") — sin cambios respecto a lo ya sabido. La imagen embebida en la
  descripción de CAM-37 en Jira sigue con la referencia rara (`blob:`/
  "externa") detectada el 2026-09-05 — tampoco se pudo confirmar
  visualmente esta vez (sin login de Jira en el navegador de la sesión).
- **2026-09-11** — CAM-25 (ABM de vehículos: alta/edición/baja
  lógica/reactivar, patente única, bloqueo por viaje abierto) y CAM-16
  completa (asignar/desasignar planes, marcar como hecho con recálculo,
  catálogo de planes editable, migrada de "Vehículos" a "Planes de
  Mantenimiento") + CAM-18 (cargar kilometraje). Todo verificado a mano
  con `curl` y en el navegador contra el backend real. Encontrado y
  arreglado en el camino: bug de `MaintenancePlan.category` (`NOT NULL`
  en la entidad, opcional en el contrato). Dos PRs abiertos a `develop`
  (backend #9, frontend #11, con comentarios cruzados aclarando el
  reparto de las cards), Jira de las dos cards actualizada con criterios
  de aceptación. Guido avisó a Tomás. Test suite del backend confirmado
  que sigue roto (mismo bug de CAM-42 reportado antes), dejando
  `VehicleServiceTest` (nuevo) sin correr.
- **2026-09-16** — Reconciliación con git/Jira: confirmados mergeados los
  PRs #9/#11 de CAM-25/CAM-16 a `develop`, y que el fix de Tomás arregló el
  test suite del backend (`./gradlew build` OK, incluido
  `VehicleServiceTest`). Investigado CAM-57 (reportado por Tomás) sin
  encontrar causa de crash real; Guido no pudo reproducirlo y se lo
  reasignó. De ahí salió el diagnóstico de CAM-61 (calendario semanal sin
  refrescar al planificar desde "Estado de la flota"), implementado,
  verificado a mano en el navegador contra el backend real, y subido en
  `bugfix/CAM-61` (PR #12) — nueva convención de ramas por tipo de issue
  (`bugfix/`/`feature/`) confirmada con Guido. Jira de CAM-61 actualizada
  con causa/fix/PR. Corregido que la regla de "sin atribución de Claude"
  del 09-05 no había quedado guardada en memoria de verdad, y que revisar
  los PRs de Guido es tarea de Tomás por default, no de Guido.
- **2026-09-16** (continuación) — Encontrado al contrastar `/retomar` contra
  git que Tomás había subido `docs/POC-documentacion.md` directo a
  `develop` sin pasar por PR (revisado, sin impacto de código). Arrancada la
  épica CAM-59 (vista de taller/técnico): refinada en Jira en 4 historias
  (CAM-67/68/69/70) tras explorar el código con 3 subagentes en paralelo
  (auth/roles, routing del frontend, modelo de datos) en plan mode.
  Confirmado con Guido el alcance del MVP (todo visible, sin auth
  enforcement nuevo, shell propio) y que el rol "Mantenimiento" de CAM-23 es
  el mismo que "Técnico". Hecho un swap de sprint para meter CAM-67/CAM-68
  sin alterar la velocity (afuera CAM-65/CAM-66, 3 SP cada una). Implementada
  y verificada a mano CAM-67 (rol Técnico) en los dos repos, con PRs
  abiertos a `develop` (backend #10, frontend #13) y Jira actualizada.
  Encontrado y corregido el mismo problema de `ddl-auto`/constraints ya
  conocido, esta vez en `users.role`.
- **2026-09-16** (continuación 2) — Confirmado con Guido el layout de
  CAM-68 (mobile-first, simple, como Chofer). Explorado el código de
  Chofer y propuesto un plan; implementada y verificada a mano CAM-68
  (shell de Técnico) en el frontend, revisada por el subagente `revisor`
  sin hallazgos bloqueantes. Descubierto que la rama activa era
  `feature/CAM-67` (todavía sin mergear) y decidido con Guido encadenar
  `feature/CAM-68` sobre ella en vez de esperar. Commiteado, pusheado y
  abierto PR #14 a `develop` con la dependencia documentada, pasado a
  Draft como traba técnica adicional, y Jira de CAM-68 actualizada con el
  mismo detalle. Guido avisó a Tomás el orden de integración (CAM-67 →
  CAM-68 → resto de CAM-59). Revisados sin hallazgos graves los dos
  commits directos de Tomás del 2026-09-13 en frontend encontrados al
  retomar.
- **2026-09-20** — Elegida CAM-22 entre las cards de Guido en "Tareas por hacer"
  del sprint (la otra es CAM-60, bloqueada por CAM-14). Explorado el código con
  dos subagentes en paralelo y planificado en plan mode. Implementados y
  verificados el detalle y el historial de vehículo (backend `GET /vehicles/{id}`
  y `/history`, frontend `VehicleDetail` con fila clickeable), revisados por el
  `revisor` y subidos en `feature/CAM-22` con PRs #11 (backend) y #15
  (frontend). Postman con 9 requests nuevos en Vehicles y Jira CAM-22 reescrita
  y comentada. Confirmado que CAM-14 (Tomás) ya cubre el dominio de órdenes de
  trabajo, por lo que no se creó una US nueva.
- **2026-09-22/23** — Verificada `feature-combined` de punta a punta con el
  subagente `revisor` en los dos repos (backend PR #12, frontend PR #19) —
  sin hallazgos bloqueantes, un contrato desactualizado (`openapi.yaml` sin
  rol `TECNICO`). Revisados los PRs de Tomás de CAM-14/62/63 (backend #13,
  frontend #18, órdenes de trabajo) y explicado su funcionamiento y valor.
  Detectado un choque de diseño entre el historial de vehículo de CAM-22 y
  el de la CAM-15 de Tomás; resuelto unificando todo en `VehicleDetail.tsx`
  (OTs pedidas aparte de `/history`). Mergeadas las ramas de CAM-14/62/63 a
  `feature-combined` local en los dos repos (sin pushear), resolviendo un
  conflicto real de repositorio duplicado en el backend y de imports/CSS en
  el frontend. Sumada una cuarta tarjeta de órdenes de trabajo a
  `VehicleDetail.tsx`, con layout en dos columnas, listas colapsables, orden
  por prioridad e indicadores en el título — iterado varias veces a partir
  de screenshots reales de Guido navegando la app. Cargados 7 defectos de
  prueba (3 bloqueantes) en el vehículo CB299ZA vía la API real para validar
  todo. Nada pusheado ni mergeado a `develop`; próxima card definida:
  CAM-60 (vínculo técnico↔OT).
- **2026-09-24/25** — CAM-60 completa sobre `feature-combined`: vínculo
  técnico↔OT, `GET /api/users`, vista mobile "Mis órdenes" del técnico con cierre
  de OT y contexto del defecto, una sola OT abierta por origen (se encontró y
  canceló un duplicado real) y "Replanificar" en Defectos. Además, mejoras de UI
  (visor de fotos CAM-53, acciones de vehículo al detalle, "Volver"/menú, ojito
  del login, mensaje de formato de foto). `openapi.yaml` con `/work-orders`
  documentado completo. Todo pasó por `revisor` (5 rondas), se pusheó, y Guido
  mergeó `feature-combined` a `develop` en los dos repos (#12, #19). Card CAM-60
  completada en Jira.
- **2026-09-26/28** — Sesión de backlog, sin código. Cruzadas las 61 cards de Jira
  contra el código de `develop`: CAM-17/38/39/54 pasadas a Finalizada (hechas o
  repetidas), CAM-52/53/69/70 reescritas, decidido que el técnico solo ve lo que
  tiene asignado. Creadas las épicas CAM-71 (Gestión de Flota) y CAM-72
  (Infraestructura), reubicadas ~15 cards de épica, creadas CAM-73 a CAM-77 y
  completadas las descripciones de 12 cards vacías o incompletas. Guido y Tomás
  priorizaron el sprint 5 por Pareto (CAM-23 → CAM-53); decidido que CAM-23 protege
  solo `/api/users` y CAM-73 extiende el filtro después.
- **2026-10-03** — Revisados y mergeados los PRs de Tomás de CAM-31/32/77/79/80/81
  (#15, fe#21). En `feature/CAM-23-CAM-30-CAM-78`: CAM-23 (usuarios y roles,
  `/api/users` con JWT, usernames con espacios y acentos), el paquete raíz
  `org.fleetguard`, CAM-78 (263 tests, 92,5% de líneas, 6 bugs corregidos, 11 tests
  de relleno descartados) y CAM-30 (GitHub Actions y JaCoCo con piso de 85%). Todo
  pasó por `revisor` (5 rondas). PRs #16 (CI verde) y fe#22 abiertos a `develop`.
  Página con la selección de tests para el profesor.
- **2026-10-03** (continuación) — CAM-75 (OTs cerradas de solo lectura, 409), CAM-74
  (validación del km con 422 y fotos en curso), CAM-82 (ruteo propio del admin en la URL) y
  CAM-53 (foto del defecto en la misma página). Todo pasó por `revisor` en 7 rondas y está
  mergeado a `develop` (#17, #18, fe#23–26). Se recuperaron con PRs nuevos dos correcciones
  que habían quedado afuera de un merge temprano, y `develop` quedó verificado con build,
  tests, CI y la app andando.
- **2026-10-07/12** — Backlog: épica de Notificaciones (CAM-95, 96 a 103) y Gastos (CAM-104 a
  109). CAM-85 descartada (la hizo Tomás). CAM-93, 84, 88, 92 y 90 hechas con el flujo nuevo de
  release por sprint, y la unificación del filtro de período con lo de Tomás. Todo pasó por
  `revisor` y entró a `develop` (#20, fe#28). Seed de demo cargado y verificado.
