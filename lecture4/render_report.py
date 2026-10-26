"""Update HTML from a TaskPool and captured test output."""
from html import escape
from pathlib import Path
import sys

def render(todo_text, test_text):
    return ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            "<title>43030 Task Manager CI report</title>"
            "<style>body{font:16px system-ui;max-width:800px;margin:40px auto;padding:16px}"
            "pre{white-space:pre-wrap;background:#f1f5f9;padding:16px;border-radius:8px}</style>"
            "</head><body><h1>43030 Task Manager CI report</h1>"
            "<h2>Tasks</h2><pre id='tasks'>" + escape(todo_text) +
            "</pre><h2>Unit Tests</h2><pre id='tests'>" + escape(test_text) +
            "</pre></body></html>")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("Usage: render_report.py task-output test-output index.html")
    Path(sys.argv[3]).write_text(render(Path(sys.argv[1]).read_text(),
                                        Path(sys.argv[2]).read_text()), encoding="utf-8")
