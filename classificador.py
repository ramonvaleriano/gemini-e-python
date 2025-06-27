# Bibliotecas Google.
from google import genai
from google.genai import types

# Variáveis de ambiente.
from read_env import GEMINI_API_KEY, MODELO_ESCOLHIDO

def genarate_content_and_dysplay_answer(chosen_model, system_prompt, question):
    # Configurando chave de acesso.
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=chosen_model,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        ),
        contents=question
    )

    return response

def execute(chosen_model, system_prompt):
    
    question_input = str(input("Digite aqui o seu produto: "))

    while question_input.lower() != "sair":
        response = genarate_content_and_dysplay_answer(chosen_model, system_prompt, question_input)
        print(response.text)

        question_input = str(input("Digite aqui o seu produto: "))

    
if __name__ == "__main__":
    lista_de_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos,Produtos de Higiene Sustentáveis"

    prompt_sistema = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.
                # Lista de Categorias Válidas
                {lista_de_categorias_possiveis.split(",")}
                
                # Formato da Saída
                Produto: Nome do Produto
                Classificação: apresente a categoria do produto
                Resumo: resumo básico do produto

                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Classificação: Eletrônicos Verdes
                Resumo: Produto feito para casas e tal
            """
    
    execute(MODELO_ESCOLHIDO, prompt_sistema)
