# Lecture 3 — Custom Docker Action (Vowel Frequency)

The lecture practical asks for Python vowel analysis, a shell README updater, an entrypoint and Docker.

A custom Docker action is stored at `.github/actions/vowel-frequency-analyzer` and processes `data.txt`. It adds a report line here **during a GitHub workflow run**, then the workflow uploads the modified README as an artifact. It does not automatically commit changes back to main, to avoid recursive runs.

## Run evidence
Open Actions → “43030 Lecture 3 - Custom Docker Action” → chosen run → Analyze step and the uploaded output artifact. Record what actually happened.
