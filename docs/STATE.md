# Estado — FleetGuard

Última actualización: **2026-09-21**
Se escribe con el ritual de `docs/guias/sesiones.md`, siempre con confirmación
de Guido.

---

## Dónde estamos

Épica **CAM-59** (vista de taller/técnico) sigue esperando merges de Tomás:
**CAM-67** (backend #10, frontend #13), **CAM-68** (frontend #14, en Draft) y
**CAM-61** (frontend #12). En paralelo, **CAM-22** (detalle e historial de
vehículo) quedó implementada y con PRs abiertos (backend #11, frontend #15),
sin depender de lo anterior. De las dos cards de Guido en el sprint queda solo
**CAM-60**, bloqueada por **CAM-14** (órdenes de trabajo, de Tomás, En curso).

## En qué quedé

- **CAM-22 implementada y subida**, rama `feature/CAM-22` en los dos repos,
  salida de `develop` (no encadenada sobre CAM-67/68):
  - Backend ([PR #11](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/11),
    commits `4e49f28` y `1cc4039`): endpoints nuevos `GET /api/vehicles/{id}` y
    `GET /api/vehicles/{id}/history` (`{ inspections[], defects[], maintenance[] }`).
    `VehicleHistoryService` aparte de `VehicleService`, queries con `join fetch`
    en `InspectionRepository`, `DefectRepository` y
    `MaintenanceCompletionRepository`. Contrato en `openapi.yaml` y
    `docs/api/CAM-22-vehicle-history-contract.md`, más tests nuevos.
  - Frontend ([PR #15](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/15),
    commits `82b042d` y `529bb31`): `VehicleDetail.tsx` nuevo (ficha + historial),
    fila clickeable en `VehiclesSection.tsx` con la patente como botón para poder
    abrirla con teclado, ruta `admin-vehicle` en `App.tsx` que vuelve a la pestaña
    Vehículos, más servicios, tipos y estilos.
- **Alcance de CAM-22:** sin órdenes de trabajo (todavía no existen). El
  historial de mantenimiento son los "marcar como hecho" de cada plan
  (`MaintenanceCompletion`). Sin paginación.
- **Verificado:** `./gradlew build`, `npm run lint` y `npm run build` en verde.
  Endpoints probados con `curl` contra la base real (200 con datos, 200 con
  listas vacías, 404 para id inexistente o malformado). Flujo visual verificado
  por Guido en su navegador. Revisado por el subagente `revisor`, sin hallazgos
  bloqueantes; se aplicaron dos ajustes menores (patente como botón, aserción
  repetida en un test).
- **Jira CAM-22** reescrita (alcance, criterios de aceptación, contrato, fuera de
  alcance) y comentada con los links de los PRs. Su estado ya figuraba como
  "Pendiente a Integrar". El título se deja como está ("...órdenes"): las
  órdenes entran al historial cuando exista el dominio.
- **Postman:** 9 requests agregados a la carpeta **Vehicles** de la colección
  `FleetGuard — CAM-11 DVIR API` (detalle, historial, alta, edición, reactivar,
  baja, kilometraje, listado de dados de baja y estado de flota). Falta que
  Guido las corra. Quedaron afuera las de asignación de planes (CAM-16).
- Se confirmó en Jira que **CAM-14** ("Crear órdenes de trabajo desde
  defectos", Tomás, En curso, épica CAM-7) es la card que construye el dominio
  de órdenes; se decidió **no** crear una US aparte que la duplique, y no se
  comentó en CAM-14.
- Sin commitear: solo `.idea/misc.xml` en backend (ruido del IDE).

## Qué sigue

- Esperar que Tomás mergee. Backend de CAM-22 (#11) antes que el frontend (#15).
  Los de CAM-59 siguen en su orden: **CAM-67** (backend #10, frontend #13) →
  **CAM-68** (frontend #14, pasar de Draft a Ready recién ahí, rebaseando contra
  `develop` primero) → **CAM-61** (frontend #12).
- **CAM-60** (dashboard de taller) y **CAM-63** (sección "Mantenimientos"/gastos)
  esperan a **CAM-14** (Tomás, En curso). Cuando se mergee, ver qué modelo de
  órdenes dejó y abrir una US chica de seguimiento con lo que falte: órdenes en
  el historial del vehículo (CAM-22), crear una orden desde el detalle del
  vehículo o desde un mantenimiento vencido, y que `workOrderId` de las
  completions apunte a una orden real.
- **CAM-69/CAM-70** (vistas de defectos/mantenimientos para el taller) quedan en
  el backlog de CAM-59, fuera del sprint. Van a necesitar contenido real dentro
  de `TechnicianShell`, que hoy es solo placeholder; el historial de CAM-22
  puede servirles de base.
- Refinar la UI/UX del detalle de vehículo en próximas cards (hoy es una base
  simple a propósito).
- Quien retome en otra máquina/base local va a necesitar el mismo fix manual del
  `CHECK` constraint de `users` antes de poder loguear un usuario técnico (ver
  Callejones).
- Cuando Tomás retome **CAM-57**: no tiene descripción en texto, solo una
  captura que no se pudo ver (el navegador de la sesión no tiene login de Jira).
- Backlog del sprint sin arrancar: **CAM-58** (evaluar rediseño UI), **CAM-62**
  (interno/tercerizado); CAM-60 y CAM-63 dependen de CAM-14.
- CAM-16: el historial de completions ahora se ve en el detalle de vehículo
  (CAM-22), pero sigue sin haber un contador de "cuántas veces se hizo un
  mantenimiento" — quedó fuera de su entrega original.
- CAM-25: validación de formato de patente e historial de altas/bajas quedaron
  fuera — menores.
- **Router del frontend**: sigue pendiente, cada vez conviven más pantallas con
  el routing manual de `App.tsx` (se sumó `admin-vehicle` esta sesión).
- **CAM-23** (gestión de usuarios y roles) — el panel admin ya existe, es
  candidata a arrancar; su rol "Mantenimiento" = "Técnico" de CAM-59.
- Confirmar con Tomás si **CAM-21** ("Vista de próximos mantenimientos"
  dedicada) sigue haciendo falta o ya quedó cubierta por el calendario (CAM-42).
- Backlog viejo en Jira sin refinar: **CAM-52** (apartado de "Gastos"),
  **CAM-53** (modal para ver foto sin salir de la página), **CAM-54** (hover en
  menú hamburguesa).
- **Proteger endpoints con el JWT real**: sigue igual, `X-Driver-Id` es lo único
  que el backend valida de verdad hoy.
- Repasar la cobertura de tests del backend más allá de `AuthService`/
  `DefectService`/`VehicleService` (controllers, `PhotoService`, mappers,
  `GlobalExceptionHandler`, `ScheduledMaintenanceService`); el mapeo con datos
  reales de `VehicleHistoryService` tampoco tiene test todavía.

## Decisiones abiertas

- **Nueva: paginación del historial de vehículo.** Se dejó sin paginar, como el
  resto de la API. Se revisa si un vehículo acumula mucho historial.
- **Nueva: cómo se vinculan las órdenes de trabajo (CAM-14) con los vehículos.**
  Conviene que el modelo contemple un vehículo (no solo un defecto) y que
  `workOrderId` de las completions pueda apuntar a una orden real. Falta
  coordinarlo con Tomás; no se comentó en CAM-14 por decisión de Guido.
- **¿Se formaliza el patrón de "rama encadenada + PR en Draft + nota de
  dependencia"** para cards que dependen de otra sin mergear? Se usó ad-hoc para
  CAM-68→CAM-67; no está escrito como convención en `docs/guias/sesiones.md`.
  (CAM-22, en cambio, salió directo de `develop`.)
- **Convención `bugfix/` vs. `feature/`.** Confirmada por Guido el 2026-09-16
  según el tipo de issue en Jira ("Error" → `bugfix/`, el resto → `feature/`).
  Falta que Tomás la adopte.
- **Router del frontend.** Sin cambios.
- **Autenticación en el resto de endpoints.** Sin cambios — JWT solo protege el
  login todavía; CAM-22 sigue el mismo patrón (sin enforcement en backend).
- **PRs de `feature/guido`.** Sin cambios, siguen abiertos (#3 en cada repo) sin
  contenido útil.
- **Flujo de ramas/PRs formal.** Parcialmente resuelto: convención de nombres
  confirmada, más que Tomás revisa/mergea los PRs de las sesiones de Guido por default. El
  acuerdo formal completo con Tomás sigue sin cerrar.
- **Cómo mantener `STATE.md` al día cuando Tomás mergea sin pasar por este
  ritual.** Sin cambios — el procedimiento de reconciliación (git + JQL) sigue
  funcionando.
- **`ddl-auto: update` no retroactiva constraints en bases ya creadas.** Sin
  cambios (ver Callejones).
- **CAM-21 vs. calendario nuevo.** Sin cambios.
- **Forma del error de la API.** Sin cambios.
- **Paginación en general.** Sigue abierta.
- **Modelo de datos / versionado de schema.** Sin cambios (JPA `ddl-auto`, sin
  Flyway).
- **CAM-66 ("Sarasa 2").** Sigue fuera del sprint y sin repurposear — es el
  comodín para sumar trabajo no planeado sin alterar la velocity. **CAM-65**
  también quedó fuera del sprint y disponible para uno futuro.

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
