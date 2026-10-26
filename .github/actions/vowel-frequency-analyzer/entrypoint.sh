#!/bin/sh
set -eu
INPUT_FILE="${1:-data.txt}"
WORKSPACE="${GITHUB_WORKSPACE:-/github/workspace}"
RESULT="$(python /app/frequency.py "$WORKSPACE/$INPUT_FILE")"
printf 'Vowel results for %s: %s\n' "$INPUT_FILE" "$RESULT"
sh /app/update_readme.sh "$RESULT" "${GITHUB_ACTOR:-local}" "$WORKSPACE/lecture3/README.md"
echo "Wrote report line to lecture3/README.md in workflow workspace"
