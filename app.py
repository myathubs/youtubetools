import os
import openai
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
import streamlit as st

st.set_page_config(page_title="📝 MyatHubs Note Engine", layout="centered")

from custom_logger import logger
# from yt_notes_generator import generate_notes_audio
from utils import TUTORIAL_ONLY, CLASS_LECTURE

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
translator = GoogleTranslator(source='auto', target='my')

st.set_page_config(page_title="📝 MyatHubs Note Engine", page_icon="🧠")

st.title("🧠 MyatHubs Note Engine")
st.subheader("🎥 How to Use")
st.markdown("1. Paste a YouTube URL in the sidebar.\n2. Choose a model and prompt style.\n3. Click **Generate Notes**.\n4. View and download the generated notes below.")
st.markdown("OpenAI-powered tool to convert YouTube videos into Burmese or English notes, summaries, and mind maps. 🇲🇲🇬🇧")

# Initialize session state
if "generated_notes" not in st.session_state:
    st.session_state.generated_notes = ""
if "show_download" not in st.session_state:
    st.session_state.show_download = False

# Sidebar inputs
with st.sidebar:
    st.header("📊 Input Parameters")
    youtube_url = st.text_input(
        "🔗 YouTube URL", placeholder="Paste your YouTube URL here..."
    )
    model_name = st.selectbox(
        "🤖 Model Name", ["gemini-1.5-pro", "gemini-1.5-flash"]
    )

    system_prompt = st.selectbox(
        "💬 System Prompt", ["tutorial-only", "class-lecture", "custom"]
    )
    if system_prompt == "tutorial-only":
        system_prompt = TUTORIAL_ONLY
    elif system_prompt == "class-lecture":
        system_prompt = CLASS_LECTURE
    elif system_prompt == "custom":
        system_prompt = st.text_area(
            "✏️ Custom System Prompt", "You are a helpful assistant."
        )

    user_prompt = st.text_area(
        "🗨️ User Prompt", "Please generate notes for this audio."
    )

    generate_button = st.button("🚀 Generate Notes", use_container_width=True)
    translate_to_mm = st.checkbox("🌐 Translate to Burmese (မြန်မာဘာသာ)")

    if st.session_state.show_download:
        st.download_button(
            label="📥 Download Notes as MD",
            data=st.session_state.generated_notes,
            file_name="notes.md",
            mime="text/markdown",
            use_container_width=True,
        )
        st.download_button(
            label="📄 Download Notes as TXT",
            data=st.session_state.generated_notes,
            file_name="notes.txt",
            mime="text/plain",
            use_container_width=True,
        )

# Main content area
st.header("📄 Generated Notes")
if generate_button:
    if youtube_url and model_name and system_prompt and user_prompt:
        with st.spinner("🔄 Generating notes... Please wait."):
            response_placeholder = st.empty()
            full_response = ""
            prompt = f"{system_prompt}\n\n{user_prompt}\n\nYouTube URL: {youtube_url}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            full_response = response["choices"][0]["message"]["content"]
            key_prompt = f"Please extract key points and suggest a mind map structure from the following notes:\n\n{full_response}"
            key_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": key_prompt}]
            )
            key_output = key_response["choices"][0]["message"]["content"]
            if translate_to_mm:
                full_response = translator.translate(full_response)
            response_placeholder.markdown(full_response)
            st.markdown("📲 **Tip:** Long-press the summary to copy and share on Messenger or Facebook.")
            st.markdown("### 🧠 Key Points & Mind Map")
            st.markdown(key_output)

        logger.info("Response successfully generated.")


        # Store generated notes in session state and show download button
        st.session_state.generated_notes = full_response
        st.session_state.show_download = True
        st.rerun()  # Rerun the app to update the sidebar

# Always display the generated notes if they exist
if st.session_state.generated_notes:
    st.markdown(st.session_state.generated_notes)
else:
    st.info("👆 Click 'Generate Notes' in the sidebar to start the process!")

# Footer
st.markdown("---")
st.markdown("---")
st.markdown("🔗 [GitHub Repository](https://github.com/myatminko)\n\n💡 Made by **Myat Min Ko** | Powered by **OpenAI**")
