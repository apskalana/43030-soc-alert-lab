"""Lecture 3: count vowel frequency in a text file."""
from collections import Counter
from pathlib import Path
import json
import sys

def count_vowels(path):
    text = Path(path).read_text(encoding="utf-8").lower()
    return {v: Counter(text)[v] for v in "aeiou"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python frequency.py FILE")
    print(json.dumps(count_vowels(sys.argv[1]), sort_keys=True))
