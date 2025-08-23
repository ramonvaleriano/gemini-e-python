from google import genai

from settings import MODELO_FLASH_LEARN, MODELO_GEMMA, GEMINI_API_KEY

CUSTO_ENTRADA_GEMMA = 0.075
CUSTO_SAIDA_GEMMA = 0.30

CUSTO_ENTRADA_FLASH_LEARN = 3.5
CUSTO_SAIDA_FLASH_LEARN = 10.0

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

question = "O que é uma calça moderna"

quantity_tokens_using_gemma = client.models.count_tokens(model=MODELO_GEMMA, contents=question)

print(f"Quantidade de tokens usando o modelo Gemma: {quantity_tokens_using_gemma.total_tokens}")

quantity_tokens_flash_learn = client.models.count_tokens(model=MODELO_FLASH_LEARN, contents=question)

print(f"Quantidade de tokens usando o modelo Flash Learn: {quantity_tokens_flash_learn.total_tokens}")

response_gemma = client.models.generate_content(
    model=MODELO_GEMMA,
    contents=question
)

tokens_prompt_gemma = response_gemma.usage_metadata.prompt_token_count
tokens_response_gemma = response_gemma.usage_metadata.candidates_token_count

custo_tota_gemma = (tokens_prompt_gemma * CUSTO_ENTRADA_GEMMA) / 1000000 + (tokens_response_gemma * CUSTO_SAIDA_GEMMA) / 1000000
print(f"Custo total para o Gemma: {custo_tota_gemma}")

response_flash_learn = client.models.generate_content(
    model=MODELO_FLASH_LEARN,
    contents=question
)

tokens_prompt_flash_learn = response_flash_learn.usage_metadata.prompt_token_count
tokens_response_flash_learn = response_flash_learn.usage_metadata.candidates_token_count

custo_tota_flash_learn = (tokens_prompt_flash_learn * CUSTO_ENTRADA_FLASH_LEARN) / 1000000 + (tokens_response_gemma * CUSTO_SAIDA_FLASH_LEARN) / 1000000
print(f"Custo total para o Flash Learn: {custo_tota_flash_learn}")