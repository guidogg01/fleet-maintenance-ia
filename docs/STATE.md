# Estado — FleetGuard

Última actualización: **2026-10-29**
Se escribe con el ritual de `docs/guias/sesiones.md`, siempre con confirmación
de Guido.

---

## Dónde estamos

La Entrega 2 está cerrada (`v1.2.0-entrega-2`). Corre el **Sprint 9 - Entrega 3** (24/10 al 31/10). De las 4
cards de Guido, CAM-134 y CAM-135 están hechas y en `release/guido-sprint-9-entrega-3`, en "Pendiente a
Integrar". Quedan CAM-109 y CAM-130, y el PR de la release a `develop`.

## En qué quedé

- **Release del sprint:** `release/guido-sprint-9-entrega-3`, creada desde `develop` en los dos repos y
  pusheada. Reemplaza a `release/guido-sprint-9`, que ya no se usa por el squash.
- **CAM-135 (defectos recurrentes), hecha:**
  - **Regla:** un control del checklist que falla 3 veces en 30 días en el mismo vehículo es recurrente; los
    dos números están en `application.yml`. Cuentan todos los defectos: bloqueantes o no, y abiertos o resueltos.
  - **Aviso:** es un tipo nuevo, `recurring_defect`, configurable en Notificaciones. Se manda una sola vez por
    ventana y se anota en `recurring_defect_alerts`.
  - **Endpoint:** `GET /api/defects/recurring`, solo para admin.
  - **Pantallas:** "Controles con fallos recurrentes" en el detalle del vehículo y "Defectos recurrentes" en el
    Resumen.
  - **Contrato:** `docs/api/CAM-135-recurring-defects-contract.md`.
- **Resumen reacomodado:** a la izquierda, mantenimiento (Estado de la flota y Próximos vencimientos); a la
  derecha, defectos (recientes y recurrentes). "Próximos vencimientos" va en un renglón desde 1280 px y en dos
  entre 641 y 1279 px. Las columnas quedan parejas.
- **CAM-134 (tiempo fuera de servicio), hecha:**
  - **Fecha de resolución:** `Defect.resolvedAt` se carga al finalizar la OT del defecto; solo vale la primera.
  - **Endpoint:** `GET /api/downtime?from&to[&vehicleId]`, solo para admin. Calcula horas fuera de servicio
    (los bloqueantes solapados se unen), paradas, disponibilidad y reparación promedio (en total, internas y
    externas). El período se corta en el momento actual.
  - **Pantallas:** "Disponibilidad de la flota" al final del Resumen, con un solo vehículo (el que más tiempo
    estuvo parado) en lugar del ranking de la card, y "Disponibilidad" en el detalle del vehículo. Las dos
    tienen filtro de período.
  - **Contrato:** `docs/api/CAM-134-downtime-contract.md`.
- **Verificación:** las dos pasaron por `revisor`, con los hallazgos menores corregidos. El backend tiene 511
  tests y 94,5% de cobertura. Las dos se probaron contra el backend real con los datos de demo.
- **Jira:** las dos cards están en "Pendiente a Integrar". Guido les agrega un comentario con las decisiones y
  el cambio de alcance (un solo vehículo en vez del ranking).
- **Repos locales:**
  - Los dos están en `release/guido-sprint-9-entrega-3`, al día con `origin`.
  - En el backend sigue `.idea/misc.xml` sin commitear; no se sube.
  - **La base local tiene datos de prueba:**
    - 4 ciclos de pre-viaje y post-viaje de `carlos.gomez` en AF102ZT, con la falla de luces;
    - un aviso "Defecto recurrente" en la campanita del admin;
    - la tabla `recurring_defect_alerts` y la columna `defects.resolved_at`, que creó `ddl-auto`.

## Qué sigue

- **Sprint 9 - Entrega 3 (cierra el 31/10):**
  - Abrir el PR de `release/guido-sprint-9-entrega-3` a `develop` en los dos repos, con CAM-134 y CAM-135 en la
    descripción.
  - Hablar con Tomás si CAM-109 y CAM-130 entran o pasan al sprint siguiente:
    - CAM-130 se puede hacer sin dependencias, con una vista de impresión en el navegador;
    - CAM-109 necesita decidir el modelo de gastos, así que conviene pasarla.
- **Avisarle a Tomás:**
  - Cuando haga CAM-127 (vencimientos de documentación), sumarla como otra causa de "fuera de servicio" en
    `DowntimeService` (contrato de CAM-134, §1).
  - CAM-133 (QR, suya) depende de CAM-131 (deploy con HTTPS), que no está en el sprint.
  - CAM-102/103 tienen la descripción desactualizada: `Trip.openedById` existe desde CAM-87.
  - CAM-136 no tiene descripción ni épica.
