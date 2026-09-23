# AI Deployment Checklist

Run through this before an LLM-powered feature touches real users or real customer data.

## Problem and value
- [ ] The workflow and success metric are written down and agreed ([Scoping Doc](02-scoping-doc.md)).
- [ ] You have tried the simplest solution first (rules, SQL, a single prompt) before building an agent.

## Data and security
- [ ] Data classification is known (PII, PHI, financial, confidential), and the customer's security team has approved the data flow.
- [ ] You know where data is processed and stored, and the retention period, including at the model provider.
- [ ] Secrets are in a secret manager, not in code, notebooks or chat. Keys are scoped and rotated.
- [ ] Access follows least privilege; the system acts with the user's permissions, not an admin's.

## Quality (evals)
- [ ] There is a labelled eval set drawn from **real** customer examples, including hard and adversarial cases.
- [ ] Pass/fail criteria are agreed with the operator, not invented by the engineer.
- [ ] Evals run automatically on every prompt or model change.
- [ ] Known failure modes are documented, with example traces.

## Safety and control
- [ ] Irreversible actions (sending, paying, deleting, writing to records) need human approval.
- [ ] Prompt injection is considered for every untrusted input (emails, documents, web pages).
- [ ] There is a fallback when the model is down, slow or uncertain.
- [ ] Output is grounded: citations, or links back to the source records.

## Operations
- [ ] Logging and tracing of inputs, outputs, tool calls and latency — with PII handling agreed.
- [ ] Cost per task is estimated and monitored, with a budget alert.
- [ ] Someone at the customer knows how to turn it off.
- [ ] A runbook exists for the top three likely incidents.

## Adoption
- [ ] End users were trained on the real workflow, not in a demo.
- [ ] There is a feedback channel (a thumbs-down with a reason is enough), and someone reads it weekly.
