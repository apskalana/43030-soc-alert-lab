#!/bin/sh
set -eu
python /app/todo.py > /app/task-output.txt
python /app/todo-test.py > /app/tests-output.txt 2>&1
sh /app/update_index.sh /app/task-output.txt /app/tests-output.txt
cat /app/task-output.txt
cat /app/tests-output.txt
