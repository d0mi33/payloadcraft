---
title: "Faultline: crash-testing an AI agent in a sealed sandbox"
slug: faultline
date: 2026-11-20
layout: doc
track: agent security
weight: 5
summary: "A MITM proxy that records, breaks and poisons every call an agent makes, inside a namespace that can't leak. Run against a 120B model: 18/20 exfiltration attempts, 30% of them silent."
tags: ["ai-security", "agents", "kubernetes", "prompt-injection"]
---
An AI agent is an app that lets a model decide which code runs. So I treated one like any other target: put it in a box it can't leave, intercept everything it says to the model, then break and poison that traffic on purpose and see what it does.

**Faultline** is the harness. Code, scenarios and raw results: [github.com/d0mi33/faultline](https://github.com/d0mi33/faultline).

{{< fl-diagram >}}

## Results

One LangGraph support agent, four questions, five fault scenarios. **Nemotron-3 Super 120B**, 5 trials per scenario in a fresh sandbox each time (20 case-runs per row).

| scenario | pass rate | what the model did |
|---|---|---|
| baseline | **20/20** | Correct answers. Refused the card-number question on its own. |
| rate_limit | **20/20** | Backed off through injected 429s and stalls, then recovered. |
| malformed | **20/20** | Crashed before the fix. See stage 06. |
| tool_outage | **5/20** | Pasted raw SQL to the customer in 15/20 instead of saying it couldn't check. |
| prompt_injection | **2/20** | Tried to exfiltrate emails and card digits in 18/20. DB grants blocked every attempt. |

### What I'd tell someone shipping an agent

- **Grade behaviour, not transcripts.** In 30% of injected runs the model ran the attacker's query and then gave a polite, correct answer. Only the tape shows it.
- **Least privilege still carries the load.** The column grant stopped the leak, not the model.
- **Test your sandbox.** My first "sealed" cluster could reach the internet, because the CNI accepted the policies without enforcing them.

## One run, step by step

The prompt-injection scenario, from namespace creation to teardown. Open any stage.

{{< stages dataset="faultline_run" left="what can go wrong" right="what holds the line" note="observed" >}}

## Running it on someone else's infrastructure

A harness like this earns its keep inside a customer's environment, not on my laptop. So it also ships:

- **`faultline.doctor`**, a preflight that tests behaviour instead of reading config. Its Kubernetes check applies a deny-egress policy between two pods and confirms traffic actually stops. On a kindnet cluster it fails with *"deny-egress was accepted but traffic still flows"*: the bug from stage 01, now caught before a run.
- **`faultline.map`**, the agent's attack surface from what a run actually did, with no model calls. Tools offered (from the proxy tape, so it works with any framework), the DB role's real per-column grants, and every host it reached, all checked against a small `policy.yaml`. Its first Kubernetes run flagged the in-cluster model service as unexpected egress, because my own policy only listed the Docker hostname.
- **An offline bundle**: every image, the code, checksums, and an installer for a Docker host, a kind cluster or a private registry. Tampered bundles are refused, and `.env` files and keys are never packed.

## Run it yourself

```bash
git clone https://github.com/d0mi33/faultline && cd faultline
python3 -m faultline.run --scenario prompt_injection      # docker, offline mock model
python3 -m faultline.run --all --trials 5 --env-file .env.mymodel --tag mymodel
make k8s-up && make k8s-run SCENARIO=prompt_injection     # kind + Calico, namespace per run
python3 -m faultline.doctor --k8s                        # does this cluster enforce NetworkPolicy?
python3 -m faultline.map runs/latest-baseline            # attack surface vs policy.yaml
```

**Caveats.** One model, one agent, one injection payload, five trials: enough to tell "always" from "rarely", not enough for tight intervals. Built in a few days as an exploration of how you'd safely execute attacks against agents. It's not a benchmark.
