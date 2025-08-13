import google.generativeai as genai

from settings import MODELO_GEMMA, MODELO_FLASH_LEARN, GEMINI_API_KEY

CUSTO_ENTRADA_GEMMA = 0.075
CUSTO_SAIDA_GEMMA = 0.30

CUSTO_ENTRADA_FLASH_LEARN = 3.5
CUSTO_SAIDA_FLASH_LEARN = 10.0

genai.configure(api_key=GEMINI_API_KEY)

model_gemma = genai.get_model(f"models/{MODELO_GEMMA}")
model_flash_learn = genai.get_model(f"models/{MODELO_FLASH_LEARN}")

limites_model_gemma = {
    "tokens_entrada": model_gemma.input_token_limit,
    "tokens_saída": model_gemma.output_token_limit
}

limites_model_flash_learn = {
    "tokens_entrada": model_flash_learn.input_token_limit,
    "tokens_saída": model_flash_learn.output_token_limit
}

print("\n\n")
print(f"Limites para o modelo Gemma: {limites_model_gemma}")
print(f"Limites para o modelo Flash Learn: {limites_model_flash_learn}")
print("\n\n")