- **Pruebas pendientes:**
  - Asignar una OT a un técnico con las push activadas y ver que le llegue con la app cerrada.
  - Tocar la notificación y que abra la pantalla del aviso.
- **Bugs encontrados por `revisor`, para cards propias:**
  - `ChecklistItemCard.handlePhotoChange` llama a `onChange` con el `state` que tenía al empezar la subida.
    Si mientras sube la foto el chofer edita el título o pasa el control a OK, al terminar se pisa todo.
  - En Gastos, mientras carga la OT de un renglón, el botón de OT de otro renglón (y los de "Órdenes más
    costosas") pueden pedir una segunda OT en paralelo. Se arregla con
    `disabled={openingWorkOrderId !== null}`.
- **Pospuestas a propósito por Guido:**
  - Confirmar que CAM-65, 104, 105, 107 y 108 quedaron en Finalizada.
  - Crear las cards de totales de Gastos en el backend, categorías configurables, el técnico cargando gastos
    y el botón cortado en el detalle de una OT en celular.
  - Refinar CAM-116.
- **Siguen de antes:**
  - Turnos: que el backend no deje reprogramar ni cancelar un turno hecho o cancelado, que valide las fechas
    pasadas al editar, y que un turno pase a "Atrasado" con la pantalla quieta.
  - `@Version` en `Vehicle`.
  - UI pendiente: el encabezado de Planes en celular, el contraste del rojo del dictado, las fotos de
    `FinalizeWorkOrderModal` al cancelar, y el botón atrás con un modal sin guardar.
  - Unificar `WORK_ORDER_FINALIZED` con `WORK_ORDER_CLOSED`.
  - CAM-92, CAM-73, CAM-69/70 y CAM-76.
  - Probar con sesión de admin CAM-82 y CAM-53.
  - Reactivar el aviso de contraseñas filtradas de Chrome.
  - Probar la cámara en un Android real, y el destello de toque de CAM-124.
  - El foco de los modales del admin.

## Decisiones abiertas

- **Sigue, y urge:** qué entra en el Sprint 9 - Entrega 3 y qué pasa al siguiente (CAM-109, CAM-130).
- **Nueva:** si la documentación vencida (CAM-127) va a contar como fuera de servicio. La card la dejaba
  abierta; por ahora no cuenta.
- **Siguen de antes:**
  - El hosting para CAM-131 (deploy con HTTPS). Destraba las push en el celular, la PWA (CAM-132) y el QR
    (CAM-133). Antes hay que resolver `ddl-auto` contra una base que no se puede perder.
  - Librería de PDF (CAM-130) y de QR (CAM-133): dependencias nuevas a decidir.
  - Si el técnico tiene que poder cargar gastos y comprobantes; hay que charlarlo con Tomás.
  - Protección de rama en `develop` con CI obligatorio, y CI para el frontend.
  - Unicidad del username con acentos.
  - Que resetear la contraseña no invalida los tokens ya emitidos.
  - CAM-33, y las épicas CAM-7 y CAM-9.
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
- **2026-10-14** — `preview_stop` dijo que los lanzadores `.cmd` habían terminado ("exited with code
  1"), pero el `java` de `bootRun` y el `node` de Vite seguían ocupando 8080 y 5173. Es el mismo
  problema del 2026-08-31, ahora con el lanzador del Code tab. Antes de matar, conviene ver qué
  proceso es con `Get-CimInstance Win32_Process` (fecha de creación y línea de comando), para no
  matar el IntelliJ de Guido.
- **2026-10-14** — Con el panel del navegador oculto, la página mide 0px de ancho: las medidas de
  layout por JavaScript no sirven y las capturas fallan. Se resolvió fijando el tamaño con
  `resize_window` (por ejemplo 1366×768), sin necesidad de mostrar el panel.
- **2026-10-14** — `printf` con rutas de Windows (`C:\Users\...`) en Bash interpretó `\U` como un
  escape y rompió los `.cmd` y `launch.json`. Los archivos con rutas de Windows se escriben con la
  herramienta Write. En JSON, usar barras `/`.
- **2026-10-14** — El costo por km tomado desde el **menor** km registrado falló con los datos reales.
  Hay inspecciones de AA846JQ con 310 y 15.000 km en un vehículo de 309.400 km: CAM-90 guarda la
  inspección con un km menor aunque no baje el del vehículo. Daba $ 8,86 por km. Se resolvió tomando
  el registro **más antiguo** por fecha.
- **2026-10-14** — Las herramientas Write y Edit convierten el escape Unicode del BOM (U+FEFF) escrito
  en el código en el carácter invisible, y un `sed` con la barra escapada se la comió y dejó `'FEFF'`.
  Anduvo escribirlo con Python armando la barra con `chr(92)`. Ante escapes Unicode en el código,
  revisar el resultado con `od -c`.
- **2026-10-14** — Para probar con backend y front propios (8081 y 5174) sin pisar los de Guido, se
  agregaron entradas temporales a `.claude/launch.json` apuntando a `.cmd` en la carpeta temporal de
  la sesión, y se revirtieron con `git checkout` al terminar. El backend de prueba usa la misma base
  local, así que `ddl-auto` le crea las columnas nuevas también a Guido.

- **2026-10-14** — CAM-106 pedía "reusar el resumen de CAM-52", pero ese resumen no existía, y lo
  que pedía ya se veía en la pestaña Gastos. Las cards de la épica de Gastos (CAM-104 a 109) se
  escribieron sin contrastarlas con lo que ya había hecho CAM-52. Antes de arrancar una card de esa
  épica, conviene compararla con la pantalla real (mejor con una captura) para ver qué aporta de nuevo.
- **2026-10-21** — Para editar por API la descripción de una card de Jira **sin perder la imagen
  embebida**, sirvió escribirla en **ADF** (`contentFormat: "adf"`). La imagen va como `mediaSingle` >
  `media` con `type: "file"`, el `id` de la URL `blob:` que muestra la lectura en markdown y
  `collection: ""`. Para conservar el ancho, se suma `width` + `widthType: "pixel"` en el `mediaSingle`. Se
  confirma leyendo con `expand: renderedFields`: tiene que aparecer un `<img>` del adjunto. Esto resuelve
  los problemas del 2026-09-05 y el 2026-09-26, que venían de escribir en markdown.
- **2026-10-21** — Para chequear finales de línea, `grep -c $'\r$'` en Git Bash dio un falso positivo:
  contó todas las líneas como CRLF. Lo confiable es `git ls-files --eol` o contar bytes con Python. Con
  `core.autocrlf=true`, el repo guarda LF y el working tree está en general en CRLF. Los archivos reescritos
  con scripts quedaron en LF, cosa que Git normaliza igual al commitear.
- **2026-10-21** — Repetición del callejón del 2026-09-24: un `python - <<'EOF'` con acentos dentro del
  heredoc rompió la comparación de textos (`Órdenes` → `�rdenes`), y además un `sed` sobre el script lo dejó
  roto. Para reemplazos con acentos, usar Read + Edit directo.
- **2026-10-21** — Una clase BEM nueva, `expenses__row`, chocó con una existente (la grilla de gráficos de
  Gastos, `display: grid`) y desarmó la tabla. Lint y build no lo detectan; Guido lo vio en la app. Antes de
  inventar un nombre de clase, buscarlo con `grep -rn` en `src/`.
- **2026-10-21** — El panel del navegador no deja usar las herramientas de página sobre un archivo local
  (`file://`). Para probar CSS suelto anduvo servir la carpeta temporal con `py -m http.server` desde una
  entrada temporal de `.claude/launch.json`, revertida con `git checkout` al terminar.
- **2026-10-23** — El navegador integrado de la sesión tiene las notificaciones bloqueadas
  (`pushManager.subscribe` falla con "permission denied"): el service worker se registra, pero las push se
  prueban en el Chrome de Guido. Para la UI de la campanita sin backend, sirvió reemplazar `window.fetch` desde
  la consola con respuestas inventadas (solo para mirar, no queda en el código).
- **2026-10-23** — Una clave VAPID mal copiada hace que Bouncy Castle tire `IllegalArgumentException`, no
  `GeneralSecurityException`. Si no se atrapan las dos, el backend entero no levanta por la push.
- **2026-10-23** — `PushService.send()` de `web-push` espera la respuesta sin límite y arma un cliente HTTP por
  envío. Se usa `sendAsync` con `get(10, SECONDS)` y `cancel` si vence el tiempo.
- **2026-10-23** — Las excepciones de un `@TransactionalEventListener` AFTER_COMMIT le llegan al pedido como 500,
  aunque el cambio ya esté guardado. Atraparlas adentro de la transacción no alcanza: queda marcada para
  rollback y el commit tira igual. Se resolvió con un `TransactionTemplate` REQUIRES_NEW y el `catch` afuera
  (`NotificationDispatcher`).
- **2026-10-24** — Al cerrar el Sprint 9, el PR de Tomás (squash) incluyó toda `release/guido-sprint-9`, porque
  su rama salió de ella. Los commits de Guido no aparecen en `develop` pero el contenido sí: se confirma con
  `git merge-base --is-ancestor <sha> origin/<rama de Tomás>`. Repetición del falso positivo del 2026-09-25.
- **2026-10-24** — Se dio por hecho que CAM-96 figuraba "Finalizada" sin estar terminada (como CAM-90 en
  2026-10-12). Era falso: Tomás la había terminado y mergeado esa misma mañana. Antes de afirmar algo así,
  mirar `origin/develop` y los PRs del otro.

- **2026-10-29** — Pasar "Próximos vencimientos" a la columna izquierda del Resumen no tapó el hueco: lo mudó a
  la derecha (1026 contra 583 px), porque la tarjeta no tenía tope de alto. Se emparejó con tope y scroll (5
  visibles en un renglón) y mostrando 6 defectos recientes. Antes de mover una tarjeta para llenar un hueco,
  conviene mirar si tiene alto fijo.
- **2026-10-29** — Con el panel del navegador oculto, las capturas fallan una y otra vez ("Screenshot timed
  out"), aunque se fije el tamaño con `resize_window`; a veces salen viejas o a medio dibujar. Se verificó
  leyendo la página con `javascript_tool` (textos, alturas y columnas de la grilla). Es una variante del
  callejón del 2026-10-14.
- **2026-10-29** — Repetición del callejón del 2026-10-03: el backend de Guido en 8080 arrancó a las 22:18 y
  CAM-134 se escribió después, así que `/api/downtime` daba 404 y todas las tarjetas decían "No se pudo cargar
  la disponibilidad." Se resolvió reiniciándolo.

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
- **2026-10-14** — Se creó `release/guido-sprint-7`. CAM-65 terminada: el calendario muestra el estado
  de cada turno (el GET acepta varios estados) y hay selectores de fecha y hora propios en toda la app.
  Pasó por `revisor` en dos rondas, se mergeó a la release y se pusheó.
- **2026-10-14** (continuación) — CAM-104 (evolución del gasto apilada por origen), CAM-105 (costo por
  km en el detalle del vehículo), CAM-108 (exportar a CSV con los filtros) y CAM-107 (número y foto del
  comprobante). Todo pasó por `revisor`, se mergeó a `release/guido-sprint-7` y se pusheó, con
  comentarios en Jira. Se creó CAM-116 (kilometraje en inspección y taller).
- **2026-10-14** (continuación 2) — CAM-106 revisada contra Gastos y cerrada sin código, como
  cubierta por CAM-52. Se abrieron los PRs del sprint 7 a `develop` (#21, con el CI en verde, y fe#29),
  con todas las cards del sprint en la descripción.
- **2026-10-21** — `/retomar`: el Sprint 7 lo mergeó Tomás el 19/10. Panorama del Sprint 9: 3 cards de UI de
  Guido libres y 4 de notificaciones bloqueadas por CAM-96. Se creó `release/guido-sprint-9` y se hicieron
  CAM-122 (texto del buscador de Gastos que se desplaza), CAM-123 (renglón de gastos que abre la OT) y
  CAM-124 (tarjeta del checklist entera clickeable). Las tres pasaron por `revisor`, se mergearon y se
  pushearon, y sus cards de Jira quedaron completas en ADF sin perder las capturas.
- **2026-10-23/29** — `/retomar`. CAM-96 (contrato, `NotificationService`, `NotificationDispatcher` y la
  campanita), CAM-99/100 (avisos al técnico sobre sus OTs), CAM-101 (recordatorio de cerrar el viaje) y CAM-119
  (push al navegador con `web-push`, probada en Chrome; falta el celular). Todo pasó por `revisor` en 2 rondas,
  se mergeó a `release/guido-sprint-9` y se pusheó, y Tomás lo incluyó en la Entrega 2 (`v1.2.0-entrega-2`).
  Backlog: épicas CAM-125 y CAM-126, e historias CAM-127 a 135.
- **2026-10-29** (continuación) — `/retomar`. Se creó `release/guido-sprint-9-entrega-3`. CAM-135 (defectos
  recurrentes, con aviso configurable) y CAM-134 (tiempo fuera de servicio y reparación promedio, con
  `Defect.resolvedAt`), más el reacomodo del Resumen en mantenimiento y defectos. Las dos pasaron por `revisor`,
  se mergearon a la release y se pushearon; quedaron en Jira en "Pendiente a Integrar".
