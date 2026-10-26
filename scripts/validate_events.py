"""Validate the synthetic JSON Lines event data."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from soc_triage import load_events

if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) == 2 else "sample_logs.jsonl"
    events = load_events(source)
    print(f"Validated {len(events)} synthetic event records in {source}")
