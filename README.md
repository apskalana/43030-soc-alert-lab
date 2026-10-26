# 43030 | Software Development and SOC Alert Triage

A professional learning project using **Python, Git, GitHub Actions, YAML, Docker, and security event analysis**.

## Project components

| Component | Implementation | Demonstration |
| --- | --- | --- |
| SOC alert triage | `soc_triage.py`, `sample_logs.jsonl`, `tests/` | Analyze simulated login events and identify alerts |
| GitHub workflow automation | `lecture2/`, `.github/workflows/lecture2.yml` | Update HTML and README through a CI workflow |
| Custom GitHub Action | `.github/actions/vowel-frequency-analyzer/` | Run a Docker-based vowel analyzer on `data.txt` |
| Task management | `lecture4/`, `.github/workflows/lecture4.yml` | Test Python tasks and generate an HTML report |
| Version control and issue tracking | Branches, commits, Issues, Pull Request #2 | Track development and review changes |

## Verified results

- **SOC analysis:** 6 Python tests passed; 2 alerts detected in the sample authentication events.
- **Docker:** SOC application image built and ran successfully in CI.
- **Custom action:** Docker-based vowel analyzer executed successfully and generated a report artifact.
- **Task manager:** 4 unit tests passed; Docker execution generated an HTML report.
- **GitHub workflow:** HTML and README automation completed successfully.

View workflow results in [GitHub Actions](https://github.com/apskalana/43030-soc-alert-lab/actions) or the [merged development pull request](https://github.com/apskalana/43030-soc-alert-lab/pull/2).

## Run locally

Requirements: Python 3 and Docker (for container exercises).

```bash
python soc_triage.py sample_logs.jsonl
python -m unittest discover -s tests -v

docker build -t soc-alert-lab .
docker run --rm soc-alert-lab

docker build -f lecture4/Dockerfile -t task-manager .
docker run --rm task-manager
```

## Documentation

- [Learning objectives](docs/LEARNING_OBJECTIVES.md)
- [Portfolio evidence log](docs/PORTFOLIO_LOG.md)
- [Lecture 2 practical](lecture2/README.md)
- [Lecture 3 practical](lecture3/README.md)
- [Lecture 4 practical](lecture4/README.md)
