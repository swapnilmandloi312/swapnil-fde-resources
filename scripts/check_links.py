#!/usr/bin/env python3
"""Check that every resource URL still resolves. Exits 1 if any are dead."""
import concurrent.futures as cf
import sys
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"User-Agent": "Mozilla/5.0 (swapnil-fde-resources link checker)"}
# Sites that block bots but are fine for humans.
SOFT_FAIL = {401, 403, 429, 999}


def check(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=25, allow_redirects=True)
        return url, r.status_code
    except requests.RequestException as e:
        return url, type(e).__name__


def main() -> None:
    urls = [r["url"] for r in yaml.safe_load((ROOT / "data" / "resources.yaml").read_text())["resources"]]
    dead = []
    with cf.ThreadPoolExecutor(10) as ex:
        for url, status in ex.map(check, urls):
            ok = status == 200 or status in SOFT_FAIL
            print(f"{'OK ' if ok else 'BAD'} {status} {url}")
            if not ok:
                dead.append((url, status))
    print(f"\n{len(urls) - len(dead)}/{len(urls)} links OK")
    sys.exit(1 if dead else 0)


if __name__ == "__main__":
    main()
