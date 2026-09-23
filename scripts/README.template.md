<div align="center">

# Swapnil FDE Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**The ranked, practical guide to becoming — and succeeding as — a Forward Deployed Engineer (FDE).**

Every resource is scored on a public rubric and can be independently re-ranked by
[Jev](https://jev-ai.pro/) (TypeSafe AI's evaluation model). Plus field-tested templates,
an interview practice set, and a 90-day plan.

<sub>{{STATS}}</sub>

[Top 10](#-top-10--start-here) · [Playbooks](#playbooks--templates) · [Interview](#interview-practice-set) · [90-Day Plan](#90-day-learning-plan) · [Contribute](CONTRIBUTING.md)

</div>

---

## What is a Forward Deployed Engineer?

An FDE is a software engineer who works **embedded with a customer** rather than behind a product team.
The job is to take a platform — increasingly an AI/LLM platform — and make it deliver a measurable outcome
inside one organisation's messy reality: their data, their systems, their politics, their deadlines.
Then bring what you learned back so the product gets better for everyone.

Palantir pioneered the role (internally called *Delta*, versus *Dev* for product engineers). Since 2025 it has become
one of the most in-demand jobs in AI, with OpenAI, Anthropic, Ramp, Scale AI and hundreds of startups hiring.

| | Product SWE | Forward Deployed Engineer | Solutions Engineer / Consultant |
|---|---|---|---|
| **Serves** | Many customers via the product | One customer at a time, deeply | Pre-sales or advisory |
| **Writes production code** | Yes | **Yes — at the customer** | Rarely / demo code |
| **Success metric** | Adoption, reliability | **Customer outcome + learnings fed back to product** | Deal closed / report delivered |
| **Core extra skill** | Scale & architecture | **Decomposition, discovery, trust** | Communication |

{{RESOURCES}}

## Playbooks & Templates

Most lists stop at links. These are working documents you can copy into a real engagement.

| Template | Use it when |
|---|---|
| [Discovery Call Guide](playbooks/01-discovery-call.md) | First conversations with a new customer team |
| [Engagement Scoping Doc](playbooks/02-scoping-doc.md) | Turning a vague ask into a 2–6 week plan with success criteria |
| [Weekly Customer Update](playbooks/03-weekly-update.md) | Every Friday — keeps executives aligned and slips visible early |
| [AI Deployment Checklist](playbooks/04-ai-deployment-checklist.md) | Before an LLM feature touches real users or data |
| [Handover & Field Report](playbooks/05-handover-field-report.md) | End of an engagement — to the customer and back to product |

## Interview Practice Set

[`interview/practice-set.md`](interview/practice-set.md) — 40 questions across the seven rounds FDE loops use
(practical coding, deployment system design, decomposition case, client simulation, behavioural, AI-specific,
and "why FDE"), each with what the interviewer is really testing.

## 90-Day Learning Plan

A plan for a working software engineer. Adjust the pace to your background.

| Weeks | Focus | Do this | Proof you can show |
|---|---|---|---|
| 1–2 | **Understand the role** | Read the Top 10. Write a one-page note on which flavour of FDE (Palantir-style data, AI-lab, startup) you want. | Your note + a target list of 20 companies |
| 3–5 | **Applied AI core** | Anthropic's agent patterns, 12-Factor Agents, Hamel's evals. Build one agent with tool use and an eval set. | Public repo with evals and a README |
| 6–7 | **Data & integration** | SQL fluency, one dbt project, read EIP messaging chapters. Connect your agent to a real API and a database. | Same repo, now integrated with a real system |
| 8–9 | **Soft stack** | The Mom Test, Pyramid Principle. Run 3 discovery calls with real small businesses using the [Discovery Guide](playbooks/01-discovery-call.md). | 3 written scoping docs |
| 10–11 | **Ship for a real user** | Deliver one small deployment for one of those businesses. Write a field report. | A case study with a measured outcome |
| 12–13 | **Interview loop** | Work through the [practice set](interview/practice-set.md); do 2 mock client simulations. Apply. | Applications out with the case study attached |

## How Resources Are Ranked

Each resource gets five 1–5 scores. The weighted total becomes a 0–100 score:

| Criterion | Weight | Question |
|---|:-:|---|
| Relevance | 30% | How directly does it serve someone doing or pursuing FDE work? |
| Practicality | 25% | Does it give steps, templates, questions or code? |
| Depth | 20% | Real substance, or a shallow overview? |
| Authority | 15% | First-hand operator / primary source vs. secondhand summary? |
| Recency | 10% | Current for the 2025–26 AI-era role? |

**Tiers:** 🥇 Essential ≥ 80 · 🥈 Recommended 65–79 · 🥉 Useful < 65.

**Jev re-ranking.** [`scripts/rank_with_jev.py`](scripts/rank_with_jev.py) sends every resource to Jev
(TypeSafe AI's System One), which returns calibrated probability scores on the same rubric. The final score is then
50% human rubric + 50% Jev, so no single opinion decides the order. Details in [RANKING.md](RANKING.md).

```bash
pip install -r requirements.txt
export TYPESAFE_API_KEY=ts_...          # console.typesafe.ai/settings/keys
python scripts/rank_with_jev.py
python scripts/build_readme.py
```

## Contributing

Found something better? Open a PR that adds one entry to [`data/resources.yaml`](data/resources.yaml) with scores and a
one-line summary, then run `python scripts/build_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).
Links are checked automatically every week.

## Maintainer

Curated by **Swapnil Mandloi** — [Swapnil AI Labs](https://swapnilailabs.netlify.app), AI automation with n8n, Claude and Python.
If this helped you, a ⭐ helps others find it.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) — to the extent possible under law, the maintainer has waived all copyright to this list. Linked resources belong to their authors.
