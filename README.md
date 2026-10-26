# 43030 Professional Learning — Software Development & SOC Lab

Student project supporting UTS 43030 **Professional Learning Report, Goal 3**, linked to Git and GitHub, CI/CD YAML workflows, Docker and security monitoring.

Sample authentication events are available in `sample_logs.jsonl`.

## Demonstrations
- **SOC triage:** `soc_triage.py` analyses `sample_logs.jsonl`, flags repeated login failures and off-hours admin login. Six Python unit tests validate behaviour.
- **Lecture 2 workflow:** `.github/workflows/ci.yml` validates data using a custom composite action, tests the code, then builds and runs a Docker image.
- **Lecture 3 practical:** `.github/actions/vowel-frequency-analyzer` is a custom Docker action for `data.txt`, with `frequency.py`, `update_readme.sh` and `entrypoint.sh`.
- **Lecture 4 practical:** `lecture4/` contains Python TaskPool code, tests, HTML report generation and a Dockerfile. `.github/workflows/lecture4.yml` runs checks.
- **Issue / PR tracker:** GitHub Issue #1 and linked pull request provide trackable planning and version control; the tracker workflow records the merged PR.

## Running the exercises
```bash
python soc_triage.py sample_logs.jsonl
python -m unittest discover -s tests -v
docker build -t soc-alert-lab .
docker run --rm soc-alert-lab
docker build -f lecture4/Dockerfile -t task-manager .
docker run --rm task-manager
```

Open the GitHub **Actions** tab to see actual workflow results. Save direct links and screenshots in your own portfolio. See `docs/PORTFOLIO_LOG.md` for the evidence log.

