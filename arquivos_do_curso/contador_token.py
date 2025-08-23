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
print("\n")

question = "O que é uma calça moderna"

llm_gemma = genai.GenerativeModel(model_name=MODELO_GEMMA)
quantity_tokens_using_gemma = llm_gemma.count_tokens(question)

print(f"Quantidade de tokens usando o modelo Gemma: {quantity_tokens_using_gemma}")

llm_flash_learn = genai.GenerativeModel(model_name=MODELO_FLASH_LEARN)
quantity_tokens_flash_learn = llm_flash_learn.count_tokens(question)

print(f"Quantidade de tokens usando o modelo Flash Learn: {quantity_tokens_flash_learn}")

response_gemma = llm_gemma.generate_content(question)
tokens_prompt_gemma = response_gemma.usage_metadata.prompt_token_count
tokens_response_gemma = response_gemma.usage_metadata.candidates_token_count

custo_tota_gemma = (tokens_prompt_gemma * CUSTO_ENTRADA_GEMMA) / 1000000 + (tokens_response_gemma * CUSTO_SAIDA_GEMMA) / 1000000
print(f"Custo total para o Gemma: {custo_tota_gemma}")

response_flash_learn= llm_gemma.generate_content(question)
tokens_prompt_flash_learn = response_gemma.usage_metadata.prompt_token_count
tokens_response_flash_learn = response_gemma.usage_metadata.candidates_token_count

custo_tota_flash_learn = (tokens_prompt_flash_learn * CUSTO_ENTRADA_FLASH_LEARN) / 1000000 + (tokens_response_gemma * CUSTO_SAIDA_FLASH_LEARN) / 1000000
print(f"Custo total para o Flash Learn: {custo_tota_flash_learn}")

