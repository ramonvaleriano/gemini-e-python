# Bibliotecas google.
import google.generativeai as genai

# Variáveis de ambiente.
from read_env import GEMINI_API_KEY, MODELO_ESCOLHIDO

# Configurando Chave de acesso
genai.configure(api_key=GEMINI_API_KEY)

def categorizar_produto(system_prompt, chosen_model):
    llm = genai.GenerativeModel(
        model_name=chosen_model,
        system_instruction=system_prompt,

    )

    return llm

def generation_question_and_display_answer(llm, question):
    response = llm.generate_content(question)

    return response

def execute(system_prompt, chosen_model, question):
    llm = categorizar_produto(system_prompt=system_prompt, chosen_model=chosen_model)
    response = generation_question_and_display_answer(llm=llm, question=question)

    return response.text

if __name__ == "__main__":
    lista_de_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos,Produtos de Higiene Sustentáveis"

    prompt_sistema = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.
                # Lista de Categorias Válidas
                {lista_de_categorias_possiveis.split(",")}
                
                # Formato da Saída
                Produto: Nome do Produto
                Categoria: apresente a categoria do produto
                Resumo: resumo básico do produto

                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Categoria: Eletrônicos Verdes
                Resumo: Produto feito para casas e tal
            """

    pergunta = str(input("Digite o produto que você deseja categorizar: "))

    while pergunta.lower() != "sair":
        response = execute(
            system_prompt=prompt_sistema,
            chosen_model=MODELO_ESCOLHIDO,
            question=pergunta
        )

        print(response)

        pergunta = str(input("Digite o produto que você deseja categorizar: "))

        