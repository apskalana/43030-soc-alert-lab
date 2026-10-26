#!/bin/sh
set -eu
python /app/render_report.py "$1" "$2" /app/index.html
printf 'Updated /app/index.html with task and test data\n'
