"""Educational triage of synthetic login events; not an enterprise SIEM."""
from __future__ import annotations
import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

REQUIRED = {"timestamp", "event_type", "source_ip", "username"}
TYPES = {"login_success", "login_failure"}

def parse_timestamp(value: str) -> datetime:
    moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if moment.tzinfo is None or moment.utcoffset() is None:
        raise ValueError("timestamp must contain a timezone offset")
    return moment

def load_events(path):
    events = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                if not isinstance(event, dict) or not REQUIRED.issubset(event):
                    raise ValueError("missing required fields")
                if event["event_type"] not in TYPES:
                    raise ValueError("unsupported event type")
                if any(not isinstance(event[key], str) or not event[key].strip() for key in REQUIRED):
                    raise ValueError("required fields must be non-empty strings")
                event["parsed_timestamp"] = parse_timestamp(event["timestamp"])
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid event on line {line_number}: {exc}") from exc
            events.append(event)
    return events

def detect_alerts(events, threshold=3, window_minutes=10):
    if threshold < 1 or window_minutes < 1:
        raise ValueError("positive detection parameters required")
    failures = defaultdict(list)
    findings = []
    for event in events:
        if event["event_type"] == "login_failure":
            failures[event["source_ip"]].append(event["parsed_timestamp"])
        elif event["username"].lower() in ("admin", "administrator"):
            hour = event["parsed_timestamp"].hour
            if hour >= 22 or hour < 6:
                findings.append({
                    "rule": "OFF_HOURS_ADMIN_LOGIN", "severity": "medium",
                    "source_ip": event["source_ip"],
                    "details": f"Administrator login at {event['timestamp']} (event timezone)"
                })
    for ip, times in failures.items():
        times.sort()
        start = 0
        for end, moment in enumerate(times):
            while moment - times[start] > timedelta(minutes=window_minutes):
                start += 1
            if end - start + 1 >= threshold:
                findings.append({
                    "rule": "REPEATED_LOGIN_FAILURES", "severity": "high",
                    "source_ip": ip,
                    "details": f"At least {threshold} failures within {window_minutes} minutes; latest at {moment.isoformat()}"
                })
                break
    return sorted(findings, key=lambda finding: (finding["rule"], finding["source_ip"]))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile", nargs="?", default="sample_logs.jsonl")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        findings = detect_alerts(load_events(args.logfile))
    except (OSError, ValueError) as exc:
        parser.exit(status=1, message=f"Error: {exc}\n")
    if args.json:
        print(json.dumps(findings, indent=2))
    elif not findings:
        print("No alerts found.")
    else:
        for finding in findings:
            print(f"[{finding['severity'].upper()}] {finding['rule']} | {finding['source_ip']} | {finding['details']}")

if __name__ == "__main__":
    main()
