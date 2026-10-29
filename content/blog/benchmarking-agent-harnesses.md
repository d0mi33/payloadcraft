---
title: "Benchmarking agent harnesses: the methodology"
slug: harness-benchmark-methodology
date: 2026-10-26
draft: true
tags: ["benchmark", "ai-security", "wip"]
---
<!-- 🚧 DRAFT — `draft: true` means this will NOT appear on the live site.
     Flip it to `draft: false` (or delete this line) when it's ready. -->

## The question

Which open-source agent harness actually finds vulnerabilities — and which one just burns tokens?

## Method (the rules I'm holding myself to)

1. **Same repo** — one reference codebase per round, with known-good known-bad splits
2. **Same model** — one model, one version, temperature pinned
3. **Same clock** — fixed wall-clock budget per harness
4. **Same hardware** — one runner, no "best of five"
5. **Published runs** — configs and raw output pushed to the repo

## What gets measured

- findings confirmed / false positives
- time to first finding
- wall-clock spend and token spend
- human intervention required (0 = fully autonomous)

## Harnesses in scope

- [ ] harness A — *(add links as you evaluate)*
- [ ] harness B
- [ ] harness C

## Results

Pending first run. Configs will live at `/benchmark/` in the repo.
