<!-- ══════════════════════ HEADER ══════════════════════ -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1200&color=7AA2F7&center=true&vCenter=true&width=620&lines=Luis+Hidalgo+%E2%80%94+Full-Stack+Engineer;Java+%C2%B7+TypeScript+%C2%B7+Flutter;From+API+contract+to+production;Del+contrato+de+la+API+a+producci%C3%B3n" alt="Full-Stack Engineer · Java · TypeScript · Flutter" />

**Diseño el contrato, construyo las tres puntas que lo consumen y automatizo el camino a producción.**
<br/>
<sub><i>I design the contract, build the three clients that consume it, and automate the path to production.</i></sub>

<br/>

<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-7AA2F7?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="Email" /></a>
<img src="https://komarev.com/ghpvc/?username=luishidalgoa&label=Profile+views&color=7AA2F7&style=flat" alt="Profile views" />

</div>

---

## 🧭 En 15 segundos · <sub>In 15 seconds</sub>

|  | |
|---|---|
| 🏗️ | **Producto multi-repo, no scripts sueltos.** Kromia es un SDK *contract-first* del que cuelgan un studio web, una API y una app móvil — con CI que impide que se desincronicen. |
| 🔐 | **Backend con seguridad de verdad.** Spring Security (JWT, OAuth2, roles, method-level) y Node/Express endurecido: Helmet, rate-limit, cookies httpOnly, bcrypt. |
| ⚡ | **Tiempo real end-to-end.** Socket.IO en el servidor y cliente WebSocket nativo en Flutter — mismo canal, dos plataformas. |
| ⚙️ | **Automatizo lo repetitivo.** GitHub Actions (iOS `.ipa`, imágenes ARM64, drift-CI, cron), despliegue *pull-based* y observabilidad Prometheus + Grafana sobre Raspberry Pi. |
| 🤖 | **IA agéntica aplicada.** Escribo **servidores MCP** propios (TypeScript, C#, Node) para que los agentes operen mis herramientas con contratos deterministas. |

<sub><i>🇬🇧 Multi-repo product engineering (contract-first SDK → web studio + API + mobile app) · hardened auth with Spring Security & Node · real-time over Socket.IO on server and Flutter · CI/CD, pull-based deploys and Prometheus/Grafana observability on self-hosted hardware · and custom MCP servers so AI agents can drive my own tooling.</i></sub>

---

## 🧰 Stack

**Lenguajes**

[![](https://skillicons.dev/icons?i=ts,java,dart,cs,py,php,js,bash&theme=dark)](https://skillicons.dev)

**Frontend**

[![](https://skillicons.dev/icons?i=angular,react,nextjs,flutter,tailwind,sass,vite,electron&theme=dark)](https://skillicons.dev)

**Backend & Datos**

[![](https://skillicons.dev/icons?i=spring,nodejs,express,nestjs,laravel,dotnet,mongodb,mysql,postgres,sqlite,prisma&theme=dark)](https://skillicons.dev)

**DevOps & Observabilidad**

[![](https://skillicons.dev/icons?i=docker,githubactions,linux,raspberrypi,nginx,prometheus,grafana,cloudflare,vercel,git&theme=dark)](https://skillicons.dev)

**Testing & Calidad**

[![](https://skillicons.dev/icons?i=jest,vitest,maven,gradle,pnpm,postman&theme=dark)](https://skillicons.dev)

<details>
<summary><b>Ver el detalle por área</b> · <i>Full breakdown</i></summary>

<br/>

| Área | Tecnologías |
|---|---|
| **Seguridad / Auth** | Spring Security · JWT (`jjwt`, `jose`, `jsonwebtoken`) · OAuth2 *client · resource server · authorization server* · login social (Google) · authorities & roles · autorización a nivel de método (`@PreAuthorize`/`@PostAuthorize`) · filtros custom · CORS/CSRF · Helmet · rate limiting · cookies httpOnly · bcrypt |
| **Tiempo real** | Socket.IO (servidor Node + cliente Flutter `socket_io_client`) · salas y eventos autenticados por JWT |
| **APIs & contrato** | REST · OpenAPI/Swagger (`springdoc`, `zod-to-openapi`) · Zod · validación de esquema · versionado de protocolo con detección automática de *drift* |
| **Microservicios** | Spring Cloud Gateway · Eureka (service discovery) · Config Server · OpenFeign · Actuator |
| **Frontend** | Angular 17–19 (SSR, standalone) · Next.js 16 + React 19 · TanStack Query · React Hook Form · Radix UI · Tailwind v4 · Flutter (Riverpod, go_router, shaders GLSL, sensores) · Ionic + Capacitor · Electron |
| **Datos** | MongoDB/Mongoose · MySQL · PostgreSQL · SQLite · Prisma (migraciones versionadas) · Turso/libSQL · MinIO · AWS S3 · Cloudflare R2 |
| **Testing** | TDD · Jest · Vitest · Playwright (e2e) · Supertest · JUnit 5 · Mockito · `spring-security-test` · `mongodb-memory-server` · Karma/Jasmine · `flutter_test` · Husky (hooks pre-push) |
| **Integraciones** | Stripe (suscripciones + webhooks) · Google Gemini API · Nodemailer · i18n (`next-intl`) · generación y escaneo de QR |

</details>

---

## 🚀 Kromia — proyecto estrella

> **Un producto, cuatro repos, una única fuente de verdad.** Un SDK define el contrato; el studio web, la API y la app móvil lo consumen. Nada se reimplementa a mano — y el CI se encarga de que siga siendo cierto.
>
> <sub><i>One product, four repos, a single source of truth. An SDK owns the contract; the web studio, the API and the mobile app consume it — and CI enforces that they never drift apart.</i></sub>

| Repo | Rol | Stack |
|---|---|---|
| 🔒 **kromia-sdk** | Monorepo del contrato: core TS + **espejo Dart** + renderers React + servidor MCP + docs | `TypeScript` · `Dart` · `pnpm workspaces` |
| 🔒 **Kromia-Studio** | Editor visual de composiciones | `Next.js 16` · `React 19` · `Tailwind v4` |
| 🔒 **Kromia_NodeJS** | API REST + tiempo real + almacenamiento de objetos | `Express` · `MongoDB` · `Socket.IO` · `MinIO` |
| 🔒 **kromia-mobile** | App del coleccionista (render 3D, foil por shaders) | `Flutter` · `Riverpod` · `GLSL` |

**Lo que lo hace interesante — más allá del código:**

- 🍏 **Build de iOS sin Mac.** Un workflow en runner `macos-latest` compila el `.ipa`, clona el SDK privado con un PAT dedicado, inyecta la URL del backend por `--dart-define` y adjunta el binario a la Release.
- 🛡️ **Drift-CI en tres capas.** El contrato vive en TypeScript y se espeja en Dart. El CI compara versiones, ejecuta un *corpus* de tests cross-language y verifica paridad de API — si el espejo se desincroniza, **abre una issue en Jira automáticamente** y pone el check en rojo.
- 🗺️ **Documentación que no puede mentir.** Un test enumera el router real de Express y lo compara con el mapa de endpoints; si alguien añade una ruta sin documentarla, el PR se bloquea.
- 📚 **Docs versionadas** en MkDocs Material desplegadas a GitHub Pages desde Actions.

<sub>🔒 = repositorio privado (producto en desarrollo).</sub>

---

## ⚙️ Automatización, DevOps y monitoreo

### CI/CD — GitHub Actions

| Patrón | Dónde y para qué |
|---|---|
| **Builds ARM64 nativos** | Runners `ubuntu-24.04-arm` para compilar imágenes de Raspberry Pi sin emulación QEMU — de decenas de minutos (y cuelgues aleatorios) a minutos estables. |
| **Release-driven** | Solo los tags `vX.Y.Z` disparan build y publicación en **GHCR**; los push a `main` no gastan minutos. |
| **Cron de vigilancia** | Un workflow diario sondea los releases de una dependencia upstream y **solo reconstruye si hay versión nueva**, marcando la versión ya construida en el repo. |
| **Gates de calidad** | Drift-CI, verificación de documentación de API y tests como *checks* obligatorios de PR. |
| **Higiene** | `concurrency` para evitar solapes · `timeout-minutes` como red de seguridad · permisos mínimos por job · `workflow_dispatch` para builds manuales. |

### Despliegue e infraestructura — Raspberry Pi self-hosted

Modelo **pull-based**: el dispositivo nunca compila. CI publica la imagen en GHCR → **Watchtower** (uno solo por host, agnóstico y activado por etiqueta) detecta la nueva `:latest` y recrea el contenedor en ~5 min. `healthcheck` + `stop_grace_period` para redepliegues sin cortar peticiones en vuelo, tras proxy inverso.

### Observabilidad — Prometheus + Grafana

Exporter **Prometheus escrito a mano** en la propia aplicación (`GET /api/metrics`, formato de exposición estándar) con *gauges* y *counters* de negocio: tráfico, latencia media, visitantes únicos y activos, descargas y bytes servidos. Se combina con `node_exporter` para métricas de host y Loki + Promtail para logs, todo visualizado en **Grafana**. Acceso protegido por *bearer token* o restringido a LAN.

### Automatización de procesos · <sub>Business process automation</sub>

**Power Automate** · **Power Apps** · **SharePoint** — automatización de flujos y aplicaciones internas de negocio (formularios, aprobaciones e integración documental), fuera del ámbito de estos repositorios públicos.

---

## 🤖 IA agéntica

No solo *uso* asistentes: construyo la capa que los hace fiables.

- **Servidores MCP propios en tres lenguajes** — *Model Context Protocol* en **TypeScript** (expone el modelo de un SDK como *tools* deterministas, con transporte stdio y HTTP), en **C#** (`ModelContextProtocol` sobre .NET Generic Host) y en **Node** (CLI publicable). Con sus tests, no como demo.
- **Repos gobernados por agentes** — `AGENTS.md` / `CLAUDE.md` como contrato ejecutable: normas de TDD, versionado y límites de propiedad que el agente debe respetar.
- **Orquestación multi-agente** — protocolo de coordinación entre dos sesiones trabajando en paralelo sobre repos distintos: reparto de propiedad, canal de *handoff*, red anti-*drift* y seguimiento en Jira.
- **Skills reutilizables** — automatizaciones empaquetadas (`.claude/skills/`) para operar GitHub Projects desde el agente.
- **IA en producto** — integración de **Google Gemini** en backend, con caché, cuotas por usuario y auditoría de las respuestas generadas.

---

## 📊 GitHub

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=luishidalgoa&theme=tokyonight" alt="Resumen de perfil" width="98%" />

<br/>

<img height="190" src="https://streak-stats.demolab.com?user=luishidalgoa&locale=es&mode=daily&theme=tokyonight&hide_border=true&border_radius=8" alt="Racha de contribuciones" />
<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=luishidalgoa&theme=tokyonight" alt="Lenguajes más usados" />

<br/>

<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=luishidalgoa&theme=tokyonight" alt="Repos por lenguaje" />
<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=luishidalgoa&theme=tokyonight&utcOffset=2" alt="Horario productivo" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=luishidalgoa&theme=tokyo-night&hide_border=true&radius=8&area=true" alt="Gráfico de actividad" width="98%" />

</div>

<sub>ℹ️ Buena parte de mi trabajo reciente vive en repositorios privados, así que estas métricas reflejan solo la actividad pública.</sub>

---

## 🌱 Proyectos públicos destacados

| Proyecto | Qué es | Stack |
|---|---|---|
| [**GameHub**](https://github.com/luishidalgoa/GameHub) | Biblioteca autoalojada con escáner de ficheros, descargas firmadas, analítica y **exporter Prometheus** | `Next.js` · `Prisma` · `Docker` · `GHCR` |
| [**Ritmo**](https://github.com/luishidalgoa/Ritmo) | App de escritorio .NET con **servidor MCP** integrado y release automatizada | `C#` · `.NET` · `MCP` |
| [**shrink-studio**](https://github.com/luishidalgoa/shrink-studio) | Compresor de vídeo a HEVC: motor PowerShell + GUI e instalador | `C#/WPF` · `PowerShell` · `Inno Setup` |
| [**yt-subs**](https://github.com/luishidalgoa/Subscription-Artists-And-Automatic-download-music) | Suscripción a canales y descarga automática, desplegado en Pi vía GHCR + Watchtower | `Python` · `Docker` · `Actions` |
| [**Spring Microservices**](https://github.com/luishidalgoa/SpringBootMicroservice) | Gateway + Eureka + Config Server + servicios con OpenFeign | `Spring Cloud` · `Docker` |
| [**Project Management System**](https://github.com/luishidalgoa/Project_Management_System) | Gestor de proyectos colaborativo — proyecto con **Atmira** | `Angular` · `Spring Boot` · `JWT` |

---

## 📜 Certificaciones

- 🅰️ [**Angular: De cero a experto**](https://www.udemy.com/certificate/UC-b8661571-511d-4c4e-8b9e-eb7d5e52b964/) — Udemy
- 🌐 [**Aprende JavaScript, HTML5 y CSS3**](https://www.udemy.com/certificate/UC-90b6fd6c-5e30-49a3-9dc1-7b7fadc86d89/) — Udemy

---

<div align="center">

### 🤝 Hablemos · <sub>Let's talk</sub>

<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" height="34" alt="Email" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="34" alt="LinkedIn" /></a>
<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" height="34" alt="Portfolio" /></a>

<sub>📍 Córdoba, España — abierto a remoto</sub>

</div>
