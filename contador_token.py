import google.generativeai as genai

from read_env import MODELO_ESCOLHIDO

custo_entrada_flash = 0.075
custo_saida_flash = 0.30

model_flash = genai.get_model(f"models/{MODELO_ESCOLHIDO}")
limites_modelo_flahs = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit
}

print(f"Os limites de tokens são: {limites_modelo_flahs}")

llm = genai.GenerativeModel(
    f"models/{MODELO_ESCOLHIDO}"
)

quantidade_tokens = llm.count_tokens("O que é um calça de shopping?")

print(f"A quantidade de token gasto é de: {quantidade_tokens}")

resposta = llm.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * custo_entrada_flash) / 1000000 + (tokens_resposta * custo_saida_flash) / 1000000
print(f"Custo Total U$ Flash: {custo_total}")
