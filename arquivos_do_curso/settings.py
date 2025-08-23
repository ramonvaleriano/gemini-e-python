import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = os.getenv("MODELO_ESCOLHIDO")
MODELO_GEMMA = os.getenv("MODELO_GEMMA", "gemma-3n-e2b-it")
MODELO_FLASH_LEARN = os.getenv("MODELO_FLASH_LEARN", "learnlm-2.0-flash-experimental")