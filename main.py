# app/main.py

import streamlit as st
from app.utils.vision import describe_image
from app.utils.memory import load_user_profile
from app.utils.planner import build_prompt
from app.utils.communicator import generate_response
from PIL import Image

st.set_page_config(page_title="Robot Assistant Demo 🤖", layout="centered")
st.title("🤖 Robot Companion Agent")

# Load user profile
user_name = "mary"
user_data = load_user_profile(user_name)
st.sidebar.markdown(f"**User Profile:** {user_data['name']}")
st.sidebar.markdown(f"**Preferences:** {', '.join(user_data['preferences']['hobbies'])}")
st.sidebar.markdown(f"**Dislikes:** {', '.join(user_data['preferences']['dislikes'])}")

# Upload image
uploaded_file = st.file_uploader("📸 Upload an image of the user", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Step 1: Vision Model
    with st.spinner("🧠 Analyzing image with Groq's vision model..."):
        vision_description = describe_image(image)
        st.markdown("**Image Description:**")
        st.info(vision_description)

    # Step 2: Build Prompt
    with st.spinner("🔧 Building prompt from user memory..."):
        prompt = build_prompt(vision_description, user_data)
        st.markdown("**Generated Prompt for Language Model:**")
        st.code(prompt, language="markdown")

    # Step 3: LLM Response
    with st.spinner("💬 Generating a personalized response..."):
        response = generate_response(prompt)
        st.markdown("### 🤖 Robot's Response")
        st.success(response)
