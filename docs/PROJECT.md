# FleetGuard — qué es y por qué está así

Documento estable. Cambia cuando cambia una decisión de fondo, no cada sesión.
Para "en qué quedé" andá a `STATE.md`; para "qué falta", a `ROADMAP.md`.

## Qué es

Sistema de **mantenimiento preventivo e inspecciones de flota**. Trabajo práctico
integrador (TIP) de facultad, hecho por un equipo, donde todos usamos asistentes
de IA para trabajar.

## Dominio

Estas son las áreas a construir. La modelación fina de cada una todavía no está
cerrada: cuando se cierre, se anota acá.

- **Flota** — los vehículos y sus datos.
- **Inspecciones** — el chequeo que alguien le hace a un vehículo, con su
  resultado.
- **Defectos** — lo que una inspección encuentra mal.
- **Órdenes de trabajo** — el trabajo de reparación que se abre para resolver
  defectos.
- **Mantenimiento preventivo** — lo que hay que hacer antes de que falle, por
  tiempo o por uso.
- **Login y roles** — quién entra y qué puede hacer.

Implementado hoy: **Inspecciones** (DVIR pre/post-trip) y **Defectos** (nacen de
una respuesta de checklist), vía CAM-11. Ver `docs/STATE.md` para el detalle y
`../TIP - Backend/docs/api/openapi.yaml` para el contrato. El resto del dominio
(flota más allá del listado, órdenes de trabajo, mantenimiento preventivo,
login/roles) sigue sin construir.

## Arquitectura

Tres repos separados, no monorepo.

| Repo | Carpeta local | Qué es |
|---|---|---|
| `fleet-maintenance` | `TIP - Backend` | API REST en Java 21 |
| `fleet-maintenance-fe` | `TIP - Frontend` | SPA en React 19 + TypeScript |
| `fleet-maintenance-ia` | `TIP - IA` | Documentación, contexto y config de Claude Code para los dos anteriores (este repo) |

Backend y frontend se comunican por REST sobre `http://localhost:8080`. El
frontend toma esa URL de `VITE_API_BASE_URL`. El contrato está en
`TIP - Backend/docs/api/openapi.yaml`, no acá — vive junto al código que
describe. `fleet-maintenance-ia` no corre código: es donde se abre Claude
Code, y desde donde se accede a los otros dos como directorios adicionales
(ver `CLAUDE.md` de este repo).

## Decisiones y por qué

