from google import genai

from settings import MODELO_FLASH_LEARN, MODELO_GEMMA, GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

model_gemma = client.models.get(model=MODELO_GEMMA)
model_flash_learn = client.models.get(model=MODELO_FLASH_LEARN)

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

quantity_tokens_using_gemma = client.models.count_tokens(model=MODELO_GEMMA, contents="O que é uma calça moderna")

print(f"Quantidade de tokens usando o modelo Gemma: {quantity_tokens_using_gemma.total_tokens}")

quantity_tokens_flash_learn = client.models.count_tokens(model=MODELO_FLASH_LEARN, contents="O que é uma calça moderna")

print(f"Quantidade de tokens usando o modelo Flash Learn: {quantity_tokens_flash_learn.total_tokens}")