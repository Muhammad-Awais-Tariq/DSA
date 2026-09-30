#!/usr/bin/env python3
"""
review.py - Simple spaced-repetition tracker for LeetCode problems.

Usage:
    python review.py add "Two Sum" "Hashmap"
        -> add a new problem, first review in 3 days

    you can use solved: Two Sum [Hashmap] this pattern when submitting with git commit to automatically use the hook

    python review.py pass "Two Sum"
        -> solved it cleanly (streak +1, interval grows)

    python review.py slip "Two Sum"
        -> right approach, small bug/typo (streak -1, not a reset)

    python review.py fail "Two Sum"
        -> forgot the approach or got it wrong (streak -2, review in 2 days)

    python review.py reset "Two Sum"
        -> genuinely couldn't start (streak back to 0)

    python review.py list
        -> shows everything, DUE items at the top

    python review.py due
        -> shows only what's due today or overdue

Data is stored in review_data.json in the same folder as this script.
"""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent / "review_data.json"

# How many streak levels each outcome costs
SLIP_PENALTY = 1
FAIL_PENALTY = 2


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def today_str():
    return date.today().isoformat()


def interval_for(streak):
    """Days until next review for a given streak. Streak 0 -> 2 days."""
    return 4 * streak if streak > 0 else 2


def get_entry(data, name):
    if name not in data:
        print(f"'{name}' not found. Add it first with: python review.py add \"{name}\" \"Pattern\"")
        return None
    return data[name]


def schedule(entry, days):
    next_review = date.today() + timedelta(days=days)
    entry["last_solved"] = today_str()
    entry["next_review"] = next_review.isoformat()
    return next_review


def add_problem(name, pattern="General"):
    data = load_data()
    if name in data:
        print(f"'{name}' already exists. Use pass/slip/fail to update it instead.")
        return
    next_review = date.today() + timedelta(days=3)
    data[name] = {
        "pattern": pattern,
        "last_solved": today_str(),
        "next_review": next_review.isoformat(),
        "streak": 0,
    }
    save_data(data)
    print(f"Added '{name}' [{pattern}]. Next review: {next_review.isoformat()}")


def mark_pass(name):
    data = load_data()
    entry = get_entry(data, name)
    if entry is None:
        return
    entry["streak"] += 1
    next_review = schedule(entry, interval_for(entry["streak"]))
    save_data(data)
    print(f"'{name}' passed. Streak: {entry['streak']}. Next review: {next_review.isoformat()}")


def mark_slip(name):
    data = load_data()
    entry = get_entry(data, name)
    if entry is None:
        return
    entry["streak"] = max(0, entry["streak"] - SLIP_PENALTY)
    next_review = schedule(entry, interval_for(entry["streak"]))
    save_data(data)
    print(f"'{name}' small slip. Streak: {entry['streak']}. Next review: {next_review.isoformat()}")


def mark_fail(name):
    data = load_data()
    entry = get_entry(data, name)
    if entry is None:
        return
    entry["streak"] = max(0, entry["streak"] - FAIL_PENALTY)
    next_review = schedule(entry, 2)
    save_data(data)
    print(f"'{name}' failed. Streak: {entry['streak']}. Next review: {next_review.isoformat()}")


def mark_reset(name):
    data = load_data()
    entry = get_entry(data, name)
    if entry is None:
        return
    entry["streak"] = 0
    next_review = schedule(entry, 2)
    save_data(data)
    print(f"'{name}' reset to 0. Next review: {next_review.isoformat()}")


def list_problems(only_due=False):
    data = load_data()
    if not data:
        print("No problems tracked yet. Add one with: python review.py add \"Problem Name\" \"Pattern\"")
        return

    today = date.today()
    rows = []
    for name, entry in data.items():
        next_review = date.fromisoformat(entry["next_review"])
        days_until = (next_review - today).days
        is_due = days_until <= 0
        if only_due and not is_due:
            continue
        rows.append((days_until, name, entry, is_due))

    # Most overdue first, then soonest, then not-yet-due
    rows.sort(key=lambda r: r[0])

    if not rows:
        print("Nothing due right now. Go solve a new problem.")
        return

    print(f"{'STATUS':<10}{'PROBLEM':<30}{'PATTERN':<18}{'NEXT REVIEW':<14}{'STREAK'}")
    print("-" * 80)
    for days_until, name, entry, is_due in rows:
        if days_until < 0:
            status = "OVERDUE"
        elif days_until == 0:
            status = "DUE TODAY"
        else:
            status = f"in {days_until}d"
        print(f"{status:<10}{name:<30}{entry['pattern']:<18}{entry['next_review']:<14}{entry['streak']}")


def print_usage():
    print(__doc__)


COMMANDS = {
    "pass": mark_pass,
    "slip": mark_slip,
    "fail": mark_fail,
    "reset": mark_reset,
}


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: python review.py add \"Problem Name\" \"Pattern\"")
            return
        name = sys.argv[2]
        pattern = sys.argv[3] if len(sys.argv) > 3 else "General"
        add_problem(name, pattern)

    elif cmd in COMMANDS:
        if len(sys.argv) < 3:
            print(f"Usage: python review.py {cmd} \"Problem Name\"")
            return
        COMMANDS[cmd](sys.argv[2])

    elif cmd == "list":
        list_problems(only_due=False)

    elif cmd == "due":
        list_problems(only_due=True)

    else:
        print_usage()


if __name__ == "__main__":
    main()