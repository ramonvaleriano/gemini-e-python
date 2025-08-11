from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO

import google.generativeai as genai


genai.configure(api_key=GEMINI_API_KEY)

prompt_system = "Liste apenas os nomes dos produto, e ofereça uma breve descrição."

config_model = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_system,
    generation_config=config_model,
)

question = "Liste três produtos de moda sustentável para ir ao shopping."

response = llm.generate_content(question)
text_response = response.text

print(f"Resposta gerada pelo Gemini: \n{text_response}")
