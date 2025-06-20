"""
    Esse código eu fiz seguindo o curso da Alura.
"""

# Importando variaveis de ambiente
from read_env import GEMINI_API_KEY

# Importando Gemini
import google.generativeai as genai

# Modelo escolhido.
MODELO_ESCOLHIDO = "learnlm-2.0-flash-experimental"

# Configurando API key
genai.configure(api_key=GEMINI_API_KEY)

prompt_sistem = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."


configuracao_modelo = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

"""
LLMs Large Linguage Model, ou Grande modelo de linguagem.
"""
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistem,
    generation_config=configuracao_modelo
)

pergunta = "Liste trê produtos de moda sustentável para ir ao shopping."

resposta = llm.generate_content(pergunta)

print(resposta.text)