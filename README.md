<!-- ══════════════════════ HEADER ══════════════════════ -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1200&color=7AA2F7&center=true&vCenter=true&width=620&lines=Luis+Hidalgo+%E2%80%94+Full-Stack+Engineer;Java+%C2%B7+TypeScript+%C2%B7+Flutter;From+API+contract+to+production" alt="Full-Stack Engineer · Java · TypeScript · Flutter" />

<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-7AA2F7?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="Email" /></a>
<img src="https://komarev.com/ghpvc/?username=luishidalgoa&label=Profile+views&color=7AA2F7&style=flat" alt="Profile views" />

</div>

---

I work across the stack, mostly Java and TypeScript, with Flutter on mobile. Right now I'm building **Kromia**: an SDK that owns a shared contract, plus the web studio, REST API and mobile app that consume it.

Alongside the product code I run the infrastructure it sits on. Authentication, WebSocket sync, GitHub Actions pipelines, and Docker deploys to a Raspberry Pi I maintain at home.

🔭 Building Kromia &nbsp;·&nbsp; 🤖 Writing MCP servers for AI agents &nbsp;·&nbsp; 📍 Córdoba, Spain, open to remote

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
| **Security / Auth** | Spring Security · JWT (`jjwt`, `jose`, `jsonwebtoken`) · OAuth2 *client · resource server · authorization server* · social login (Google) · authorities and roles · method-level authorization (`@PreAuthorize`/`@PostAuthorize`) · custom filters · CORS/CSRF · Helmet · rate limiting · httpOnly cookies · bcrypt |
| **Real-time** | Socket.IO (Node server and Flutter `socket_io_client`) · JWT-authenticated rooms and events |
| **APIs & contract** | REST · OpenAPI/Swagger (`springdoc`, `zod-to-openapi`) · Zod · schema validation · protocol versioning with automated drift detection |
| **Microservices** | Spring Cloud Gateway · Eureka service discovery · Config Server · OpenFeign · Actuator |
| **Frontend** | Angular 17–19 (SSR, standalone) · Next.js 16 + React 19 · TanStack Query · React Hook Form · Radix UI · Tailwind v4 · Flutter (Riverpod, go_router, GLSL shaders, sensors) · Ionic + Capacitor · Electron |
| **Data** | MongoDB/Mongoose · MySQL · PostgreSQL · SQLite · Prisma (versioned migrations) · Turso/libSQL · MinIO · AWS S3 · Cloudflare R2 |
| **Testing** | TDD · Jest · Vitest · Playwright (e2e) · Supertest · JUnit 5 · Mockito · `spring-security-test` · `mongodb-memory-server` · Karma/Jasmine · `flutter_test` · Husky pre-push hooks |
| **Integrations** | Stripe (subscriptions and webhooks) · Google Gemini API · Nodemailer · i18n (`next-intl`) · QR generation and scanning |

</details>

---

## 🚀 Kromia

One SDK owns the contract. The web studio, the API and the mobile app consume it, and CI checks that they stay in sync.

| Repo | Role | Stack |
|---|---|---|
| 🔒 **kromia-sdk** | Contract monorepo: TS core, Dart mirror, React renderers, MCP server, docs | `TypeScript` · `Dart` · `pnpm workspaces` |
| 🔒 **Kromia-Studio** | Visual composition editor | `Next.js 16` · `React 19` · `Tailwind v4` |
| 🔒 **Kromia_NodeJS** | REST API, real-time, object storage | `Express` · `MongoDB` · `Socket.IO` · `MinIO` |
| 🔒 **kromia-mobile** | Collector app with 3D rendering and shader-based foil | `Flutter` · `Riverpod` · `GLSL` |

Some of the pipeline work behind it:

- 🍏 **iOS builds on CI.** A `macos-latest` runner compiles the `.ipa`, clones the private SDK with a dedicated PAT, injects the backend URL through `--dart-define`, and attaches the binary to the Release.
- 🛡️ **Drift detection in three layers.** The contract lives in TypeScript and is mirrored in Dart. CI compares versions, runs a cross-language test corpus and checks API parity. When the mirror falls behind, it opens a Jira issue and fails the check.
- 🗺️ **Endpoint map tied to a test.** The test enumerates the Express router and diffs it against the documented map, so adding a route without documenting it fails the PR.
- 📚 **Versioned docs** built with MkDocs Material and deployed to GitHub Pages from Actions.

<sub>🔒 = private repository, product in development.</sub>

---

## ⚙️ Automation, DevOps & Monitoring

### CI/CD with GitHub Actions

| Pattern | Where and why |
|---|---|
| **Native ARM64 builds** | `ubuntu-24.04-arm` runners build the Raspberry Pi images without QEMU emulation, which used to hang at random and burn the full timeout. |
| **Release-driven** | Only `vX.Y.Z` tags trigger a build and a push to **GHCR**. Plain pushes to `main` don't spend minutes. |
| **Upstream watch cron** | A daily job polls an upstream dependency's releases and rebuilds only when a new version ships, checkpointing the last built version in the repo. |
| **Quality gates** | Drift detection, API documentation checks and tests all run as required PR checks. |
| **Hygiene** | `concurrency` to stop overlapping runs, `timeout-minutes` as a backstop, least-privilege permissions per job, `workflow_dispatch` for manual builds. |

### Deployment to a self-hosted Raspberry Pi

