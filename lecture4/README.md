# Lecture 4 | Task Manager and CI/CD

## Objective

Create a Python task-management application with automated unit testing, an HTML report and a Docker-based CI/CD workflow.

## Implementation

- **Application:** `todo.py` — `Task` and `TaskPool` classes.
- **Tests:** `todo-test.py` — task creation, completion and filtering.
- **Report:** `render_report.py` and `update_index.sh` — write an HTML report.
- **Container:** `Dockerfile` and `entrypoint.sh` — execute the application and tests.
- **Workflow:** `.github/workflows/lecture4.yml` — test, build Docker and upload an HTML artifact.

## Test results and evidence

**4 unit tests passed.** Docker ran the task manager and produced the `lecture4-task-manager-report` artifact.

- [Successful Lecture 4 run](https://github.com/apskalana/43030-soc-alert-lab/actions/runs/40345248482)
- [Workflow overview](https://github.com/apskalana/43030-soc-alert-lab/actions/workflows/lecture4.yml)

## Run locally

```bash
docker build -f lecture4/Dockerfile -t 43030-task-manager .
docker run --rm 43030-task-manager
```
