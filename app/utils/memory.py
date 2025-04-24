# app/utils/memory.py

import json
import os

def load_user_profile(user_name: str) -> dict:
    profile_path = f"data/mary.json"
    if not os.path.exists(profile_path):
        raise FileNotFoundError(f"Profile for user '{user_name}' not found at {profile_path}")
    
    with open(profile_path, "r") as f:
        profile = json.load(f)
    return profile
