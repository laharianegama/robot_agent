import json
import os
from datetime import datetime

MEMORY_FILE = "robot_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"observations": []}

def save_observation(observation: str):
    memory = load_memory()
    memory["observations"].append({
        "timestamp": datetime.now().isoformat(),
        "description": observation
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def get_observations():
    memory = load_memory()
    return [obs["description"] for obs in memory["observations"]]

def clear_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump({"observations": []}, f)
