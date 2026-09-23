# How Resources Are Ranked

The goal is an order you can trust, and can check for yourself.

## 1. Collection
Candidates come from web search across the FDE topic: operator essays, company engineering blogs, investor and product writing, interview guides, applied-AI references, community repos and job-market data. Each candidate was opened and read. The one-line `summary` in [`data/resources.yaml`](data/resources.yaml) is drawn from the source itself, not from its title.

Excluded: paywalled-only content with no useful free portion, pages that are only job ads, and near-duplicate SEO articles.

## 2. Human rubric (always on)

| Criterion | Weight | 1 = | 5 = |
|---|:-:|---|---|
| Relevance | 30% | General tech content | Written for FDE work specifically |
| Practicality | 25% | Opinion only | Templates, questions, code, steps |
| Depth | 20% | Overview | Dense, original insight |
| Authority | 15% | Anonymous or secondhand | First-hand operator or primary source |
| Recency | 10% | Before 2015 | 2025–26 |

`score = Σ weight × (value − 1) / 4 × 100` → a number from 0 to 100.

Timeless books score low on recency by design. They still rank well where depth and authority carry them.

## 3. Jev re-ranking (optional, recommended)
[Jev](https://jev-ai.pro/) is TypeSafe AI's System One model. Instead of generating text, it answers typed questions with **calibrated probability distributions**, which suits consistent grading.

[`scripts/rank_with_jev.py`](scripts/rank_with_jev.py) sends each resource's metadata and summary to `POST https://api.typesafe.ai/v1/systemone`. It asks four `score` questions (relevance, practicality, depth, authority) on a five-level scale. Jev returns an expected level for each; these are normalised and weighted into a 0–100 Jev score and saved to `data/jev_scores.json`.

Once Jev scores exist, the README uses:

```
final = 0.5 × human rubric + 0.5 × Jev
```

and the header shows that Jev was used.

## 4. Keeping it honest
- Every score is in plain YAML. Disagree? Open a PR changing the number, with a reason.
- A weekly GitHub Action checks every link.
- Re-running Jev with `--all` after a model update re-grades everything consistently.
