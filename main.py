import streamlit as st
from app.utils.vision import describe_image
from app.utils.memory import load_user_profile
from app.utils.planner import build_prompt
from app.utils.communicator import generate_response
from app.utils.memory_dict import save_observation, get_observations, clear_memory
from app.utils.task_memory import load_task, save_task, clear_task
from PIL import Image
import hashlib

st.set_page_config(page_title="Robot Assistant Demo 🤖", layout="centered")
st.title("🤖 Real-Time Robot Companion")

# Load user profile
user_name = "mary"
user_data = load_user_profile(user_name)

# Load task
current_task, task_status = load_task()

# Sidebar: User profile + Task Manager
st.sidebar.title("👩 User Info")
st.sidebar.markdown(f"**Name:** {user_data['name']}")
st.sidebar.markdown(f"**Likes:** {', '.join(user_data['preferences']['hobbies'])}")
st.sidebar.markdown(f"**Dislikes:** {', '.join(user_data['preferences']['dislikes'])}")

st.sidebar.title("🎯 Task Manager")
if current_task:
    st.sidebar.success(f"Task: {current_task} ({task_status})")
else:
    st.sidebar.warning("No task set.")

new_task = st.sidebar.text_input("📝 Set a New Task for Mary:")

if st.sidebar.button("Save Task"):
    if new_task.strip():
        save_task(new_task.strip())
        st.success(f"Task '{new_task.strip()}' saved.")
        st.rerun()

if st.sidebar.button("Clear Task"):
    clear_task()
    st.success("Task cleared.")
    st.experimental_rerun()

# Session tracking
if "last_image_hash" not in st.session_state:
    st.session_state.last_image_hash = None

# Upload image
uploaded_file = st.file_uploader("📸 Upload a New Image", type=["jpg", "jpeg", "png"])

def get_file_hash(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    file_hash = get_file_hash(file_bytes)

    if file_hash == st.session_state.last_image_hash:
        st.warning("You've uploaded the same image again. Please upload a new one.")
    else:
        st.session_state.last_image_hash = file_hash

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Step 1: Vision Model
        with st.spinner("🧠 Analyzing image with Groq's Vision model..."):
            vision_description = describe_image(image)
            save_observation(vision_description)
            st.markdown("**Image Description:**")
            st.info(vision_description)

        # Step 2: Build Prompt
        with st.spinner("🔧 Building robot prompt..."):
            observations = get_observations()
            prompt = build_prompt(vision_description, user_data, observations, current_task)
            st.markdown("**Generated Prompt for Language Model:**")
            st.code(prompt, language="markdown")

        # Step 3: LLM Response
        with st.spinner("💬 Robot is thinking..."):
            response = generate_response(prompt)
            st.markdown("### 🤖 Robot's Response")
            st.success(response)

# Display robot memory
observations = get_observations()
if observations:
    st.markdown("---")
    st.markdown("### 🧠 Robot Memory: Past Observations")
    for i, obs in enumerate(observations):
        st.markdown(f"**Step {i+1}:** {obs}")

# Memory Reset
if st.button("🔁 Reset Robot Memory"):
    clear_memory()
    st.success("Robot memory cleared.")
    st.session_state.last_image_hash = None

