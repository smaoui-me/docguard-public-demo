# DocGuard integration demo

A small application for CI acceptance testing, not an independent benchmark.

Scenario branches: `scenario/stale`, `scenario/already-correct`, `scenario/missing-evidence`, `scenario/no-impact`. Open each against `main`. Application tests pass in all branches; documentation outcomes differ.

The missing-evidence scenario calls stdlib math.ceil and intentionally requires source unavailable in the repository. It should route to review without an AI request.

Read the DocGuard `docs/ci-benchmark-demo.md` guide before enabling publication. Never add an API key to this repository.
