"""
    Esse código que fiz me meseando na documentação.
"""
# Variáveis de ambiente
from read_env import GEMINI_API_KEY

# Bibliotecas Google
from google.genai import Client, types


# Modelo escohido.
MODELO_ESCOLHIDO = "learnlm-2.0-flash-experimental"

# Configurando Chabe de acesso.
client = Client(api_key=GEMINI_API_KEY)

prompt_system = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

pergunta = "Liste trê produtos de moda sustentável para ir ao shopping."

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(
        system_instruction=prompt_system
    ),
    contents=pergunta
)

print(response.text)