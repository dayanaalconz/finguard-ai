# Architecture notes

FinGuard AI is planned as a modular Python ML core, a FastAPI service, and a React/TypeScript web client.

## Initial development order

1. Select and document a dataset with clear redistribution terms.
2. Build a leakage-safe baseline with reproducible evaluation.
3. Serve one transaction risk score through an API.
4. Replay synthetic or public transactions locally.
5. Visualize scores and account relationships in the browser.

**Graph caveat:** Connections must be present in source data or explicitly simulated and labeled as such.

**Operational caveat:** Live means replayed events in the demo, not access to a bank or live financial network.

No external services, message brokers, databases or GPU are required for the first milestone.
