# Agregar un endpoint de punta a punta

El orden importa: **primero el contrato, después el backend, después el
frontend.** Al revés es como se llega a que la home diga "offline" durante días
sin que nadie sepa por qué.

## 1. Contrato (`../TIP - Backend/docs/api/openapi.yaml`)

Antes de escribir código, anotá en `openapi.yaml`: ruta, método, parámetros,
forma exacta del JSON de éxito con un ejemplo real, y los códigos de error con
su forma. Si hay decisiones puntuales de la card que no entran en el spec,
sumá un `docs/api/<CARD>-contract.md` al lado (ver `CAM-11-dvir-contract.md` o
`CAM-43-login-contract.md` como ejemplo). Si algo no está claro acá, va a
estar peor en el código.

## 2. Backend (`TIP - Backend`)

Sigue la arquitectura en capas de `backend-AGENTS.md` → "Estructura hoy"
(actualizada tras la migración a Spring Boot del 2026-08-31):

1. **Entidad** (`entity/`), si hace falta tabla nueva: clase `@Entity` con
   `@Id`/`@GeneratedValue` y las columnas.
2. **Repository** (`repository/`): interfaz que extiende `JpaRepository` (o
   `CrudRepository`). Spring Data genera la implementación — no se escribe SQL
   a mano salvo que haga falta un `@Query` explícito.
3. **DTOs** (`dto/`): `record`s de request/response con los campos de
   `openapi.yaml`. No exponer la entidad JPA directamente.
4. **Mapper** (`mapper/`): función entidad ↔ DTO.
5. **Service** (`service/`): la lógica de negocio — llama al repository,
   aplica reglas, lanza excepciones de dominio (`exception/`) si algo no
   cierra.
6. **Controller** (`controller/`): `@RestController` con `@RequestMapping`
   (ruta plana, sin `/api` — el prefijo lo pone `server.servlet.context-path`).
   Delega todo al service, no pone lógica acá.
7. No hace falta "registrar" nada a mano: Spring detecta el `@RestController`
   solo. Probalo con curl o Postman antes de tocar el frontend:
   ```bash
   curl -i http://localhost:8080/api/loquesea
   ```
   Verificá que la respuesta sea **idéntica** a lo que dice `openapi.yaml`. Si
   no lo es, corregí el código o corregí el contrato, pero que queden iguales.

## 3. Frontend (`TIP - Frontend`)

1. Escribí el `type` de la respuesta copiando los campos de `openapi.yaml`.
2. Hacé el `fetch` contra `${API_BASE_URL}/api/...`, con `API_BASE_URL` saliendo
   de `import.meta.env.VITE_API_BASE_URL`.
3. Manejá los tres estados: cargando, ok, error. El error también es una pantalla.
4. `npm run lint && npm run build`.

## 4. Cierre

- Antes de commitear, pedí una revisión con el subagente `revisor`.
- Commiteá el backend y el frontend por separado, cada uno en su repo.
- Corré `/cierre` para dejar anotado en `STATE.md` qué quedó y qué sigue.
