<div align="center">

# Niaga Labs

**Software for businesses that actually ship.**

A small studio in Malaysia building production systems end to end: the storefront, the services behind it,
and the infrastructure they run on.

[niagalabs.com](https://niagalabs.com) · [hello@niagalabs.com](mailto:hello@niagalabs.com)

</div>

---

## What we build

| Product | What it is | Status |
|---|---|---|
| **Niaga** | E-commerce platform: storefront, admin panel, Shopee and TikTok Shop sync, orders, multi-courier shipping, returns and refunds. It is being pointed at our own factory-direct dropship store first. | **Active.** Runs end to end on a local stack; not in production yet. [Full architecture →](https://github.com/niaga-labs/.github/blob/main/niaga-platform.md) |
| **Kilat Pet Delivery** | Pet transport: owners book a runner, track the trip live and pay into escrow; pet shops sell as merchants. | **On hold.** |
| **niagalabs.com** | The company site. | **Live** on Cloudflare Pages. |
| Research | Internal quantitative and on-chain research. | Private. Not a product. |

## How the work is organised

- **One organisation, one naming rule.** Every repository here is `niaga-labs-<product>-<name>`, with the
  product codes `ecom`, `pet`, `quant`, `platform`, `hq` and `chain`. Niaga's repositories still carry their
  short names (`service-order`, `frontend-admin`, …) until their rename.
- **Stack:** Go microservices · Next.js / TypeScript · PostgreSQL and PostGIS · NATS and Kafka · Docker · Cloudflare.
- **Every change starts from a ticket.** It goes on its own branch and through a review gate, and CI builds
  the services on every push. Backups are encrypted and restore-tested.
- **Built by one engineer, with an AI-assisted workflow he designed.** Claude Code runs with custom skills,
  hooks and review agents, and a human owns every decision.

## Who

**Muhammad Luqman**: founder and engineer, Malaysia. Designs, builds and runs everything here.
[@MuhammadLuqman-99](https://github.com/MuhammadLuqman-99)
