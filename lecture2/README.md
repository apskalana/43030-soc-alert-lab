# Lecture 2 — Automate HTML and README

This folder follows the submitted UTS Lecture 2 practical activities:

1. Set up a YAML workflow in `.github/workflows/lecture2.yml`
2. Update the HTML page based on the GitHub actor
3. Add a README log entry with the actor, timestamp and commit
4. Commit and push those changes from GitHub Actions
5. Verify the workflow via the Actions tab

The workflow runs on pushes affecting this folder or the workflow itself, and can be manually triggered. The CI runner uses its built-in GitHub token with minimal `contents: write` permission; **do not paste personal access tokens or other credentials in files**.

## Update history

- Updated by apskalana on 2026-10-26 14:59:14 UTC (trigger commit: 25d765b69309)
