# payloadcraft

**Offensive security, red team tooling, and honest benchmarks.** Writing by [d0mi33](https://github.com/d0mi33).

▸ **https://d0mi33.github.io/payloadcraft/**

> If it can't be reproduced, it's a story, not a writeup.

## What's here

| | |
|---|---|
| **[research](https://d0mi33.github.io/payloadcraft/research/)** | The **agent harness benchmark**: open-source harnesses run on the same repo, with the same model and the same time budget. Configs and raw output are published with each round. |
| | [One web request, attacked at every hop](https://d0mi33.github.io/payloadcraft/research/web-request-lifecycle/): DNS → TCP → TLS → HTTP → browser policy → cookies, with the attacks and defenses at each stage. |
| | [AWS for AppSec: a field guide](https://d0mi33.github.io/payloadcraft/research/aws-appsec-field-guide/): the AWS security catalogue, grouped by the job each service does, with worked scenarios. |
| **[blog](https://d0mi33.github.io/payloadcraft/blog/)** | Writeups with receipts: commands you can run, configs you can copy, results you can verify. |

Follow along via RSS: [`/blog/index.xml`](https://d0mi33.github.io/payloadcraft/blog/index.xml)

## The rules

1. Every post ships with something reproducible: a command, a config, or a result
2. Benchmarks publish their configs and raw output, not just the chart
3. No trackers, no analytics, no third-party requests

## Built with

Hugo and a hand-rolled "field manual" theme (Fraunces + IBM Plex Mono, self-hosted). There is no framework, and the only JavaScript is the dark-mode toggle. Every push deploys to GitHub Pages via Actions.

```bash
hugo server -D   # preview locally at http://localhost:1313
```

---

Found something wrong in a writeup? [Open an issue](https://github.com/d0mi33/payloadcraft/issues). Corrections are welcome and get credited.
