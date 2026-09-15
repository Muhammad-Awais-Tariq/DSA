# DSA

My solutions to classic Data Structures & Algorithms problems — working through patterns (hashmaps, prefix sums, heaps, etc.) to build interview-ready problem-solving skills, with a built-in spaced-repetition system so I don't forget what I've already solved.

🔗 **LeetCode profile:** [leetcode.com/u/MAwaisTariq87](https://leetcode.com/u/MAwaisTariq87/)

> 🚧 Work in progress — new problems are added as I solve them.

---

## Structure

Every problem gets its own folder:

```
problem-name/
├── problem-name.py   # My optimal solution
└── readme.md         # Problem statement
```

Root of the repo:

```
DSA/
├── problem-name/         # One folder per problem (solution + statement)
├── review.py             # Spaced-repetition CLI — tracks what to revisit and when
├── review_data.json       # Data store for review.py (auto-generated/updated)
├── pyproject.toml         # Project config (uv)
├── uv.lock                # Locked dependencies (uv)
├── .python-version        # Python version pin
├── .gitignore
└── README.md
```

---

## Spaced Repetition — `review.py`

Solving a problem once doesn't mean it sticks. `review.py` is a small CLI that applies spaced repetition to LeetCode-style problems, so I revisit them right before I'd otherwise forget them.

**Commands:**

```bash
python review.py add "Two Sum" "Hashmap"   # add a new problem, first review in 3 days
python review.py pass "Two Sum"            # solved it cleanly -> streak grows, next interval grows
python review.py fail "Two Sum"            # fumbled it -> streak resets, review again in 2 days
python review.py list                      # show everything, most overdue first
python review.py due                       # show only what's due today or overdue
```

**How the interval grows:** every `pass` increases the streak by 1, and the next review is scheduled `4 * streak` days out (4, 8, 12, 16...). A `fail` resets the streak to 0 and schedules the next review in just 2 days, so shaky problems come back around quickly.

**Git hook shortcut:** committing with a message like `solved: Two Sum [Hashmap]` triggers the same logic as `add`, so review tracking updates automatically as part of the normal solve → commit workflow.

## `review_data.json`

The data file `review.py` reads from and writes to. Each entry looks like:

```json
"Two Sum": {
  "pattern": "Hashmap",
  "last_solved": "2026-09-07",
  "next_review": "2026-09-19",
  "streak": 3
}
```

- **pattern** — the technique/category the problem belongs to (Hashmap, Prefix/Suffix, Hashset, etc.), useful for spotting weak patterns at a glance
- **last_solved** — date it was last attempted
- **next_review** — date it's next due for a revisit
- **streak** — consecutive clean solves; drives how far out the next review gets pushed

`review.py list` and `review.py due` read this file to surface OVERDUE and DUE TODAY problems first, so I always know what to revisit next.

---

## Problems

Some of the problems solved so far (see the repo for the full, growing list):

- Two Sum
- Contains Duplicate
- Contains Duplicate II
- Valid Anagram
- Group Anagram
- Product of Array Except Self
- Top K Frequent Elements
- Roman to Integer
- Verifying an Alien Dictionary
- Longest Consecutive Sequence
- First Missing Positive
- Best Time to Buy and Sell Stock

---

## Why

Practicing here to build strong DSA fundamentals — pattern recognition, clean optimal solutions, and long-term retention through spaced repetition, instead of solving a problem once and forgetting it a month later.

---

## Author

Muhammad Awais Tariq

---
If you find this useful, consider giving it a star ⭐