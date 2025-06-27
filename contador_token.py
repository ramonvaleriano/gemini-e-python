import google.generativeai as genai

from read_env import MODELO_ESCOLHIDO

custo_entrada_flash = 0.075
custo_saida_flash = 0.30

model_flash = genai.get_model(f"models/{MODELO_ESCOLHIDO}")
limites_modelo_flahs = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit
}

print(limites_modelo_flahs)


