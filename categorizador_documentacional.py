from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO

from google import genai
from google.genai import types


def get_prompt_system(lista_categorias_possiveis: str) -> str:
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
    return prompt_system


def gerator_response(
    modelo_escolhido: str, api_key: str, system_instruction: str, question: str
) -> str:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=modelo_escolhido,
        config=types.GenerateContentConfig(system_instruction=system_instruction),
        contents=question,
    )

    response_text = response.text

    return response_text


question = "Escova de dentes de bambu"


def execute(question: str) -> str:
    lista_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos, Produtos de Higiene Sustentáveis"

    system_instruction = get_prompt_system(lista_categorias_possiveis)
    response = gerator_response(
        modelo_escolhido=MODELO_ESCOLHIDO,
        api_key=GEMINI_API_KEY,
        system_instruction=system_instruction,
        question=question,
    )

    return response


question = "Escova de dentes de bambu"

response = execute(question=question)


print("\n\n")
print(f"A Pergunta: \n{question}!")
print(f"A resposta: \n{response}")
print("\n\n")
