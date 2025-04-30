# 🤖 Robot Companion Agent

A personalized, image-driven robot assistant that simulates how a robot would perceive, remember, and respond to a user in real time.

Built with:

- 🧠 Open-source LLMs via **Groq API**
- 👁️ Visual scene understanding (image captioning)
- 💬 Streamlit app for interactive UI
- 📷 Real-time memory & task reasoning

---

## 📦 Features

- Upload images one-by-one to simulate **real-time robot observation**
- Robot **analyzes user state** from the image
- Maintains a memory of all visual observations
- Lets user **set a task** (e.g., "Water the plants")
- Robot will track progress and give task-relevant instructions
- If the task is completed, it congratulates the user
- If not, it guides the user on what to do next

---

## 🛠 Setup Instructions

### 1. Clone the Repository and create a .env file

```bash
git clone https://github.com/laharianegama/robot_agent.git
```

```bash
HUGGINGFACE_TOKEN= <YOUR TOKEN>
GROQ_API_KEY= <YOUR TOKEN>
```

```bash
cd robot-agent
pip install -r requirements.txt
streamlit run main.py
```
