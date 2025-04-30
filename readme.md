# 🤖 Robot Companion Agent

A personalized, image-driven robot assistant that simulates how a caregiving robot would perceive, remember, and respond to a user in real time.

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

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/robot-companion-agent.git
cd robot-companion-agent
pip install -r requirements.txt
streamlit run main.py
```
