# Estado — FleetGuard

Última actualización: **2026-09-11**
Se escribe con el ritual de `docs/guias/sesiones.md`, siempre con confirmación
de Guido.

---

## Dónde estamos

El panel de admin quedó con ABM completo de vehículos (alta/edición/baja
lógica/reactivar, patente única, kilometraje) y de planes de mantenimiento
(catálogo editable + asignación + "marcar como hecho", con recálculo
automático de vencimientos y refresco en vivo entre pestañas). Dos PRs
abiertos a `develop` (backend
[#9](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/9),
frontend
[#11](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/11))
cubriendo CAM-25 y CAM-16 juntas — Tomás ya está al tanto. El test suite del
backend sigue roto por un bug suyo pendiente (de CAM-42), lo que dejó sin
correr el test nuevo que agregamos hoy.

## En qué quedé

- **Backend, rama `feature/CAM-25`** (commit `e4a6db7`, pusheada,
  [PR #9](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/9)
  contra `develop`): ABM de vehículos (`POST/PATCH/DELETE
  /api/vehicles[/{id}]`, ver `docs/api/CAM-25-vehicle-abm-contract.md`) +
  fix de `MaintenancePlan.category` (era `NOT NULL`, el contrato siempre lo
  documentó opcional). `VehicleServiceTest` nuevo, sin correr (ver
  Decisiones abiertas).
- **Frontend, rama `feature/CAM-25`** (commit `1cdcb6d`, pusheada,
  [PR #11](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/11)
  contra `develop`): ABM de vehículos + CAM-16 completa (migrada de
  "Vehículos" a "Planes de Mantenimiento": asignar/desasignar planes,
  marcar como hecho, catálogo editable) + carga de kilometraje (CAM-18).
- Jira **CAM-16** y **CAM-25** actualizadas con historia + criterios de
  aceptación + links a los PRs — las dos pasaron solas a "Pendiente a
  Integrar".
- Comentarios cruzados en los dos PRs aclarando que las dos cards van en
  el PR de frontend, y que el de backend es solo CAM-25.
- Guido ya le avisó a Tomás de los PRs.
- Fix aplicado a mano en la base local de Guido (no versionado, no lo hace
  `ddl-auto`): `ALTER TABLE maintenance_plans ALTER COLUMN category DROP
  NOT NULL`.
- Working directories de código parados en `feature/CAM-25` en los dos
  repos (no en `develop`).

## Qué sigue

- Revisar y mergear los PRs
  [#9](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/9) y
  [#11](https://github.com/Tomas-Neira-Guitera/fleet-maintenance-fe/pull/11).
- Cuando Tomás arregle `DefectMapperTest`/`DefectServiceTest`: correr
  `./gradlew build` completo y confirmar que `VehicleServiceTest` pasa.
- Quien levante el proyecto con una base local ya creada (no fresca) va a
  necesitar correr a mano `ALTER TABLE maintenance_plans ALTER COLUMN
  category DROP NOT NULL` — avisarle a Tomás también.
- CAM-16: historial visible de completions (cuántas veces se hizo un
  mantenimiento) quedó fuera de esta entrega.
- CAM-25: validación de formato de patente e historial de altas/bajas
  quedaron fuera — menores.
- **Router del frontend**: sigue pendiente, cada vez conviven más
  pantallas con el routing manual de `App.tsx`.
- **CAM-23** (gestión de usuarios y roles) — el panel admin ya existe, es
  candidata a arrancar.
- Confirmar con Tomás si **CAM-21** ("Vista de próximos mantenimientos"
  dedicada) sigue haciendo falta o ya quedó cubierta por el calendario
  (CAM-42).
- Backlog nuevo en Jira sin refinar: **CAM-52** (apartado de "Gastos"),
  **CAM-53** (modal para ver foto sin salir de la página), **CAM-54**
  (hover en menú hamburguesa).
- **Proteger endpoints con el JWT real**: sigue igual, `X-Driver-Id` es lo
  único que el backend valida de verdad hoy.
- Repasar la cobertura de tests del backend más allá de `AuthService`/
  `DefectService`/`VehicleService` (controllers, `PhotoService`, mappers,
  `GlobalExceptionHandler`, `ScheduledMaintenanceService`) — sigue
  pendiente de sesiones anteriores.

## Decisiones abiertas

- **Router del frontend.** Sin cambios.
- **Autenticación en el resto de endpoints.** Sin cambios — JWT solo
  protege el login todavía.
- **PRs de `feature/guido`.** Sin cambios, siguen abiertos (#3 en cada
  repo) sin contenido útil.
- **Flujo de ramas/PRs formal.** Parcialmente resuelto: Guido fijó
  `feature/<CARD-ID>` como convención para sus propias ramas (antes era
  solo el ID) — el acuerdo formal con Tomás sigue sin cerrar.
- **Nueva: test suite del backend roto.** Bug de Tomás en
  `DefectMapperTest`/`DefectServiceTest` (firma vieja de `DefectMapper`)
  sigue sin arreglar — confirmado de nuevo hoy con `git fetch` +
  recompilar, cero cambios en `origin/develop`. Bloquea correr cualquier
  test del backend, incluido el nuevo `VehicleServiceTest`.
- **Nueva: `ddl-auto: update` no retroactiva constraints en bases ya
  creadas.** Ver Callejones sin salida, 2026-09-11 — cualquiera con una
  base local vieja se va a topar con el mismo problema al traer estos PRs.
- **Cómo mantener `STATE.md` al día cuando Tomás mergea sin pasar por este
  ritual.** Sin cambios.
- **CAM-21 vs. calendario nuevo.** Sin cambios.
- **Forma del error de la API.** Sin cambios.
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
