# Lecture 2 | GitHub Workflow Automation

## Objective

Configure a GitHub Actions workflow that updates an HTML page and records changes in a README.

## Implementation

- **Workflow:** `.github/workflows/lecture2.yml`
- **Script:** `lecture2/update.py`
- **Output:** `lecture2/index.html` and this README

The workflow checks out the repository, executes the update script, verifies the HTML changes and commits the generated files.

## Test results and evidence

The HTML update and commit steps completed successfully.

- [Successful Lecture 2 run](https://github.com/apskalana/43030-soc-alert-lab/actions/runs/40345248338)
- [Workflow overview](https://github.com/apskalana/43030-soc-alert-lab/actions/workflows/lecture2.yml)

## Workflow activity

The workflow automatically records the GitHub actor and triggering commit.

- Workflow executed by apskalana (trigger commit: d5e32ef6a90a)
