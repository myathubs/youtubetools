# ----------------------------------------
# 📌 MyatHubs YouTube Notes Generator Tool
# Environment and constants setup
# ----------------------------------------
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from dotenv import load_dotenv

_ = load_dotenv(dotenv_path=".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DIR_NOTES_PATH = os.getenv("DIR_NOTES_PATH")
DIR_AUDIO_PATH = os.getenv("DIR_AUDIO_PATH")
