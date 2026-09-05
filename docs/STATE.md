# Estado — FleetGuard

Última actualización: **2026-09-05**
Se escribe con el ritual de `docs/guias/sesiones.md`, siempre con confirmación
de Guido.

---

## Dónde estamos

Toda la documentación/contexto de IA se centralizó en un repo nuevo,
`fleet-maintenance-ia` (`TIP - IA`) — las sesiones arrancan ahí de ahora en
más. Se reconcilió con una limpieza equivalente que Tomás hizo por su cuenta
en CAM-43 (`docs/API.md` → `docs/api/openapi.yaml`, que se queda en el
backend). CAM-37 (widget de defectos recientes en el panel admin) quedó
implementado, verificado a mano y con PR abierto en los dos repos.

## En qué quedé

- **`fleet-maintenance-ia`** (rama `master`, pusheada, sin PR — repo nuevo,
  solo de Guido por ahora): migración completa de `docs/` (PROJECT, STATE,
  ROADMAP, SETUP, guías), los dos `AGENTS.md` (como `backend-AGENTS.md` /
  `frontend-AGENTS.md`) y `.claude/` (comandos, subagente `revisor`) desde
  el backend. Reconciliado con lo de Tomás: `docs/api/` y `docs/db/` se
  quedan en el backend (especificación versionada con el código, no
  contexto de sesión). `ROADMAP.md` actualizado con lo que CAM-40 ya
  entregó en silencio (ver más abajo, Jira desactualizado).
- **Backend, rama `chore/mover-docs-ia`**
  ([PR #6](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/6)
  contra `develop`): termina de sacar `docs/PROJECT.md`/`ROADMAP.md`/
  `SETUP.md`, que Tomás no había tocado en su propia limpieza.
- **Backend, rama `CAM-37`** (commit `6f80f7d`, pusheada,
  [PR #7](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/7)
  contra `develop`): agrega `reportedBy` a `GET /api/defects` (`DefectDto`,
  `DefectMapper`, `openapi.yaml`), resuelto desde `Inspection.driverName`
  sin queries extra. Tests actualizados (`DefectServiceTest`) y nuevos
  (`DefectMapperTest`).
- **Frontend, rama `chore/mover-docs-ia`**
  ([PR #6](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/6)
  contra `develop`): saca `AGENTS.md`/`CLAUDE.md`.
- **Frontend, rama `CAM-37`** (commit `e167320`, pusheada,
  [PR #7](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/7)
  contra `develop`): widget "Defectos abiertos recientes" en el panel admin
  (`RecentDefectsCard`, `SeverityBadge` compartido con `DefectsList`,
  `utils/relativeTime.ts`), con botón "← Volver" mínimo para admin.
  Verificado end-to-end a mano (inspección real → defecto → widget → "Ver
  todos" → volver). Revisado con el agente general-purpose (`revisor` no
  estaba disponible en esta sesión — ver Callejones sin salida) sin
  hallazgos bloqueantes.
- **CAM-37 en Jira** actualizada con historia de usuario + criterios de
  aceptación, mismo formato que CAM-43. El estado pasó solo de "En
  refinamiento" a "Pendiente a Integrar" (probablemente la integración
  Jira-GitHub al detectar el PR, no una transición manual) — **falta
  confirmar a simple vista que el mock de la card no se rompió** al
  reescribir la descripción vía API.
- Encontrado, revisando ROADMAP + backlog de Jira: **CAM-16/17/18/20/46/47/48
  ya están hechas** (mantenimiento preventivo, dashboard de flota) gracias a
  CAM-40, pero Jira las sigue mostrando "por hacer"/"pendiente a integrar".
- Guido pidió no volver a poner atribución de Claude (`Co-Authored-By`,
  "Generated with Claude Code") en commits ni PRs — aplicado desde ahora,
  guardado en memoria.
- `.idea/misc.xml` volvió a aparecer modificado en el backend — drift de
  JDK de siempre, no se toca.

## Qué sigue

- Arrancar **CAM-20** (dashboard de admin completo — KPIs, sidebar,
  próximos vencimientos) en una sesión nueva, parada en `TIP - IA`.
- Mergear los PRs de hoy: `chore/mover-docs-ia` (#6) y `CAM-37` (#7) en
  cada repo.
- **Hablar con Tomás** de tres cosas:
  1. Sincronizar el estado de Jira (CAM-16/17/18/20/46/47/48 ya hechas).
  2. Qué hacer con los PRs de `feature/guido` (#3 en cada repo, todavía
     abiertos) — quedaron sin contenido útil, todo se mudó a
     `fleet-maintenance-ia`.
  3. La convención `chore/<descripción>` usada hoy para infraestructura sin
     card de Jira, como extensión de "una rama por card".
- Confirmar visualmente que el mock de CAM-37 en Jira sigue intacto.
- **Proteger endpoints con el JWT real**: sigue igual, `X-Driver-Id` es lo
  único que el backend valida de verdad hoy.
- **CAM-23** (gestión/invitación de usuarios) queda para cuando exista el
  panel admin.
- Repasar la cobertura de tests del backend más allá de `AuthService`/
  `DefectService` (controllers, `VehicleService`/`PhotoService`, mappers,
  `GlobalExceptionHandler`) — sigue pendiente de sesiones anteriores.

## Decisiones abiertas

- **Router del frontend.** Sigue sin resolverse, y ahora bloquea
  directamente CAM-20 (sidebar de admin con varias secciones).
- **Autenticación en el resto de endpoints.** Sin cambios — JWT solo
  protege el login todavía (reemplazo real de `X-Driver-Id`/
  `HeaderDriverResolver`, sigue sin fecha).
- **PRs de `feature/guido`.** Nueva: quedaron sin contenido útil (todo se
  mudó a `fleet-maintenance-ia`) — a decidir con Tomás si se cierran sin
  mergear.
- **Flujo de ramas/PRs formal.** Sigue sin consensuarse con Tomás — hoy
  conviven "una rama por card" y, desde hoy, `chore/<descripción>` para
  trabajo sin card.
- **Forma del error de la API.** Sin cambios — CAM-11 ya usa
  `{ error, message }` de hecho, falta confirmarla como convención general.
- **Paginación.** Sigue abierta.
- **Modelo de datos / versionado de schema.** Sin cambios (JPA `ddl-auto`,
  sin Flyway).

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
