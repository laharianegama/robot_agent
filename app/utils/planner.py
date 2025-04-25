def build_prompt(current_observation: str, user_profile: dict, past_observations: list) -> str:
    name = user_profile["name"]
    hobbies = ", ".join(user_profile["preferences"].get("hobbies", []))
    dislikes = ", ".join(user_profile["preferences"].get("dislikes", []))
    routine = user_profile["schedule"].get("daily_routine", "")
    visits = user_profile["schedule"].get("daughter_visits", "")

    past = "\n".join(f"- {obs}" for obs in past_observations[:-1])
    memory_block = f"{past}" if past else "None yet."

    prompt = f"""
You are a compassionate robot assistant assigned to help a woman named {name} in her home and surroundings.

Here are important facts about her:
- Likes: {hobbies}
- Dislikes: {dislikes}
- Routine: {routine}
- Her daughter visits: {visits}

🧠 Memory of past observations:
{memory_block}

👁️ Current observation (most important, focus on this):
- {current_observation}

Now, speak directly to {name}. Respond as if you're physically next to her, seeing what you see now.

Rules:
- Be empathetic and emotionally appropriate
- Focus mostly on the current observation
- You may gently reflect on the past only if helpful
- Keep it short, warm, and relevant (max 100 words)
- Do not include meta reasoning or internal thoughts
- Begin your response directly as if talking to Mary
"""
    return prompt.strip()


