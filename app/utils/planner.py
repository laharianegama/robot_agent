# app/utils/planner.py

def build_prompt(vision_description: str, user_profile: dict) -> str:
    name = user_profile.get("name", "the user")
    dislikes = ", ".join(user_profile["preferences"].get("dislikes", []))
    hobbies = ", ".join(user_profile["preferences"].get("hobbies", []))
    routine = user_profile.get("schedule", {}).get("daily_routine", "")
    visits = user_profile.get("schedule", {}).get("daughter_visits", "")

    prompt = f"""
You are a helpful and empathetic robot assistant helping {name}.
Based on the following scene: "{vision_description}"

Here is what you know about {name}:
- Dislikes: {dislikes}
- Hobbies: {hobbies}
- Daily Routine: {routine}
- Daughter visits: {visits}

Please generate a comforting and supportive message you would say to {name} in this situation.
"""
    return prompt.strip()