**Documentación de IA y `.claude/` en un tercer repo (`fleet-maintenance-ia`),
desde 2026-09-05.** Reemplaza las decisiones de que "la documentación
compartida vive en `fleet-maintenance/docs/`" y de que "el backend es la casa
del proyecto" (ver más abajo el porqué original de las dos, quedan como
registro histórico). Guido decidió separar la documentación de **contexto
para sesiones de IA** — `docs/PROJECT.md`, `docs/STATE.md`, `docs/ROADMAP.md`,
`docs/SETUP.md`, `docs/guias/`, `.claude/` (comandos, subagentes) y los
`AGENTS.md` de cada repo de código — del código de aplicación, en un repo
aparte: `fleet-maintenance-ia`, carpeta local `TIP - IA`. Claude Code se abre
parado acá; `TIP - Backend` y `TIP - Frontend` se acceden como directorios
adicionales (`.claude/settings.json`), el mismo mecanismo que antes se usaba
solo para que el backend llegara al frontend. Los `AGENTS.md` de cada repo se
movieron como `backend-AGENTS.md` y `frontend-AGENTS.md`. **El contrato de API
(`docs/api/openapi.yaml`, los `*-contract.md` por card) y los datos de arranque
(`docs/db/`) se quedan en `fleet-maintenance` (backend)** — a diferencia del
resto, no son contexto de sesión sino especificación versionada junto al
código que describen; separarlos de ahí los volvería a desincronizar, que es
justo el problema que ya resolvió la decisión de abajo ("Contrato de API en
OpenAPI"). Costo aceptado: un tercer repo para clonar y mantener sincronizado
(y una migración que rompe todas las rutas relativas que asumían "parado en
`TIP - Backend`"); a cambio, ningún commit de documentación de contexto vuelve
a mezclarse con el historial de código de ninguno de los dos repos, y el mismo
contexto sirve para los dos por igual sin duplicar nada.

**Contrato de API en OpenAPI, desde 2026-09-05.** Reemplaza la decisión
anterior ("Contrato de API en markdown, no OpenAPI", ver más abajo el porqué
original). Tomás, al mergear CAM-43 (login), reemplazó `docs/API.md` por
`docs/api/openapi.yaml` + un `docs/api/<CARD>-contract.md` por card cuando
hacen falta decisiones puntuales (`CAM-11-dvir-contract.md`,
`CAM-43-login-contract.md`) — sin esperar a que se cumpliera ninguno de los
tres disparadores que la decisión original había fijado. `docs/API.md` no
existe más en ningún repo. Costo aceptado: un spec que hay que mantener en vez
de un markdown de lectura rápida; a cambio, un solo lugar sin la ambigüedad de
"¿esto ya está en API.md o solo en el código?" que tenía convivir con
`docs/api/openapi.yaml` de CAM-11 desde el principio.

**Backend con Spring Boot, desde 2026-08-31.** Reemplaza la decisión anterior
("sin frameworks", ver más abajo el porqué original). Guido y Tomás venían
trabajando cada uno en su propio stack (`HttpServer`/JDBC a mano en un repo,
Spring Boot en el otro) y habían hablado de converger — Tomás migró primero su
parte (CAM-11, PR
[`fleet-maintenance#2`](https://github.com/Tomas-Neira-Guitera/fleet-maintenance/pull/2))
y la mergeó a `develop` antes de que se terminara de decidir formalmente entre
los dos. Guido confirmó adoptar ese stack como el del equipo y se hizo el merge
de `develop` a `feature/guido`, descartando la implementación vieja
(`HttpServer`/JDBC/JSON a mano) por completo. Costo aceptado: se pierde el
valor pedagógico original de escribir el servidor HTTP a mano; a cambio, todo
el equipo trabaja sobre el mismo stack sin tener que mantener dos arquitecturas
en paralelo.

**Backend sin frameworks — decisión original, revertida el 2026-08-31 (ver
arriba).** `com.sun.net.httpserver.HttpServer` del JDK y JDBC pelado, sin
Spring ni ORM. Fue una decisión del equipo: en un TIP se aprende más viendo
cómo funciona un servidor HTTP y una query que aprendiendo a configurar un
framework. Se mantiene acá como registro histórico de por qué el proyecto
empezó así.

**JSON vía Jackson, desde 2026-08-31.** Corolario de la migración a Spring
Boot — reemplaza el JSON armado a mano con `String.format`. Los DTOs son
`record`s de Java; Jackson los deserializa desde el JSON de entrada usando los
nombres de los parámetros del constructor (compilador con `-parameters`, sin
`@JsonCreator` manual).

**Arquitectura en capas en el backend, desde 2026-08-28 — vigente, con capas
nuevas desde 2026-08-31.** Arrancó como `controller`/`model`/`dao` (reemplazando
"un handler por endpoint en `Main.java`") a pedido de Guido, antes de que
doliera de verdad. Con la migración a Spring Boot se suman `service`,
`repository`, `dto`, `mapper` y `exception` — las capas que trae Tomás de CAM-11.
El criterio de fondo no cambió: mantener la misma estructura desde el principio
en vez de refactorizar más adelante. El molde queda anotado en
`backend-AGENTS.md` → "Estructura hoy".

**Repos separados.** Se despliegan y evolucionan por separado, y el equipo puede
trabajar en uno sin tocar el otro.

**La documentación compartida vive en `fleet-maintenance/docs/` — decisión
original, revertida el 2026-09-05 (ver arriba).** No en un tercer repo. Cinco
markdown no justifican un repo entero, con su clone, su permiso y su
historial. Costo aceptado en su momento: los commits de estado se mezclaban en
el historial del backend, mitigado con la regla de que el commit de estado va
solo y toca únicamente `docs/`. Se mantiene acá como registro histórico de por
qué el proyecto empezó así — la razón por la que se revirtió (evitar esa
mezcla del todo, no solo mitigarla) está en la decisión de arriba.

**Contrato de API en markdown, no OpenAPI — decisión original, revertida el
2026-09-05 (ver arriba).** Un `API.md` que se lee de un vistazo valía más en
su momento que un spec que hay que mantener y del que nadie genera nada. Se
iba a migrar a OpenAPI cuando pasara cualquiera de estas tres cosas: más de
~10 endpoints estables, el primer bug por un campo desalineado, o querer
generar tipos de TypeScript automáticamente — CAM-11 ya usaba OpenAPI en
paralelo desde el principio sin esperar ninguno de los tres, y CAM-43
terminó de decidirlo de hecho. Se mantiene acá como registro histórico.

**El contenido va en `AGENTS.md`, y `CLAUDE.md` es un puntero.** Claude Code
lee únicamente `CLAUDE.md`; otras herramientas (OpenCode, Cursor, Codex) leen
`AGENTS.md`. Poner el contenido en el formato universal deja las reglas
legibles por cualquier herramienta y por cualquier humano, sin duplicarlas.
Desde el 2026-09-05 hay dos, `backend-AGENTS.md` y `frontend-AGENTS.md` (ver
la decisión de arriba), y `CLAUDE.md` ya no los importa con `@` — los señala
como lectura obligatoria antes de tocar el repo que corresponda, para no
cargar las reglas de un código en sesiones que solo tocan el otro.

**Todo el contexto vive dentro de los repos.** Reglas, documentación, comandos
y subagentes están versionados — hoy repartidos en `fleet-maintenance-ia`
(`docs/`, `AGENTS.md` de cada repo, `.claude/`) y `fleet-maintenance`
(`docs/api/`, `docs/db/`). Nada queda en una carpeta suelta de una sola
máquina: quien clona los repos recibe el sistema completo, sin que nadie
tenga que pasarle archivos por chat.

**El backend es la casa del proyecto — decisión original, revertida el
2026-09-05 (ver arriba).** Claude Code se abría parado en `TIP - Backend`, que
era donde estaban `docs/` y `.claude/`, y llegaba al frontend como directorio
adicional. Se mantiene acá como registro histórico: la casa del proyecto pasó
a ser `fleet-maintenance-ia`, que llega a los dos repos de código como
directorio adicional por igual, en vez de que uno de los dos repos de código
tuviera ese rol especial.

**Agentes por modo de trabajo, no por área del código.** Un agente "backend" y
uno "frontend" duplicarían lo que ya dice cada `AGENTS.md`. Lo que sí cambia
el comportamiento es *cómo* se trabaja: proponer sin tocar (plan mode),
construir (modo normal), revisar sin poder editar (`revisor`).

**Guías en markdown plano, no skills.** Una guía en `docs/guias/` la lee
cualquier herramienta y cualquier persona del equipo, hoy y dentro de dos años.
Una skill la lee una sola herramienta. Cuando una guía se vuelva un procedimiento
que se repite idéntico muchas veces, ahí se evalúa convertirla.

## Convenciones

- Java: paquete `org.example`, package-by-layer (ver `backend-AGENTS.md`).
- Frontend: Oxlint como linter, TypeScript estricto vía `tsc -b` en el build.
- Sin CI/CD todavía. Sin convención de nombres de commit todavía.
- **Ramas y PRs, desde 2026-08-31.** Ya no es rama única sin PRs: hay `main`,
  `develop` y ramas de feature (`feature/guido`, `feature/CAM-11-dvir-checklist`)
  en los dos repos, con PRs de feature branches hacia `develop`/`main` en
  GitHub. El flujo exacto (¿todo pasa por `develop`? ¿quién aprueba?) todavía no
  está escrito en ningún lado — anotado como decisión abierta en `STATE.md`.
