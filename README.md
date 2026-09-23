<div align="center">

# Swapnil FDE Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**The ranked, practical guide to becoming — and succeeding as — a Forward Deployed Engineer (FDE).**

Every resource is scored on a public rubric and can be independently re-ranked by
[Jev](https://jev-ai.pro/) (TypeSafe AI's evaluation model). Plus field-tested templates,
an interview practice set, and a 90-day plan.

<sub>47 resources · 9 categories · ranking: transparent rubric (Jev re-rank ready)</sub>

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

## 🏆 Top 10 — Start Here

If you read nothing else, read these, in this order.

| # | Resource | Why it matters | Score |
|:-:|---|---|:-:|
| 1 | [The Rise of the Forward Deployed Engineer — and How To Do the Job Right](https://www.latent.space/p/forward-deployed-engineer-best-practices)<br><sub>Vinoo Ganesh (Latent Space) · 2026</sub> | Operator playbook: map the customer's 'nouns and verbs', report to product not sales, and treat an engagement that changes nothing upstream as a failure. | **100** |
| 2 | [Forward Deployed Engineer Interview: The Definitive 2026 Guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde)<br><sub>Aced (formerly Exponent) · 2026</sub> | The most complete round-by-round map: recruiter, HM, practical coding, system design, decomposition case, client simulation, behavioural. | **96** |
| 3 | [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)<br><sub>Anthropic · 2024</sub> | Workflows vs. agents, and five composable patterns (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser). Start simple. | **90** |
| 4 | [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)<br><sub>Hamel Husain · 2024</sub> | Why unit tests, human review and LLM-as-judge are the backbone of shipping AI to customers. Evals are how FDEs prove ROI. | **88** |
| 5 | [What We Learned from a Year of Building with LLMs](https://applied-llms.org/)<br><sub>Yan, Bischof, Frye, Husain, Liu, Shankar · 2024</sub> | Tactical, operational and strategic lessons from six practitioners — the closest thing to a field manual for applied LLM work. | **88** |
| 6 | [Model Context Protocol — documentation](https://modelcontextprotocol.io/)<br><sub>MCP project · 2026</sub> | The standard way to connect models to a customer's tools and data. Increasingly expected knowledge in FDE loops. | **88** |
| 7 | [Palantir Learning (Foundry & AIP)](https://learn.palantir.com/)<br><sub>Palantir · 2026</sub> | Free official training on ontology, pipelines and AIP — the platform most FDSEs deploy. | **88** |
| 8 | [12-Factor Agents](https://github.com/humanlayer/12-factor-agents)<br><sub>HumanLayer (Dex Horthy) · 2025</sub> | Principles for LLM software that is reliable enough to hand to production customers — own your prompts, context and control flow. | **86** |
| 9 | [What are Forward Deployed Engineers, and why are they so in demand?](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)<br><sub>Gergely Orosz (The Pragmatic Engineer) · 2025</sub> | The best single overview: what FDEs do, how OpenAI, Ramp and Palantir structure the teams, and how the role differs from solutions architects. Partly paywalled. | **85** |
| 10 | [Forward Deployed Engineer Interview Guide 2026: Complete Prep](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)<br><sub>Sundeep Teki · 2026</sub> | Prep plan with an AI-lab slant — how OpenAI/Anthropic-style FDE loops differ from Palantir's. | **81** |

## Contents

- [1. Understand the Role](#1-understand-the-role)
- [2. Why FDEs Are in Demand Now](#2-why-fdes-are-in-demand-now)
- [3. Doing the Job Well](#3-doing-the-job-well)
- [4. Interview Preparation](#4-interview-preparation)
- [5. Technical Stack: Applied AI](#5-technical-stack-applied-ai)
- [6. Technical Stack: Data, Systems & Integration](#6-technical-stack-data-systems--integration)
- [7. The Soft Stack: Discovery, Communication, Consulting](#7-the-soft-stack-discovery-communication-consulting)
- [8. Roadmaps & Other Curated Lists](#8-roadmaps--other-curated-lists)
- [9. Jobs, Market Data & Compensation](#9-jobs-market-data--compensation)
- [Playbooks & Templates](#playbooks--templates)
- [Interview Practice Set](#interview-practice-set)
- [90-Day Learning Plan](#90-day-learning-plan)
- [How Resources Are Ranked](#how-resources-are-ranked)

## 1. Understand the Role

_What an FDE is, where the role came from, and how it differs from SWE, solutions engineering and consulting._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 📰 [What are Forward Deployed Engineers, and why are they so in demand?](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)<br><sub>Gergely Orosz (The Pragmatic Engineer) · 2025 · 🥇 Essential</sub> | The best single overview: what FDEs do, how OpenAI, Ramp and Palantir structure the teams, and how the role differs from solutions architects. Partly paywalled. | 85 |
| 2 | 📄 [Dev versus Delta: Demystifying engineering roles at Palantir](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)<br><sub>Palantir · 2019 · 🥈 Recommended</sub> | The original definition. Devs build the platform for many customers; Deltas (FDSEs) deploy it to deliver outcomes for one — decomposition, autonomy and user empathy are the core skills. | 75 |
| 3 | 📄 [WTF is a forward deployed engineer? (and why everyone is hiring them)](https://posthog.com/blog/forward-deployed-engineer)<br><sub>Jina Yoon (PostHog) · 2026 · 🥈 Recommended</sub> | Plain-English explainer; notes FDEs spend roughly 60-80% of their time with customers and optimise for depth over generality. | 74 |
| 4 | 📄 [A Day in the Life of a Palantir Forward Deployed Software Engineer](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1)<br><sub>Palantir · 2020 · 🥈 Recommended</sub> | Hour-by-hour view of an FDSE's day on a customer site — useful to test whether the rhythm of the job suits you. | 70 |
| 5 | ✍️ [Reflections on Palantir](https://nabeelqu.co/reflections-on-palantir)<br><sub>Nabeel S. Qureshi · 2024 · 🥈 Recommended</sub> | Eight years inside Palantir. The best first-hand account of the culture that invented forward deployment and why it worked. | 69 |
| 6 | 🔖 [Forward Deployed Engineer (Wikipedia)](https://en.wikipedia.org/wiki/Forward_Deployed_Engineer)<br><sub>Wikipedia · 2026 · 🥉 Useful</sub> | Neutral reference for history and terminology (FDE, FDSE, Delta, deployment strategist). | 42 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 2. Why FDEs Are in Demand Now

_The business case: why AI companies trade margin for moat and hire FDEs at scale._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 🎥 [Head of Forward Deployed Engineering at OpenAI: Trust. Product. Impact.](https://www.youtube.com/watch?v=cBD7_R-Cizg)<br><sub>Colin Jarvis (OpenAI) · 2025 · 🥈 Recommended</sub> | The leader of OpenAI's FDE function on how the team gets customers to production and what it looks for. | 75 |
| 2 | ✍️ [Trading Margin for Moat: Why the Forward Deployed Engineer Is the Hottest Job in Startups](https://a16z.com/services-led-growth/)<br><sub>Joe Schmidt (a16z) · 2025 · 🥈 Recommended</sub> | The investor thesis: services-led growth beats pure PLG for enterprise AI, because the team that implements owns the data layer. | 74 |
| 3 | ✍️ [Forward Deployed Engineers](https://www.svpg.com/forward-deployed-engineers/)<br><sub>Marty Cagan (SVPG) · 2025 · 🥈 Recommended</sub> | Product-management view: FDEs are a discovery engine. Learn across many customers, then feed one product — accelerated by AI prototyping. | 68 |
| 4 | 📄 [Why OpenAI and Anthropic are hiring forward deployed engineer teams](https://thenewstack.io/forward-deployed-engineers-ai/)<br><sub>The New Stack · 2025 · 🥉 Useful</sub> | How frontier labs use FDEs to get enterprise LLM projects from pilot to production. | 61 |
| 5 | 🗞️ [Forward-deployed engineers are the AI industry's latest talent obsession](https://techcrunch.com/2026/07/30/forward-deployed-engineers-are-the-ai-industrys-latest-talent-obsession/)<br><sub>TechCrunch · 2026 · 🥉 Useful</sub> | Market numbers: share of companies planning to hire FDEs jumped from 5-10% to about 70% in the first half of 2026. | 49 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 3. Doing the Job Well

_Operator writing on how good FDEs actually work in the field._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | ✍️ [The Rise of the Forward Deployed Engineer — and How To Do the Job Right](https://www.latent.space/p/forward-deployed-engineer-best-practices)<br><sub>Vinoo Ganesh (Latent Space) · 2026 · 🥇 Essential</sub> | Operator playbook: map the customer's 'nouns and verbs', report to product not sales, and treat an engagement that changes nothing upstream as a failure. | 100 |
| 2 | 🔬 [Forward Deployed Engineering: Bringing Enterprise LLM Applications to Production](https://www.zenml.io/llmops-database/forward-deployed-engineering-bringing-enterprise-llm-applications-to-production)<br><sub>ZenML LLMOps Database (OpenAI case) · 2025 · 🥈 Recommended</sub> | How OpenAI's FDE team runs engagements: domain depth, eval-driven development, AI plus deterministic code — and how field work became products like the Agents SDK. | 79 |
| 3 | 📰 [Inside OpenAI's Forward Deployed Engineer Role](https://newsletter.eng-leadership.com/p/inside-openais-forward-deployed-engineer)<br><sub>Engineering Leadership newsletter · 2025 · 🥈 Recommended</sub> | Interview-style breakdown of day-to-day work, success metrics and hiring bar for OpenAI FDEs. | 76 |
| 4 | 📄 [What a Forward-Deployed Engineer Actually Does at Palantir, Runway, and Greptile](https://www.paraform.com/insights/forward-deployed-engineer-palantir-runway-greptile)<br><sub>Paraform · 2026 · 🥈 Recommended</sub> | Side-by-side of the role at three very different companies — useful for picking which flavour of FDE fits you. | 70 |
| 5 | 📄 [Forward Deployed Engineer vs Applied AI Engineer](https://fde.academy/blog/forward-deployed-engineer-vs-applied-ai-engineer)<br><sub>FDE Academy · 2026 · 🥉 Useful</sub> | Clarifies two titles that are often confused in job posts; helps you target applications. | 61 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 4. Interview Preparation

_Round-by-round guides and question banks. Pair these with the practice set in /interview._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 🧭 [Forward Deployed Engineer Interview: The Definitive 2026 Guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde)<br><sub>Aced (formerly Exponent) · 2026 · 🥇 Essential</sub> | The most complete round-by-round map: recruiter, HM, practical coding, system design, decomposition case, client simulation, behavioural. | 96 |
| 2 | 🧭 [Forward Deployed Engineer Interview Guide 2026: Complete Prep](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)<br><sub>Sundeep Teki · 2026 · 🥇 Essential</sub> | Prep plan with an AI-lab slant — how OpenAI/Anthropic-style FDE loops differ from Palantir's. | 81 |
| 3 | 💻 [Forward Deployed Engineer role — interview prep (awesome-generative-ai-guide)](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/interview_prep/roles/forward-deployed-engineer/README.md)<br><sub>Aishwarya Naresh Reganti · 2025 · 🥈 Recommended</sub> | Question bank inside a well-known GenAI repo; strongest on the applied-AI technical questions. | 78 |
| 4 | 🧭 [The forward-deployed engineer interview guide](https://joinplank.com/forward-deployed-engineer/interview-guide)<br><sub>Plank · 2026 · 🥈 Recommended</sub> | Concise guide focused on the decomposition and customer-simulation rounds most candidates under-prepare for. | 76 |
| 5 | 🧭 [ElevenLabs Forward Deployed Engineer Interview Guide](https://www.tryexponent.com/guides/elevenlabs-forward-deployed-engineer-interview)<br><sub>Aced (formerly Exponent) · 2026 · 🥈 Recommended</sub> | Company-specific loop and sample questions — a good model of what an AI-startup FDE loop looks like. | 69 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 5. Technical Stack: Applied AI

_The AI-engineering core most FDE roles now test: agents, evals, RAG, tool use._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 📄 [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)<br><sub>Anthropic · 2024 · 🥇 Essential</sub> | Workflows vs. agents, and five composable patterns (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser). Start simple. | 90 |
| 2 | 📄 [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)<br><sub>Hamel Husain · 2024 · 🥇 Essential</sub> | Why unit tests, human review and LLM-as-judge are the backbone of shipping AI to customers. Evals are how FDEs prove ROI. | 88 |
| 3 | 🧭 [What We Learned from a Year of Building with LLMs](https://applied-llms.org/)<br><sub>Yan, Bischof, Frye, Husain, Liu, Shankar · 2024 · 🥇 Essential</sub> | Tactical, operational and strategic lessons from six practitioners — the closest thing to a field manual for applied LLM work. | 88 |
| 4 | 📚 [Model Context Protocol — documentation](https://modelcontextprotocol.io/)<br><sub>MCP project · 2026 · 🥇 Essential</sub> | The standard way to connect models to a customer's tools and data. Increasingly expected knowledge in FDE loops. | 88 |
| 5 | 💻 [12-Factor Agents](https://github.com/humanlayer/12-factor-agents)<br><sub>HumanLayer (Dex Horthy) · 2025 · 🥇 Essential</sub> | Principles for LLM software that is reliable enough to hand to production customers — own your prompts, context and control flow. | 86 |
| 6 | 💻 [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)<br><sub>Anthropic · 2026 · 🥇 Essential</sub> | Runnable notebooks for RAG, tool use, classification and extraction — ready-made starting points for customer prototypes. | 80 |
| 7 | 📚 [OpenAI Cookbook](https://cookbook.openai.com/)<br><sub>OpenAI · 2026 · 🥇 Essential</sub> | Large library of worked examples; good for rapid prototyping in the first week of an engagement. | 80 |
| 8 | 📄 [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)<br><sub>Eugene Yan · 2023 · 🥈 Recommended</sub> | Seven patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback) with references. | 71 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 6. Technical Stack: Data, Systems & Integration

_Enterprise data and integration fundamentals — the part of the job that eats most of the calendar._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 🎓 [Palantir Learning (Foundry & AIP)](https://learn.palantir.com/)<br><sub>Palantir · 2026 · 🥇 Essential</sub> | Free official training on ontology, pipelines and AIP — the platform most FDSEs deploy. | 88 |
| 2 | 🔖 [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)<br><sub>Gregor Hohpe & Bobby Woolf · 2003 · 🥈 Recommended</sub> | Vocabulary for connecting legacy systems — messaging, routing, transformation. Still how enterprises think. | 69 |
| 3 | 🎓 [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals)<br><sub>dbt Labs · 2025 · 🥈 Recommended</sub> | Free course on modern data transformation — common in customer data stacks you will inherit. | 69 |
| 4 | 📘 [Designing Data-Intensive Applications](https://dataintensive.net/)<br><sub>Martin Kleppmann · 2017 · 🥈 Recommended</sub> | The reference for reasoning about the customer databases, queues and pipelines you will be integrating with. | 65 |
| 5 | 🎓 [Select Star SQL](https://selectstarsql.com/)<br><sub>Zi Chong Kao · 2020 · 🥉 Useful</sub> | Free interactive SQL book. Fast way to get fluent before customer data work. | 64 |
| 6 | 🔖 [The Twelve-Factor App](https://12factor.net/)<br><sub>Adam Wiggins (Heroku) · 2011 · 🥉 Useful</sub> | Deployment and configuration discipline that keeps customer-specific code maintainable. | 59 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 7. The Soft Stack: Discovery, Communication, Consulting

_Customer discovery, structured thinking and trust — what separates FDEs from strong backend engineers._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 📘 [The Mom Test](https://www.momtestbook.com/)<br><sub>Rob Fitzpatrick · 2013 · 🥈 Recommended</sub> | How to run discovery conversations that surface real problems instead of polite compliments. Essential for scoping. | 76 |
| 2 | 📄 [The Pyramid Principle (summary)](https://medium.com/lessons-from-mckinsey/the-pyramid-principle-f0885dd3c5c7)<br><sub>Lessons from McKinsey · 2016 · 🥈 Recommended</sub> | Answer first, then support. The structure for every executive update and decomposition interview. | 65 |
| 3 | 📄 [A Day in the Life of a Palantir Deployment Strategist](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96)<br><sub>Palantir · 2020 · 🥉 Useful</sub> | The non-engineering partner of the FDSE — shows the stakeholder side of a deployment you will work alongside. | 62 |
| 4 | 📘 [The Trusted Advisor](https://trustedadvisor.com/books/the-trusted-advisor)<br><sub>David Maister, Charles Green, Robert Galford · 2000 · 🥉 Useful</sub> | The trust equation (credibility + reliability + intimacy over self-orientation) — how FDEs earn the right to change a customer's workflow. | 60 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 8. Roadmaps & Other Curated Lists

_Other community repos worth knowing, with what each is best for._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 💻 [Awesome-FDE-Roadmap](https://github.com/pierpaolo28/Awesome-FDE-Roadmap)<br><sub>Pier Paolo Ippolito · 2026 · 🥈 Recommended</sub> | Three-phase roadmap (data engineering, GCP cloud, consulting mindset). Strong on data; GCP-centric and light on hands-on labs. | 75 |
| 2 | 💻 [awesome-forward-deployed-engineering](https://github.com/HamzaShaikh17/awesome-forward-deployed-engineering)<br><sub>Hamza Shaikh · 2026 · 🥈 Recommended</sub> | Production-first engineering playbook for AI FDEs. | 66 |
| 3 | 💻 [forward-deployed-engineer-roadmap](https://github.com/thecoder8890/forward-deployed-engineer-roadmap)<br><sub>thecoder8890 · 2026 · 🥈 Recommended</sub> | Step-by-step path from coding and system design to customer problems and deployment impact. | 66 |
| 4 | 🔖 [GitHub topic: forward-deployed-engineer](https://github.com/topics/forward-deployed-engineer)<br><sub>GitHub · 2026 · 🥉 Useful</sub> | Live index of every repo tagged with the topic — check it for new projects. | 46 |

<p align="right"><a href="#readme">↑ back to top</a></p>

## 9. Jobs, Market Data & Compensation

_Where FDE roles are posted and what the market pays._

| Rank | Resource | Summary | Score |
|:-:|---|---|:-:|
| 1 | 📊 [FDE Job Market report](https://joinplank.com/fde-job-market)<br><sub>Plank · 2026 · 🥇 Essential</sub> | 1,300+ live FDE postings across 565 companies; median posted base about $193K, from ~$150K at seed to ~$243K at frontier labs (equity excluded). | 81 |
| 2 | 💼 [FDE Pulse — jobs and salaries](https://fdepulse.com/)<br><sub>FDE Pulse · 2026 · 🥈 Recommended</sub> | Job listings plus salary data points for FDE roles. | 68 |
| 3 | 💼 [Forward Deployed Engineer Job Board (fwddeploy)](https://www.fwddeploy.com/jobs)<br><sub>fwddeploy · 2026 · 🥉 Useful</sub> | Dedicated FDE job board. | 62 |
| 4 | 💼 [Work at a Startup (YC) — search 'forward deployed'](https://www.workatastartup.com/)<br><sub>Y Combinator · 2026 · 🥉 Useful</sub> | YC startups hire FDEs heavily; the best place for early-stage roles. | 62 |

<p align="right"><a href="#readme">↑ back to top</a></p>


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
