# Lecture 4 — GitHub Projects and CI/CD Task Manager

This demonstration aligns with the supplied 43030 Lecture 4 practical: `todo.py`, `todo-test.py`, `update_index.sh`, `entrypoint.sh`, Dockerfile and the CI workflow.

The container populates six example tasks, runs four unit tests and updates `index.html`. Open **Actions → 43030 Lecture 4 - Task Manager CI** and inspect the logs for actual evidence.

**GitHub Projects board:** Not created by this repository code. Issue tracking and linked pull requests are provided, and an optional tracker workflow comments on the linked issue after merge. This is not the same as moving an item to Done on a GitHub Projects board.

Run locally: `docker build -f lecture4/Dockerfile -t 43030-task-manager . && docker run --rm 43030-task-manager`
