# Lecture 2 | GitHub Workflow Automation

## Objective

Configure a GitHub Actions workflow that updates an HTML page and records changes in a README.

## Implementation

- **Workflow:** `.github/workflows/lecture2.yml`
- **Script:** `lecture2/update.py`
- **Output:** `lecture2/index.html` and this README

The workflow runs on relevant pushes or by manual dispatch. It checks out the repository, executes the update script, verifies the HTML changes and commits the generated files.

## Test results

The update and commit steps completed successfully in GitHub Actions.

[View Lecture 2 workflow](https://github.com/apskalana/43030-soc-alert-lab/actions/workflows/lecture2.yml)

## Workflow activity

The workflow automatically adds a short entry here with the GitHub actor and triggering commit.

