"""
    Esse código que fiz me meseando na documentação.
"""
# Variáveis de ambiente
from read_env import GEMINI_API_KEY

# Bibliotecas Google
from google.genai import Client, types


# Dados padrão.
MODELO_ESCOLHIDO = "learnlm-2.0-flash-experimental"
TEMPERATURE = 1.0
TOP_P = 0.95
TOP_K = 64
MAX_OUTPUT_TOKENS = 8192
RESPONSE_MIME_TYPE = "text/plain"


# Configurando Chabe de acesso.
client = Client(api_key=GEMINI_API_KEY)

prompt_system = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."


pergunta = "Liste trê produtos de moda sustentável para ir ao shopping."

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(
        system_instruction=prompt_system,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        top_k=TOP_K,
        max_output_tokens=MAX_OUTPUT_TOKENS,
        response_mime_type=RESPONSE_MIME_TYPE
    ),
    contents=pergunta
)

print(response.text)