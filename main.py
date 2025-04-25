# app/main.py

import streamlit as st
from app.utils.vision import describe_image
from app.utils.memory import load_user_profile
from app.utils.planner import build_prompt
from app.utils.communicator import generate_response
from app.utils.memory_dict import save_observation, get_observations, clear_memory
from PIL import Image
import hashlib

st.set_page_config(page_title="Robot Assistant Demo 🤖", layout="centered")
st.title("🤖 Real-Time Robot Observer")

# Load user profile
user_name = "mary"
user_data = load_user_profile(user_name)
st.sidebar.markdown(f"**User Profile:** {user_data['name']}")
st.sidebar.markdown(f"**Hobbies:** {', '.join(user_data['preferences']['hobbies'])}")
st.sidebar.markdown(f"**Dislikes:** {', '.join(user_data['preferences']['dislikes'])}")

# Upload image
uploaded_file = st.file_uploader("📸 Upload a new image for observation", type=["jpg", "jpeg", "png"])

# Track last uploaded image hash to avoid reprocessing
if "last_image_hash" not in st.session_state:
    st.session_state.last_image_hash = None

def get_file_hash(file_bytes):
    import hashlib
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
        with st.spinner("🧠 Analyzing image with Groq's vision model..."):
            vision_description = describe_image(image)
            save_observation(vision_description)
            st.markdown("**Image Description:**")
            st.info(vision_description)

        # Step 2: Build Prompt using all observations
        with st.spinner("🔧 Building prompt from previous observations..."):
            observations = get_observations()
            prompt = build_prompt(vision_description, user_data, observations)
            st.markdown("**Generated Prompt for Language Model:**")
            st.code(prompt, language="markdown")

        # Step 3: Generate response
        with st.spinner("💬 Generating a personalized response..."):
            response = generate_response(prompt)
            st.markdown("### 🤖 Robot's Response")
            st.success(response)

# Show past memory
observations = get_observations()
if observations:
    st.markdown("---")
    st.markdown("### 👁️ Robot Memory: Past Observations")
    for i, obs in enumerate(observations):
        st.markdown(f"**Observation {i+1}:** {obs}")

# Reset button
if st.button("🔁 Reset Robot Memory"):
    clear_memory()
    st.success("All observations cleared.")
    st.session_state.last_image_hash = None
