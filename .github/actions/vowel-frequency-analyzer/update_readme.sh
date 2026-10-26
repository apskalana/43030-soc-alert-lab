#!/bin/sh
set -eu
RESULT="$1"
USER_NAME="$2"
OUT_FILE="$3"
{
  printf '\n### Vowel report\n'
  printf 'Actor: %s | UTC: %s | Counts: %s\n' "$USER_NAME" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$RESULT"
} >> "$OUT_FILE"
