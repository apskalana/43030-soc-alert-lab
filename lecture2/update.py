"""Lecture 2: update HTML and record a GitHub workflow execution in README."""
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import os

actor = os.environ.get("GITHUB_ACTOR", "local-test")
commit = os.environ.get("GITHUB_SHA", "local-test")[:12]
timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
html_file = Path(__file__).with_name("index.html")
readme_file = Path(__file__).with_name("README.md")
data = html_file.read_text(encoding="utf-8")
paragraph = f"<p>Updated by {escape(actor)} at {escape(timestamp)}</p>"
if "</body>" not in data:
    raise SystemExit("Expected closing body element")
html_file.write_text(data.replace("</body>", paragraph + "</body>", 1), encoding="utf-8")
with readme_file.open("a", encoding="utf-8") as stream:
    stream.write(f"\n- Workflow executed by {actor} (trigger commit: {commit})\n")
print(f"Updated HTML and README for {actor}")
