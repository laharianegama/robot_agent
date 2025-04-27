# app/utils/task_memory.py

import json
import os

TASK_FILE = "task_memory.json"

def load_task():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            data = json.load(f)
            return data.get("task", ""), data.get("status", "pending")
    return "", "pending"

def save_task(task):
    with open(TASK_FILE, "w") as f:
        json.dump({"task": task, "status": "pending"}, f)

def mark_task_completed():
    task, _ = load_task()
    with open(TASK_FILE, "w") as f:
        json.dump({"task": task, "status": "completed"}, f)

def clear_task():
    with open(TASK_FILE, "w") as f:
        json.dump({"task": "", "status": "pending"}, f)
