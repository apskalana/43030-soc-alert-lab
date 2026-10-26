import tempfile
import unittest
from pathlib import Path
from soc_triage import detect_alerts, load_events, parse_timestamp

def event(time, kind="login_failure", ip="198.51.100.17", user="alex"):
    return {"timestamp": time, "parsed_timestamp": parse_timestamp(time),
            "event_type": kind, "source_ip": ip, "username": user}

class TriageTests(unittest.TestCase):
    def test_three_failures_alert(self):
        logs = [event(f"2026-10-27T09:0{n}:00+11:00") for n in (0, 2, 3)]
        self.assertEqual(detect_alerts(logs)[0]["rule"], "REPEATED_LOGIN_FAILURES")

    def test_failures_outside_window(self):
        logs = [event(f"2026-10-27T09:{n:02}:00+11:00") for n in (0, 12, 25)]
        self.assertEqual(detect_alerts(logs), [])

    def test_admin_after_hours(self):
        logs = [event("2026-10-27T23:45:00+11:00", "login_success", user="admin")]
        self.assertEqual(detect_alerts(logs)[0]["rule"], "OFF_HOURS_ADMIN_LOGIN")

    def test_normal_user_after_hours(self):
        logs = [event("2026-10-27T23:45:00+11:00", "login_success", user="alex")]
        self.assertEqual(detect_alerts(logs), [])

    def test_invalid_log(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.jsonl"
            path.write_text('{"timestamp":"2026-10-27T09:00:00+11:00"}\n')
            with self.assertRaisesRegex(ValueError, "line 1"):
                load_events(path)

    def test_sample_data(self):
        path = Path(__file__).resolve().parents[1] / "sample_logs.jsonl"
        self.assertEqual(len(detect_alerts(load_events(path))), 2)

if __name__ == "__main__":
    unittest.main()
