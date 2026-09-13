<div align="center">

<a href="https://niagalabs.com"><img src="assets/banner.svg" width="100%" alt="Niaga Labs, an independent software studio in Malaysia. Software for commerce. Tools for what's next. Product lines: Niaga Commerce, in development. Quant research, paper trading. Chain Analytics and the Chain trading tool, coming soon. Kilat Pet Delivery, later." /></a>

<a href="https://niagalabs.com"><img alt="Website: niagalabs.com" src="https://img.shields.io/badge/web-niagalabs.com-0B1F3A?style=flat-square" /></a>
<a href="mailto:hello@niagalabs.com"><img alt="Email: hello@niagalabs.com" src="https://img.shields.io/badge/email-hello%40niagalabs.com-0F8B8D?style=flat-square" /></a>
<img alt="Based in Malaysia" src="https://img.shields.io/badge/based%20in-Malaysia-0B1F3A?style=flat-square" />
<a href="https://github.com/MuhammadLuqman-99"><img alt="Founder: @MuhammadLuqman-99" src="https://img.shields.io/badge/founder-%40MuhammadLuqman--99-0F8B8D?style=flat-square&logo=github&logoColor=white" /></a>

### An independent software studio in Malaysia.

We build an e-commerce platform for our own store and a research platform that tests trading ideas on paper.<br />
More products follow, one at a time. Everything is designed, built and run in-house.

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg" />
  <img src="assets/stats-light.svg" width="100%" alt="By the numbers. 65 repositories in one organisation, 29 public and 8 archived. Niaga Commerce: 10 Go services and 3 Next.js apps, 17 PostgreSQL schemas in one database, Shopee and TikTok Shop live-capable with Lazada built. Quant research: 20 audited strategy trials, all kept on the record, and 0 promoted to real money." />
</picture>

<details>
<summary><b>Where these numbers come from</b></summary>
<br />

