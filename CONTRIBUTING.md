# Contributing

Thanks for helping improve Swapnil FDE Resources.

## Add a resource
1. Add **one** entry to [`data/resources.yaml`](data/resources.yaml) in the right category:
   ```yaml
   - title: "Exact title of the piece"
     url: https://...
     author: Person or organisation
     year: 2026
     type: article   # article | essay | newsletter | news | guide | video | podcast | repo | docs | book | course | reference | case-study | data | job-board
     category: field # see the categories list at the top of the file
     summary: "One or two lines on what it actually contains — read it first."
     scores: {relevance: 4, depth: 4, practicality: 4, authority: 4, recency: 5}
   ```
2. Score it using the rubric in [RANKING.md](RANKING.md). Be honest: most things are 3s.
3. Run `python scripts/build_readme.py` and commit both files.
4. In the PR description, say why it deserves a place.

## Quality bar
- It must be useful to someone doing or pursuing FDE work.
- It must be freely accessible, or have a substantial free portion (books are the exception).
- No affiliate links, no job-spam pages, no AI-generated SEO content.

## Improve a template
Templates in `/playbooks` should stay short and usable in a real engagement. Field-tested edits are especially welcome.
