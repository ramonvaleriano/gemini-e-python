import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = os.getenv("MODELO_ESCOLHIDO")