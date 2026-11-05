---
title: "Hello, world. Again."
slug: hello-world
date: 2026-10-26
draft: false
tags: ["meta", "recon"]
---
Every security blog starts the same way: "I wanted a place to dump my notes." This one starts the same way, but with a rule attached — nothing goes up here that I haven't actually run.

## What to expect

- **Writeups** — reproducible steps, actual commands, the parts the vendor advisory left out
- **Benchmarks** — same repo, same model, same clock: open-source agent harnesses against each other
- **Tooling** — the small scripts that save an hour during an engagement
- **Opinions** — clearly labeled as such

## The bar for posts

> If it can't be reproduced, it's a story, not a writeup.

Every post here should have at least one of: a command you can run, a config you can copy, or a result you can verify. Otherwise it belongs on social media, where unverifiable claims go to thrive.

## First command on every engagement

Before scanning anything, check where it actually points. Scope is a list of names; what you're allowed to touch is wherever those names resolve.

```bash
# confirm what a scoped name resolves to before you scan it
dig +short target.example A
dig +short www.target.example CNAME
```

A CNAME pointing at a deprovisioned cloud resource is a finding in its own right (subdomain takeover). An A record pointing outside the client's IP ranges means stop and ask.
