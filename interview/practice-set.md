# FDE Interview Practice Set

40 questions across the rounds most FDE loops use. Each one names **what the interviewer is really testing**.
Practise out loud, with a timer, and ideally with someone playing the customer.

Round structure is based on the guides ranked in the main README (Aced/Exponent, Sundeep Teki, Plank). The questions are original practice prompts written in that style.

---

## 1. Practical coding (6)
_Practical engineering, not algorithm trivia. Talk through trade-offs as you type._

| # | Question | Really testing |
|:-:|---|---|
| 1 | Write a rate limiter that supports per-user and global limits. | Fundamentals, edge cases, concurrency awareness |
| 2 | Parse a messy CSV export (bad encodings, inconsistent dates, duplicate rows) into a clean table. Explain each rule. | Real-world data hygiene, and saying which assumptions to check with the customer |
| 3 | Write a client for a paginated REST API with retries and exponential backoff. | Integration robustness |
| 4 | Given two record sets from different systems, reconcile them and report mismatches. | Joining imperfect data; defining "match" |
| 5 | Implement a small job queue with idempotent workers. | Reliability thinking |
| 6 | Add structured logging and a health check to an existing script. | Production instinct |

## 2. Deployment system design (6)
_Enterprise constraints first: security, existing systems, data residency, who operates it._

| # | Question | Really testing |
|:-:|---|---|
| 7 | Design a private, VPC-deployed RAG system for a healthcare customer with 50M documents and HIPAA constraints. | Compliance, retrieval at scale, access control |
| 8 | A bank wants an AI agent that drafts responses to customer complaints. Design it end to end. | Human-in-the-loop, auditability |
| 9 | Integrate your product with a customer's on-prem ERP that only supports nightly batch exports. | Pragmatism with legacy systems |
| 10 | Design the eval and monitoring setup for an LLM feature used by 5,000 employees. | Quality as a system, not a vibe |
| 11 | The customer's data team owns the warehouse and won't give write access. How do you ship? | Working within constraints |
| 12 | Design multi-tenant deployment so one customer's custom code doesn't fork the product. | Thinking about product, not just this customer |

## 3. Decomposition / case (6)
_Scope, surface assumptions, sequence. Structure beats speed. State the metric early._

| # | Question | Really testing |
|:-:|---|---|
| 13 | A city wants to reduce 911 emergency response times using call, traffic and ambulance GPS data. You have 60 minutes. Go. | Scoping under ambiguity |
| 14 | A manufacturer's defect rate went up 30% last quarter. They have sensor data and maintenance logs. Where do you start? | Hypothesis-driven investigation |
| 15 | A retailer wants to "use AI in customer support". Turn that into a 6-week engagement. | Turning a vague ask into an outcome |
| 16 | A hospital wants to cut bed-allocation delays. What data do you need, and what would you build first? | Sequencing; the smallest valuable slice |
| 17 | A logistics company's planners override the optimiser 60% of the time. Why, and what do you do? | User empathy; the real problem vs. the stated one |
| 18 | An insurer wants to speed up claims triage. How would you measure success in week one? | Metrics thinking |

## 4. Client simulation (6)
_Role-play. Ownership language, calm de-escalation, a clear next step. Never blame the customer or your own company._

| # | Scenario | Really testing |
|:-:|---|---|
| 19 | The deployment slipped three weeks. The customer's CTO is on the line. Tell them. | Owning bad news |
| 20 | The executive sponsor wants a feature your product will never support. | Saying no while keeping trust |
| 21 | The end users say the tool is slower than their spreadsheet. | Listening before defending |
| 22 | Security blocks your data access two days before a demo. | Escalation and plan B |
| 23 | Two stakeholders give you conflicting priorities in the same meeting. | Facilitation; surfacing the decision owner |
| 24 | The model made a visible mistake in front of the customer's CEO. | Composure, explanation, remediation plan |

## 5. Behavioural (6)
_Use STAR, but lead with the result. Say "I", and name the numbers._

| # | Question | Really testing |
|:-:|---|---|
| 25 | Walk me through the most technically challenging project you owned end to end. | Real ownership and depth |
| 26 | Tell me about a time you shipped something imperfect on purpose. | Judgement about trade-offs |
| 27 | Tell me about a time you learned a new domain fast. | Learning velocity |
| 28 | Describe a disagreement with a customer or stakeholder and how it ended. | Conflict handling |
| 29 | When did you change a product or process based on what you saw in the field? | Feeding learnings back |
| 30 | Tell me about a failure you caused. | Honesty, and what changed afterwards |

## 6. AI-specific (6)
_Increasingly its own round at AI labs and AI startups._

| # | Question | Really testing |
|:-:|---|---|
| 31 | When would you use a workflow instead of an autonomous agent? | Knowing the simplest thing that works |
| 32 | How do you build an eval set for a customer when there is no labelled data? | Practical eval craft |
| 33 | Retrieval quality is poor. Walk through how you'd debug it. | Systematic RAG debugging |
| 34 | How do you defend an agent that reads customer emails from prompt injection? | Security instinct |
| 35 | The customer wants to fine-tune. How do you decide whether they should? | Cost and benefit versus prompting and RAG |
| 36 | How would you estimate and control the LLM cost of a deployment? | Unit economics |

## 7. "Why FDE?" (4)

| # | Question | Really testing |
|:-:|---|---|
| 37 | Why FDE rather than product engineering? | Self-awareness about the trade-offs (travel, context-switching, less deep ownership of one codebase) |
| 38 | What does a great FDE engagement look like to you? | Whether you think in outcomes plus learnings fed back to product |
| 39 | How would you split your time between the customer and the core product team? | Understanding the two-way role |
| 40 | Why this company's customers? | Research and genuine interest |

---

### How to practise
1. **Timebox:** 45 minutes for cases and design, 20 for client simulations.
2. **Record yourself:** listen for filler, hedging and not stating the answer first.
3. **Use the templates:** the [Scoping Doc](../playbooks/02-scoping-doc.md) structure is a ready framework for decomposition cases.
