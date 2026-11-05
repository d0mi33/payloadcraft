---
title: "Benchmarking agent harnesses: the methodology"
slug: harness-benchmark-methodology
date: 2026-10-26
track: harness benchmark
status: in progress
weight: 10
summary: "Which open-source agent harness finds real vulnerabilities, and which one just burns tokens. The rules, the metrics, the setup."
tags: ["benchmark", "ai-security", "agents"]
---
## The question

Which open-source agent harness actually finds vulnerabilities, and which one just burns tokens?

## Method (the rules I'm holding myself to)

1. **Same repo**: one reference codebase per round, split into known-good and known-bad code
2. **Same model**: one model, one version, temperature pinned
3. **Same clock**: a fixed wall-clock budget per harness
4. **Same hardware**: one runner, no "best of five"
5. **Published runs**: configs and raw output pushed to the repo

## What gets measured

- findings confirmed vs. false positives
- time to first finding
- wall-clock spend and token spend
- human intervention required (0 = fully autonomous)

## Harnesses in scope

The round 01 line-up is published alongside the first run, so every entry gets the same setup.

## Results

Round 01 is in progress. Configs and raw output will be published with the writeup.
