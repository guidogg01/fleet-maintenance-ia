# FleetGuard — documentación y contexto de IA (`fleet-maintenance-ia`)

Este repo es la casa de la documentación compartida del proyecto y de la
configuración de Claude Code: acá viven `docs/` (contexto, estado, contrato de
API) y `.claude/` (comandos, subagentes) que usan los dos repos de código.
**Abrí Claude Code parado acá**, no en `TIP - Backend` ni en `TIP - Frontend`
directamente.

El contexto general del proyecto se carga solo desde estos archivos:

@docs/PROJECT.md
@docs/STATE.md
@docs/API.md

## Los otros dos repos

El código vive en dos repos hermanos, agregados como directorios adicionales
en `.claude/settings.json`:

- `../TIP - Backend` (`fleet-maintenance`) — API REST en Java 21 + Spring Boot.
- `../TIP - Frontend` (`fleet-maintenance-fe`) — SPA en React 19 + TypeScript.

**Antes de tocar cualquier archivo de uno de los dos, leé sus reglas:**

- Backend → [`backend-AGENTS.md`](backend-AGENTS.md)
- Frontend → [`frontend-AGENTS.md`](frontend-AGENTS.md)

No se importan automáticamente acá (con `@`) para no cargar las reglas de un
repo en sesiones que solo tocan el otro.

Si el acceso a alguno de los dos no funciona, corré `/add-dir "../TIP - Backend"`
o `/add-dir "../TIP - Frontend"` a mano y avisame que hay que arreglar
`settings.json`.

## Documentación que se lee a pedido

- `docs/ROADMAP.md` — qué falta construir, por hitos
- `docs/SETUP.md` — armar el proyecto en una máquina nueva
- `docs/guias/sesiones.md` — el ritual de `/retomar` y `/cierre`, y la referencia
  rápida de cómo se usa todo esto
- `docs/guias/nuevo-endpoint.md` — agregar un endpoint de punta a punta
