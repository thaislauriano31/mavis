import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_TOKEN", "")
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")


if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL e SUPABASE_KEY precisam estar configurados no .env")