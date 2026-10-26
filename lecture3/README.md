# Lecture 3 | Custom GitHub Action and Docker

## Objective

Create a reusable Docker-based GitHub Action to analyze text input and report vowel frequencies.

## Implementation

| File | Purpose |
| --- | --- |
| `.github/actions/vowel-frequency-analyzer/action.yml` | Custom action metadata and inputs |
| `.github/actions/vowel-frequency-analyzer/Dockerfile` | Container image |
| `.github/actions/vowel-frequency-analyzer/frequency.py` | Python vowel-frequency analysis |
| `.github/actions/vowel-frequency-analyzer/update_readme.sh` | Append analysis results to a report |
| `.github/actions/vowel-frequency-analyzer/entrypoint.sh` | Run the analysis and reporting steps |
| `data.txt` | Sample input |

## Test results

The custom Docker Action executed successfully and produced a downloadable report artifact in GitHub Actions.

[View Lecture 3 workflow](https://github.com/apskalana/43030-soc-alert-lab/actions/workflows/lecture3.yml)
