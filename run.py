from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO

from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

config_model = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

question = "Liste três produtos de moda sustentável para ir ao shopping."
prompt_system = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(
        system_instruction=prompt_system,
        temperature=config_model["temperature"],
        top_p=config_model["top_p"],
        top_k=config_model["top_k"],
        max_output_tokens=config_model["max_output_tokens"],
        response_mime_type=config_model["response_mime_type"]
    ),
    contents=question,
)

text_response = response.text

print(f"Resposta gerada pelo Gemini: \n{text_response}")
