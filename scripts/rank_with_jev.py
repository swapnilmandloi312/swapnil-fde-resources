#!/usr/bin/env python3
"""Re-rank every resource with Jev (TypeSafe AI's System One model).

Jev does not generate text — it answers typed questions with calibrated
probabilities. We ask it to grade each resource on the same rubric used by
humans (relevance, practicality, depth, authority) and store the results in
data/jev_scores.json. build_readme.py then blends Jev's score 50/50 with the
human rubric score.

Usage:
    export TYPESAFE_API_KEY=ts_...        # create at console.typesafe.ai/settings/keys
    # optional: export JEV_API_URL=https://jev-ai.pro/api/v1/systemone   (Jev AI gateway)
    python scripts/rank_with_jev.py        # only scores resources not yet scored
    python scripts/rank_with_jev.py --all  # re-score everything
    python scripts/build_readme.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "resources.yaml"
SCORES = ROOT / "data" / "jev_scores.json"
API = os.environ.get("JEV_API_URL", "https://api.typesafe.ai/v1/systemone")
MODEL = os.environ.get("JEV_MODEL", "jev-latest")

LEVELS = ["very poor", "poor", "adequate", "strong", "exceptional"]
WEIGHTS = {"relevance": 0.35, "practicality": 0.30, "depth": 0.20, "authority": 0.15}

QUESTIONS = {
    "relevance": {
        "type": "score",
        "instructions": ("How useful is this resource for someone who wants to become, or already works as, "
                         "a Forward Deployed Engineer (an engineer embedded with enterprise customers to deploy "
                         "software/AI and deliver outcomes)?"),
        "criteria": LEVELS,
    },
    "practicality": {
        "type": "score",
        "instructions": "How actionable is it — does it give concrete steps, templates, questions, code or frameworks?",
        "criteria": LEVELS,
    },
    "depth": {
        "type": "score",
        "instructions": "How much real substance and insight does it contain, versus a shallow overview?",
        "criteria": LEVELS,
    },
    "authority": {
        "type": "score",
        "instructions": ("How authoritative is the source — first-hand practitioners or primary sources score high; "
                         "anonymous or SEO-style summaries score low?"),
        "criteria": LEVELS,
    },
}


def describe(r: dict) -> str:
    return (f"Title: {r['title']}\nAuthor/publisher: {r['author']}\nYear: {r['year']}\n"
            f"Format: {r['type']}\nURL: {r['url']}\nWhat it contains: {r['summary']}")


def ask_jev(session: requests.Session, r: dict) -> dict:
    payload = {"model": MODEL, "state": describe(r), "questions": QUESTIONS}
    for attempt in range(4):
        resp = session.post(API, json=payload, timeout=60)
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(2 ** attempt)
            continue
        resp.raise_for_status()
        body = resp.json()
        answers = body["answers"]
        dims = {k: round(answers[k]["score"] / (len(LEVELS) - 1), 3) for k in QUESTIONS}
        score = round(sum(WEIGHTS[k] * dims[k] for k in WEIGHTS) * 100, 1)
        return {"score": score, **dims, "model": body.get("model", MODEL), "ranked_at": date.today().isoformat()}
    raise RuntimeError(f"Jev API kept failing for {r['url']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="re-score every resource")
    args = ap.parse_args()

    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        sys.exit("Set TYPESAFE_API_KEY first (create one at console.typesafe.ai/settings/keys).")

    resources = yaml.safe_load(DATA.read_text(encoding="utf-8"))["resources"]
    scores = json.loads(SCORES.read_text()) if SCORES.exists() else {}

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {key}", "Content-Type": "application/json"})

    todo = [r for r in resources if args.all or r["url"] not in scores]
    print(f"Scoring {len(todo)} of {len(resources)} resources with {MODEL}…")
    for i, r in enumerate(todo, 1):
        scores[r["url"]] = ask_jev(session, r)
        print(f"  [{i}/{len(todo)}] {scores[r['url']]['score']:5.1f}  {r['title']}")
        SCORES.write_text(json.dumps(scores, indent=2, sort_keys=True))  # save as we go
    print(f"Saved {SCORES.relative_to(ROOT)}. Now run: python scripts/build_readme.py")


if __name__ == "__main__":
    main()
