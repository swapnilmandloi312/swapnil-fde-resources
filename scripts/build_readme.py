#!/usr/bin/env python3
"""Render README.md from data/resources.yaml.

Ranking = weighted rubric score (0-100). If a resource has a `jev` block
(written by rank_with_jev.py), the final score blends the rubric with Jev's
independent judgement: final = 0.5 * rubric + 0.5 * jev.
"""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "resources.yaml"
TEMPLATE = ROOT / "scripts" / "README.template.md"
OUT = ROOT / "README.md"

WEIGHTS = {"relevance": 0.30, "practicality": 0.25, "depth": 0.20, "authority": 0.15, "recency": 0.10}
TYPE_ICON = {
    "article": "📄", "essay": "✍️", "newsletter": "📰", "news": "🗞️", "guide": "🧭",
    "video": "🎥", "podcast": "🎧", "repo": "💻", "docs": "📚", "book": "📘",
    "course": "🎓", "reference": "🔖", "case-study": "🔬", "data": "📊", "job-board": "💼",
}


def rubric_score(s: dict) -> float:
    return round(sum(WEIGHTS[k] * (s[k] - 1) / 4 for k in WEIGHTS) * 100, 1)


def final_score(r: dict) -> float:
    base = rubric_score(r["scores"])
    jev = r.get("jev", {}).get("score")
    return round(0.5 * base + 0.5 * jev, 1) if jev is not None else base


def tier(score: float) -> str:
    if score >= 80:
        return "🥇 Essential"
    if score >= 65:
        return "🥈 Recommended"
    return "🥉 Useful"


def main() -> None:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    res = data["resources"]
    jev_file = ROOT / "data" / "jev_scores.json"
    jev_scores = json.loads(jev_file.read_text()) if jev_file.exists() else {}
    for r in res:
        if r["url"] in jev_scores:
            r["jev"] = jev_scores[r["url"]]
    for r in res:
        r["_score"] = final_score(r)
    jev_used = any("jev" in r for r in res)

    lines: list[str] = []

    # Top 10 overall
    top = sorted(res, key=lambda r: -r["_score"])[:10]
    lines += ["## 🏆 Top 10 — Start Here", "",
              "If you read nothing else, read these, in this order.", "",
              "| # | Resource | Why it matters | Score |", "|:-:|---|---|:-:|"]
    for i, r in enumerate(top, 1):
        lines.append(f"| {i} | [{r['title']}]({r['url']})<br><sub>{r['author']} · {r['year']}</sub> "
                     f"| {r['summary']} | **{r['_score']:.0f}** |")
    lines += [""]

    # Contents
    lines += ["## Contents", ""]
    for c in data["categories"]:
        anchor = c["title"].lower().replace(" ", "-")
        anchor = "".join(ch for ch in anchor if ch.isalnum() or ch == "-")
        lines.append(f"- [{c['title']}](#{anchor})")
    lines += ["- [Playbooks & Templates](#playbooks--templates)",
              "- [Interview Practice Set](#interview-practice-set)",
              "- [90-Day Learning Plan](#90-day-learning-plan)",
              "- [How Resources Are Ranked](#how-resources-are-ranked)", ""]

    # Categories
    for c in data["categories"]:
        items = sorted([r for r in res if r["category"] == c["id"]], key=lambda r: -r["_score"])
        if not items:
            continue
        lines += [f"## {c['title']}", "", f"_{c['blurb']}_", "",
                  "| Rank | Resource | Summary | Score |", "|:-:|---|---|:-:|"]
        for i, r in enumerate(items, 1):
            icon = TYPE_ICON.get(r["type"], "🔗")
            lines.append(f"| {i} | {icon} [{r['title']}]({r['url']})<br><sub>{r['author']} · {r['year']} · {tier(r['_score'])}</sub> "
                         f"| {r['summary']} | {r['_score']:.0f} |")
        lines += ["", "<p align=\"right\"><a href=\"#readme\">↑ back to top</a></p>", ""]

    body = "\n".join(lines)
    stats = (f"{len(res)} resources · {len(data['categories'])} categories · "
             f"ranking: {'rubric + Jev (TypeSafe AI)' if jev_used else 'transparent rubric (Jev re-rank ready)'}")
    out = TEMPLATE.read_text(encoding="utf-8").replace("{{RESOURCES}}", body).replace("{{STATS}}", stats)
    OUT.write_text(out, encoding="utf-8")
    print(f"README.md written — {stats}")


if __name__ == "__main__":
    main()