The Pi never compiles. CI pushes the image to GHCR, **Watchtower** notices the new `:latest` and recreates the container within about five minutes. One Watchtower per host, label-driven, so any project can opt in by adding a label. `healthcheck` and `stop_grace_period` keep redeploys from dropping in-flight requests behind the reverse proxy.

### Observability with Prometheus and Grafana

GameHub exposes `GET /api/metrics` in Prometheus text format, which I wrote by hand rather than pulling in a client library. It publishes traffic, average latency, unique and active visitors, downloads and bytes served. `node_exporter` covers host metrics, Loki and Promtail collect the logs, and Grafana reads all three. The endpoint needs a bearer token or a LAN address.

### Business process automation

**Power Automate**, **Power Apps** and **SharePoint** for internal workflows and apps: forms, approval flows and document integration. That work sits outside these public repositories.

---

## 🤖 Agentic AI

I write MCP servers so agents call my tools through a fixed schema instead of guessing at them.

- **MCP servers in three languages.** TypeScript, exposing an SDK's model as tools over both stdio and HTTP transports. C#, on the .NET Generic Host with the `ModelContextProtocol` package. Node, as a publishable CLI. Each one has its own test suite.
- **Agent rules committed to the repo.** `AGENTS.md` and `CLAUDE.md` set the TDD workflow, versioning policy and ownership boundaries an agent has to work within.
- **Multi-agent orchestration.** Two sessions run in parallel across separate repos, with a defined ownership split, a handoff channel and Jira tracking.
- **Packaged skills** in `.claude/skills/` for driving GitHub Projects.
- **Gemini in production**, with caching, per-user quotas and auditing of the generated output.

---

## 📊 GitHub

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=luishidalgoa&theme=tokyonight" alt="Profile summary" width="98%" />

<br/>

<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=luishidalgoa&theme=tokyonight" alt="Most used languages" />
<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=luishidalgoa&theme=tokyonight&utcOffset=2" alt="Commits by hour" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=luishidalgoa&theme=tokyo-night&hide_border=true&radius=8&area=true" alt="Activity graph" width="98%" />

</div>

<sub>ℹ️ Much of my recent work sits in private repositories, so these charts only cover public activity.</sub>

---

## 🌱 Selected public projects

| Project | What it is | Stack |
|---|---|---|
| [**GameHub**](https://github.com/luishidalgoa/GameHub) | Self-hosted library with a filesystem scanner, signed downloads, analytics and the Prometheus exporter above | `Next.js` · `Prisma` · `Docker` · `GHCR` |
| [**Ritmo**](https://github.com/luishidalgoa/Ritmo) | .NET desktop app with a built-in MCP server and automated releases | `C#` · `.NET` · `MCP` |
| [**shrink-studio**](https://github.com/luishidalgoa/shrink-studio) | HEVC video compressor: PowerShell engine, GUI and installer | `C#/WPF` · `PowerShell` · `Inno Setup` |
| [**yt-subs**](https://github.com/luishidalgoa/Subscription-Artists-And-Automatic-download-music) | Channel subscriptions and automatic downloads, deployed to the Pi through GHCR and Watchtower | `Python` · `Docker` · `Actions` |
| [**Spring Microservices**](https://github.com/luishidalgoa/SpringBootMicroservice) | Gateway, Eureka, Config Server and services wired with OpenFeign | `Spring Cloud` · `Docker` |
| [**Project Management System**](https://github.com/luishidalgoa/Project_Management_System) | Collaborative project manager, built with Atmira | `Angular` · `Spring Boot` · `JWT` |

---

## 🎓 Education & Certifications

**Education**

- **Higher Vocational Diploma in Multiplatform Application Development** (CFGS DAM) · IES Francisco de los Ríos, 2022–2024
- **Higher Vocational Diploma in Web Application Development** (CFGS DAW) · IES Francisco de los Ríos, 2024–2025
- **Vocational Diploma in Computer Systems and Networks** (CFGM SMR)

**Certifications**

- 🧠 **Programming for AI and Big Data in 5G Environments** · 150 h, official certificate, Junta de Andalucía / Vodafone 5G Plus · 2026
- 🌐 **Programming for IoT and Smart City Solutions in 5G Environments** · 150 h, official certificate, Junta de Andalucía / Vodafone 5G Plus · 2026
- 🟣 **Apache Kafka** · Academia DavinchiCoder · 2025
- 🔐 [**Spring Security 6: Zero to Master with JWT and OAuth2**](https://ude.my/UC-80427d30-2e7d-4645-82cd-23d567618789) · Udemy, Eazy Bytes · 2024
- 🅰️ [**Angular: De cero a experto**](https://www.udemy.com/certificate/UC-b8661571-511d-4c4e-8b9e-eb7d5e52b964/) · Udemy
- 🌐 [**JavaScript, HTML5 y CSS3**](https://www.udemy.com/certificate/UC-90b6fd6c-5e30-49a3-9dc1-7b7fadc86d89/) · Udemy

---

<div align="center">

### 🤝 Let's talk

<a href="mailto:luishidalgoa@outlook.es"><img src="https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" height="34" alt="Email" /></a>
<a href="https://www.linkedin.com/in/luis-hidalgo-aguilar-576463231/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="34" alt="LinkedIn" /></a>
<a href="https://portfolio.hdglabs.com/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" height="34" alt="Portfolio" /></a>

</div>