| Number | Source |
|---|---|
| 65 repositories, 29 public, 8 archived | `gh repo list niaga-labs`, 13 Sep 2026 |
| 10 Go services, 3 Next.js apps | the `niaga-labs-ecom-service-*` and `niaga-labs-ecom-frontend-*` repositories, and the [Niaga write-up](https://github.com/niaga-labs/niaga-labs-ecom-showcase) |
| 17 PostgreSQL schemas | `niaga-labs-ecom-infra-database` and the Niaga write-up |
| 2 + 1 marketplaces | Shopee and TikTok Shop sync is live-capable. Lazada is complete but proven against fixtures only (Niaga write-up) |
| 20 trials, 0 promoted | the [quant research notes](https://github.com/niaga-labs/niaga-labs-quant-showcase), section 7, as of 10 Sep 2026 |

</details>

## What we build

<a href="https://github.com/niaga-labs/niaga-labs-ecom-showcase"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-commerce-dark.svg" /><img src="assets/card-commerce-light.svg" width="49%" alt="Niaga Commerce. E-commerce platform, in development. A commerce platform that connects a storefront with catalogue, orders, payments and fulfilment. Our own dropship store is the starting point. Catalogue, orders, payments and refunds. Shopee and TikTok Shop sync. Multi-courier shipping and returns. Go, Next.js, PostgreSQL, NATS. Opens the architecture write-up." /></picture></a>
<a href="https://github.com/niaga-labs/niaga-labs-quant-showcase"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-quant-dark.svg" /><img src="assets/card-quant-light.svg" width="49%" alt="Quant research platform. Quantitative research, paper trading. Our own paper-trading platform for testing strategies. Every idea is judged the same way, and failures stay on the record. It is not a service. Pre-registered strategy specs. One shared walk-forward audit. Eleven-criterion promotion gate. Python, FastAPI, React, PostgreSQL. Opens the research notes." /></picture></a>

Click a card for its public write-up; the code itself stays private. The quant platform trades our own paper
book only. It is not a signal, subscription or trading service, and nothing on this page is investment advice.

### What comes next

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-chain-analytics-dark.svg" /><img src="assets/card-chain-analytics-light.svg" width="32%" alt="Chain Analytics. Robinhood Chain, coming soon. A dashboard for Robinhood Chain market activity. Read-only research is under way first." /></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-chain-tool-dark.svg" /><img src="assets/card-chain-tool-light.svg" width="32%" alt="Chain trading tool. Robinhood Chain, coming soon. A tool for traders on Robinhood Chain, planned once the dashboard has proven useful." /></picture>
<a href="https://github.com/orgs/niaga-labs/repositories?q=niaga-labs-pet&type=public"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-kilat-dark.svg" /><img src="assets/card-kilat-light.svg" width="32%" alt="Kilat Pet Delivery. Logistics, later. Booking and live tracking for pet transport. Paused while we focus on commerce. Opens its public repositories." /></picture></a>

Planned products, shown so you know where the studio is heading. No dates or prices yet.

## How it fits together

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#0B1F3A", "primaryTextColor": "#FFFFFF", "nodeTextColor": "#FFFFFF", "primaryBorderColor": "#0F8B8D", "lineColor": "#0F8B8D", "titleColor": "#0F8B8D", "textColor": "#0F8B8D"}}}%%
flowchart TB
    NL["<b>Niaga Labs</b><br/>software studio · Malaysia"]

    subgraph NOW["Building now"]
        COM["<b>Niaga Commerce</b><br/>e-commerce platform"]
        QNT["<b>Quant research</b><br/>our own paper book"]
    end

    subgraph NEXT["Next, one at a time"]
        CA["<b>Chain Analytics</b><br/>coming soon"]
        CT["<b>Chain trading tool</b><br/>coming soon"]
        KPD["<b>Kilat Pet Delivery</b><br/>later"]
    end

    subgraph PLAT["Shared platform"]
        STACK["<b>Dev stack</b><br/>one command"]
        CF["<b>Cloudflare</b><br/>site · email · backups"]
        FLOW["<b>Jira + GitHub</b><br/>ticket → merge"]
    end

    NL --> NOW
    NL -.-> NEXT
    NOW --> PLAT
    NEXT -.-> PLAT

    classDef root fill:#0F8B8D,stroke:#0F8B8D,color:#FFFFFF
    classDef soon fill:#12304F,stroke:#0F8B8D,stroke-dasharray:5 4,color:#D8E6F0
    classDef later fill:#1C2A3D,stroke:#6B7C90,stroke-dasharray:5 4,color:#B8C4D0
    class NL root
    class CA,CT soon
    class KPD later
    style NOW fill:none,stroke:#0F8B8D
    style NEXT fill:none,stroke:#6B7C90,stroke-dasharray:5 4
    style PLAT fill:none,stroke:#0F8B8D
```

## Inside Niaga Commerce

Ten Go services behind a Next.js storefront and admin, one PostgreSQL database with a schema per service, and
NATS JetStream for events. Built from 2023 to 2026 for a single online store, then generalised.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#0B1F3A", "primaryTextColor": "#FFFFFF", "nodeTextColor": "#FFFFFF", "primaryBorderColor": "#0F8B8D", "lineColor": "#0F8B8D", "titleColor": "#0F8B8D", "textColor": "#0F8B8D"}}}%%
flowchart LR
    subgraph CH["Sales channels"]
        direction TB
        SF["Storefront<br/>Next.js"]
        SH["Shopee"]
        TT["TikTok Shop"]
        LZ["Lazada<br/>built, not live"]
    end

    subgraph CORE["Ten Go services"]
        direction TB
        MKT["marketplace"]
        ORD["order<br/>cart · payments · shipping"]
        CAT["catalog"]
        INV["inventory"]
        RPT["reporting"]
        NOTIF["notification"]
        REST["auth · customer<br/>support · agent"]
    end

    ADM["Admin<br/>Next.js"]
    BUS(["NATS JetStream"])
    PG[("PostgreSQL 16<br/>17 schemas")]

    SF --> ORD
    SH --> MKT
    TT --> MKT
    LZ -.-> MKT
    MKT --> ORD
    ORD --> INV
    ORD --> CAT
    ORD --> BUS
    BUS --> NOTIF
    BUS --> RPT
    ADM --> CORE
    CORE --> PG

    classDef soon fill:#12304F,stroke:#0F8B8D,stroke-dasharray:5 4,color:#D8E6F0
    classDef infra fill:#0F8B8D,stroke:#0F8B8D,color:#FFFFFF
    class LZ soon
    class BUS,PG infra
    style CH fill:none,stroke:#0F8B8D
    style CORE fill:none,stroke:#0F8B8D
```

The full story is in the [Niaga write-up](https://github.com/niaga-labs/niaga-labs-ecom-showcase) and the
[platform document](https://github.com/niaga-labs/.github/blob/main/niaga-platform.md): every service, the order
flow, the database design and the patterns behind them.

## How we work

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#0B1F3A", "primaryTextColor": "#FFFFFF", "nodeTextColor": "#FFFFFF", "primaryBorderColor": "#0F8B8D", "lineColor": "#0F8B8D"}}}%%
flowchart LR
    T["<b>Jira ticket</b><br/>acceptance criteria"] --> B["<b>Branch</b><br/>named for the ticket"]
    B --> C["<b>Code + tests</b><br/>exact counts"]
    C --> R["<b>Review agent</b><br/>must approve"]
    R --> P["<b>Pull request</b><br/>CI runs"]
    P --> M["<b>Merge</b><br/>changelog · ticket done"]

    classDef done fill:#0F8B8D,stroke:#0F8B8D,color:#FFFFFF
    class M done
```

- **Ticket first.** Every change starts from a Jira ticket and lands on its own branch, named for it.
- **Green before it ships.** Tests pass before a commit, and the exact counts go into the pull request.
- **Reviewed, then merged.** A review agent checks the diff against the ticket's acceptance criteria and has to
  approve it before the merge.
- **Written down as it happens.** A changelog entry for every change and a lessons log for every surprise, so the
  reasoning is still there six months later.
- **Safe by default.** Hooks keep secrets out of every repository. Database backups are encrypted and
  restore-tested.
- **Built by a person, with AI in the toolkit.** ChatGPT and Claude help explore, build and review. A human sets
  the direction and owns every decision.

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=go,ts,nextjs,react,tailwind,python,fastapi,postgres,redis,kafka,docker,nginx,cloudflare,githubactions,swift&theme=dark&perline=15" />
  <img alt="Go, TypeScript, Next.js, React, Tailwind CSS, Python, FastAPI, PostgreSQL, Redis, Kafka, Docker, nginx, Cloudflare, GitHub Actions, Swift" src="https://skillicons.dev/icons?i=go,ts,nextjs,react,tailwind,python,fastapi,postgres,redis,kafka,docker,nginx,cloudflare,githubactions,swift&theme=light&perline=15" />
</picture>

| Layer | What we use |
|---|---|
| Services | Go 1.25 microservices · Python 3.12 with FastAPI |
| Front ends | Next.js · React · TypeScript · Tailwind · SwiftUI for the Kilat iOS apps |
| Data | PostgreSQL 16 with PostGIS · Redis · MinIO · Meilisearch |
| Messaging | NATS JetStream for Niaga · Kafka for Kilat |
| Platform | Docker Compose · nginx · GitHub Actions · Cloudflare Pages, DNS, Email Routing and R2 |

## Where the code lives

Every repository is named `niaga-labs-<product>-<name>`.

| Product code | Product | Repositories | Start here |
|---|---|---|---|
| `ecom` | Niaga Commerce | 21, 3 public | [write-up](https://github.com/niaga-labs/niaga-labs-ecom-showcase) · [`lib-common`](https://github.com/niaga-labs/niaga-labs-ecom-lib-common) · [`lib-ui`](https://github.com/niaga-labs/niaga-labs-ecom-lib-ui) |
| `quant` | Quant research platform | 2, 1 public | [research notes](https://github.com/niaga-labs/niaga-labs-quant-showcase) |
| `chain` | Chain Analytics and the Chain trading tool | 1, private | coming soon |
| `pet` | Kilat Pet Delivery | 30, 24 public | [public repositories](https://github.com/orgs/niaga-labs/repositories?q=niaga-labs-pet&type=public) |
| `platform` · `hq` | Shared dev stack · company site | 2, private | [niagalabs.com](https://niagalabs.com) |
| `crm` | Early CRM scaffolds | 8, archived | |

## Who

<img src="https://github.com/MuhammadLuqman-99.png?size=120" width="60" height="60" align="left" alt="" />

**Muhammad Luqman**, founder and engineer. Designs, builds and runs everything here.<br />
[GitHub](https://github.com/MuhammadLuqman-99) · [LinkedIn](https://www.linkedin.com/in/muhammad-luqman-b894a4337) · [hello@niagalabs.com](mailto:hello@niagalabs.com)

<br clear="left" />

<div align="center">
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/wordmark-white.svg" />
  <img src="assets/wordmark-navy.svg" height="34" alt="Niaga Labs" />
</picture>

<sub>© 2026 Niaga Labs · Malaysia · <a href="https://niagalabs.com">niagalabs.com</a></sub>
</div>
