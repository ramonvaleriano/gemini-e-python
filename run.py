from settings import (
    GEMINI_API_KEY,
    MODELO_ESCOLHIDO
)

from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

question = "Liste três produtos de moda sustentável para ir ao shopping."
prompt_system = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(
        system_instruction=prompt_system
    ),
    contents=question
)

text_response = response.text

print(f"Resposta gerada pelo Gemini: \n{text_response}")
