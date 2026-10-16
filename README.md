# FinGuard AI

**Fraud Detection & Graph Intelligence Platform**

FinGuard AI is an educational, portfolio-focused financial fraud investigation platform. The goal is to combine reproducible machine learning, simulated transaction scoring, graph analytics, explainability, and an interactive web interface.

> **Status:** Project foundation — no trained model, live scoring, or deployed dashboard yet.

## Planned experience

1. **Command Center:** fraud alerts and model performance.
2. **Live Transactions:** replay public or synthetic transactions and score them.
3. **Graph Explorer:** investigate connected accounts and suspicious clusters.
4. **AI Investigator:** inspect predictions and feature contributions.
5. **Decision Lab:** compare review/block thresholds under explicit cost assumptions.

## Architecture (planned)

- **ML core:** Python, scikit-learn baseline, LightGBM candidate.
- **API:** FastAPI.
- **Web:** React + TypeScript; Cytoscape.js for interactive networks.
- **Simulation:** local event replay first; a message broker only if justified.
- **Quality:** pytest, Ruff, CI, documented evaluation and data provenance.

## Development principles

- Only publicly licensed or synthetic datasets; no employer data, code, or credentials.
- Start with an end-to-end vertical slice before adding infrastructure.
- Prevent leakage; use time-aware evaluation when transaction timestamps permit.
- Never present simulated events as actual financial activity.
- Never claim production readiness or performance metrics without evidence.

## Roadmap

- [ ] **Phase 0:** Repository foundation, dataset assessment, environment and CI.
- [ ] **Phase 1:** Data pipeline, baseline model and evaluation.
- [ ] **Phase 2:** Scoring API and local transaction replay.
- [ ] **Phase 3:** Interactive web dashboard and graph explorer.
- [ ] **Phase 4:** Explainability, decision analysis, monitoring and demo.

## Getting started

The repository is being scaffolded. Setup instructions will be added once the first executable slice is implemented.

## License and data

No license has been selected yet. Dataset sources and redistribution terms will be documented before any data is committed.
