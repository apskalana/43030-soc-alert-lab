# Lecture 4 | Task Manager and CI/CD

## Objective

Create a Python task-management application with automated unit testing, an HTML report and a Docker-based CI/CD workflow.

## Implementation

- **Application:** `todo.py` — `Task` and `TaskPool` classes.
- **Tests:** `todo-test.py` — task creation, completion and filtering.
- **Report:** `render_report.py` and `update_index.sh` — write an HTML report.
- **Container:** `Dockerfile` and `entrypoint.sh` — execute the application and tests.
- **Workflow:** `.github/workflows/lecture4.yml` — run tests, build Docker and upload an HTML artifact.

## Test results

**4 unit tests passed.** The Docker task-manager run completed and the HTML report was generated.

[View Lecture 4 workflow](https://github.com/apskalana/43030-soc-alert-lab/actions/workflows/lecture4.yml)

## Run locally

```bash
docker build -f lecture4/Dockerfile -t 43030-task-manager .
docker run --rm 43030-task-manager
```
