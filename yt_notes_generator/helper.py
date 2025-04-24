# 📌 MyatHubs AI Notes - Audio Note Generation Helper
# This module downloads YouTube audio, extracts filenames, and generates notes using AI

import streamlit as st
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import openai
from utils import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY


def generate_notes_audio(
    youtube_url: str, model_name: str, system_prompt: str, user_prompt: str
):
    audio_file_path = download_youtube_audio(dir_path=DIR_AUDIO_PATH, url=youtube_url)
    base_name, file_name = extract_filename(audio_file_path)
    logger.info(f"[MyatHubs] Downloaded file: {base_name}")

    prompt = f"{system_prompt}\n\n{user_prompt}\n\nAudio file: {file_name}"
    logger.info(f"[MyatHubs] Generating notes using {model_name}...")

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    logger.info(f"[MyatHubs] Deleting local file: {base_name}")
    os.remove(audio_file_path)

    return response["choices"][0]["message"]["content"]
