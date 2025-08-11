import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_key = os.getenv("GEMINI_API_key")
MODELO_ESCOLHIDO = os.getenv("MODELO_ESCOLHIDO")