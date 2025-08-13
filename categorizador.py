from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO

import google.generativeai as genai


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
):
    genai.configure(api_key=api_key)

    llm = genai.GenerativeModel(
        model_name=modelo_escolhido, system_instruction=system_instruction
    )

    response = llm.generate_content(question)

    response_text = response.text

    return response_text


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


def execute_while() -> str:
    question = str(input("Digite o tipo de produto que você deseja listar: "))
    while question not in ["", " ", None]:
        response = execute(question=question)

    return response


response = execute_while()


print("\n\n")
print(f"A resposta: \n{response}")
print("\n\n")
