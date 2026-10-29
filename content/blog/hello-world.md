---
title: "Hello, world. Again."
slug: hello-world
date: 2026-10-26
draft: false
tags: ["meta", "starter"]
---
<!-- 👋 This is your starter post — edit or delete it freely.
     New posts: run `hugo new content blog/my-post.md` and flip draft to false. -->

Every security blog starts the same way: "I wanted a place to dump my notes." This one starts the same way, but with a rule attached — nothing goes up here that I haven't actually run.

## What to expect

- **Writeups** — reproducible steps, actual commands, the parts the vendor advisory left out
- **Benchmarks** — same repo, same model, same clock: open-source agent harnesses against each other
- **Tooling** — the small scripts that save an hour during an engagement
- **Opinions** — clearly labeled as such

## The bar for posts

> If it can't be reproduced, it's a story, not a writeup.

Every post here should have at least one of: a command you can run, a config you can copy, or a result you can verify. Otherwise it belongs on social media, where unverifiable claims go to thrive.

## Sample code block

Because every blog post needs one:

```bash
# check where your subdomains actually point before you scan them
dig +short payloadcraft.com A
dig +short www.payloadcraft.com CNAME
```

That's it. The real posts start next. `draft: false` is the only gatekeeping here.
