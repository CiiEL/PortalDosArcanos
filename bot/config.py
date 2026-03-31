import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_QUOTE_URL = os.getenv("API_QUOTE_URL", "https://api.quotable.io/random")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN não encontrado. Crie um arquivo .env com TELEGRAM_TOKEN=xxx")
