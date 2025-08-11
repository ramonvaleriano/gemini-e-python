from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO

from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

lista_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos, Produtos de Higiene Sustentáveis"

prompt_system = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.

            # Lista de Categorias Válidas
            {lista_categorias_possiveis.split(",")}

            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
        """

question = "Escova de dentes de bambu"

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(system_instruction=prompt_system),
    contents=question,
)

response_text = response.text

print("\n\n")
print(f"A Pergunta: \n{question}!")
print(f"A resposta: \n{response_text}")
print("\n\n")
