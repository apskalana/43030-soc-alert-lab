# Lecture 4 — GitHub Projects and CI/CD Task Manager

This demonstration aligns with the supplied 43030 Lecture 4 practical: `todo.py`, `todo-test.py`, `update_index.sh`, `entrypoint.sh`, Dockerfile and the CI workflow.

The container populates six example tasks, runs four unit tests and updates `index.html`. Open **Actions → 43030 Lecture 4 - Task Manager CI** and inspect the logs for actual evidence.

Run locally: `docker build -f lecture4/Dockerfile -t 43030-task-manager . && docker run --rm 43030-task-manager`
