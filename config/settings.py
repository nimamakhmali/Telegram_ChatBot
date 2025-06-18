import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HF_API_KEY = os.getenv("HF_API_KEY")  # 👈 به جای OPENAI_API_KEY
# کلید جدید OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
