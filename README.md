<!-- ══════════════════════ HEADER ══════════════════════ -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1200&color=7AA2F7&center=true&vCenter=true&width=620&lines=Luis+Hidalgo+%E2%80%94+Full-Stack+Engineer;Java+%C2%B7+TypeScript+%C2%B7+Flutter;From+API+contract+to+production" alt="Full-Stack Engineer · Java · TypeScript · Flutter" />

<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-7AA2F7?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="Email" /></a>
<img src="https://komarev.com/ghpvc/?username=luishidalgoa&label=Profile+views&color=7AA2F7&style=flat" alt="Profile views" />

</div>

---

I build **multi-repo products and the machinery that keeps them coherent** — a contract-first SDK feeding a web studio, a REST API and a Flutter app, with CI that fails the build the moment they drift apart.

Most of my time goes to the parts that are easy to skip: hardened authentication, real-time that behaves on both ends of the wire, pull-based deploys onto self-hosted hardware, and metrics you can actually alert on.

🔭 Currently building **Kromia** &nbsp;·&nbsp; 🤖 Writing **MCP servers** so AI agents can drive my own tooling &nbsp;·&nbsp; 📍 Córdoba, Spain — open to remote

---

## 🧰 Stack

**Languages**

[![](https://skillicons.dev/icons?i=ts,java,dart,cs,py,php,js,bash&theme=dark)](https://skillicons.dev)

**Frontend**

[![](https://skillicons.dev/icons?i=angular,react,nextjs,flutter,tailwind,sass,vite,electron&theme=dark)](https://skillicons.dev)

**Backend & Data**

[![](https://skillicons.dev/icons?i=spring,nodejs,express,nestjs,laravel,dotnet,mongodb,mysql,postgres,sqlite,prisma&theme=dark)](https://skillicons.dev)

**DevOps & Observability**

[![](https://skillicons.dev/icons?i=docker,githubactions,linux,raspberrypi,nginx,prometheus,grafana,cloudflare,vercel,git&theme=dark)](https://skillicons.dev)

**Testing & Quality**

[![](https://skillicons.dev/icons?i=jest,vitest,maven,gradle,pnpm,postman&theme=dark)](https://skillicons.dev)

<details>
<summary><b>Full breakdown by area</b></summary>

<br/>

| Area | Technologies |
|---|---|
| **Security / Auth** | Spring Security · JWT (`jjwt`, `jose`, `jsonwebtoken`) · OAuth2 *client · resource server · authorization server* · social login (Google) · authorities & roles · method-level authorization (`@PreAuthorize`/`@PostAuthorize`) · custom filters · CORS/CSRF · Helmet · rate limiting · httpOnly cookies · bcrypt |
| **Real-time** | Socket.IO (Node server + Flutter `socket_io_client`) · JWT-authenticated rooms and events |
| **APIs & contract** | REST · OpenAPI/Swagger (`springdoc`, `zod-to-openapi`) · Zod · schema validation · protocol versioning with automated drift detection |
| **Microservices** | Spring Cloud Gateway · Eureka service discovery · Config Server · OpenFeign · Actuator |
| **Frontend** | Angular 17–19 (SSR, standalone) · Next.js 16 + React 19 · TanStack Query · React Hook Form · Radix UI · Tailwind v4 · Flutter (Riverpod, go_router, GLSL shaders, sensors) · Ionic + Capacitor · Electron |
| **Data** | MongoDB/Mongoose · MySQL · PostgreSQL · SQLite · Prisma (versioned migrations) · Turso/libSQL · MinIO · AWS S3 · Cloudflare R2 |
| **Testing** | TDD · Jest · Vitest · Playwright (e2e) · Supertest · JUnit 5 · Mockito · `spring-security-test` · `mongodb-memory-server` · Karma/Jasmine · `flutter_test` · Husky pre-push hooks |
| **Integrations** | Stripe (subscriptions + webhooks) · Google Gemini API · Nodemailer · i18n (`next-intl`) · QR generation and scanning |

</details>

---

## 🚀 Kromia — flagship project

> **One product, four repos, a single source of truth.** An SDK owns the contract; the web studio, the API and the mobile app consume it. Nothing is reimplemented by hand — and CI enforces that it stays that way.

| Repo | Role | Stack |
|---|---|---|
| 🔒 **kromia-sdk** | Contract monorepo: TS core + **Dart mirror** + React renderers + MCP server + docs | `TypeScript` · `Dart` · `pnpm workspaces` |
| 🔒 **Kromia-Studio** | Visual composition editor | `Next.js 16` · `React 19` · `Tailwind v4` |
| 🔒 **Kromia_NodeJS** | REST API + real-time + object storage | `Express` · `MongoDB` · `Socket.IO` · `MinIO` |
| 🔒 **kromia-mobile** | Collector app (3D rendering, shader-based foil) | `Flutter` · `Riverpod` · `GLSL` |

**What makes it interesting — beyond the code:**

- 🍏 **iOS builds without a Mac.** A workflow on a `macos-latest` runner compiles the `.ipa`, clones the private SDK with a dedicated PAT, injects the backend URL via `--dart-define`, and attaches the binary to the Release.
- 🛡️ **Three-layer drift CI.** The contract lives in TypeScript and is mirrored in Dart. CI compares versions, runs a cross-language test corpus, and verifies API parity — if the mirror falls out of sync it **opens a Jira issue automatically** and turns the check red.
- 🗺️ **Documentation that can't lie.** A test enumerates the real Express router and diffs it against the endpoint map; add a route without documenting it and the PR is blocked.
- 📚 **Versioned docs** built with MkDocs Material and deployed to GitHub Pages from Actions.

<sub>🔒 = private repository (product in development).</sub>

---

## ⚙️ Automation, DevOps & Monitoring

### CI/CD — GitHub Actions

| Pattern | Where and why |
|---|---|
| **Native ARM64 builds** | `ubuntu-24.04-arm` runners build Raspberry Pi images without QEMU emulation — from tens of minutes (and random hangs) down to stable minutes. |
| **Release-driven** | Only `vX.Y.Z` tags trigger a build and push to **GHCR**; plain pushes to `main` don't burn minutes. |
| **Upstream watch cron** | A daily workflow polls an upstream dependency's releases and **rebuilds only when a new version ships**, checkpointing the last built version in the repo. |
| **Quality gates** | Drift CI, API documentation verification and tests as required PR checks. |
| **Hygiene** | `concurrency` to prevent overlapping runs · `timeout-minutes` as a safety net · least-privilege permissions per job · `workflow_dispatch` for manual builds. |

### Deployment — self-hosted Raspberry Pi

**Pull-based** model: the device never compiles. CI publishes the image to GHCR → **Watchtower** (one per host, project-agnostic, label-driven) detects the new `:latest` and recreates the container within ~5 minutes. `healthcheck` plus `stop_grace_period` keep redeploys from cutting off in-flight requests, behind a reverse proxy.

### Observability — Prometheus + Grafana

A **hand-written Prometheus exporter** inside the application itself (`GET /api/metrics`, standard text exposition format) publishing business gauges and counters: traffic, average latency, unique and active visitors, downloads and bytes served. Paired with `node_exporter` for host metrics and Loki + Promtail for logs, all visualized in **Grafana**. Access is guarded by bearer token or restricted to LAN.

### Business process automation

**Power Automate** · **Power Apps** · **SharePoint** — internal workflow and app automation (forms, approval flows, document integration), outside the scope of these public repositories.

---

## 🤖 Agentic AI

I don't just *use* assistants — I build the layer that makes them dependable.

- **Custom MCP servers in three languages** — Model Context Protocol in **TypeScript** (exposing an SDK's model as deterministic tools over both stdio and HTTP transports), **C#** (`ModelContextProtocol` on the .NET Generic Host) and **Node** (publishable CLI). With test suites, not as demos.
- **Agent-governed repositories** — `AGENTS.md` / `CLAUDE.md` as an executable contract: TDD rules, versioning policy and ownership boundaries the agent has to respect.
- **Multi-agent orchestration** — a coordination protocol between two sessions working in parallel across separate repos: ownership split, handoff channel, anti-drift safety net and Jira tracking.
- **Reusable skills** — packaged automations (`.claude/skills/`) for driving GitHub Projects from the agent.
- **AI in production** — Google Gemini integrated into a backend with caching, per-user quotas and auditing of generated output.

---

## 📊 GitHub

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=luishidalgoa&theme=tokyonight" alt="Profile summary" width="98%" />

<br/>

<img height="190" src="https://streak-stats.demolab.com?user=luishidalgoa&mode=daily&theme=tokyonight&hide_border=true&border_radius=8" alt="Contribution streak" />
<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=luishidalgoa&theme=tokyonight" alt="Most used languages" />

<br/>

<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=luishidalgoa&theme=tokyonight" alt="Repos per language" />
<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=luishidalgoa&theme=tokyonight&utcOffset=2" alt="Productive time" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=luishidalgoa&theme=tokyo-night&hide_border=true&radius=8&area=true" alt="Activity graph" width="98%" />

</div>

<sub>ℹ️ A good share of my recent work lives in private repositories, so these charts reflect public activity only.</sub>

---

## 🌱 Selected public projects

| Project | What it is | Stack |
|---|---|---|
| [**GameHub**](https://github.com/luishidalgoa/GameHub) | Self-hosted library with a filesystem scanner, signed downloads, analytics and a **Prometheus exporter** | `Next.js` · `Prisma` · `Docker` · `GHCR` |
| [**Ritmo**](https://github.com/luishidalgoa/Ritmo) | .NET desktop app with a built-in **MCP server** and automated releases | `C#` · `.NET` · `MCP` |
| [**shrink-studio**](https://github.com/luishidalgoa/shrink-studio) | HEVC video compressor: PowerShell engine plus GUI and installer | `C#/WPF` · `PowerShell` · `Inno Setup` |
| [**yt-subs**](https://github.com/luishidalgoa/Subscription-Artists-And-Automatic-download-music) | Channel subscription and automatic downloads, deployed to a Pi via GHCR + Watchtower | `Python` · `Docker` · `Actions` |
| [**Spring Microservices**](https://github.com/luishidalgoa/SpringBootMicroservice) | Gateway + Eureka + Config Server + services wired with OpenFeign | `Spring Cloud` · `Docker` |
| [**Project Management System**](https://github.com/luishidalgoa/Project_Management_System) | Collaborative project manager — built with **Atmira** | `Angular` · `Spring Boot` · `JWT` |

---

## 📜 Certifications

- 🅰️ [**Angular: De cero a experto**](https://www.udemy.com/certificate/UC-b8661571-511d-4c4e-8b9e-eb7d5e52b964/) — Udemy
- 🌐 [**Aprende JavaScript, HTML5 y CSS3**](https://www.udemy.com/certificate/UC-90b6fd6c-5e30-49a3-9dc1-7b7fadc86d89/) — Udemy

---

<div align="center">

### 🤝 Let's talk

<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" height="34" alt="Email" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="34" alt="LinkedIn" /></a>
<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" height="34" alt="Portfolio" /></a>

</div>
